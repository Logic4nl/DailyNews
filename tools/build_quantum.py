#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quantum short-term rotation sleeve dashboard.
Single timestamped fetch -> quantum_prices.json. Live-gated entry/exit/invalidation
computed from QTUM relative strength vs SPY. No hand-authored verdict or action text.
Mirrors the miner dashboard global rules: one fetch per run, freshness gating,
degrade-not-freeze, never print a bullish action on stale data.
"""
import os, sys, json, html, datetime, argparse
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
def P(name): return os.path.join(ROOT, name)

def esc(s): return html.escape(str(s), quote=True)

def load_cfg():
    rules = yaml.safe_load(open(P("quantum_rules.yaml")))
    book = json.load(open(P("quantum_positions.json")))
    return rules, book

def fetch(rules):
    import yfinance as yf
    v = rules["vehicles"]; b = rules["benchmarks"]
    vehicles = v["core"] + v["beta_boosters"] + v["crypto_adjacent"] + v["nanos"]
    bench = [b["spy"]] + b["defensives"] + b["high_beta"]
    macro = ["BTC-USD", "2YY=F", "^IRX"]
    tickers = list(dict.fromkeys(vehicles + bench + macro))
    data = yf.download(tickers, period="3mo", interval="1d",
                       auto_adjust=True, progress=False, threads=True)
    # Extract Close frame robustly
    close = data["Close"] if "Close" in data.columns.get_level_values(0) else data
    out = {}
    for t in tickers:
        try:
            s = close[t].dropna()
            out[t] = [round(float(x), 6) for x in s.tolist()][-40:]
        except Exception:
            out[t] = []
    price_ok = len(out.get(b["spy"], [])) >= 21 and len(out.get("QTUM", [])) >= 21
    snap = {
        "fetched_at": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "source": "yfinance",
        "is_stale": (not price_ok),
        "series": out,
    }
    json.dump(snap, open(P("quantum_prices.json"), "w"), indent=2)
    print("quantum_prices.json written; price_ok=%s; tickers=%d" % (price_ok, len(out)))
    return snap

# ---- analytics ----
def pct(series, n):
    if len(series) < n + 1: return None
    a, b = series[-1], series[-1 - n]
    if b == 0: return None
    return (a / b - 1.0) * 100.0

def rel_pct(t, spy, n):
    """Relative-strength change of t vs spy over n sessions, in percent."""
    if len(t) < n + 1 or len(spy) < n + 1: return None
    rel_now = t[-1] / spy[-1]
    rel_then = t[-1 - n] / spy[-1 - n]
    if rel_then == 0: return None
    return (rel_now / rel_then - 1.0) * 100.0

def fmt(x, suff="", dp=2):
    return "N/A" if x is None else ("%+.*f%s" % (dp, x, suff) if suff == "%" else "%.*f%s" % (dp, x, suff))

def sign_class(x):
    if x is None: return "mut"
    return "grn" if x > 0 else ("red" if x < 0 else "mut")

def build(date_iso):
    rules, book = load_cfg()
    snap = json.load(open(P("quantum_prices.json")))
    S = snap["series"]; stale = snap.get("is_stale", False)
    spy = S.get("SPY", [])
    qtum = S.get("QTUM", [])

    # QTUM relative strength vs SPY
    q1 = rel_pct(qtum, spy, 1); q5 = rel_pct(qtum, spy, 5); q20 = rel_pct(qtum, spy, 20)

    def gate_state():
        if None in (q5, q20): return "NO DATA"
        if q20 > 0 and q5 > 0 and (q1 or 0) > 0: return "IMPROVING"
        if q20 > 0 and q5 <= 0: return "ROLLING OVER"
        if q20 <= 0 and q5 > 0: return "BASING"
        return "LAGGING"
    gstate = gate_state()
    entry_confirmed = (q1 is not None and q5 is not None and q20 is not None and q1 > 0 and q5 > 0 and q20 > 0)
    chase_blocked = (q5 is not None and q5 < 0)

    # Secondary confirm: defensives stop Leading, high-beta firms up
    defs = rules["benchmarks"]["defensives"]; hb = rules["benchmarks"]["high_beta"]
    def_leading = []
    for d in defs:
        r5 = rel_pct(S.get(d, []), spy, 5); r20 = rel_pct(S.get(d, []), spy, 20)
        if r5 is not None and r20 is not None and r5 > 0 and r20 > 0:
            def_leading.append(d)
    hb_vals = [rel_pct(S.get(h, []), spy, 5) for h in hb]
    hb_firming = all(x is not None and x > 0 for x in hb_vals) if hb_vals else False
    secondary_ok = (len(def_leading) == 0) and hb_firming

    # Invalidation
    btc = S.get("BTC-USD", [])
    btc_last = btc[-1] if btc else None
    btc_break = (btc_last is not None and btc_last < rules["invalidation"]["btc_breakdown_below"])
    # 2yr yield proxy: prefer 2YY=F (yield), fallback ^IRX
    y_series = S.get("2YY=F", []) or S.get("^IRX", [])
    y_src = "2YY=F" if S.get("2YY=F", []) else ("^IRX (13wk proxy)" if S.get("^IRX", []) else None)
    y_5d_bps = None
    if len(y_series) >= 6:
        y_5d_bps = (y_series[-1] - y_series[-6]) * 100.0   # yield levels in %, *100 -> bps
    rates_spike = (y_5d_bps is not None and y_5d_bps > rules["invalidation"]["rates_2y_spike_bps"])
    qtum_20d_neg = (q20 is not None and q20 < 0)
    inval_reasons = []
    if btc_break: inval_reasons.append("BTC < 55k")
    if rates_spike: inval_reasons.append("2yr yield spike")
    if qtum_20d_neg: inval_reasons.append("QTUM 20D rel negative")
    invalidated = len(inval_reasons) > 0

    positions = book.get("positions", [])
    flat = (len(positions) == 0)

    # Verdict (computed; bullish actions suppressed on stale data)
    if stale:
        verdict = "STALE DATA - stand aside, no entry"; posture = "Defensive"; vclass = "red"
    elif invalidated:
        verdict = "INVALIDATED - rotation killed: " + ", ".join(inval_reasons); posture = "Defensive"; vclass = "red"
    elif not flat:
        verdict = "POSITION OPEN - manage to exits below"; posture = "Constructive"; vclass = "grn"
    elif entry_confirmed and secondary_ok:
        verdict = "ENTER - full sleeve eligible (3-5%)"; posture = "Constructive"; vclass = "grn"
    elif entry_confirmed and not secondary_ok:
        verdict = "ENTER STARTER ONLY - primary OK, secondary unconfirmed (1/3)"; posture = "Neutral"; vclass = "yel"
    elif chase_blocked:
        verdict = "STAND ASIDE - 5D rel negative, do not chase. 1/3 probe optional, tight stop"; posture = "Neutral"; vclass = "yel"
    else:
        verdict = "WATCH - primary trigger not yet confirmed"; posture = "Neutral"; vclass = "yel"

    # What changed vs previous run
    prev_path = P("quantum_state_prev.json")
    prev = {}
    if os.path.exists(prev_path):
        try: prev = json.load(open(prev_path))
        except Exception: prev = {}
    changes = []
    if not prev:
        changes.append("Quantum sleeve module initialized.")
    else:
        if prev.get("gate") != gstate:
            changes.append("Gate state %s -> %s" % (prev.get("gate", "?"), gstate))
        if prev.get("verdict") != verdict:
            changes.append("Verdict updated")
        if prev.get("invalidated") != invalidated and invalidated:
            changes.append("INVALIDATION fired: " + ", ".join(inval_reasons))
    if not changes:
        changes.append("No change in gate, verdict or invalidation since last run.")
    json.dump({"gate": gstate, "verdict": verdict, "invalidated": invalidated,
               "date": date_iso}, open(prev_path, "w"), indent=2)

    htmlout = render(rules, book, snap, date_iso, dict(
        q1=q1, q5=q5, q20=q20, gstate=gstate, entry_confirmed=entry_confirmed,
        chase_blocked=chase_blocked, def_leading=def_leading, hb_vals=hb_vals,
        hb=hb, defs=defs, secondary_ok=secondary_ok, btc_last=btc_last,
        btc_break=btc_break, y_5d_bps=y_5d_bps, y_src=y_src, rates_spike=rates_spike,
        qtum_20d_neg=qtum_20d_neg, invalidated=invalidated, inval_reasons=inval_reasons,
        verdict=verdict, posture=posture, vclass=vclass, changes=changes, flat=flat, stale=stale))
    open(P("quantum.html"), "w", encoding="utf-8").write(htmlout)
    print("quantum.html written (%d bytes); gate=%s; verdict=%s; stale=%s" % (len(htmlout), gstate, verdict, stale))

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#0d1117;--card:#161b22;--bd:#21262d;--tx:#c9d1d9;--mut:#8b949e;--grn:#3fb950;--red:#f85149;--blu:#58a6ff;--yel:#d29922}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--tx);line-height:1.55}
.tab-bar{display:flex;justify-content:center;border-bottom:3px solid var(--bd);background:var(--card)}
.tab-bar a{padding:.7rem 1.6rem;font-weight:600;color:var(--mut);text-decoration:none;border-bottom:3px solid transparent;margin-bottom:-3px;font-size:.9rem}
.tab-bar a:hover{color:var(--tx)}
.tab-bar a.active{color:var(--blu);border-bottom-color:var(--blu)}
.wrap{max-width:1100px;margin:0 auto;padding:1.2rem}
h1{font-family:'Newsreader',serif;font-size:1.7rem;margin:.2rem 0}
h2{font-size:1.05rem;margin:1.4rem 0 .6rem;color:var(--blu);border-bottom:1px solid var(--bd);padding-bottom:.3rem}
.sub{color:var(--mut);font-size:.82rem;margin-bottom:.8rem}
.banner{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:1rem 1.1rem;margin-top:.8rem}
.chip{display:inline-block;padding:.18rem .55rem;border-radius:6px;font-size:.72rem;font-weight:700;letter-spacing:.02em}
.c-grn{background:#3fb95022;color:var(--grn)} .c-red{background:#f8514922;color:var(--red)} .c-yel{background:#d2992222;color:var(--yel)} .c-blu{background:#58a6ff22;color:var(--blu)} .c-mut{background:#8b949e22;color:var(--mut)}
.verdict{font-size:1.15rem;font-weight:700;margin:.5rem 0}
.grn{color:var(--grn)} .red{color:var(--red)} .yel{color:var(--yel)} .blu{color:var(--blu)} .mut{color:var(--mut)}
.changes{margin:.5rem 0 0;padding-left:1.1rem} .changes li{font-size:.85rem;margin:.15rem 0;color:var(--mut)}
table{width:100%;border-collapse:collapse;font-size:.83rem;margin-top:.4rem}
th,td{padding:.42rem .5rem;text-align:right;border-bottom:1px solid var(--bd)}
th:first-child,td:first-child{text-align:left}
th{color:var(--mut);font-weight:600;font-size:.74rem;text-transform:uppercase;letter-spacing:.03em}
.role{color:var(--mut);font-size:.74rem}
.card{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:.9rem 1rem;margin-top:.6rem}
.kv{display:flex;justify-content:space-between;padding:.25rem 0;border-bottom:1px solid var(--bd);font-size:.85rem}
.kv:last-child{border-bottom:none}
.note{color:var(--mut);font-size:.8rem;margin-top:.5rem;font-style:italic}
.foot{color:var(--mut);font-size:.75rem;margin-top:1.6rem;border-top:1px solid var(--bd);padding-top:.7rem}
"""

