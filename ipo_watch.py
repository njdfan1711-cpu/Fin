"""
ipo_watch.py

Keeps your scan universe from going stale by automatically catching new IPOs.

How it works (all free, official SEC sources, no API key):

1. NEW REGISTRATIONS
   Search SEC EDGAR Full-Text Search for recently filed Form S-1 (the form
   companies file to register for an IPO). Any CIK (SEC's company ID) that
   files an S-1 and isn't already in our universe gets added to a local
   "pending_ipos.json" watch list.

   Endpoint: https://efts.sec.gov/LATEST/search-index?forms=S-1&dateRange=custom...
   This is the SEC's own full-text search API. It's free but they DO require
   a descriptive User-Agent identifying you/your app, and a max of 10
   requests/second -- this script stays well under that.

2. GOING LIVE
   An S-1 filing alone doesn't mean the company will actually IPO, or when.
   The reliable "it's actually trading now" signal is SEC's own ticker map:

   https://www.sec.gov/files/company_tickers.json

   This free file maps every CIK to its active ticker. Each run, we check
   every CIK in our pending list against this file. The moment a pending CIK
   shows up with a ticker, that means the IPO priced and the stock is live --
   we add it straight into universe.csv and drop it from pending.

Run this once a day, before your main scan job, right after universe_builder.py.

NOTE: Needs outbound access to efts.sec.gov and www.sec.gov. If running in a
network-restricted sandbox, allow those domains or run this step elsewhere.
"""

import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, timedelta

# SEC requires a real identifying User-Agent for automated access -- put your
# own name/email here per SEC's fair-access rules (https://www.sec.gov/os/webmaster-faq#developers)
USER_AGENT = "personal-stock-scanner contact: your-email@example.com"

FULLTEXT_SEARCH_URL = "https://efts.sec.gov/LATEST/search-index"
TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"

PENDING_FILE = "pending_ipos.json"
UNIVERSE_FILE = "universe.csv"


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def load_pending() -> dict:
    if os.path.exists(PENDING_FILE):
        with open(PENDING_FILE) as f:
            return json.load(f)
    return {}


def save_pending(pending: dict):
    with open(PENDING_FILE, "w") as f:
        json.dump(pending, f, indent=2)


def find_new_s1_filings(days_back: int = 7) -> list[dict]:
    """
    Query EDGAR full-text search for S-1 filings in the last `days_back` days.
    Returns a list of {cik, company_name, filed_at}.
    """
    start = (date.today() - timedelta(days=days_back)).isoformat()
    end = date.today().isoformat()

    params = {
        "forms": "S-1",
        "dateRange": "custom",
        "startdt": start,
        "enddt": end,
    }
    url = f"{FULLTEXT_SEARCH_URL}?{urllib.parse.urlencode(params)}"

    data = _get(url)
    hits = data.get("hits", {}).get("hits", [])

    results = []
    for h in hits:
        src = h.get("_source", {})
        cik_list = src.get("ciks", [])
        if not cik_list:
            continue
        results.append({
            "cik": cik_list[0].lstrip("0"),  # normalize, e.g. "0001234567" -> "1234567"
            "company_name": src.get("display_names", ["Unknown"])[0],
            "filed_at": src.get("file_date", ""),
        })
    return results


def fetch_ticker_map() -> dict:
    """
    Returns {cik_str: ticker} for every company SEC currently has an active
    ticker for.
    """
    data = _get(TICKER_MAP_URL)
    mapping = {}
    for entry in data.get("data", []):
        # company_tickers.json format: list of [cik, name, ticker] under "data",
        # with "fields": ["cik","name","ticker"] -- handle dict or list shape
        if isinstance(entry, list):
            cik, name, ticker = entry
        else:
            cik, name, ticker = entry.get("cik"), entry.get("name"), entry.get("ticker")
        mapping[str(cik)] = ticker
    return mapping


def append_to_universe(symbol: str, name: str, exchange: str = "NEW-IPO"):
    import csv
    file_exists = os.path.exists(UNIVERSE_FILE)
    with open(UNIVERSE_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["symbol", "name", "exchange", "etf", "test_issue"])
        writer.writerow([symbol, name, exchange, "N", "N"])


def main():
    pending = load_pending()

    # Step 1: pick up any new S-1 filings from the last week
    print("Checking for new S-1 filings...", file=sys.stderr)
    new_filings = find_new_s1_filings(days_back=7)
    added = 0
    for f in new_filings:
        if f["cik"] not in pending:
            pending[f["cik"]] = {
                "company_name": f["company_name"],
                "filed_at": f["filed_at"],
                "status": "pending",
            }
            added += 1
    print(f"  {added} new S-1 filing(s) added to pending list "
          f"({len(pending)} total pending)", file=sys.stderr)

    # Be polite to SEC's servers between calls
    time.sleep(1)

    # Step 2: check which pending companies now have a live ticker
    print("Checking SEC ticker map for newly-live IPOs...", file=sys.stderr)
    ticker_map = fetch_ticker_map()

    newly_live = []
    still_pending = {}
    for cik, info in pending.items():
        ticker = ticker_map.get(cik)
        if ticker:
            newly_live.append((cik, info["company_name"], ticker))
        else:
            still_pending[cik] = info

    for cik, name, ticker in newly_live:
        print(f"  IPO LIVE: {name} ({ticker}) -- adding to universe", file=sys.stderr)
        append_to_universe(ticker, name)

    save_pending(still_pending)

    print(f"\n{len(newly_live)} new ticker(s) added to {UNIVERSE_FILE}. "
          f"{len(still_pending)} still pending IPO.", file=sys.stderr)


if __name__ == "__main__":
    main()
