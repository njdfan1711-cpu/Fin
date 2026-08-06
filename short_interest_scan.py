"""
short_interest_scan.py

Runs on FINRA's own bi-monthly (twice-a-month) short interest reporting
schedule -- checking more often just re-reads the same numbers, since
that's how often the underlying data actually updates.

Source: FINRA's official, free Equity Short Interest query API.
  https://api.finra.org/data/group/otcMarket/name/EquityShortInterest
No API key required for this public query endpoint.

This pulls the most recent settlement date's full report in one call,
then filters down to your eligible tickers locally and flags any with a
significant increase in short interest since the prior report (potential
squeeze setup).

NOTE: needs outbound access to api.finra.org. Test in your actual
deployment, not in a network-restricted sandbox.
"""

import csv
import json
import sys
import urllib.request

from config import ELIGIBLE_FILE, SHORT_INTEREST_SPIKE_PCT
from alert_log import filter_new
from notify import send_batch_alert

API_URL = "https://api.finra.org/data/group/otcMarket/name/EquityShortInterest"


def load_eligible() -> set:
    with open(ELIGIBLE_FILE, newline="") as f:
        return {row["symbol"] for row in csv.DictReader(f)}


def fetch_latest_short_interest(limit: int = 20000) -> list[dict]:
    """
    Fetches the most recent report, sorted by settlement date descending.
    We over-fetch (limit) and then only keep rows matching the single most
    recent settlementDate actually present in the response, since a query
    without a specific date returns whatever the API considers current.
    """
    payload = {
        "limit": limit,
        "sortFields": ["-settlementDate"],
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "personal-stock-scanner",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    eligible = load_eligible()
    print(f"Fetching latest FINRA short interest report...", file=sys.stderr)

    try:
        rows = fetch_latest_short_interest()
    except Exception as e:
        print(f"[error fetching short interest] {e}", file=sys.stderr)
        return

    if not rows:
        print("No data returned.", file=sys.stderr)
        return

    latest_date = rows[0].get("settlementDate")
    latest_rows = [r for r in rows if r.get("settlementDate") == latest_date]
    print(f"  {len(latest_rows)} row(s) for settlement date {latest_date}", file=sys.stderr)

    all_matches = []
    for r in latest_rows:
        symbol = r.get("issueSymbolIdentifier", "")
        if symbol not in eligible:
            continue

        change_pct = r.get("changePercent")
        if change_pct is None:
            continue
        try:
            change_pct = float(change_pct)
        except (TypeError, ValueError):
            continue

        if change_pct >= SHORT_INTEREST_SPIKE_PCT:
            reason = [f"Short interest up {change_pct:.1f}% since last report"]
            fresh = filter_new(symbol, reason)
            if fresh:
                all_matches.append({"symbol": symbol, "reasons": fresh})

    print(f"\n{len(all_matches)} ticker(s) matched short interest spike.", file=sys.stderr)
    send_batch_alert(all_matches)


if __name__ == "__main__":
    main()
