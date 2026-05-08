# tools/analytics_pipeline.py

Daily TA + sentiment refresh for the AI / HPC Analytics dashboard.

## What it does

For 15 tickers (5 Core Holdings: WULF, CIFR, IREN, SLNH, BGDE; 10 peers: CORZ, HUT, CLSK, APLD, MARA, RIOT, BTDR, BITF, BTBT, HIVE), it fetches:

1. **TA from TradingView** via `tradingview-ta` (free, no auth):
   - Last close, daily change %, daily and weekly RSI
   - MACD line and signal
   - SMA20 / SMA50 / SMA200, Bollinger Bands upper / lower
   - Volume, daily high / low, summary recommendation (BUY / NEUTRAL / SELL)

2. **Sentiment**:
   - StockTwits public stream API → bull / bear tag counts (last ~30 messages)
   - Reddit anonymous JSON search → mention counts in r/wallstreetbets, r/stocks, r/pennystocks, r/Bitcoin, r/CryptoCurrency over the past 7 days

3. **Composite scores** (computed locally from the above):
   - Setup (0-100): is this a clean entry today?
   - Pivot Conviction (0-100): is this acting like a real AI/HPC name?
   - Hype Stage: Quiet / Building / Hot / Mania / Distribution
   - Sentiment label: Quiet / Mixed / Bearish lean / Bullish lean / Heavy bullish / Retail euphoria

Output is written to `analytics_snapshot.json` in the repo root.

## Install

```bash
pip install --break-system-packages -r requirements.txt
```

## Run

```bash
python3 tools/analytics_pipeline.py
```

Or with a custom output path:

```bash
python3 tools/analytics_pipeline.py --out /tmp/snapshot.json
```

## Schema

```jsonc
{
  "version": "1.0",
  "generated_at_utc": "2026-05-08 02:29:02",
  "core_holdings": ["WULF", "CIFR", "IREN", "SLNH", "BGDE"],
  "peers": ["CORZ", "HUT", "CLSK", "APLD", "MARA", "RIOT", "BTDR", "BITF", "BTBT", "HIVE"],
  "tickers": [
    {
      "ticker": "WULF",
      "ta": {
        "last_close": 24.02,
        "daily_change_pct": -6.68,
        "rsi_d": 64.5,
        "rsi_w": 75.0,
        "macd_macd": 1.76,
        "macd_signal": 1.46,
        "sma20": 21.05,
        "sma50": 17.75,
        "sma200": 13.48,
        "bb_upper": 24.40,
        "bb_lower": 17.69,
        "volume": 36738612,
        "summary": "BUY",
        "error": null
      },
      "sentiment": {
        "stocktwits_bull": 15,
        "stocktwits_bear": 1,
        "stocktwits_total": 30,
        "reddit_mentions_7d": 2,
        "reddit_subs_breakdown": {"wallstreetbets": 1, "stocks": 0, "pennystocks": 0, "Bitcoin": 1, "CryptoCurrency": 0},
        "error": null
      },
      "scores": {
        "setup": 75,
        "pivot": 95,
        "hype_stage": "Hot",
        "sentiment_label": "Heavy bullish"
      }
    }
  ]
}
```

## Behavior on partial failures

- If a single TA fetch fails (network, rate limit), the script retries up to 3 times with exponential backoff (3s / 6s / 12s). If all retries fail, that ticker's `ta.error` is set and `last_close` is null.
- StockTwits and Reddit failures are isolated to their own block on each ticker; a Reddit failure on r/stocks does not break the rest of the run.
- The script exits with code 2 only if fewer than 5 tickers returned valid TA data.
- Otherwise it exits 0 and writes whatever data it has. The HTML refresh step in the daily skill is responsible for handling missing fields gracefully.

## Known issues

- **BITF**: Bitfarms has been undergoing a rebrand to Keel Infrastructure (ticker KEEL); TradingView lookups via `BITF` on NASDAQ may fail. If the snapshot consistently shows BITF as failed for several days, update the symbol to whatever TradingView is now serving (KEEL on NASDAQ, or BITF on TSX).
- TradingView rate-limits aggressively. Running this twice in quick succession may produce a partial snapshot. The daily skill is the only intended caller.

## Why these specific data sources

- TradingView gives ready-computed indicators across daily and weekly intervals — no need to maintain our own TA library or feed.
- StockTwits has explicit Bullish / Bearish tags applied by users, which is a much cleaner signal than NLP sentiment scoring.
- Reddit mention counts correlate well with retail attention but don't claim to measure sentiment polarity.
- Composite scores are computed locally so the framework can evolve without depending on third-party scoring APIs.

## Adding tickers

Edit the `CORE_HOLDINGS` and `PEERS` lists at the top of `tools/analytics_pipeline.py`. If a ticker is not on NASDAQ, add an entry to `EXCHANGE_OVERRIDES`. Re-run the script to verify.
