#!/usr/bin/env python3
"""
refresh_dashboard.py — refresh miner-analytics.html in place using analytics_snapshot.json.

Reads the snapshot the analytics pipeline produced and patches the dashboard's
TA Scoreboard rows, Core Holdings Live pills + P&L, Sentiment Cockpit cards,
disclaimer timestamp, and date headers. All other sections (Market Summary,
Reference fold, Alert Feed, SEC Filings, Peer Heatmap, TradingView charts)
are left intact for the daily-morning-journal task to edit by hand if needed.

Usage:
    python3 tools/refresh_dashboard.py                 # uses today's UTC date
    python3 tools/refresh_dashboard.py --date 2026-05-08

Exit codes:
    0 — wrote a refreshed dashboard
    2 — refused to edit (dashboard missing or didn't pass sanity checks)
"""
from __future__ import annotations

import argparse
import html.parser as hp
import json
import os
import re
import sys
from datetime import datetime, timezone


# ---------------------------------------------------------------------------
# CLI / paths
# ---------------------------------------------------------------------------

def repo_root() -> str:
    """Return the repo root by walking up from this file."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(here)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--date", default=None, help="Date YYYY-MM-DD (default: today UTC)")
    p.add_argument("--repo", default=None, help="Path to repo (default: parent of this script)")
    return p.parse_args()


# ---------------------------------------------------------------------------
# Style helpers
# ---------------------------------------------------------------------------

def setup_class(s):
    if s is None: return "sc-stale"
    if s >= 80: return "sc-great"
    if s >= 60: return "sc-good"
    if s >= 40: return "sc-mid"
    return "sc-warn"


def pivot_class(s, hype):
    if s is None: return "sc-stale"
    if s >= 85 and hype in ("Mania", "Distribution"): return "sc-late"
    if s >= 80: return "sc-great"
    if s >= 60: return "sc-good"
    if s >= 40: return "sc-mid"
    return "sc-warn"


def hype_class(h):
    return {
        "Quiet": "hs-0",
        "Building": "hs-1",
        "Hot": "hs-2",
        "Mania": "hs-3",
        "Distribution": "hs-4",
    }.get(h, "hs-2")


def sent_class(label):
    if label in ("Retail euphoria", "Heavy bullish"): return "sent-eup"
    if label in ("Bullish lean", "Bullish"): return "sent-bull"
    if label in ("Bearish lean", "Bearish"): return "sent-bear"
    if label == "Mixed": return "sent-mix"
    return "sent-quiet"


def fmt_pct(v):
    return "N/A" if v is None else f"{v:+.1f}%"


def rsi_class(r):
    if r is None or r < 40: return "rsi-cool"
    if r >= 80: return "rsi-extreme"
    if r >= 70: return "rsi-hot"
    if r >= 60: return "rsi-warm"
    return "rsi-cool"


def macd_arrow(t):
    m, s = t.get("macd_macd"), t.get("macd_signal")
    if m is None or s is None: return ('down', '↓')
    return ('up', '↑') if m > s else ('down', '↓')


def ma_stack_text(t):
    c = t.get("last_close"); s20 = t.get("sma20"); s50 = t.get("sma50"); s200 = t.get("sma200")
    if None in (c, s20, s50, s200): return "N/A"
    n = sum([c > s20, c > s50, c > s200, s50 > s200])
    return f"{n}/4"


# ---------------------------------------------------------------------------
# Ticker tier map (used to render the scoreboard rows)
# ---------------------------------------------------------------------------
TIER_MAP = {
    "CIFR": "core", "IREN": "core", "SLNH": "core", "BGDE": "core",
    "WULF": "pivot", "CORZ": "pivot", "HUT": "pivot", "CLSK": "pivot", "APLD": "pivot",
    "MARA": "btc", "RIOT": "btc", "BTDR": "btc", "BITF": "btc", "BTBT": "core", "HIVE": "btc",
}


# ---------------------------------------------------------------------------
# Main refresh logic
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    repo = args.repo or repo_root()
    date_iso = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    weekday_human = datetime.strptime(date_iso, "%Y-%m-%d").strftime("%A, %B %-d, %Y")

    html_path = os.path.join(repo, "miner-analytics.html")
    snapshot_path = os.path.join(repo, "analytics_snapshot.json")
    entry_path = os.path.join(repo, "entry_prices.json")

    with open(snapshot_path) as f:
        snap = json.load(f)
    by_ticker = {r["ticker"]: r for r in snap["tickers"]}

    with open(entry_path) as f:
        entries = json.load(f)["avg_prices"]

    with open(html_path) as f:
        doc = f.read()

    # Sanity checks before editing
    if "AI / HPC Analytics" not in doc:
        print("ERROR: file does not look like the dashboard", file=sys.stderr)
        return 2
    if len(doc) < 30000:
        print("ERROR: dashboard is too small", file=sys.stderr)
        return 2

    # -- Disclaimer ----------------------------------------------------------
    gen = snap["generated_at_utc"]
    new_disc = (
        f'<div class="disclaimer">TA snapshot fetched <strong>{gen} UTC</strong> '
        f'· Price &amp; P&amp;L overlay refreshed <strong>{date_iso}</strong> '
        f'via TradingView screener. Social signals from StockTwits + Reddit. '
        f'Charts stream live from TradingView. Composite scores (Setup, Pivot Conviction, Hype Stage) '
        f'are computed locally from public indicators; weights documented in /tools/README.md. '
        f'Not financial advice.</div>'
    )
    doc = re.sub(
        r'<div class="disclaimer">TA snapshot fetched.*?Not financial advice\.</div>',
        new_disc, doc, count=1, flags=re.DOTALL,
    )

    # Drop any temporary "Today's refresh" callout banner from prior runs
    doc = re.sub(
        r'<div style="background:#1f2a3d[^>]*>\s*<strong[^>]*>Today\'s refresh:.*?</div>\s*',
        '', doc, count=1, flags=re.DOTALL,
    )

    # -- TA Scoreboard rows --------------------------------------------------
    def pull_existing_perf(ticker):
        """Carry forward 5d / 1m perf from the existing row (snapshot doesn't track these)."""
        pat = re.compile(
            r'<tr>\s*<td><strong>' + ticker + r'</strong>.*?'
            r'<td class="(?:up|down)">([+\-\d\.]+)%</td>\s*'
            r'<td class="(?:up|down)">([+\-\d\.]+)%</td>\s*'
            r'<td class="(?:up|down)">([+\-\d\.]+)%</td>',
            re.DOTALL,
        )
        m = pat.search(doc)
        return (float(m.group(2)), float(m.group(3))) if m else (0.0, 0.0)

    def avg_pnl_cells(ticker, close):
        avg = entries.get(f"NASDAQ:{ticker}")
        if avg is None:
            return '<td class="muted">\u2014</td>\n<td class="muted">\u2014</td>\n'
        pnl = (close - avg) / avg * 100
        pc = 'up' if pnl >= 0 else 'down'
        return f'<td>${avg:,.2f}</td>\n<td class="{pc}">{fmt_pct(pnl)}</td>\n'

    def build_row(ticker, tier, p5, p1m):
        rec = by_ticker.get(ticker)
        if not rec or rec["ta"].get("last_close") is None:
            return None
        ta = rec["ta"]; sc = rec["scores"]
        close = ta["last_close"]; chg = ta.get("daily_change_pct") or 0
        rsi_d = ta.get("rsi_d") or 0; rsi_w = ta.get("rsi_w") or 0
        setup = sc.get("setup"); pivot = sc.get("pivot")
        hype = sc.get("hype_stage", "Hot"); label = sc.get("sentiment_label", "Mixed")
        mc, ms = macd_arrow(ta)
        cc = "up" if chg >= 0 else "down"
        p5c = "up" if p5 >= 0 else "down"
        p1c = "up" if p1m >= 0 else "down"
        return (
            f'<tr>\n'
            f'<td><strong>{ticker}</strong> <span class="tier-{tier}">{tier}</span></td>\n'
            f'<td>${close:,.2f}</td>\n'
            f'{avg_pnl_cells(ticker, close)}'
            f'<td class="{cc}">{fmt_pct(chg)}</td>\n'
            f'<td class="{p5c}">{fmt_pct(p5)}</td>\n<td class="{p1c}">{fmt_pct(p1m)}</td>\n'
            f'<td class="{rsi_class(rsi_d)}">{rsi_d:.1f}</td>\n'
            f'<td class="{rsi_class(rsi_w)}">{rsi_w:.1f}</td>\n'
            f'<td class="{mc}">{ms}</td>\n<td>{ma_stack_text(ta)}</td>\n'
            f'<td class="{setup_class(setup)}">{setup if setup is not None else "—"}</td>\n'
            f'<td class="{pivot_class(pivot,hype)}">{pivot if pivot is not None else "—"}</td>\n'
            f'<td class="{hype_class(hype)}">{hype}</td>\n'
            f'<td class="{sent_class(label)}">{label}</td>\n'
            f'</tr>'
        )

    for ticker, tier in TIER_MAP.items():
        p5, p1m = pull_existing_perf(ticker)
        row = build_row(ticker, tier, p5, p1m)
        if row is None:
            continue
        pat = re.compile(
            r'<tr>\s*<td><strong>' + ticker + r'</strong>[^<]*<span class="tier-[a-z]+">[a-z]+</span></td>.*?</tr>',
            re.DOTALL,
        )
        doc, _ = pat.subn(row, doc, count=1)

    # BITF "No TA data available" placeholder — replace if we have data
    if by_ticker.get("BITF", {}).get("ta", {}).get("last_close") is not None:
        bitf_row = build_row("BITF", "btc", 0.0, 0.0)
        if bitf_row:
            doc = doc.replace(
                '<tr><td><strong>BITF</strong></td><td colspan="11" class="muted">No TA data available</td></tr>',
                bitf_row,
            )

    # -- Core Holdings Live cards -------------------------------------------
    def update_core(ticker):
        nonlocal doc
        rec = by_ticker.get(ticker)
        if not rec or rec["ta"].get("last_close") is None:
            return
        ta = rec["ta"]; sc = rec["scores"]
        close = ta["last_close"]; chg = ta.get("daily_change_pct") or 0
        rsi_d = ta.get("rsi_d") or 0; rsi_w = ta.get("rsi_w") or 0
        setup = sc.get("setup"); pivot = sc.get("pivot")
        hype = sc.get("hype_stage", "Hot"); label = sc.get("sentiment_label", "Mixed")
        cc = "up" if chg >= 0 else "down"

        # Match the full core-card. Try with catalyst-line first, then fallback to action-line only.
        for tail in ('catalyst-line', 'action-line'):
            pat = re.compile(
                r'(<div class="core-card">\s*<div class="core-head">\s*<div class="core-ticker">'
                + ticker + r'</div>.*?<div class="' + tail + r'">.*?</div>\s*</div>\s*</div>)',
                re.DOTALL,
            )
            m = pat.search(doc)
            if m:
                break
        else:
            return

        card = m.group(1)
        new = card

        new = re.sub(
            r'<div class="fund-row"><span class="label">Last</span><span class="value">\$[\d\.,]+ <span class="(?:up|down)" style="font-size:0\.72rem">[+\-\d\.]+%</span></span></div>',
            f'<div class="fund-row"><span class="label">Last</span><span class="value">${close:,.2f} <span class="{cc}" style="font-size:0.72rem">{fmt_pct(chg)}</span></span></div>',
            new, count=1,
        )
        new = re.sub(
            r'<div class="fund-row"><span class="label">RSI \(D / W\)</span><span class="value"><span class="rsi-[a-z]+">[\d\.]+</span> / <span class="rsi-[a-z]+">[\d\.]+</span></span></div>',
            f'<div class="fund-row"><span class="label">RSI (D / W)</span><span class="value"><span class="{rsi_class(rsi_d)}">{rsi_d:.1f}</span> / <span class="{rsi_class(rsi_w)}">{rsi_w:.1f}</span></span></div>',
            new, count=1,
        )
        new = re.sub(
            r'<div class="fund-row"><span class="label">MA Stack</span><span class="value">\d / \d</span></div>',
            f'<div class="fund-row"><span class="label">MA Stack</span><span class="value">{ma_stack_text(ta).replace("/", " / ")}</span></div>',
            new, count=1,
        )

        sb = (
            f'<div class="score-block">\n'
            f'<div class="score-pill {setup_class(setup)}">Setup <strong>{setup if setup is not None else "—"}</strong></div>\n'
            f'<div class="score-pill {pivot_class(pivot,hype)}">Pivot <strong>{pivot if pivot is not None else "—"}</strong></div>\n'
            f'<div class="score-pill {hype_class(hype)}">{hype}</div>\n'
            f'<div class="score-pill {sent_class(label)}">{label}</div>\n'
            f'</div>'
        )
        new = re.sub(
            r'<div class="score-block">.*?</div>\s*(?=<div class="action-line">)',
            sb + '\n', new, count=1, flags=re.DOTALL,
        )

        avg = entries.get(f"NASDAQ:{ticker}")
        if avg is not None:
            pnl = (close - avg) / avg * 100
            cls = "up" if pnl >= 0 else "down"
            sign = "+" if pnl >= 0 else ""
            new = re.sub(
                r'<div class="position-line">Avg cost <strong>\$[\d\.,]+</strong> · Unrealized <span class="(?:up|down)">[+\-\d\.]+%</span></div>',
                f'<div class="position-line">Avg cost <strong>${avg:.2f}</strong> · Unrealized <span class="{cls}">{sign}{pnl:.1f}%</span></div>',
                new, count=1,
            )

        if new != card:
            doc = doc.replace(card, new, 1)

    for ticker in ("CIFR", "IREN", "SLNH", "BGDE", "BTBT"):
        update_core(ticker)

    # -- Sentiment Cockpit cards --------------------------------------------
    def update_sent(ticker):
        nonlocal doc
        rec = by_ticker.get(ticker)
        if not rec:
            return
        s = rec["sentiment"]; sc = rec["scores"]
        bull = s.get("stocktwits_bull", 0); bear = s.get("stocktwits_bear", 0)
        total = s.get("stocktwits_total", 0); rd = s.get("reddit_mentions_7d", 0)
        label = sc.get("sentiment_label", "Mixed")
        pct = f"{int(round(bull / (bull + bear) * 100))}% bull" if (bull + bear) > 0 else ""

        pat = re.compile(
            r'(<div class="sent-card">\s*<div class="sent-head">\s*<span class="ticker-badge">'
            + ticker + r'</span>.*?<div class="sent-alpha">.*?</div>\s*</div>)',
            re.DOTALL,
        )
        m = pat.search(doc)
        if not m:
            return
        card = m.group(1); new = card

        new = re.sub(
            r'<span class="sent-tag sent-[a-z]+">[^<]+</span>',
            f'<span class="sent-tag {sent_class(label)}">{label}</span>',
            new, count=1,
        )
        if pct:
            new = re.sub(
                r'<span class="sent-pct">[^<]+</span>',
                f'<span class="sent-pct">{pct}</span>',
                new, count=1,
            )
        new = re.sub(
            r'<div class="sent-stat"><span class="label">StockTwits</span><span class="value">[^<]+</span></div>',
            f'<div class="sent-stat"><span class="label">StockTwits</span><span class="value">{bull}🟢 / {bear}🔴 ({total} msgs)</span></div>',
            new, count=1,
        )
        new = re.sub(
            r'<div class="sent-stat"><span class="label">Reddit 7d</span><span class="value">[^<]+</span></div>',
            f'<div class="sent-stat"><span class="label">Reddit 7d</span><span class="value">{rd} mentions (last 7 days)</span></div>',
            new, count=1,
        )
        if new != card:
            doc = doc.replace(card, new, 1)

    for ticker in ("WULF", "CIFR", "IREN", "SLNH", "BGDE", "CORZ", "HUT", "CLSK", "APLD",
                   "MARA", "RIOT", "BTDR", "BTBT", "HIVE"):
        update_sent(ticker)

    # -- Title and date stamps ----------------------------------------------
    short_date = datetime.strptime(date_iso, "%Y-%m-%d").strftime("%B %-d, %Y")
    doc = re.sub(
        r'<title>AI / HPC Analytics - The Daily Brief - [^<]+</title>',
        f'<title>AI / HPC Analytics - The Daily Brief - {short_date}</title>',
        doc, count=1,
    )
    doc = re.sub(
        r'<div class="date">AI / HPC Analytics Dashboard - [^<]+</div>',
        f'<div class="date">AI / HPC Analytics Dashboard - {weekday_human}</div>',
        doc, count=1,
    )

    # -- Verify and write ----------------------------------------------------
    class P(hp.HTMLParser):
        def __init__(self): super().__init__(); self.errs = []
    P().feed(doc)

    required = ['Market Summary', 'TA Scoreboard', 'Reference', 'Core Holdings Live',
                'Sentiment Cockpit', 'Alert Feed', 'SEC Filings']
    missing = [s for s in required if s not in doc]
    if missing:
        print(f"ERROR: missing required sections after edit: {missing}", file=sys.stderr)
        return 2

    size = len(doc)
    if not (40000 < size < 200000):
        print(f"ERROR: file size {size} bytes is out of bounds", file=sys.stderr)
        return 2

    with open(html_path, "w") as f:
        f.write(doc)

    print(f"Wrote {html_path} ({size} bytes); TA snapshot from {gen} UTC; date stamp {date_iso}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
