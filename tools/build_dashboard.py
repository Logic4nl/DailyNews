#!/usr/bin/env python3
"""Build the AI/HPC miner analytics dashboard to the 5-section spec.

One price fetch per run -> prices.json. Rules engine (rules.yaml) evaluated against
live prices. Positions from positions.json (broker export). Every verdict is computed,
never hand-authored. Freshness gating suppresses bullish actions on stale data.

Usage: python3 tools/build_dashboard.py [--date YYYY-MM-DD]
"""
import argparse, json, os, sys, html, datetime as dt
from concurrent.futures import ThreadPoolExecutor

import yaml
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analytics_pipeline as ap

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TIER = {  # universe tier badge
    "CIFR": "hpc", "IREN": "hpc", "SLNH": "hpc", "BGDE": "hpc", "BTBT": "hpc",
    "CORZ": "hpc", "HUT": "hpc", "CLSK": "hpc", "APLD": "hpc", "WULF": "hpc",
    "MARA": "btc", "RIOT": "btc", "BTDR": "btc", "BITF": "btc", "HIVE": "btc",
}

# ----------------------------------------------------------------------------
# 1. SINGLE CONSOLIDATED FETCH -> prices.json
# ----------------------------------------------------------------------------

def fetch_crypto(symbol, yf_symbol):
    try:
        from tradingview_ta import TA_Handler
        h = TA_Handler(symbol=symbol, exchange="BINANCE", screener="crypto", interval="1d")
        ind = h.get_analysis().indicators
        if ind.get("close") is not None:
            return {"last": ind.get("close"), "day_pct": ind.get("change"), "src": "tradingview"}
    except Exception:
        pass
    try:
        import yfinance as yf
        d = yf.Ticker(yf_symbol).history(period="5d")
        if len(d) >= 2:
            last = float(d["Close"].iloc[-1]); prev = float(d["Close"].iloc[-2])
            return {"last": last, "day_pct": (last/prev - 1)*100, "src": "yfinance"}
    except Exception as e:
        return {"last": None, "day_pct": None, "error": str(e)}
    return {"last": None, "day_pct": None}

def eth_weekly_close():
    try:
        import yfinance as yf
        d = yf.Ticker("ETH-USD").history(period="3mo", interval="1wk")
        if len(d):
            return float(d["Close"].iloc[-1])
    except Exception:
        pass
    return None

def _rsi(series, n=14):
    import pandas as pd
    d = series.diff()
    up = d.clip(lower=0); dn = -d.clip(upper=0)
    ag = up.ewm(alpha=1/n, adjust=False).mean(); al = dn.ewm(alpha=1/n, adjust=False).mean()
    rs = ag / al.replace(0, 1e-9)
    return float((100 - 100/(1+rs)).iloc[-1])

def yf_data(tickers):
    """Daily+weekly history from yfinance, with TA indicators computed from it.
    Used for perf, trailing high, stop checks, and as the indicator source when the
    primary TradingView screener is unavailable (degrade, do not freeze)."""
    import pandas as pd
    out = {}
    try:
        import yfinance as yf
        data = yf.download(tickers, period="1y", interval="1d", group_by="ticker",
                           progress=False, threads=True)
    except Exception:
        return {t: {} for t in tickers}
    for t in tickers:
        try:
            df = data[t] if len(tickers) > 1 else data
            close = df["Close"].dropna()
            closes = [float(x) for x in close.tolist()]
            highs = [float(x) for x in df["High"].dropna().tolist()]
            if len(closes) < 2:
                out[t] = {"closes": [], "highs": []}; continue
            ema12 = close.ewm(span=12, adjust=False).mean()
            ema26 = close.ewm(span=26, adjust=False).mean()
            macd = ema12 - ema26
            signal = macd.ewm(span=9, adjust=False).mean()
            wk = close.resample("W").last().dropna()
            out[t] = {
                "closes": closes, "highs": highs,
                "rsi_d": _rsi(close), "rsi_w": _rsi(wk) if len(wk) > 15 else None,
                "macd_macd": float(macd.iloc[-1]), "macd_signal": float(signal.iloc[-1]),
                "sma20": float(close.rolling(20).mean().iloc[-1]) if len(closes) >= 20 else None,
                "sma50": float(close.rolling(50).mean().iloc[-1]) if len(closes) >= 50 else None,
                "sma200": float(close.rolling(200).mean().iloc[-1]) if len(closes) >= 200 else None,
            }
        except Exception:
            out[t] = {"closes": [], "highs": []}
    return out

def pct(a, b):
    if a is None or b in (None, 0):
        return None
    return (a / b - 1.0) * 100.0

