"""
short_interest_scan.py

Runs on FINRA's own bi-monthly (twice-a-month) short interest reporting
schedule -- checking more often just re-reads the same numbers, since
that's how often the underlying data actually updates.

Source: FINRA's official Equity Short Interest query API.
  https://api.finra.org/data/group/otcMarket/name/EquityShortInterest

BUG FIX (post-launch): the original version got an HTTP 400 because it
requested results sorted by settlementDate without also including a
required filter locking to one exact date -- FINRA's API requires an
EQUAL compareFilter on a dataset's "partition field" any time you sort
by it. Rather than guess at a date, this version first asks FINRA's
/partitions endpoint which settlement dates actually exist, picks the
most recent one, and then queries with an explicit filter for that date.

NOTE: needs outbound access to api.finra.org. Test in your actual
deployment, not in a network-restricted sandbox.
"""

import csv
import json
import sys
import urllib.request

from config import ELIGIBLE_FILE, SHORT_INTEREST_SPIKE_PCT
from signals_store import record_signal

DATA_URL = "https://api.finra.org/data/group/otcMarket/name/EquityShortInterest"
PARTITIONS_URL = "https://api.finra.org/partitions/group/otcMarket/name/EquityShortInterest"


def load_eligible() -> set:
    with open(ELIGIBLE_FILE, newline="") as f:
        return {row["symbol"] for row in csv.DictReader(f)}


def _post(url: str, payload: dict) -> list:
    req = urllib.request.Request(
        url,
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


def _get(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/json",
                                                 "User-Agent": "personal-stock-scanner"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_latest_settlement_date() -> str | None:
    """
    Asks FINRA which settlement dates actually exist for this dataset and
    returns the most recent one. This is the correct way to discover
    "today's report date" rather than guessing.
    """
    try:
        data = _get(PARTITIONS_URL)
    except Exception as e:
        print(f"[error fetching partitions] {e}", file=sys.stderr)
        return None

    # Response shape can vary -- handle a couple of plausible structures
    # defensively rather than assuming one exact format.
    dates = []
    if isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict):
                val = entry.get("settlementDate") or entry.get("value")
                if val:
                    dates.append(val)
            elif isinstance(entry, str):
                dates.append(entry)
    elif isinstance(data, dict):
        dates = data.get("settlementDate", []) or data.get("values", [])

    if not dates:
        return None
    return sorted(dates)[-1]  # most recent, dates sort correctly as ISO strings


def fetch_short_interest_for_date(settlement_date: str, limit: int = 20000) -> list[dict]:
    payload = {
        "compareFilters": [
            {"compareType": "EQUAL", "fieldName": "settlementDate", "fieldValue": settlement_date}
        ],
        "limit": limit,
    }
    return _post(DATA_URL, payload)


def main():
    eligible = load_eligible()
    print("Looking up the latest FINRA short interest settlement date...", file=sys.stderr)

    latest_date = get_latest_settlement_date()
    if not latest_date:
        print("Could not determine latest settlement date -- skipping this run.", file=sys.stderr)
        return
    print(f"  Latest settlement date: {latest_date}", file=sys.stderr)

    try:
        rows = fetch_short_interest_for_date(latest_date)
    except Exception as e:
        print(f"[error fetching short interest data] {e}", file=sys.stderr)
        return

    print(f"  {len(rows)} row(s) returned for {latest_date}", file=sys.stderr)

    total_signals = 0
    for r in rows:
        symbol = r.get("issueSymbolIdentifier", "")
        if symbol not in eligible:
            continue

        change_pct = r.get("changePercent") or r.get("percentageChangefromPreviousShort")
        if change_pct is None:
            continue
        try:
            change_pct = float(change_pct)
        except (TypeError, ValueError):
            continue

        if change_pct >= SHORT_INTEREST_SPIKE_PCT:
            detail = f"Short interest up {change_pct:.1f}% since last report"
            strength = min(change_pct / 50, 1.0)
            record_signal(symbol, "short_interest", detail, strength=strength)
            total_signals += 1

    print(f"\n{total_signals} short interest signal(s) recorded.", file=sys.stderr)


if __name__ == "__main__":
    main()
