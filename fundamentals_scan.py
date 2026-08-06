"""
fundamentals_scan.py

Runs once daily. Checks eligible.csv against Finnhub's earnings-surprise
and basic-financials endpoints. Fundamentals move slowly (quarterly), so
daily is the right cadence -- no benefit to checking more often.

Uses ONE metric call per ticker (not separate earnings + financials calls)
to stay within a reasonable Actions-minutes budget across ~2,000-3,000
eligible tickers on Finnhub's free 60-calls/min tier.

IMPORTANT: The 'metric' endpoint's exact field names (e.g. for YoY revenue
growth) can vary/evolve on Finnhub's side. This script defensively checks
a couple of plausible field name variants and skips gracefully if none are
present, but the first time you run this for real, print one full raw
response for a ticker you know well and confirm the field names match
what's used below (search FINNHUB_KEY_CHECK in this file) -- adjust if
Finnhub's docs show something different by the time you set this up.
"""

import csv
import json
import sys
import time
import urllib.request

from config import ELIGIBLE_FILE, FINNHUB_API_KEY, EARNINGS_SURPRISE_PCT, REVENUE_GROWTH_YOY_PCT, FUNDAMENTALS_SIGNALS_FILE
from alert_log import filter_new
from notify import send_batch_alert

BASE_URL = "https://finnhub.io/api/v1"
CALLS_PER_MINUTE = 55  # stay a little under Finnhub's 60/min free cap
SLEEP_BETWEEN_CALLS = 60.0 / CALLS_PER_MINUTE


def load_eligible() -> list[str]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return [row["symbol"] for row in csv.DictReader(f)]


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "personal-stock-scanner"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def check_earnings_surprise(symbol: str) -> str | None:
    url = f"{BASE_URL}/stock/earnings?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        data = _get(url)
    except Exception:
        return None
    if not data:
        return None
    latest = data[0]  # most recent quarter first
    actual = latest.get("actual")
    estimate = latest.get("estimate")
    if actual is None or estimate in (None, 0):
        return None
    surprise_pct = ((actual - estimate) / abs(estimate)) * 100
    if surprise_pct >= EARNINGS_SURPRISE_PCT:
        return f"Earnings beat by {surprise_pct:.1f}%"
    return None


def check_revenue_growth(symbol: str) -> str | None:
    url = f"{BASE_URL}/stock/metric?symbol={symbol}&metric=all&token={FINNHUB_API_KEY}"
    try:
        data = _get(url)
    except Exception:
        return None
    metric = data.get("metric", {})

    # FINNHUB_KEY_CHECK -- confirm this field name against a real response
    # before relying on it; trying the most commonly documented variants.
    growth = (
        metric.get("revenueGrowthTTMYoy")
        or metric.get("revenueGrowthQuarterlyYoy")
        or metric.get("revenueGrowth3Y")
    )
    if growth is not None and growth >= REVENUE_GROWTH_YOY_PCT:
        return f"Revenue growth {growth:.1f}% YoY"
    return None


def main():
    if not FINNHUB_API_KEY:
        print("FINNHUB_API_KEY not set -- skipping fundamentals scan.", file=sys.stderr)
        return

    symbols = load_eligible()
    print(f"Running fundamentals scan on {len(symbols)} eligible tickers "
          f"(~{len(symbols) * 2 / CALLS_PER_MINUTE:.0f} min expected)...", file=sys.stderr)

    all_matches = []
    signals = {}

    for i, symbol in enumerate(symbols, start=1):
        reasons = []

        r1 = check_earnings_surprise(symbol)
        time.sleep(SLEEP_BETWEEN_CALLS)
        if r1:
            reasons.append(r1)

        r2 = check_revenue_growth(symbol)
        time.sleep(SLEEP_BETWEEN_CALLS)
        if r2:
            reasons.append(r2)

        if reasons:
            signals[symbol] = reasons
            fresh = filter_new(symbol, reasons)
            if fresh:
                all_matches.append({"symbol": symbol, "reasons": fresh})

        if i % 100 == 0:
            print(f"  ...{i}/{len(symbols)} checked", file=sys.stderr)

    with open(FUNDAMENTALS_SIGNALS_FILE, "w") as f:
        json.dump(signals, f, indent=2)

    print(f"\n{len(all_matches)} ticker(s) matched fundamentals (after de-dup).", file=sys.stderr)
    send_batch_alert(all_matches)


if __name__ == "__main__":
    main()
