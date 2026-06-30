# Quantum Short-Term Rotation Module

Tactical short-term satellite sleeve inside the AI/HPC book, published as the third tab
(`quantum.html`) of the Daily Brief: **News | Miner Analytics | Quantum**.

It is a trade, not a hold. Funded by miner/HPC trims, never by core positions and never by
ETH-earmarked capital. It runs parallel to the ETH rotation, which stays on its own slower track.

## Build (part of the daily run)

```bash
cd /tmp/DailyNews
pip install --break-system-packages yfinance pyyaml
python3 tools/build_quantum.py --fetch-only                 # one fetch -> quantum_prices.json
python3 tools/build_quantum.py --render-only --date YYYY-MM-DD   # -> quantum.html
```

Inputs the generator reads: `quantum_rules.yaml` (vehicles, sizing, entry/exit/invalidation
thresholds, owner-maintained) and `quantum_positions.json` (the sleeve book; FLAT until an
entry is taken). It writes `quantum_prices.json` (the single timestamped fetch) and
`quantum_state_prev.json` (for the "what changed" diff). Do not hand-edit `quantum.html` and
do not hand-author any price, gate or verdict string. If the spec changes, edit the generator.

## Global rules (mirror the miner book)

- One price fetch per run, persisted to `quantum_prices.json` with `fetched_at` (UTC) and source.
- Freshness gating: if the fetch fails or is stale, show the red STALE chip and suppress every
  bullish action. Only stand-aside and exit verdicts may render on stale data.
- Never hand-author the gate state or verdict. Everything is computed from `quantum_rules.yaml`
  against the live fetch. If a verdict is not computed it does not render.
- Degrade, do not freeze: thin or delisted names (e.g. ONE nano) render N/A, they do not block.

## Thesis

Trade the quantum policy and federal-funding catalyst as a high-beta risk-on move.

## Entry (confirmation-gated; QTUM is currently Rolling over)

- Primary trigger: QTUM relative strength vs SPY flips Rolling over to Improving, i.e. the 1D
  and 5D rel turn positive while 20D stays positive. Do not chase while 5D rel is negative.
- Secondary confirm: defensives (XLV, XLP, XLU) stop Leading and high-beta (IGV, SMH) firms up.
- Immediate-entry option: a 1/3 starter probe before confirmation, treated as a probe with a
  tight stop.

## Vehicles

- Core: QTUM (theme exposure without single-name blowup risk).
- Beta booster: equal-weighted IONQ, RGTI, QBTS, QUBT. Equal weight so one blowup cannot sink the sleeve.
- Crypto-adjacent: BTQ. ARQQ, LAES optional.
- Nanos (ONE/OONEF etc): token-watch position only, never sized.

## Sizing

- Total sleeve 3-5% of risk capital, sized so a 50% sleeve drawdown is survivable.
- Single nano name: tiny. Illiquid and promotion-prone.

## Exits

- Stop: -15 to -20% on the sleeve, or QTUM 5D rel rolling back negative, whichever first.
- Take profit: scale out 1/3 on the first +20-30% pop, trail the rest. These spike then fade.
- Time stop: no relative outperformance within 4-6 weeks, recycle capital to the HPC book.

## Invalidation (kill the rotation)

- BTC breaks down hard (below 55k, the same macro trigger as the miner book).
- 2yr yields spike (rates risk-off regime returns).
- QTUM 20D rel turns negative (structurally lagging, not just consolidating).

## Book interaction

Quantum and the HPC miners share the same risk-on driver. Net high-beta compute exposure stays
inside the overall risk budget. Do not double up.

## Page structure (4 sections)

1. Sleeve Verdict + Data Health: health chip, computed posture, gate state chip, three lines of what changed.
2. Entry Gate: QTUM 1D/5D/20D rel vs SPY with live values, plus the secondary confirm row.
3. Sleeve Book: position table or FLAT, sizing budget, exits.
4. Invalidation + Macro: BTC level, 2yr yield move, QTUM 20D rel sign, each CLEAR or TRIGGERED.

## Owner-maintained between runs

`quantum_positions.json` (sleeve book; paste fills when an entry is taken) and the thresholds in
`quantum_rules.yaml`. Do not edit these on a normal daily run unless a real event has occurred.
