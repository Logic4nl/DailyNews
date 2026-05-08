#!/usr/bin/env python3
"""
analytics_pipeline.py — daily TA + sentiment refresh for the AI / HPC Analytics dashboard.

Produces analytics_snapshot.json next to this script's parent dir (i.e. the repo root).
Intended to be run as part of the daily-morning-journal scheduled task before the
miner-analytics.html in-place refresh.

Sources (all free, no credentials required):
  - tradingview-ta library (daily + weekly indicators, last close, change, volume)
  - StockTwits public stream API (bull/bear sentiment tags)
  - Reddit anonymous JSON (mention counts in r/wallstreetbets, r/stocks, r/pennystocks,
    r/Bitcoin in the last 7 days)

Usage:
    python3 tools/analytics_pipeline.py [--out path/to/analytics_snapshot.json]

Exit codes:
    0 — wrote a usable snapshot (may have partial data; check the per-ticker errors field)
    2 — could not produce any usable data (network outage, library import failure, etc.)
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional

import requests

try:
    from tradingview_ta import TA_Handler, Interval
except ImportError:
    print("ERROR: tradingview-ta not installed. Run `pip install --break-system-packages tradingview-ta requests`.", file=sys.stderr)
    sys.exit(2)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CORE_HOLDINGS = ["WULF", "CIFR", "IREN", "SLNH", "BGDE"]
PEERS = ["CORZ", "HUT", "CLSK", "APLD", "MARA", "RIOT", "BTDR", "BITF", "BTBT", "HIVE"]
ALL_TICKERS = CORE_HOLDINGS + PEERS

# Some tickers are quoted on different exchanges. Default is NASDAQ.
EXCHANGE_OVERRIDES = {
    "BTDR": "NASDAQ",
    "BITF": "NASDAQ",
    "HIVE": "NASDAQ",
    "HUT":  "NASDAQ",
    "BTBT": "NASDAQ",
}

REDDIT_SUBS = ["wallstreetbets", "stocks", "pennystocks", "Bitcoin", "CryptoCurrency"]

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

STOCKTWITS_HEADERS = {
    "User-Agent": UA,
    "Accept": "application/json",
    "Referer": "https://stocktwits.com/",
    "Origin": "https://stocktwits.com",
}

REDDIT_HEADERS = {"User-Agent": UA}

REQUEST_TIMEOUT = 12  # seconds


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class TASnapshot:
    """Daily + weekly indicator snapshot for one ticker."""
    ticker: str
    last_close: Optional[float] = None
    daily_change_pct: Optional[float] = None
    rsi_d: Optional[float] = None
    rsi_w: Optional[float] = None
    macd_macd: Optional[float] = None
    macd_signal: Optional[float] = None
    sma20: Optional[float] = None
    sma50: Optional[float] = None
    sma200: Optional[float] = None
    bb_upper: Optional[float] = None
    bb_lower: Optional[float] = None
    volume: Optional[float] = None
    high_d: Optional[float] = None
    low_d: Optional[float] = None
    summary: Optional[str] = None  # BUY / NEUTRAL / SELL aggregate
    error: Optional[str] = None

    @property
    def macd_above_signal(self) -> Optional[bool]:
        if self.macd_macd is None or self.macd_signal is None:
            return None
        return self.macd_macd > self.macd_signal

    @property
    def ma_stack_score(self) -> Optional[int]:
        """Count how many of (close > sma20, close > sma50, close > sma200, sma50 > sma200) are true."""
        if self.last_close is None or self.sma20 is None or self.sma50 is None or self.sma200 is None:
            return None
        c = self.last_close
        score = 0
        if c > self.sma20: score += 1
        if c > self.sma50: score += 1
        if c > self.sma200: score += 1
        if self.sma50 > self.sma200: score += 1
        return score  # 0..4

    @property
    def bb_position(self) -> Optional[float]:
        """0 = lower band, 1 = upper band."""
        if self.last_close is None or self.bb_upper is None or self.bb_lower is None:
            return None
        rng = self.bb_upper - self.bb_lower
        if rng <= 0:
            return None
        return max(0.0, min(1.0, (self.last_close - self.bb_lower) / rng))


@dataclass
class SentimentSnapshot:
    """Aggregated sentiment for one ticker."""
    ticker: str
    stocktwits_bull: int = 0
    stocktwits_bear: int = 0
    stocktwits_total: int = 0
    reddit_mentions_7d: int = 0
    reddit_subs_breakdown: dict = field(default_factory=dict)
    error: Optional[str] = None

    @property
    def bull_ratio(self) -> Optional[float]:
        labelled = self.stocktwits_bull + self.stocktwits_bear
        if labelled == 0:
            return None
        return self.stocktwits_bull / labelled


# ---------------------------------------------------------------------------
# TradingView fetch
# ---------------------------------------------------------------------------

def fetch_one_interval(ticker: str, exchange: str, interval, retries: int = 3) -> dict[str, Any]:
    """Return the indicators dict for a given interval, or {error:str} on failure.

    Retries with exponential backoff on TradingView 429 rate limits.
    """
    last_err = "unknown"
    for attempt in range(retries):
        try:
            h = TA_Handler(symbol=ticker, screener="america", exchange=exchange, interval=interval)
            a = h.get_analysis()
            return {"indicators": a.indicators, "summary": a.summary}
        except Exception as exc:  # noqa: BLE001
            last_err = f"{type(exc).__name__}: {exc}"
            if "429" in str(exc) and attempt < retries - 1:
                # Exponential backoff: 3s, 6s, 12s
                time.sleep(3 * (2 ** attempt))
                continue
            return {"error": last_err}
    return {"error": last_err}


def fetch_ta(ticker: str) -> TASnapshot:
    exchange = EXCHANGE_OVERRIDES.get(ticker, "NASDAQ")
    snap = TASnapshot(ticker=ticker)

    daily = fetch_one_interval(ticker, exchange, Interval.INTERVAL_1_DAY)
    if "error" in daily:
        snap.error = f"daily: {daily['error']}"
        return snap

    ind = daily["indicators"]
    snap.last_close = ind.get("close")
    snap.daily_change_pct = ind.get("change")
    snap.rsi_d = ind.get("RSI")
    snap.macd_macd = ind.get("MACD.macd")
    snap.macd_signal = ind.get("MACD.signal")
    snap.sma20 = ind.get("SMA20")
    snap.sma50 = ind.get("SMA50")
    snap.sma200 = ind.get("SMA200")
    snap.bb_upper = ind.get("BB.upper")
    snap.bb_lower = ind.get("BB.lower")
    snap.volume = ind.get("volume")
    snap.high_d = ind.get("high")
    snap.low_d = ind.get("low")
    snap.summary = daily["summary"].get("RECOMMENDATION") if "summary" in daily else None

    # Weekly RSI (best-effort; not fatal if it fails).
    weekly = fetch_one_interval(ticker, exchange, Interval.INTERVAL_1_WEEK)
    if "indicators" in weekly:
        snap.rsi_w = weekly["indicators"].get("RSI")

    return snap


# ---------------------------------------------------------------------------
# StockTwits fetch
# ---------------------------------------------------------------------------

def fetch_stocktwits(ticker: str) -> dict[str, Any]:
    url = f"https://api.stocktwits.com/api/2/streams/symbol/{ticker}.json"
    try:
        r = requests.get(url, headers=STOCKTWITS_HEADERS, timeout=REQUEST_TIMEOUT)
        if r.status_code != 200:
            return {"error": f"http {r.status_code}"}
        msgs = r.json().get("messages", [])
        bull = bear = 0
        for m in msgs:
            s = m.get("entities", {}).get("sentiment") or {}
            tag = s.get("basic")
            if tag == "Bullish":
                bull += 1
            elif tag == "Bearish":
                bear += 1
        return {"bull": bull, "bear": bear, "total": len(msgs)}
    except Exception as exc:  # noqa: BLE001
        return {"error": f"{type(exc).__name__}: {exc}"}


# ---------------------------------------------------------------------------
# Reddit fetch
# ---------------------------------------------------------------------------

def fetch_reddit_mentions(ticker: str) -> dict[str, Any]:
    """Count posts mentioning the ticker symbol in each subreddit over the past week.

    Uses Reddit's anonymous JSON search endpoint. Cap at the first 25 results per sub
    (Reddit's default page) so this stays fast and below rate limits.
    """
    breakdown = {}
    total = 0
    errors = []

    for sub in REDDIT_SUBS:
        url = f"https://www.reddit.com/r/{sub}/search.json"
        params = {
            "q": ticker,
            "restrict_sr": "on",
            "sort": "new",
            "t": "week",
            "limit": 25,
        }
        try:
            r = requests.get(url, params=params, headers=REDDIT_HEADERS, timeout=REQUEST_TIMEOUT)
            if r.status_code != 200:
                errors.append(f"{sub}: http {r.status_code}")
                breakdown[sub] = 0
                continue
            data = r.json()
            children = data.get("data", {}).get("children", [])
            count = len(children)
            breakdown[sub] = count
            total += count
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{sub}: {type(exc).__name__}")
            breakdown[sub] = 0
        time.sleep(0.6)  # be polite

    out = {"breakdown": breakdown, "total": total}
    if errors:
        out["errors"] = errors
    return out


def fetch_sentiment(ticker: str) -> SentimentSnapshot:
    snap = SentimentSnapshot(ticker=ticker)

    st = fetch_stocktwits(ticker)
    if "error" in st:
        snap.error = f"stocktwits: {st['error']}"
    else:
        snap.stocktwits_bull = st["bull"]
        snap.stocktwits_bear = st["bear"]
        snap.stocktwits_total = st["total"]

    rd = fetch_reddit_mentions(ticker)
    snap.reddit_mentions_7d = rd["total"]
    snap.reddit_subs_breakdown = rd["breakdown"]
    if "errors" in rd:
        prev = snap.error or ""
        snap.error = (prev + " | reddit: " + ",".join(rd["errors"])).strip(" |")

    return snap


# ---------------------------------------------------------------------------
# Composite scoring
# ---------------------------------------------------------------------------

def score_setup(ta: TASnapshot) -> Optional[int]:
    """Setup score (0-100): is this a clean entry today?

    Reward: RSI in 50-65, MACD > signal, BB position 0.4-0.7 (not pinned to bands),
    MA stack 3-4. Penalize RSI > 75 or RSI < 35.
    """
    if ta.rsi_d is None:
        return None

    score = 50

    # RSI sweet spot
    if 50 <= ta.rsi_d <= 65:
        score += 20
    elif 45 <= ta.rsi_d < 50 or 65 < ta.rsi_d <= 70:
        score += 10
    elif ta.rsi_d > 75:
        score -= 25
    elif ta.rsi_d < 35:
        score -= 15

    # MACD
    if ta.macd_above_signal is True:
        score += 10
    elif ta.macd_above_signal is False:
        score -= 5

    # BB position — penalise pinned to upper band
    bb = ta.bb_position
    if bb is not None:
        if 0.35 <= bb <= 0.7:
            score += 10
        elif bb > 0.9:
            score -= 15
        elif bb < 0.1:
            score -= 5

    # MA stack
    stack = ta.ma_stack_score
    if stack is not None:
        if stack == 4:
            score += 10
        elif stack == 3:
            score += 5
        elif stack <= 1:
            score -= 10

    return max(0, min(100, score))


def score_pivot(ta: TASnapshot) -> Optional[int]:
    """Pivot Conviction (0-100): is this acting like a real AI/HPC infrastructure stock?

    Reward strong MA stack, MACD positive, multi-month trend (sma50 > sma200), price
    above SMA200 by a healthy margin.
    """
    if ta.last_close is None or ta.sma200 is None:
        return None

    score = 50

    stack = ta.ma_stack_score
    if stack == 4:
        score += 25
    elif stack == 3:
        score += 15
    elif stack == 2:
        score += 5
    elif stack <= 1:
        score -= 15

    if ta.macd_above_signal is True:
        score += 10
    elif ta.macd_above_signal is False:
        score -= 5

    # Distance from SMA200 (golden cross territory)
    if ta.sma200 > 0:
        dist = (ta.last_close - ta.sma200) / ta.sma200
        if dist > 1.5:    # price more than 2.5x SMA200 — extreme strength
            score += 15
        elif dist > 0.5:
            score += 10
        elif dist > 0.1:
            score += 5
        elif dist < -0.1:
            score -= 10

    return max(0, min(100, score))


def hype_stage(ta: TASnapshot, sent: SentimentSnapshot) -> str:
    """Classify the retail-cycle stage.

    0 Quiet:        low sentiment volume, RSI < 50
    1 Building:     rising mentions, RSI 50-60
    2 Hot:          RSI 60-70, strong bull ratio
    3 Mania:        RSI > 70, very high mentions, bull ratio > 0.85
    4 Distribution: RSI > 75 + bull ratio > 0.9 + heavy volume
    """
    rsi = ta.rsi_d if ta.rsi_d is not None else 0
    bull = sent.bull_ratio
    mentions = sent.reddit_mentions_7d + sent.stocktwits_total

    if rsi >= 75 and bull is not None and bull > 0.9:
        return "Distribution"
    if rsi >= 70 and bull is not None and bull > 0.85 and mentions > 60:
        return "Mania"
    if rsi >= 60 and (bull is None or bull > 0.7):
        return "Hot"
    if rsi >= 50 or mentions > 25:
        return "Building"
    return "Quiet"


def sentiment_label(sent: SentimentSnapshot) -> str:
    """Human label for the sentiment cockpit cell."""
    bull = sent.bull_ratio
    mentions = sent.reddit_mentions_7d + sent.stocktwits_total

    if bull is None:
        return "Quiet"
    if bull > 0.95 and mentions > 60:
        return "Retail euphoria"
    if bull > 0.85:
        return "Heavy bullish"
    if bull > 0.65:
        return "Bullish lean"
    if bull < 0.35:
        return "Bearish lean"
    return "Mixed"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def gather(ticker: str) -> dict[str, Any]:
    ta = fetch_ta(ticker)
    sent = fetch_sentiment(ticker)
    setup = score_setup(ta)
    pivot = score_pivot(ta)
    hype = hype_stage(ta, sent)
    label = sentiment_label(sent)
    return {
        "ticker": ticker,
        "ta": asdict(ta),
        "sentiment": asdict(sent),
        "scores": {
            "setup": setup,
            "pivot": pivot,
            "hype_stage": hype,
            "sentiment_label": label,
        },
    }


def build_snapshot() -> dict[str, Any]:
    logging.info("Fetching TA + sentiment for %d tickers", len(ALL_TICKERS))
    results: list[dict[str, Any]] = []

    # Pull tickers in parallel. 3 workers + retries on 429 keeps total runtime near 45s
    # in the typical case. Retries use exponential backoff (3s, 6s, 12s).
    with ThreadPoolExecutor(max_workers=3) as ex:
        futures = {ex.submit(gather, t): t for t in ALL_TICKERS}
        for fut in as_completed(futures):
            t = futures[fut]
            try:
                results.append(fut.result())
                logging.info("  %s ok", t)
            except Exception as exc:  # noqa: BLE001
                logging.warning("  %s FAILED: %s", t, exc)
                results.append({"ticker": t, "error": str(exc)})

    # Preserve canonical ordering (Core Holdings first).
    order = {t: i for i, t in enumerate(ALL_TICKERS)}
    results.sort(key=lambda r: order.get(r["ticker"], 999))

    return {
        "version": "1.0",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "core_holdings": CORE_HOLDINGS,
        "peers": PEERS,
        "tickers": results,
    }


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        default=None,
        help="Path to write the snapshot JSON. Defaults to <repo root>/analytics_snapshot.json.",
    )
    args = parser.parse_args()

    if args.out is None:
        # Default: parent of the script's directory (repo root).
        here = os.path.dirname(os.path.abspath(__file__))
        repo_root = os.path.dirname(here)
        args.out = os.path.join(repo_root, "analytics_snapshot.json")

    snapshot = build_snapshot()

    # Sanity: must have at least 5 tickers with non-null las