def consolidated_fetch():
    universe = ap.ALL_TICKERS
    ta_ok = 0
    rows = {}

    def one(t):
        ta = ap.fetch_ta(t)
        st = ap.fetch_stocktwits(t)
        sent = ap.SentimentSnapshot(ticker=t)
        if "error" not in st:
            sent.stocktwits_bull = st["bull"]; sent.stocktwits_bear = st["bear"]; sent.stocktwits_total = st["total"]
        return t, ta, sent

    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(one, universe))

    hist = yf_data(universe)

    tv_ok = 0; ind_ok = 0
    for t, ta, sent in results:
        h = hist.get(t, {})
        closes = h.get("closes", []); highs = h.get("highs", [])
        tv_valid = ta.last_close is not None
        if tv_valid:
            tv_ok += 1; ind_src = "tradingview"
        elif closes:
            # synthesize indicators from yfinance history (degrade, do not freeze)
            ta.last_close = closes[-1]
            ta.rsi_d = h.get("rsi_d"); ta.rsi_w = h.get("rsi_w")
            ta.macd_macd = h.get("macd_macd"); ta.macd_signal = h.get("macd_signal")
            ta.sma20 = h.get("sma20"); ta.sma50 = h.get("sma50"); ta.sma200 = h.get("sma200")
            ind_src = "yfinance"
        else:
            ind_src = "none"
        last = ta.last_close
        if ta.rsi_d is not None:
            ind_ok += 1
        ta_ok = tv_ok
        day_pct = ta.daily_change_pct
        if day_pct is None and len(closes) >= 2:
            day_pct = pct(last, closes[-2])
        p5 = pct(last, closes[-6]) if len(closes) >= 6 else None
        p1m = pct(last, closes[-22]) if len(closes) >= 22 else None
        trail_high = max(highs[-40:]) if highs else None
        rows[t] = {
            "last": last, "src": ind_src,
            "day_pct": day_pct,
            "p5": p5, "p1m": p1m,
            "rsi_d": ta.rsi_d, "rsi_w": ta.rsi_w,
            "macd_dir": "up" if ta.macd_above_signal else ("down" if ta.macd_above_signal is False else None),
            "ma_stack": ta.ma_stack_score,
            "setup": ap.score_setup(ta), "pivot": ap.score_pivot(ta),
            "hype": ap.hype_stage(ta, sent), "sent_label": ap.sentiment_label(sent),
            "stk_bull": sent.stocktwits_bull, "stk_bear": sent.stocktwits_bear, "stk_total": sent.stocktwits_total,
            "closes": closes[-5:], "trail_high": trail_high,
        }

    btc = fetch_crypto("BTCUSDT", "BTC-USD"); eth = fetch_crypto("ETHUSDT", "ETH-USD")
    eth_wk = eth_weekly_close()

    price_ok = sum(1 for t in rows if rows[t]["last"] is not None)
    primary_ok = tv_ok >= len(universe) * 0.6
    is_stale = price_ok == 0                 # red: no live prices at all => suppress bullish
    indicators_stale = tv_ok < len(universe) * 0.6
    if primary_ok:
        source, health = "tradingview", "green"
    elif ind_ok >= len(universe) * 0.6:
        source, health = "yfinance-computed", "amber"
    elif price_ok > 0:
        source, health = "yfinance-prices-only", "amber"
    else:
        source, health = "none", "red"

    prices = {
        "fetched_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source": source,
        "health": health,
        "primary_ok": primary_ok,
        "is_stale": is_stale,
        "indicators_stale": indicators_stale,
        "ta_valid": tv_ok,
        "ind_valid": ind_ok,
        "price_valid": price_ok,
        "universe_size": len(universe),
        "btc": btc, "eth": eth, "eth_weekly_close": eth_wk,
        "tickers": rows,
    }
    return prices

# ----------------------------------------------------------------------------
# 2. RULES ENGINE
# ----------------------------------------------------------------------------

