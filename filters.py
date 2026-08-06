"""
filters.py

Runs once daily. Takes universe.csv (~7,500 tickers) and narrows it to
eligible.csv: only tickers meeting your liquidity floor and price floor,
with delisting-risk names excluded. This is what the intraday 30-min
technical/news scans actually run against -- scanning the full 7,500
every 30 min isn't sustainable on free infrastructure, but a filtered
~2,000-3,000 name list is.

Filters applied (see config.py to tune):
  - Price >= MIN_PRICE
  - 20-day average volume >= MIN_AVG_VOLUME
  - Not currently flagged in delisting_risk.json

Uses yfinance in batches (much more efficient than one ticker at a time).
This is the heaviest job in the whole pipeline, expect it to take a while
for ~7,500 tickers -- that's normal, it's why it only runs once a day.

NOTE: needs yfinance installed (see requirements.txt) and outbound access
to Yahoo Finance's endpoints. Test in your actual deployment, not in a
network-restricted sandbox.
"""

import csv
import json
import os
import sys
import time

import yfinance as yf

from config import (
    UNIVERSE_FILE,
    ELIGIBLE_FILE,
    DELISTING_RISK_FILE,
    MIN_PRICE,
    MIN_AVG_VOLUME,
)

BATCH_SIZE = 200          # tickers per yfinance batch request
BATCH_PAUSE_SECONDS = 2   # small pause between batches to be a polite citizen


def load_universe() -> list[dict]:
    with open(UNIVERSE_FILE, newline="") as f:
        return list(csv.DictReader(f))


def load_delisting_risk() -> set:
    if os.path.exists(DELISTING_RISK_FILE):
        with open(DELISTING_RISK_FILE) as f:
            return set(json.load(f).keys())
    return set()


def chunk(lst: list, size: int):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def get_price_volume_batch(symbols: list[str]) -> dict:
    """
    Returns {symbol: {"price": float, "avg_volume": float}} for whichever
    symbols yfinance successfully returns data for. Missing/delisted/bad
    tickers are simply omitted rather than crashing the run.
    """
    results = {}
    try:
        data = yf.download(
            tickers=" ".join(symbols),
            period="1mo",
            interval="1d",
            group_by="ticker",
            threads=True,
            progress=False,
        )
    except Exception as e:
        print(f"  [batch error] {e}", file=sys.stderr)
        return results

    for sym in symbols:
        try:
            if len(symbols) == 1:
                df = data
            else:
                df = data[sym]
            df = df.dropna()
            if df.empty:
                continue
            last_price = float(df["Close"].iloc[-1])
            avg_volume = float(df["Volume"].mean())
            results[sym] = {"price": last_price, "avg_volume": avg_volume}
        except Exception:
            continue  # ticker had no usable data this batch, skip it

    return results


def main():
    universe = load_universe()
    delisting_risk = load_delisting_risk()

    symbols = [r["symbol"] for r in universe]
    name_map = {r["symbol"]: r["name"] for r in universe}
    exchange_map = {r["symbol"]: r["exchange"] for r in universe}

    print(f"Screening {len(symbols)} tickers in batches of {BATCH_SIZE}...", file=sys.stderr)

    eligible = []
    total_batches = (len(symbols) + BATCH_SIZE - 1) // BATCH_SIZE

    for i, batch in enumerate(chunk(symbols, BATCH_SIZE), start=1):
        print(f"  Batch {i}/{total_batches}...", file=sys.stderr)
        pv = get_price_volume_batch(batch)

        for sym, vals in pv.items():
            if sym in delisting_risk:
                continue
            if vals["price"] < MIN_PRICE:
                continue
            if vals["avg_volume"] < MIN_AVG_VOLUME:
                continue
            eligible.append({
                "symbol": sym,
                "name": name_map.get(sym, ""),
                "exchange": exchange_map.get(sym, ""),
                "price": round(vals["price"], 2),
                "avg_volume": int(vals["avg_volume"]),
            })

        time.sleep(BATCH_PAUSE_SECONDS)

    with open(ELIGIBLE_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["symbol", "name", "exchange", "price", "avg_volume"])
        writer.writeheader()
        writer.writerows(eligible)

    print(f"\nWrote {len(eligible)} eligible tickers to {ELIGIBLE_FILE} "
          f"(excluded {len(delisting_risk)} delisting-risk names, "
          f"filtered from {len(symbols)} total)", file=sys.stderr)


if __name__ == "__main__":
    main()
