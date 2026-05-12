# Daily Pipeline — Authoritative Instructions

This file is the source of truth for the daily-morning-journal run. The scheduled task's SKILL.md should reference these instructions. If the SKILL.md and this file disagree, this file wins.

Version: 2026-05-12 (added positioning + options vol layer).

## Pipeline order

1. Setup clone, set git user, determine date (Europe/Amsterdam).
2. **TA + sentiment** — `python3 tools/analytics_pipeline.py` (refreshes `analytics_snapshot.json`).
3. **Positioning + options vol** (new) — `pip install --break-system-packages yfinance` then `python3 tools/positioning_options.py` (refreshes `positioning_snapshot.json`).
4. **Patch dashboard** — `python3 tools/refresh_dashboard.py --date YYYY-MM-DD`.
5. **Hand-write Market Summary, Alert Feed, SEC Filings** — see voice and template rules below.
6. **Insert Positioning Scoreboard + Options Vol Cockpit** sections (between Sentiment Cockpit and Alert Feed) using the latest `positioning_snapshot.json` data.
7. **Build News Journal HTML** for the day.
8. `cp journal-YYYY-MM-DD.html index.html`.
9. Sanity check, commit, push, copy to `/sessions/<session>/mnt/outputs/`.

## Market Summary structure (top to bottom)

- Single-line `<p class="data-health">` Data Health status: `yfinance ok/degraded/failed, Fintel ok/failed (one-line reason if failed), AlphaQuery ok/failed, FINRA ok/failed, EDGAR ok/failed`.
- `<h3>Market context</h3>` — price tape, cohort moves, RSI shifts, hype-stage transitions. Add one sentence on aggregate SI if it moved materially.
- `<h3>The directional read</h3>` — trim/trail/add posture, with positioning + vol references where they confirm or contradict the TA call.
- `<h3>Core holdings findings</h3>` — one block per core ticker using the inline template (see below).
- `<h3>Peer cohort signal</h3>` — same template, shorter, one positioning line + one options line per ticker.
- `<h3>Sentiment alpha</h3>` — StockTwits + Reddit vs positioning + options convergence/divergence.
- `<h3>Positioning and vol</h3>` — two paragraphs, cohort-level positioning then cohort-level vol. Close with `<em>Pushback:</em>` italic sentence naming contradictions.
- Closing `<em>Snapshot data:</em>` italic line with both pipeline timestamps.

## Per-ticker inline template

```
[TICKER] $price, +/-X% on the day. Daily RSI Y, Setup A, Pivot B, Hype C. [1-2 sentences existing price/momentum.]
Positioning: SI %float X%, [Δ vs prior]. Borrow rate Y%. Insider net 30d $Z [if non-zero].
Options: IV30 X% (IV Rank Y). IV30/RV30 ratio Z. [Term structure or skew note only if non-neutral.] [Earnings implied move only if earnings within 30 days.]
Recommendation: [existing recommendation]. [One new sentence integrating positioning/options into the action.]
```

SLNH and BGDE: positioning only, no options. State explicitly "Options module skipped by policy, chain too illiquid."
BTBT and BTDR: front-month IV only, term structure n/a. Earnings implied move is the highest-value option signal.
If a data point is n/a, omit it silently. Do not write "positioning data unavailable" in the per-ticker commentary; that belongs in the Data Health line only.

## Positioning Scoreboard table

Columns: Ticker, SI %Float, SI Δ vs prior, DTC, Borrow %, Borrow Avail, OffEx Short %, 13F Net Δ Q, Insider Net 30d, Flag.

Flag rules:
- Squeeze setup: SI %Float > 20% AND Hype Hot or above.
- Distribution risk: SI %Float < 8% AND Hype Distribution.
- Insider accumulation: insider net 30d > $500K.
- Insider distribution: insider net 30d < -$500K.

Sort by SI %Float descending. Highlight non-neutral rows.

## Options Vol Cockpit table

Columns: Ticker, IV30, IV Rank, IV30/RV30, Term Slope, 25Δ Skew, Earnings Move, Flag.

Flag rules:
- Vol expensive: IV30/RV30 > 1.5 AND IV Rank > 70 (relax to ratio-only if IV Rank n/a).
- Vol cheap: IV30/RV30 < 0.9 AND IV Rank < 30.
- Backwardated: Term Slope > +5 vol points.
- Upside chase: 25Δ Skew < -5.
- Downside fear: 25Δ Skew > +5.

Show n/a rows for SLNH and BGDE with note "chain too illiquid". Sort by IV Rank descending (then IV30 fallback). Match TA Scoreboard styling exactly.

## Alert Feed new types

Alongside existing News / Contract / Analyst / Insider / Activist:
- **SI Spike**: SI %Float rose >3pp on new FINRA print.
- **SI Crush**: SI %Float fell >3pp on new FINRA print.
- **Borrow Rate Spike**: Fintel borrow rate jumped >2x prior day.
- **IV Crush Pending**: term structure flipped from backwardation to contango.
- **IV Spike**: IV30 jumped >20% in a session.
- **Insider Sale**: Form 4 officer/director sale >$500K.
- **Insider Buy**: Form 4 officer/director buy of any size.
- **13F Drop**: institutional holder cut position by >25%.

Do not fire SI Spike/Crush unless the underlying FINRA report date changed from prior day.

## Voice and integrity rules

- No em dashes, no Oxford commas, no emoji.
- Replace soft language with the data point that prompted it. "SI 28%" beats "shorts are crowded".
- Drop any phrase you cannot back with a number on the dashboard.
- When two signals point opposite directions, name the conflict.
- Never repeat in the analyst note a number already shown in a scoreboard table. The note's job is interpretation.
- Never write "positioning data unavailable" or "options data not pulled today" inside the analyst note. That belongs in the Data Health line.
- Files under 200KB each.
- Never fabricate price, RSI, MACD, sentiment, SI, IV, RV or P&L data. The pipelines are the only writers of those numbers.
- Mark missing data n/a.

## Pushback rules (critical)

Wilko wants honest signals, not confirmation. Surface contradictions:
- TA trim (Distribution) but rising SI → flag squeeze risk against the trim trigger.
- TA add (Setup 90) but insiders selling → flag scepticism.
- TA hold but backwardation → flag near-term binary, tighten stop or hedge.
- IV crush ahead of earnings on high implied move → flag that the move may already be priced.

## Footer disclaimer

Must read exactly: "TA + sentiment fetched via tools/analytics_pipeline.py. Positioning data from yfinance + FINRA + Fintel (free tier) + SEC EDGAR + OpenInsider. Options vol from yfinance + AlphaQuery. Public market data only; no private account data is loaded or displayed. Composite scores documented in /tools/README.md. Not financial advice."

## Known gaps to wire over time

- Fintel borrow-rate scrape — fragile, blocked from cloud sandboxes. All Borrow % cells read n/a today.
- AlphaQuery IV history scrape — fragile, blocked. IV Rank reads n/a today.
- FINRA daily off-exchange short volume CSV — not yet wired. OffEx Short % reads n/a.
- OpenInsider RSS feed parser — not yet wired. Insider Net 30d reads n/a.
- SEC EDGAR 13F-HR aggregator — CIK map already pulled and cached; 13F Net Δ Q parser not yet wired.
- 25Δ skew interpolation — chain often too sparse for clean 25-delta strikes; column reads n/a for now.
- Earnings implied move — yfinance straddle pull frequently fails to return a clean ATM call+put pair; the script should be hardened next cycle.

Each gap should be closed one at a time. The Data Health line surfaces which sources are alive on a given day.