def evaluate_rules(prices, rules, positions):
    flags = rules.get("manual_flags", {})
    btc = prices["btc"].get("last")
    eth = prices["eth"].get("last")
    eth_wk = prices.get("eth_weekly_close")
    slnh = prices["tickers"].get("SLNH", {})
    out = []

    def money(x):
        return f"${x:,.0f}" if x is not None else "N/A"

    for r in rules.get("committed_rules", []):
        rid = r["id"]; state = "CLEAR"; live = ""; dist = ""; extra = r.get("note", "")
        if rid == "slnh_hard_stop":
            closes = slnh.get("closes", []) or []
            thr = r["threshold"]
            consec = 0
            for c in reversed(closes):
                if c < thr: consec += 1
                else: break
            last = slnh.get("last")
            if consec >= r["sessions"]: state = "FIRED"
            elif last is not None and last < thr: state = "ARMED"
            elif last is not None and last < thr * 1.18: state = "ARMED"
            live = f"SLNH ${last:.2f}, {consec} consec close < ${thr:.2f}" if last else "SLNH N/A"
            dist = f"${last - thr:.2f} above the ${thr:.2f} stop" if last else "N/A"
        elif rid == "slnh_year_end_trim":
            satisfied = bool(flags.get(r["satisfied_when_flag"]))
            deadline = dt.date.fromisoformat(r["deadline"])
            today = dt.date.today()
            days = (deadline - today).days
            if satisfied: state = "CLEAR"
            elif days < 0: state = "FIRED"
            else: state = "ARMED"
            live = "named IG hyperscaler tenant FILED" if satisfied else "no named tenant lease on file"
            dist = f"{days} days to {r['deadline']}"
        elif rid == "slnh_upside_ladder":
            last = slnh.get("last")
            levels = r["levels"]
            nxt = next((l for l in levels if last is not None and last < l["price"]), None)
            state = "ARMED" if (last is not None and last >= 7) else "CLEAR"
            live = f"SLNH ${last:.2f}" if last else "N/A"
            if nxt: dist = f"next level ${nxt['price']} ({nxt['action']}), ${nxt['price']-last:.2f} away"
            else: dist = "above top ladder level"
            extra = "; ".join(f"${l['price']}: {l['action']}" for l in levels)
        elif rid == "slnh_invalidations":
            fired = []
            if btc is not None and btc < r["btc_threshold"]:
                fired.append("BTC < 55k")
            for cond in r["any_of"]:
                k = cond["key"]
                if k == "btc_below_55k":
                    continue
                if flags.get(k):
                    fired.append(cond["label"])
            if fired: state = "FIRED"
            elif btc is not None and btc < r["btc_threshold"] * 1.12: state = "ARMED"
            live = f"BTC {money(btc)}" + (f"; triggers: {', '.join(fired)}" if fired else "; no manual flags set")
            dist = f"{money((btc - r['btc_threshold']) if btc else None)} above the 55k line"
            extra = "any one fires => REVIEW, cut. " + " | ".join(c["label"] for c in r["any_of"])
        elif rid == "btbt_sleeve_invalidation":
            thr = r["eth_weekly_threshold"]
            if eth_wk is not None and eth_wk < thr: state = "FIRED"
            elif eth_wk is not None and eth_wk < thr * 1.07: state = "ARMED"
            live = f"ETH weekly close {money(eth_wk)}"
            dist = f"{money((eth_wk - thr) if eth_wk else None)} above the {thr} weekly line"
        elif rid == "btbt_add_condition":
            thr = r["eth_threshold"]
            gate_open = eth is not None and eth > thr
            state = "ARMED" if gate_open else "CLEAR"
            live = f"ETH {money(eth)}, gate {'OPEN' if gate_open else 'closed'}"
            dist = f"needs ETH > {money(thr)}; {money((thr - eth) if eth else None)} away" if not gate_open else "gate open"
        out.append({"id": rid, "ticker": r["ticker"], "desc": r["desc"], "type": r["type"],
                    "state": state, "live": live, "dist": dist, "action": r.get("action", ""), "note": extra})

    # tool trails
    trails = []
    tcfg = rules.get("tool_trails", {})
    pct_default = tcfg.get("default_pct", 12)
    overrides = tcfg.get("overrides", {}) or {}
    held = {p["ticker"] for p in positions["positions"]}
    for t in held:
        row = prices["tickers"].get(t, {})
        last = row.get("last"); hi = row.get("trail_high")
        p = overrides.get(t, pct_default)
        trail = hi * (1 - p / 100.0) if hi else None
        if last is None or trail is None:
            state = "N/A"; live = "N/A"; dist = "N/A"
        else:
            breached = last < trail
            state = "BREACHED" if breached else "CLEAR"
            live = f"{t} ${last:.2f} vs trail ${trail:.2f} ({p}% below ${hi:.2f} high)"
            dist = f"${last - trail:.2f} above trail" if not breached else f"${trail - last:.2f} below trail"
        trails.append({"ticker": t, "state": state, "live": live, "dist": dist, "pct": p})
    return out, trails

# ----------------------------------------------------------------------------
# 3. YOUR BOOK
# ----------------------------------------------------------------------------

