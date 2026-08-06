"""
delisting_risk_scan.py

Flags tickers currently under an exchange listing-compliance deficiency
notice (e.g. minimum bid price, minimum market cap, minimum shareholder
equity) so the eligible-universe filter can exclude or de-prioritize them,
per your preference to generally avoid delisting-risk names.

Source: SEC EDGAR full-text search for Form 8-K filings (Item 3.01,
"Notice of Delisting or Failure to Satisfy a Continued Listing Rule") --
this is the exact form/item companies are legally required to file when
they receive such a notice. Free, official, no API key.

A flag here means "received a deficiency notice and hasn't yet shown as
resolved" -- it's a caution flag, not a certainty of delisting. Companies
often regain compliance. This errs toward inclusion in the risk list
rather than missing a real risk.

Output: delisting_risk.json -- {ticker: {"company_name", "filed_at", "cik"}}

NOTE: needs outbound access to efts.sec.gov / sec.gov. Test in your actual
deployment (GitHub Actions), not in a network-restricted sandbox.
"""

import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, timedelta

USER_AGENT = "personal-stock-scanner contact: your-email@example.com"
FULLTEXT_SEARCH_URL = "https://efts.sec.gov/LATEST/search-index"
TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json"

OUTPUT_FILE = "delisting_risk.json"

# Companies generally have a cure period (often 180 days, sometimes longer
# with extensions) to regain compliance. We look back further than that
# window to stay conservative, then rely on re-running this regularly --
# a flag naturally ages out if no new deficiency notice keeps appearing.
LOOKBACK_DAYS = 270


def _get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_ticker_map() -> dict:
    """Returns {cik_str: ticker}"""
    data = _get(TICKER_MAP_URL)
    mapping = {}
    for entry in data.get("data", []):
        if isinstance(entry, list):
            cik, name, ticker = entry
        else:
            cik, name, ticker = entry.get("cik"), entry.get("name"), entry.get("ticker")
        mapping[str(cik)] = ticker
    return mapping


def find_deficiency_filings(days_back: int = LOOKBACK_DAYS) -> list[dict]:
    start = (date.today() - timedelta(days=days_back)).isoformat()
    end = date.today().isoformat()

    params = {
        "forms": "8-K",
        "dateRange": "custom",
        "startdt": start,
        "enddt": end,
        # Full text search across 8-K item text -- searching for the
        # standard language used in Item 3.01 disclosures.
        "q": "\"notice of delisting\" OR \"failure to satisfy\" OR \"minimum bid price\"",
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
            "cik": cik_list[0].lstrip("0"),
            "company_name": src.get("display_names", ["Unknown"])[0],
            "filed_at": src.get("file_date", ""),
        })
    return results


def main():
    print("Searching SEC EDGAR for delisting-risk 8-K filings...", file=sys.stderr)
    filings = find_deficiency_filings()
    print(f"  Found {len(filings)} filing(s) in the lookback window", file=sys.stderr)

    time.sleep(1)  # be polite to SEC's servers between calls

    print("Mapping CIKs to tickers...", file=sys.stderr)
    ticker_map = fetch_ticker_map()

    flagged = {}
    unmatched = 0
    for f in filings:
        ticker = ticker_map.get(f["cik"])
        if ticker:
            flagged[ticker] = {
                "company_name": f["company_name"],
                "filed_at": f["filed_at"],
                "cik": f["cik"],
            }
        else:
            unmatched += 1

    with open(OUTPUT_FILE, "w") as out:
        json.dump(flagged, out, indent=2)

    print(f"Wrote {len(flagged)} flagged ticker(s) to {OUTPUT_FILE} "
          f"({unmatched} filing(s) had no active ticker, likely already delisted)",
          file=sys.stderr)


if __name__ == "__main__":
    main()