def render(rules, book, snap, date_iso, d):
    def cell(x, suff="%", dp=2):
        return '<td class="%s">%s</td>' % (sign_class(x), fmt(x, suff, dp))
    health_chip = ('<span class="chip c-red">STALE</span>' if d["stale"]
                   else '<span class="chip c-grn">LIVE</span>')
    # Entry gate table
    def gd(x):  # distance/sign helper text
        return fmt(x, "%")
    gate_rows = (
        '<tr><td>QTUM rel vs SPY (1D)</td>%s<td class="mut">turn positive to arm</td></tr>'
        '<tr><td>QTUM rel vs SPY (5D)</td>%s<td class="mut">must be positive, do not chase if negative</td></tr>'
        '<tr><td>QTUM rel vs SPY (20D)</td>%s<td class="mut">must stay positive (else structurally lagging)</td></tr>'
        % (cell(d["q1"]), cell(d["q5"]), cell(d["q20"]))
    )
    gate_chip = {"IMPROVING":"c-grn","ROLLING OVER":"c-yel","BASING":"c-blu","LAGGING":"c-red","NO DATA":"c-mut"}.get(d["gstate"],"c-mut")

    # Secondary confirm
    sec_def = "none leading" if not d["def_leading"] else (", ".join(d["def_leading"]) + " still leading")
    sec_def_ok = (len(d["def_leading"]) == 0)
    hb_txt = ", ".join("%s %s" % (h, fmt(v, "%")) for h, v in zip(d["hb"], d["hb_vals"]))
    sec_rows = (
        '<tr><td>Defensives (XLV/XLP/XLU)</td><td class="%s">%s</td><td class="mut">want them to stop leading</td></tr>'
        '<tr><td>High-beta (IGV/SMH) 5D rel</td><td>%s</td><td class="mut">want firming (positive)</td></tr>'
        % ("grn" if sec_def_ok else "red", sec_def, hb_txt)
    )

    # Sleeve book
    if d["flat"]:
        book_html = ('<div class="card"><div class="kv"><span>Sleeve state</span><span class="yel">FLAT - no position</span></div>'
                     '<div class="kv"><span>Sizing budget</span><span>%d-%d%% of risk capital (50%% drawdown survivable)</span></div>'
                     '<div class="kv"><span>Starter probe cap</span><span>1/3 sleeve, tight stop</span></div>'
                     '<div class="kv"><span>Funding</span><span>miner / HPC trims only, not ETH capital</span></div>'
                     '<p class="note">%s</p></div>'
                     % (rules["sizing"]["sleeve_pct_low"], rules["sizing"]["sleeve_pct_high"], esc(book.get("note",""))))
    else:
        rows = ""
        for p in book["positions"]:
            rows += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (
                esc(p.get("ticker")), esc(p.get("shares")), esc(p.get("avg")), esc(p.get("role","")))
        book_html = ('<table><tr><th>Ticker</th><th>Shares</th><th>Avg</th><th>Role</th></tr>%s</table>'
                     '<p class="note">Exits: stop %d%% (band %s), scale 1/3 on first +%d%% pop then trail, time stop %d weeks.</p>'
                     % (rows, rules["exits"]["sleeve_stop_pct"], rules["exits"]["sleeve_stop_band"],
                        rules["exits"]["take_profit_first_pop_pct"], rules["exits"]["time_stop_weeks"]))

    # Vehicle watchlist
    S = snap["series"]; spy = S.get("SPY", [])
    v = rules["vehicles"]
    groups = [("Core (theme)", v["core"]), ("Beta boosters (equal weight)", v["beta_boosters"]),
              ("Crypto-adjacent", v["crypto_adjacent"]), ("Nanos (token-watch, never sized)", v["nanos"])]
    wrows = ""
    for label, tl in groups:
        wrows += '<tr><td colspan="5" class="role">%s</td></tr>' % esc(label)
        for t in tl:
            s = S.get(t, [])
            last = ("%.2f" % s[-1]) if s else "N/A"
            day = pct(s, 1); r5 = pct(s, 5); rel5 = rel_pct(s, spy, 5)
            wrows += "<tr><td>%s</td><td>%s</td>%s%s%s</tr>" % (
                t, last, _c(day), _c(r5), _c(rel5))

    # Invalidation / macro
    def flag(ok_clear, label, val):
        chip = '<span class="chip c-grn">CLEAR</span>' if ok_clear else '<span class="chip c-red">TRIGGERED</span>'
        return '<div class="kv"><span>%s</span><span>%s &nbsp; %s</span></div>' % (esc(label), esc(val), chip)
    btc_val = ("${:,.0f}".format(d["btc_last"])) if d["btc_last"] else "N/A"
    y_val = ("%s, 5D %s bps" % (d["y_src"], fmt(d["y_5d_bps"], "", 1))) if d["y_src"] else "N/A"
    q20_val = fmt(d["q20"], "%")
    inval_html = (flag(not d["btc_break"], "BTC breakdown < 55k", btc_val)
                  + flag(not d["rates_spike"], "2yr yield spike (>25 bps/5D)", y_val)
                  + flag(not d["qtum_20d_neg"], "QTUM 20D rel negative", q20_val))

    changes_li = "".join("<li>%s</li>" % esc(c) for c in d["changes"])

    return ("""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Quantum Rotation - %s</title>
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Crect width='32' height='32' rx='6' fill='%%230d1117'/%%3E%%3Ctext x='16' y='22' font-family='Georgia,serif' font-size='14' font-weight='bold' fill='%%2358a6ff' text-anchor='middle'%%3EQ%%3C/text%%3E%%3C/svg%%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:wght@400;600;700&display=swap" rel="stylesheet">
<style>%s</style></head><body>
<div class="tab-bar"><a href="index.html">News</a><a href="miner-analytics.html">Miner Analytics</a><a href="quantum.html" class="active">Quantum</a></div>
<div class="wrap">
<h1>Quantum Short-Term Rotation</h1>
<div class="sub">Tactical satellite sleeve inside the AI/HPC book. This is a trade, not a hold. %s</div>

<div class="banner">
  <div>%s &nbsp; <span class="chip c-blu">Posture: %s</span> &nbsp; <span class="chip %s">Gate: %s</span></div>
  <div class="verdict %s">%s</div>
  <div class="sub">Fetched %s &middot; source %s</div>
  <ul class="changes">%s</ul>
</div>

<h2>1 &middot; Entry Gate (confirmation-gated)</h2>
<table><tr><th>Signal</th><th>Live</th><th>Rule</th></tr>%s</table>
<div class="card">%s</div>
<p class="note">Primary trigger: QTUM rel strength flips Rolling over to Improving (1D and 5D rel positive, 20D positive). Immediate-entry option: a 1/3 starter probe before confirmation, treated as a probe with a tight stop.</p>

<h2>2 &middot; Sleeve Book</h2>
%s

<h2>3 &middot; Vehicle Watchlist</h2>
<table><tr><th>Ticker</th><th>Last</th><th>Day %%</th><th>5D %%</th><th>5D rel vs SPY</th></tr>%s</table>

<h2>4 &middot; Invalidation + Macro</h2>
<div class="card">%s</div>
<p class="note">Any one invalidation kills the rotation: recycle capital back to the HPC book.</p>

<div class="foot">
Sizing: total sleeve %d-%d%% of risk capital, sized so a 50%% sleeve drawdown is survivable. Single nano name stays tiny.<br>
Exits: stop -15 to -20%% on the sleeve or QTUM 5D rel rolling back negative, whichever first. Scale out 1/3 on first +20-30%% pop, trail the rest. Time stop 4-6 weeks with no relative outperformance.<br>
Book interaction: %s<br>
Generated from one timestamped fetch. No price, verdict or action string is hand-authored. Not investment advice.
</div>
</div></body></html>""" % (
        esc(date_iso), CSS,
        esc(book.get("source","")),
        health_chip, esc(d["posture"]), ("c-grn" if d["vclass"]=="grn" else "c-red" if d["vclass"]=="red" else "c-yel"), esc(d["gstate"]),
        d["vclass"], esc(d["verdict"]),
        esc(snap["fetched_at"]), esc(snap["source"]), changes_li,
        gate_rows, sec_rows_block(sec_rows),
        book_html, wrows, inval_html,
        rules["sizing"]["sleeve_pct_low"], rules["sizing"]["sleeve_pct_high"],
        esc(rules["book_interaction"]),
    ))

def sec_rows_block(sec_rows):
    return ('<table style="margin-top:.6rem"><tr><th>Secondary confirm</th><th>Live</th><th>Want</th></tr>%s</table>' % sec_rows)

def _c(x):
    return '<td class="%s">%s</td>' % (sign_class(x), fmt(x, "%"))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fetch-only", action="store_true")
    ap.add_argument("--render-only", action="store_true")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    rules, _ = load_cfg()
    if a.fetch_only:
        fetch(rules)
    elif a.render_only:
        build(a.date)
    else:
        fetch(rules); build(a.date)