def build_book(prices, positions, committed, trails):
    fired_by_t = {}
    armed_inval_by_t = {}
    for r in committed:
        if r["state"] == "FIRED": fired_by_t.setdefault(r["ticker"], []).append(r)
        if r["type"] == "invalidation" and r["state"] == "ARMED": armed_inval_by_t.setdefault(r["ticker"], True)
    trail_breach = {tr["ticker"] for tr in trails if tr["state"] == "BREACHED"}
    # committed stop levels per ticker
    stop_level = {"SLNH": 0.85}

    rows = []
    total_mv = 0.0
    for p in positions["positions"]:
        t = p["ticker"]; row = prices["tickers"].get(t, {})
        last = row.get("last"); mv = (last or 0) * p["shares"]; total_mv += mv
    for p in positions["positions"]:
        t = p["ticker"]; row = prices["tickers"].get(t, {})
        last = row.get("last"); avg = p["avg"]
        mv = (last or 0) * p["shares"]
        weight = (mv / total_mv * 100) if total_mv else 0
        unreal = ((last - avg) / avg * 100) if last else None
        # stop / trail
        if t in stop_level:
            stop = stop_level[t]; stop_lbl = f"${stop:.2f} hard stop"
        else:
            tr = next((x for x in trails if x["ticker"] == t), None)
            hi = row.get("trail_high"); pctv = tr["pct"] if tr else 12
            stop = hi * (1 - pctv / 100.0) if hi else None
            stop_lbl = f"${stop:.2f} trail" if stop else "N/A"
        dist_stop = f"{((last - stop)/last*100):+.1f}%" if (last and stop) else "N/A"
        # status chip
        if t in fired_by_t: chip = "RULE FIRED"
        elif t in armed_inval_by_t: chip = "INVALIDATION WATCH"
        elif t in trail_breach: chip = "TRAIL BREACHED"
        else: chip = "HOLD"
        rows.append({
            "ticker": t, "last": last, "day_pct": row.get("day_pct"), "avg": avg,
            "unreal": unreal, "weight": weight, "stop_lbl": stop_lbl, "dist_stop": dist_stop,
            "chip": chip, "thesis": p["thesis"], "thesis_note": p["thesis_note"], "shares": p["shares"],
        })
    rows.sort(key=lambda r: r["weight"], reverse=True)
    return rows, total_mv

# ----------------------------------------------------------------------------
# 4. POSTURE + WHAT CHANGED
# ----------------------------------------------------------------------------

def posture_line(prices, committed, trails, book):
    if prices["is_stale"]:
        return "Defensive", "Stale data: bullish actions suppressed until a fresh fetch."
    any_fired = any(r["state"] == "FIRED" for r in committed)
    any_armed_inval = any(r["type"] == "invalidation" and r["state"] == "ARMED" for r in committed)
    any_breach = any(tr["state"] == "BREACHED" for tr in trails)
    btc = prices["btc"].get("last"); eth_wk = prices.get("eth_weekly_close")
    macro_off = (btc is not None and btc < 55000) or (eth_wk is not None and eth_wk < 1500)
    if any_fired or macro_off:
        return "Defensive", "A committed rule has fired or macro is risk-off; act on fired rules first, no adds."
    if any_armed_inval or any_breach:
        return "Neutral", "Invalidation lines armed or a trail breached; hold and watch the named levels, no adds."
    return "Neutral", "No committed rule fired and no trail breached; hold the book, act only on the printed levels."

def what_changed(prices, committed, trails, prev_state, catalysts, fetched_date):
    lines = []
    cur = {r["id"]: r["state"] for r in committed}
    if prev_state:
        for r in committed:
            ps = prev_state.get(r["id"])
            if ps and ps != r["state"]:
                lines.append(f"{r['desc']}: {ps} -> {r['state']} ({r['live']})")
    else:
        for r in committed:
            if r["state"] in ("FIRED", "ARMED"):
                lines.append(f"{r['desc']} is {r['state']} ({r['live']})")
    for tr in trails:
        if tr["state"] == "BREACHED":
            lines.append(f"{tr['ticker']} tool trail breached ({tr['live']})")
    for c in catalysts.get("items", []):
        if c["date"] == fetched_date and c["relevance"] == "THESIS":
            lines.append(f"{c['ticker']} filing: {c['text'][:90]}")
    return lines[:3] if lines else ["No fired rules, no armed invalidations, no trail breaches since the last run."]

# ----------------------------------------------------------------------------
# 5. RENDER
# ----------------------------------------------------------------------------

def esc(s):
    return html.escape(str(s), quote=True)

def fmt_pct(v):
    return "N/A" if v is None else f"{v:+.1f}%"

