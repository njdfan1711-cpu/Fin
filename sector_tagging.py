"""
sector_tagging.py

Runs once daily (industry classification doesn't change day to day). Looks
up each eligible ticker's industry via Finnhub's company profile endpoint
and stores it for sector_alerts to use later.

This is intentionally a separate, simple script rather than folded into
fundamentals_scan.py -- keeps that script focused, and this one is cheap
(one call per ticker, no pacing-sensitive multi-call logic).

Output: sectors.json -- {symbol: industry_string}

NOTE: needs FINNHUB_API_KEY and outbound network access.
"""

import csv
import json
import sys
import time
import urllib.request

from config import ELIGIBLE_FILE, FINNHUB_API_KEY, TICKER_SECTORS_FILE

BASE_URL = "https://finnhub.io/api/v1"
CALLS_PER_MINUTE = 55
SLEEP_BETWEEN_CALLS = 60.0 / CALLS_PER_MINUTE


def load_eligible() -> list[str]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return [row["symbol"] for row in csv.DictReader(f)]


def fetch_industry(symbol: str) -> str:
    url = f"{BASE_URL}/stock/profile2?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "personal-stock-scanner"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("finnhubIndustry", "")
    except Exception:
        return ""


def main():
    if not FINNHUB_API_KEY:
        print("FINNHUB_API_KEY not set -- skipping sector tagging.", file=sys.stderr)
        return

    symbols = load_eligible()
    print(f"Tagging sectors for {len(symbols)} eligible tickers "
          f"(~{len(symbols) / CALLS_PER_MINUTE:.0f} min expected)...", file=sys.stderr)

    sectors = {}
    for i, symbol in enumerate(symbols, start=1):
        industry = fetch_industry(symbol)
        if industry:
            sectors[symbol] = industry
        time.sleep(SLEEP_BETWEEN_CALLS)

        if i % 200 == 0:
            print(f"  ...{i}/{len(symbols)} checked", file=sys.stderr)

    with open(TICKER_SECTORS_FILE, "w") as f:
        json.dump(sectors, f, indent=2)

    print(f"\nTagged {len(sectors)} ticker(s) with industry data.", file=sys.stderr)


if __name__ == "__main__":
    main()
