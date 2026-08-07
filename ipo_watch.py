"""
ipo_watch.py

Keeps your scan universe from going stale by automatically catching new IPOs.

How it works (all free, official SEC sources, no API key):

1. NEW REGISTRATIONS
   Uses SEC EDGAR's "current filings" feed, filtered to Form S-1 (the form
   companies file to register for an IPO). This is an Atom/RSS feed
   purpose-built for "show me recent filings of this type" -- unlike
   EDGAR's full-text SEARCH API, it doesn't require a keyword/query term,
   which is what caused an HTTP 500 in the original version (that endpoint
   expects an actual search query, and we were only passing form+date
   filters with nothing to search for).

   Endpoint: https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=S-1&...&output=atom

2. GOING LIVE
   An S-1 filing alone doesn't mean the company will actually IPO, or when.
   The reliable "it's actually trading now" signal is SEC's own ticker map:

   https://www.sec.gov/files/company_tickers.json

   This free file maps every CIK to its active ticker. Each run, we check
   every CIK in our pending list against this file. The moment a pending CIK
   shows up with a ticker, that means the IPO priced and the stock is live --
   we add it straight into universe.csv and drop it from pending.

Run this once a day, before your main scan job, right after universe_builder.py.

NOTE: Needs outbound access to sec.gov. If running in a network-restricted
sandbox, allow that domain or run this step elsewhere.
"""

import json
import os
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

# SEC requires a real identifying User-Agent for automated access -- put your
# own name/email here per SEC's fair-access rules (https://www.sec.gov/os/webmaster-faq#developers)
USER_AGENT = "personal-stock-scanner contact: your-email@example.com"

CURRENT_FILINGS_URL = (
    "https://www.sec.gov/cgi-bin/browse-edgar"
    "?action=getcurrent&type=S-1&company=&dateb=&owner=include&count=100&output=atom"
)
TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"

ATOM_NS = {"a": "http://www.w3.org/2005/Atom"}
# Matches "S-1 - COMPANY NAME (0001234567) (Filer)" style titles, pulling
# out the CIK from the parentheses.
CIK_PATTERN = re.compile(r"\((\d{7,10})\)")

PENDING_FILE = "pending_ipos.json"
UNIVERSE_FILE = "universe.csv"


def _get_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def _get_json(url: str) -> dict:
    return json.loads(_get_bytes(url).decode("utf-8"))


def load_pending() -> dict:
    if os.path.exists(PENDING_FILE):
        with open(PENDING_FILE) as f:
            return json.load(f)
    return {}


def save_pending(pending: dict):
    with open(PENDING_FILE, "w") as f:
        json.dump(pending, f, indent=2)


def find_new_s1_filings() -> list[dict]:
    """
    Fetches the current-filings Atom feed for Form S-1 and parses out
    company name, CIK, and filed date. Returns a list of
    {cik, company_name, filed_at}.
    """
    try:
        raw = _get_bytes(CURRENT_FILINGS_URL)
    except Exception as e:
        print(f"[error fetching current filings feed] {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(raw)
    except ET.ParseError as e:
        print(f"[error parsing Atom feed] {e}", file=sys.stderr)
        return []

    results = []
    for entry in root.findall("a:entry", ATOM_NS):
        title_el = entry.find("a:title", ATOM_NS)
        updated_el = entry.find("a:updated", ATOM_NS)
        if title_el is None or not title_el.text:
            continue

        title = title_el.text  # e.g. "S-1 - EXAMPLE CORP (0001234567) (Filer)"
        cik_match = CIK_PATTERN.search(title)
        if not cik_match:
            continue
        cik = cik_match.group(1).lstrip("0")

        # Company name is everything between "S-1 - " and " (CIK...)"
        name_part = title.split(" - ", 1)[-1]
        company_name = CIK_PATTERN.split(name_part)[0].strip()

        filed_at = updated_el.text[:10] if updated_el is not None and updated_el.text else ""

        results.append({"cik": cik, "company_name": company_name, "filed_at": filed_at})

    return results


def fetch_ticker_map() -> dict:
    """Returns {cik_str: ticker} for every company SEC currently has an active ticker for."""
    data = _get_json(TICKER_MAP_URL)
    mapping = {}
    for entry in data.get("data", []):
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

    print("Checking for new S-1 filings...", file=sys.stderr)
    new_filings = find_new_s1_filings()
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

    time.sleep(1)  # be polite to SEC's servers between calls

    print("Checking SEC ticker map for newly-live IPOs...", file=sys.stderr)
    try:
        ticker_map = fetch_ticker_map()
    except Exception as e:
        print(f"[error fetching ticker map] {e}", file=sys.stderr)
        ticker_map = {}

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
