"""
universe_builder.py

Builds the master scan universe: every actively-listed ticker on Nasdaq, NYSE,
NYSE American, and Cboe BZX (which covers Dow components automatically, since
the Dow is just 30 stocks that already trade on Nasdaq/NYSE -- there's no
separate "Dow list" to pull).

Source: Nasdaq Trader's free public Symbol Directory. No API key, no signup.
    https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt   (Nasdaq)
    https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt    (NYSE, NYSE American, Cboe BZX, etc.)

These files are refreshed daily by Nasdaq, so re-running this script gives you
a fresh universe each time (run it once a day before your scan job).

Output: universe.csv with columns: symbol, name, exchange, etf, test_issue

NOTE: This script needs outbound access to www.nasdaqtrader.com. If you're
running it somewhere with restricted network egress (e.g. a locked-down
sandbox), allow that domain or run this step from an unrestricted machine.
"""

import csv
import io
import sys
import urllib.request

NASDAQ_URL = "https://www.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt"
OTHER_URL = "https://www.nasdaqtrader.com/dynamic/SymDir/otherlisted.txt"

# Nasdaq's server wants a normal-looking User-Agent or it may reject the request.
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; personal-stock-scanner/1.0)"}


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_nasdaqlisted(raw: str) -> list[dict]:
    """
    Pipe-delimited, header row, and a footer line starting with 'File Creation Time'
    that must be dropped.
    """
    lines = [l for l in raw.splitlines() if l and not l.startswith("File Creation Time")]
    reader = csv.DictReader(lines, delimiter="|")
    rows = []
    for r in reader:
        rows.append({
            "symbol": r["Symbol"].strip(),
            "name": r["Security Name"].strip(),
            "exchange": "NASDAQ",
            "etf": r.get("ETF", "N").strip(),
            "test_issue": r.get("Test Issue", "N").strip(),
        })
    return rows


def parse_otherlisted(raw: str) -> list[dict]:
    """
    Same idea, different column names. 'Exchange' column contains a code:
    N = NYSE, A = NYSE American, P = NYSE Arca, Z = Cboe BZX, V = IEX, etc.
    """
    lines = [l for l in raw.splitlines() if l and not l.startswith("File Creation Time")]
    reader = csv.DictReader(lines, delimiter="|")
    exch_map = {
        "N": "NYSE",
        "A": "NYSE American",
        "P": "NYSE Arca",
        "Z": "Cboe BZX",
        "V": "IEX",
    }
    rows = []
    for r in reader:
        code = r.get("Exchange", "").strip()
        rows.append({
            "symbol": r["ACT Symbol"].strip(),
            "name": r["Security Name"].strip(),
            "exchange": exch_map.get(code, code or "OTHER"),
            "etf": r.get("ETF", "N").strip(),
            "test_issue": r.get("Test Issue", "N").strip(),
        })
    return rows


def build_universe(include_etfs: bool = False) -> list[dict]:
    print("Fetching Nasdaq-listed symbols...", file=sys.stderr)
    nasdaq_rows = parse_nasdaqlisted(fetch_text(NASDAQ_URL))

    print("Fetching NYSE / NYSE American / other-listed symbols...", file=sys.stderr)
    other_rows = parse_otherlisted(fetch_text(OTHER_URL))

    combined = nasdaq_rows + other_rows

    # Drop test issues always -- they're not real tradeable securities.
    combined = [r for r in combined if r["test_issue"] != "Y"]

    # Drop preferred shares, warrants, rights, units, and when-issued
    # securities -- Nasdaq's symbol file encodes these with a '$' in the
    # symbol (e.g. "ALL$I"), and SPAC units/warrants/dual-class notations
    # often use a '.' suffix (e.g. "ALUB.U", "AKO.A"). Yahoo Finance uses
    # different conventions for some of these (hyphens instead of dots),
    # which caused a wall of "no price data found" noise. More importantly,
    # these instruments don't have their own fundamentals in the way this
    # strategy needs -- they derive from the underlying common stock -- so
    # treating all of them as out of scope keeps things simple and avoids
    # naming-convention mismatches across Yahoo/FINRA/Finnhub.
    combined = [r for r in combined if "$" not in r["symbol"] and "." not in r["symbol"]]

    if not include_etfs:
        combined = [r for r in combined if r["etf"] != "Y"]

    # Dedupe by symbol (a handful of tickers can appear in both files due to
    # dual listings) -- keep the first occurrence.
    seen = set()
    deduped = []
    for r in combined:
        if r["symbol"] in seen or not r["symbol"]:
            continue
        seen.add(r["symbol"])
        deduped.append(r)

    deduped.sort(key=lambda r: r["symbol"])
    return deduped


def main():
    include_etfs = "--include-etfs" in sys.argv
    universe = build_universe(include_etfs=include_etfs)

    out_path = "universe.csv"
    with open(out_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["symbol", "name", "exchange", "etf", "test_issue"])
        writer.writeheader()
        writer.writerows(universe)

    print(f"Wrote {len(universe)} tickers to {out_path}", file=sys.stderr)
    by_exchange = {}
    for r in universe:
        by_exchange[r["exchange"]] = by_exchange.get(r["exchange"], 0) + 1
    for exch, count in sorted(by_exchange.items()):
        print(f"  {exch}: {count}", file=sys.stderr)


if __name__ == "__main__":
    main()
