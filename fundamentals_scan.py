"""
fundamentals_scan.py

Runs once daily. Checks eligible.csv against Finnhub's earnings-surprise
and basic-financials endpoints.

IMPORTANT FIX (post-launch): the original version matched on "the most
recent known earnings beat" with no regard for how long ago that was --
which meant a beat from months earlier still matched every single day,
forever. That's what caused the 329-ticker alert. This version only
counts an earnings beat if it was actually reported within the last
EARNINGS_RECENCY_DAYS (see config.py) -- i.e. it has to be genuinely
recent news, not old news still sitting in the data.

Signals are RECORDED via signals_store.py, not pushed directly --
compose_alerts.py decides what's push-worthy based on confluence across
multiple signal categories.

IMPORTANT: The 'metric' endpoint's exact field names (e.g. for YoY revenue
growth) can vary/evolve on Finnhub's side. This script defensively checks
a couple of plausible field name variants and skips gracefully if none are
present -- search FINNHUB_KEY_CHECK below if you need to adjust these
against a real response.
"""

import csv
import json
import sys
import time
import urllib.request
from datetime import date, datetime

from config import (
    ELIGIBLE_FILE,
    FINNHUB_API_KEY,
    EARNINGS_SURPRISE_PCT,
    EARNINGS_RECENCY_DAYS,
    REVENUE_GROWTH_YOY_PCT,
    FUNDAMENTALS_SIGNALS_FILE,
)
from signals_store import record_signal

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


def check_earnings_surprise(symbol: str):
    """Returns (detail_str, strength) or None. Only counts RECENT beats."""
    url = f"{BASE_URL}/stock/earnings?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        data = _get(url)
    except Exception:
        return None
    if not data:
        return None

    latest = data[0]  # most recent quarter first

    # Recency check -- this is the actual bug fix. 'period' is the
    # reporting period date, formatted YYYY-MM-DD in Finnhub's docs.
    period_str = latest.get("period")
    if not period_str:
        return None
    try:
        period_date = datetime.strptime(period_str, "%Y-%m-%d").date()
    except ValueError:
        return None

    days_ago = (date.today() - period_date).days
    if days_ago < 0 or days_ago > EARNINGS_RECENCY_DAYS:
        return None  # too old (or oddly in the future) -- not "news" anymore

    actual = latest.get("actual")
    estimate = latest.get("estimate")
    if actual is None or estimate in (None, 0):
        return None
    surprise_pct = ((actual - estimate) / abs(estimate)) * 100

    if surprise_pct >= EARNINGS_SURPRISE_PCT:
        detail = f"Earnings beat by {surprise_pct:.1f}% ({days_ago}d ago)"
        strength = min(surprise_pct / 20, 1.0)  # bigger beats rank higher
        return (detail, strength)
    return None


def check_revenue_growth(symbol: str):
    url = f"{BASE_URL}/stock/metric?symbol={symbol}&metric=all&token={FINNHUB_API_KEY}"
    try:
        data = _get(url)
    except Exception:
        return None
    metric = data.get("metric", {})

    # FINNHUB_KEY_CHECK -- confirm this field name against a real response
    # before relying on it long-term.
    growth = (
        metric.get("revenueGrowthTTMYoy")
        or metric.get("revenueGrowthQuarterlyYoy")
        or metric.get("revenueGrowth3Y")
    )
    if growth is not None and growth >= REVENUE_GROWTH_YOY_PCT:
        detail = f"Revenue growth {growth:.1f}% YoY"
        strength = min(growth / 30, 1.0)
        return (detail, strength)
    return None


def main():
    if not FINNHUB_API_KEY:
        print("FINNHUB_API_KEY not set -- skipping fundamentals scan.", file=sys.stderr)
        return

    symbols = load_eligible()
    print(f"Running fundamentals scan on {len(symbols)} eligible tickers "
          f"(~{len(symbols) * 2 / CALLS_PER_MINUTE:.0f} min expected)...", file=sys.stderr)

    signals = {}
    total_signals = 0

    for i, symbol in enumerate(symbols, start=1):
        details = []
        strengths = []

        r1 = check_earnings_surprise(symbol)
        time.sleep(SLEEP_BETWEEN_CALLS)
        if r1:
            details.append(r1[0])
            strengths.append(r1[1])

        r2 = check_revenue_growth(symbol)
        time.sleep(SLEEP_BETWEEN_CALLS)
        if r2:
            details.append(r2[0])
            strengths.append(r2[1])

        if details:
            # Combine into ONE fundamentals-category signal so a second
            # finding doesn't silently overwrite the first in the store.
            combined_detail = "; ".join(details)
            combined_strength = max(strengths)
            record_signal(symbol, "fundamentals", combined_detail, strength=combined_strength)
            signals[symbol] = details
            total_signals += len(details)

        if i % 100 == 0:
            print(f"  ...{i}/{len(symbols)} checked", file=sys.stderr)

    with open(FUNDAMENTALS_SIGNALS_FILE, "w") as f:
        json.dump(signals, f, indent=2)

    print(f"\n{total_signals} fundamentals signal(s) recorded "
          f"(only earnings beats within the last {EARNINGS_RECENCY_DAYS} days count).",
          file=sys.stderr)


if __name__ == "__main__":
    main()