def cls_pct(v):
    return "muted" if v is None else ("up" if v >= 0 else "down")

def render(prices, book, total_mv, committed, trails, posture, posture_note, changed, positions, date_stamp):
    stale = prices["is_stale"]
    src = prices["source"]
    health = prices.get("health", "red" if stale else "green")
    health_lbl = {"green": "LIVE", "amber": "FALLBACK SOURCE", "red": "STALE"}[health]
    fetched = prices["fetched_at"]
    btc = prices["btc"].get("last"); btc_d = prices["btc"].get("day_pct")
    eth = prices["eth"].get("last"); eth_d = prices["eth"].get("day_pct")
    eth_wk = prices.get("eth_weekly_close")

    def chip_cls(chip):
        return {"HOLD": "chip-hold", "RULE FIRED": "chip-fired",
                "INVALIDATION WATCH": "chip-watch", "TRAIL BREACHED": "chip-trail"}.get(chip, "chip-hold")
    def thesis_cls(th):
        return {"CONFIRMED": "th-conf", "PENDING": "th-pend", "SPECIAL-SIT": "th-spec"}.get(th, "th-pend")
    def state_cls(s):
        return {"CLEAR": "st-clear", "ARMED": "st-armed", "FIRED": "st-fired",
                "BREACHED": "st-fired", "N/A": "muted"}.get(s, "muted")

    # Your Book rows
    book_rows = ""
    for r in book:
        book_rows += (
            f'<tr><td class="tk">{esc(r["ticker"])}</td>'
            f'<td>{("$%.2f"%r["last"]) if r["last"] else "N/A"}</td>'
            f'<td class="{cls_pct(r["day_pct"])}">{fmt_pct(r["day_pct"])}</td>'
            f'<td>${r["avg"]:.2f}</td>'
            f'<td class="{cls_pct(r["unreal"])}">{fmt_pct(r["unreal"])}</td>'
            f'<td>{r["weight"]:.1f}%</td>'
            f'<td class="muted">{esc(r["stop_lbl"])}</td>'
            f'<td>{esc(r["dist_stop"])}</td>'
            f'<td><span class="chip {chip_cls(r["chip"])}">{esc(r["chip"])}</span></td>'
            f'<td><span class="th {thesis_cls(r["thesis"])}">{esc(r["thesis"])}</span> '
            f'<span class="muted tiny">{esc(r["thesis_note"])}</span></td></tr>\n'
        )

    # Rules
    def rule_block(r, bullish=False):
        suppressed = bullish and stale
        action = "" if suppressed else (f' &middot; <span class="act">{esc(r["action"])}</span>' if r.get("action") else "")
        sup = ' <span class="muted tiny">(bullish action suppressed on stale data)</span>' if suppressed else ""
        note = f'<div class="rnote">{esc(r["note"])}</div>' if r.get("note") else ""
        return (f'<div class="rule"><div class="rline"><span class="st {state_cls(r["state"])}">{esc(r["state"])}</span>'
                f'<strong>{esc(r["desc"])}</strong> <span class="rtk">{esc(r["ticker"])}</span>{action}{sup}</div>'
                f'<div class="rlive">{esc(r["live"])} &middot; <span class="muted">{esc(r["dist"])}</span></div>{note}</div>\n')

    committed_html = ""
    for r in committed:
        committed_html += rule_block(r, bullish=(r["type"] == "add_gate"))
    trails_html = ""
    for tr in trails:
        trails_html += (f'<div class="rule trail"><div class="rline"><span class="st {state_cls(tr["state"])}">{esc(tr["state"])}</span>'
                        f'<strong>{esc(tr["ticker"])} tool trail</strong> <span class="muted tiny">(not committed; watch only)</span></div>'
                        f'<div class="rlive">{esc(tr["live"])} &middot; <span class="muted">{esc(tr["dist"])}</span></div></div>\n')

    # Universe scoreboard
    uni_rows = ""
    for t in ap.ALL_TICKERS:
        row = prices["tickers"].get(t, {})
        tier = TIER.get(t, "btc")
        held = any(p["ticker"] == t for p in positions["positions"])
        macd = row.get("macd_dir")
        macd_html = '<span class="up">&uarr;</span>' if macd == "up" else ('<span class="down">&darr;</span>' if macd == "down" else "&mdash;")
        stk = row.get("stk_total") or 0
        sent_cell = f'{esc(row.get("sent_label") or "Quiet")} <span class="muted tiny">{row.get("stk_bull") or 0}/{row.get("stk_bear") or 0}</span>' if stk else '<span class="muted">N/A</span>'
        uni_rows += (
            f'<tr><td class="tk">{esc(t)}{" &#9733;" if held else ""} <span class="tier tier-{tier}">{tier}</span></td>'
            f'<td>{("$%.2f"%row["last"]) if row.get("last") else "N/A"}</td>'
            f'<td class="{cls_pct(row.get("day_pct"))}">{fmt_pct(row.get("day_pct"))}</td>'
            f'<td class="{cls_pct(row.get("p5"))}">{fmt_pct(row.get("p5"))}</td>'
            f'<td class="{cls_pct(row.get("p1m"))}">{fmt_pct(row.get("p1m"))}</td>'
            f'<td>{("%.0f"%row["rsi_d"]) if row.get("rsi_d") is not None else "N/A"}/{("%.0f"%row["rsi_w"]) if row.get("rsi_w") is not None else "N/A"}</td>'
            f'<td>{macd_html}</td>'
            f'<td>{row.get("ma_stack") if row.get("ma_stack") is not None else "N/A"}/4</td>'
            f'<td>{row.get("setup") if row.get("setup") is not None else "&mdash;"}</td>'
            f'<td>{row.get("pivot") if row.get("pivot") is not None else "&mdash;"}</td>'
            f'<td class="tiny">{sent_cell}</td></tr>\n'
        )

    # Catalysts
    cat = json.load(open(os.path.join(REPO, "catalysts.json")))
    items = sorted(cat["items"], key=lambda x: (x["relevance"] != "THESIS", x["date"] < "9999"), reverse=False)
    # held-name THESIS first, then by date desc
    items = sorted(cat["items"], key=lambda x: (0 if x["relevance"] == "THESIS" else 1, ), )
    items = sorted(items, key=lambda x: x["date"], reverse=True)
    items = sorted(items, key=lambda x: 0 if x["relevance"] == "THESIS" else 1)
    cat_rows = ""
    for c in items:
        rc = "rel-thesis" if c["relevance"] == "THESIS" else "rel-macro"
        trust = c.get("trust", "")
        tflag = f' <span class="muted tiny">[{esc(trust)}]</span>' if trust else ""
        cat_rows += (f'<div class="cat {rc}"><span class="cdate">{esc(c["date"])}</span> '
                     f'<span class="ctk">{esc(c["ticker"])}</span> <span class="crel">{esc(c["relevance"])}</span> '
                     f'{esc(c["text"])} <span class="muted tiny">- {esc(c.get("source",""))}{tflag}</span></div>\n')

    changed_html = "".join(f"<li>{esc(l)}</li>" for l in changed)
    posture_cls = {"Defensive": "p-def", "Neutral": "p-neu", "Constructive": "p-con"}.get(posture, "p-neu")
    pos_note = positions.get("note", "")
    cash = positions.get("cash", {})
    shown = len(positions["positions"]); total_pos = positions.get("reported_total_positions", shown)

    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Miner Analytics - {esc(date_stamp)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital@0;1&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0d1117;--card:#161b22;--bd:#21262d;--tx:#c9d1d9;--mut:#8b949e;--grn:#3fb950;--red:#f85149;--blu:#58a6ff;--yel:#d29922;--amb:#e3893f}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--tx);font-family:Inter,sans-serif;font-size:14px;line-height:1.5}}
.wrap{{max-width:1080px;margin:0 auto;padding:0 12px 60px}}
.tab-bar{{display:flex;justify-content:center;border-bottom:3px solid var(--bd);background:var(--card)}}
.tab-bar a{{padding:.7rem 1.6rem;font-weight:600;color:var(--mut);text-decoration:none;border-bottom:3px solid transparent;margin-bottom:-3px}}
.tab-bar a.active{{color:var(--blu);border-bottom-color:var(--blu)}}
h1{{font-family:Newsreader,serif;font-size:1.5rem;margin:.8rem 0 .2rem;letter-spacing:.04em}}
h2{{font-family:Newsreader,serif;font-size:1.15rem;border-bottom:1px solid var(--bd);padding-bottom:.3rem;margin:1.6rem 0 .6rem}}
.up{{color:var(--grn)}}.down{{color:var(--red)}}.muted{{color:var(--mut)}}.tiny{{font-size:.72rem}}
.banner{{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:.9rem 1rem;margin-top:.8rem}}
.health{{display:inline-block;font-weight:700;font-size:.72rem;padding:.18rem .6rem;border-radius:20px;letter-spacing:.05em}}
.h-green{{background:#13321d;color:var(--grn);border:1px solid var(--grn)}}
.h-amber{{background:#3a2c12;color:var(--amb);border:1px solid var(--amb)}}
.h-red{{background:#3a1614;color:var(--red);border:1px solid var(--red)}}
.posture{{font-size:1.05rem;font-weight:700;margin:.5rem 0 .2rem}}
.p-def{{color:var(--red)}}.p-neu{{color:var(--yel)}}.p-con{{color:var(--grn)}}
.changed{{margin:.3rem 0 0;padding-left:1.1rem}}.changed li{{margin:.15rem 0}}
table{{width:100%;border-collapse:collapse;font-size:.82rem}}
th,td{{text-align:right;padding:.4rem .45rem;border-bottom:1px solid var(--bd);white-space:nowrap}}
th:first-child,td:first-child{{text-align:left}}th{{color:var(--mut);font-weight:600;font-size:.7rem;text-transform:uppercase;letter-spacing:.03em}}
td:last-child,th:last-child{{text-align:left;white-space:normal}}
.tk{{font-weight:700}}
.chip{{font-weight:700;font-size:.68rem;padding:.12rem .45rem;border-radius:5px}}
.chip-hold{{background:#1c2430;color:var(--mut)}}.chip-fired{{background:#3a1614;color:var(--red)}}
.chip-watch{{background:#3a2c12;color:var(--yel)}}.chip-trail{{background:#222c1a;color:var(--amb)}}
.th{{font-weight:700;font-size:.66rem;padding:.1rem .4rem;border-radius:4px}}
.th-conf{{background:#13321d;color:var(--grn)}}.th-pend{{background:#3a2c12;color:var(--yel)}}.th-spec{{background:#222033;color:#b083f0}}
.tier{{font-size:.6rem;padding:.05rem .3rem;border-radius:4px;color:var(--mut);border:1px solid var(--bd)}}
.rules{{display:block}}.rule{{background:var(--card);border:1px solid var(--bd);border-left:3px solid var(--bd);border-radius:7px;padding:.55rem .7rem;margin:.4rem 0}}
.rule.trail{{opacity:.72;border-left-color:#30363d}}
.rline{{display:flex;flex-wrap:wrap;gap:.4rem;align-items:center}}
.rtk{{font-size:.66rem;color:var(--mut);border:1px solid var(--bd);padding:.04rem .35rem;border-radius:4px}}
.rlive{{font-size:.8rem;margin-top:.2rem}}.rnote{{font-size:.72rem;color:var(--mut);margin-top:.25rem}}
.act{{color:var(--blu);font-weight:600}}
.st{{font-weight:700;font-size:.66rem;padding:.1rem .4rem;border-radius:4px}}
.st-clear{{background:#13321d;color:var(--grn)}}.st-armed{{background:#3a2c12;color:var(--yel)}}.st-fired{{background:#3a1614;color:var(--red)}}
.committed-hd{{font-weight:700;color:var(--tx);margin-top:.4rem}}.trails-hd{{font-weight:700;color:var(--mut);margin-top:1rem}}
.cat{{background:var(--card);border:1px solid var(--bd);border-left:3px solid var(--bd);border-radius:6px;padding:.45rem .6rem;margin:.3rem 0;font-size:.82rem}}
.rel-thesis{{border-left-color:var(--blu)}}.rel-macro{{border-left-color:#30363d;opacity:.9}}
.cdate{{color:var(--mut);font-size:.72rem}}.ctk{{font-weight:700}}
.crel{{font-size:.62rem;padding:.05rem .3rem;border-radius:4px;background:#1c2430;color:var(--mut)}}
.scroll{{overflow-x:auto}}
.disc{{color:var(--mut);font-size:.72rem;margin-top:1.4rem;border-top:1px solid var(--bd);padding-top:.6rem}}
@media(max-width:640px){{th,td{{padding:.35rem .3rem;font-size:.74rem}}h1{{font-size:1.25rem}}}}
</style></head>
<body>
<div class="tab-bar"><a href="index.html">News</a><a href="miner-analytics.html" class="active">Miner Analytics</a></div>
<div class="wrap">
<h1>AI / HPC Miner Analytics</h1>
<div class="muted tiny">Glenda's IB book &middot; self-directed &middot; BTC miner-to-HPC pivot &middot; {esc(date_stamp)}</div>

<div class="banner">
<span class="health h-{health}">{health_lbl}</span>
<span class="muted tiny"> &middot; fetched {esc(fetched)} &middot; source {esc(src)} &middot; BTC ${(f"{btc:,.0f}" if btc else "N/A")} ({fmt_pct(btc_d)}) &middot; ETH ${(f"{eth:,.0f}" if eth else "N/A")} ({fmt_pct(eth_d)}) &middot; ETH wk close ${(f"{eth_wk:,.0f}" if eth_wk else "N/A")}</span>
<div class="posture {posture_cls}">Posture: {esc(posture)}</div>
<div class="muted">{esc(posture_note)}</div>
<div class="committed-hd tiny" style="margin-top:.5rem">What changed since the last run:</div>
<ul class="changed">{changed_html}</ul>
</div>

<h2>Your Book</h2>
<div class="muted tiny">{esc(pos_note)} Showing {shown} of {total_pos} reported positions. Cash: ${cash.get('USD','N/A')} USD (${cash.get('total_in_hkd','N/A')} total in HKD). Book market value ${total_mv:,.0f}.</div>
<div class="scroll"><table>
<thead><tr><th>Name</th><th>Live</th><th>Day</th><th>Avg cost</th><th>Unreal.</th><th>Weight</th><th>Trail/stop</th><th>Dist</th><th>Status</th><th>Thesis</th></tr></thead>
<tbody>{book_rows}</tbody></table></div>

<h2>Rules + Triggers</h2>
<div class="committed-hd">Committed plan</div>
<div class="rules">{committed_html}</div>
<div class="trails-hd">Tool trails <span class="muted tiny">(situational, not committed - a breach is a watch flag, never a sell)</span></div>
<div class="rules">{trails_html}</div>

<h2>Universe Scoreboard</h2>
<div class="muted tiny">15-name TA scan. &#9733; = held. Setup/Pivot 0-100. Sentiment from StockTwits (bull/bear).</div>
<div class="scroll"><table>
<thead><tr><th>Ticker</th><th>Last</th><th>Day</th><th>5d</th><th>1M</th><th>RSI D/W</th><th>MACD</th><th>MA</th><th>Setup</th><th>Pivot</th><th>Sentiment</th></tr></thead>
<tbody>{uni_rows}</tbody></table></div>

<h2>Catalysts + Filings</h2>
{cat_rows}

<div class="disc">Every price on this page traces to one fetch at {esc(fetched)} ({esc(src)}). Verdicts are computed from rules.yaml against live prices; nothing here is hand-authored. Source trust: SEC filings / Mike Alfred (SLNH) high; HC Wainwright and B. Riley conflicted (underwriter/lender); retail confirmation-only. Not financial advice. Owner's private analyst note.</div>
</div></body></html>"""

# ----------------------------------------------------------------------------
# MAIN
# ----------------------------------------------------------------------------

def main():
    ap_arg = argparse.ArgumentParser()
    ap_arg.add_argument("--date", default=dt.date.today().isoformat())
    ap_arg.add_argument("--fetch-only", action="store_true")
    ap_arg.add_argument("--render-only", action="store_true")
    args = ap_arg.parse_args()

    pp = os.path.join(REPO, "prices.json")
    if args.render_only:
        prices = json.load(open(pp))
    else:
        prices = consolidated_fetch()
        json.dump(prices, open(pp, "w"), indent=2)
        print(f"prices.json written; ta_valid={prices['ta_valid']}/{prices['universe_size']}; source={prices['source']}; stale={prices['is_stale']}")
        if args.fetch_only:
            return

    rules = yaml.safe_load(open(os.path.join(REPO, "rules.yaml")))
    positions = json.load(open(os.path.join(REPO, "positions.json")))
    catalysts = json.load(open(os.path.join(REPO, "catalysts.json")))

    committed, trails = evaluate_rules(prices, rules, positions)
    book, total_mv = build_book(prices, positions, committed, trails)
    posture, posture_note = posture_line(prices, committed, trails, book)

    prev_path = os.path.join(REPO, "rule_state_prev.json")
    prev_state = json.load(open(prev_path)) if os.path.exists(prev_path) else None
    fetched_date = prices["fetched_at"][:10]
    changed = what_changed(prices, committed, trails, prev_state, catalysts, fetched_date)
    json.dump({r["id"]: r["state"] for r in committed}, open(prev_path, "w"), indent=2)

    html_doc = render(prices, book, total_mv, committed, trails, posture, posture_note, changed, positions, args.date)
    open(os.path.join(REPO, "miner-analytics.html"), "w").write(html_doc)
    print(f"Wrote miner-analytics.html ({len(html_doc)} bytes); posture={posture}; "
          f"stale={prices['is_stale']}; ta_valid={prices['ta_valid']}/{prices['universe_size']}")
    fired = [r['id'] for r in committed if r['state'] == 'FIRED']
    armed = [r['id'] for r in committed if r['state'] == 'ARMED']
    print("FIRED:", fired or "none", "| ARMED:", armed or "none")

if __name__ == "__main__":
    main()
