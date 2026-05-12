"""Fetch positioning + options vol data for the cohort. Output JSON."""
import json, os, sys, math
import urllib.request, urllib.error
from datetime import datetime, timezone, timedelta
import warnings
warnings.filterwarnings('ignore')

CORE = ['WULF', 'CIFR', 'IREN', 'SLNH', 'BGDE', 'BTBT']
PEERS = ['CORZ', 'HUT', 'CLSK', 'APLD', 'MARA', 'RIOT', 'BTDR', 'BITF', 'HIVE']
ALL_TICKERS = CORE + PEERS
NO_OPTIONS = ['SLNH', 'BGDE']  # Skip options for these
THIN_OPTIONS = ['BTBT', 'BTDR']  # Front-month only

result = {
    'generated_at_utc': datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
    'data_health': {
        'yfinance': 'unknown',
        'fintel': 'failed',  # Free scraping blocked from cloud sandbox
        'alphaquery': 'failed',
        'finra': 'failed',
        'edgar': 'unknown',
    },
    'tickers': {}
}

try:
    import yfinance as yf
except ImportError:
    print("yfinance not installed", file=sys.stderr)
    sys.exit(1)

yf_ok = 0
yf_fail = 0

# Fetch SEC EDGAR CIK map once
try:
    req = urllib.request.Request(
        'https://www.sec.gov/files/company_tickers.json',
        headers={'User-Agent': 'Wilko Tam wilko@poolparty.market'}
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        cik_data = json.loads(r.read().decode())
    cik_map = {}
    for _, v in cik_data.items():
        if v.get('ticker') in ALL_TICKERS:
            cik_map[v['ticker']] = str(v['cik_str']).zfill(10)
    result['data_health']['edgar'] = 'ok' if len(cik_map) > 10 else 'degraded'
except Exception as e:
    cik_map = {}
    result['data_health']['edgar'] = 'failed'

for ticker in ALL_TICKERS:
    try:
        t = yf.Ticker(ticker)
        info = t.info or {}
        spot = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        si_pct_float = info.get('shortPercentOfFloat')
        if si_pct_float is not None:
            si_pct_float = round(si_pct_float * 100, 2)
        si_shares = info.get('sharesShort')
        avg_vol = info.get('averageVolume10days') or info.get('averageVolume')
        dtc = None
        if si_shares and avg_vol and avg_vol > 0:
            dtc = round(si_shares / avg_vol, 2)
        si_report_date = info.get('dateShortInterest')

        entry = {
            'ticker': ticker,
            'spot': spot,
            'si_pct_float': si_pct_float,
            'si_shares': si_shares,
            'dtc': dtc,
            'si_report_date': si_report_date,
            'borrow_rate': None,  # Fintel scrape failed
            'borrow_avail': None,
            'offex_short_pct': None,  # FINRA daily CSV not pulled
            'insider_net_30d_usd': None,  # OpenInsider RSS not pulled
            'inst_13f_net_q': None,  # SEC EDGAR 13F parsing not implemented
            'iv30': None,
            'iv60': None,
            'iv90': None,
            'rv30': None,
            'iv_rank': None,  # AlphaQuery scrape failed
            'term_slope': None,
            'skew_25d': None,
            'earnings_move_pct': None,
            'earnings_date': None,
        }

        # 30-day historical realised vol
        try:
            hist = t.history(period='2mo')
            if hist is not None and len(hist) >= 21:
                import math
                closes = hist['Close'].tolist()[-31:]
                rets = []
                for i in range(1, len(closes)):
                    if closes[i-1] and closes[i-1] > 0:
                        rets.append(math.log(closes[i] / closes[i-1]))
                if len(rets) >= 20:
                    mean = sum(rets) / len(rets)
                    var = sum((r - mean) ** 2 for r in rets) / (len(rets) - 1)
                    rv30 = math.sqrt(var) * math.sqrt(252) * 100
                    entry['rv30'] = round(rv30, 2)
        except Exception:
            pass

        # Options data (skip if illiquid)
        if ticker not in NO_OPTIONS:
            try:
                expirations = t.options or ()
                if expirations:
                    today = datetime.now(timezone.utc).date()
                    # Pick 3 expirations: nearest >=20d, ~60d, ~90d
                    def days_to(d):
                        return (datetime.strptime(d, '%Y-%m-%d').date() - today).days
                    exp_30 = next((e for e in expirations if days_to(e) >= 20 and days_to(e) <= 45), None)
                    exp_60 = next((e for e in expirations if days_to(e) >= 50 and days_to(e) <= 75), None)
                    exp_90 = next((e for e in expirations if days_to(e) >= 80 and days_to(e) <= 110), None)

                    def atm_iv(exp_date):
                        if not exp_date or not spot:
                            return None
                        try:
                            opt = t.option_chain(exp_date)
                            calls = opt.calls
                            puts = opt.puts
                            if calls is None or len(calls) == 0:
                                return None
                            # Volume weighted ATM IV using strikes within ±5% of spot
                            cw = calls[(calls['strike'] >= spot * 0.95) & (calls['strike'] <= spot * 1.05)]
                            pw = puts[(puts['strike'] >= spot * 0.95) & (puts['strike'] <= spot * 1.05)]
                            ivs = []
                            for _, row in cw.iterrows():
                                iv = row.get('impliedVolatility')
                                vol = row.get('volume') or 0
                                if iv and iv > 0 and iv < 5:
                                    ivs.append((iv, vol + 1))
                            for _, row in pw.iterrows():
                                iv = row.get('impliedVolatility')
                                vol = row.get('volume') or 0
                                if iv and iv > 0 and iv < 5:
                                    ivs.append((iv, vol + 1))
                            if not ivs:
                                return None
                            total_w = sum(w for _, w in ivs)
                            wiv = sum(iv * w for iv, w in ivs) / total_w
                            return round(wiv * 100, 2)
                        except Exception:
                            return None

                    iv30 = atm_iv(exp_30)
                    entry['iv30'] = iv30
                    if ticker not in THIN_OPTIONS:
                        iv60 = atm_iv(exp_60)
                        iv90 = atm_iv(exp_90)
                        entry['iv60'] = iv60
                        entry['iv90'] = iv90
                        if iv30 and iv90:
                            entry['term_slope'] = round(iv30 - iv90, 2)

                    if entry['iv30'] and entry['rv30']:
                        entry['iv_rv_ratio'] = round(entry['iv30'] / entry['rv30'], 2)

                    # Earnings move from nearest expiry post earnings
                    try:
                        cal = t.calendar
                        if cal is not None and 'Earnings Date' in cal:
                            ed = cal['Earnings Date']
                            if isinstance(ed, list) and ed:
                                ed = ed[0]
                            if hasattr(ed, 'strftime'):
                                ed_str = ed.strftime('%Y-%m-%d')
                                entry['earnings_date'] = ed_str
                                if (ed.date() if hasattr(ed, 'date') else ed) <= today + timedelta(days=30):
                                    # Find expiry after earnings
                                    post_exp = next((e for e in expirations if days_to(e) >= (ed.date() - today).days), None)
                                    if post_exp and spot:
                                        opt = t.option_chain(post_exp)
                                        calls = opt.calls
                                        puts = opt.puts
                                        # ATM call + put
                                        atm_call = calls.iloc[(calls['strike'] - spot).abs().argsort()[:1]]
                                        atm_put = puts.iloc[(puts['strike'] - spot).abs().argsort()[:1]]
                                        if len(atm_call) and len(atm_put):
                                            c_price = atm_call.iloc[0]['lastPrice']
                                            p_price = atm_put.iloc[0]['lastPrice']
                                            straddle = c_price + p_price
                                            if straddle and spot:
                                                entry['earnings_move_pct'] = round(straddle / spot * 100, 2)
                    except Exception:
                        pass

            except Exception as e:
                pass

        result['tickers'][ticker] = entry
        yf_ok += 1
        print(f"  {ticker} ok SI={si_pct_float} IV30={entry['iv30']} RV30={entry['rv30']}", file=sys.stderr)
    except Exception as e:
        yf_fail += 1
        result['tickers'][ticker] = {'ticker': ticker, 'error': str(e)[:80]}
        print(f"  {ticker} FAIL {e}", file=sys.stderr)

result['data_health']['yfinance'] = 'ok' if yf_fail == 0 else (f'degraded ({yf_fail}/15)' if yf_fail < 5 else 'failed')

# Sanity filter: an ATM volume-weighted IV that came back below 5 or above 400 percent
# almost always means yfinance returned mixed-unit values across strikes. Mark n/a rather
# than publish a misleading number.
for tk, t in result['tickers'].items():
    iv30 = t.get('iv30')
    if iv30 is not None and (iv30 != iv30 or iv30 < 5 or iv30 > 400):
        t['iv30'] = None
        t['iv_rv_ratio'] = None
        t['term_slope'] = None
    iv60 = t.get('iv60')
    if iv60 is not None and (iv60 != iv60 or iv60 < 5 or iv60 > 400):
        t['iv60'] = None
    iv90 = t.get('iv90')
    if iv90 is not None and (iv90 != iv90 or iv90 < 5 or iv90 > 400):
        t['iv90'] = None
        t['term_slope'] = None

import argparse
ap = argparse.ArgumentParser()
default_out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'positioning_snapshot.json')
ap.add_argument('--out', default=default_out)
args, _ = ap.parse_known_args()
with open(args.out, 'w') as f:
    json.dump(result, f, indent=2, default=str)
print(f"Wrote snapshot to {args.out}", file=sys.stderr)

print(f"DONE: yf_ok={yf_ok}, yf_fail={yf_fail}", file=sys.stderr)
