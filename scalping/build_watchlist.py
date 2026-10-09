"""
build_watchlist.py -- builds the scalp bot's daily watch list from the
Daily Scan's eligible.csv (price >= $3, 20-day avg volume >= 500k).

Scalping only works where it is cheap to get in and out, so this narrows
the ~2,400 eligible names to the most liquid, reasonably priced ones:

  * price between MIN_PRICE and MAX_PRICE (cheap stocks have spreads that
    are huge relative to a ~0.35% target; MAX_PRICE keeps $3,000 buying at
    least a few shares)
  * dollar volume (price x 20-day avg volume) >= MIN_DOLLAR_VOLUME
  * plain symbols only (letters), to avoid quote-format surprises with
    class shares like BRK.B
  * if measured_spreads.csv is present (from spread_report.py), names whose
    measured median spread is above MAX_MEDIAN_SPREAD_PCT are dropped.
    Names with no measured spread yet are KEPT (so the logger can measure
    them) and marked spread_known = no.
  * ranked by dollar volume, capped at MAX_NAMES

Run from the scalping/ folder:  python build_watchlist.py
Reads ../eligible.csv, writes scalp_watchlist.csv. Standard library only.

LATER: once spread_logger.py has real bid/ask data, add a measured-spread
filter here (e.g. drop anything whose median spread is above ~1.5 cents).
"""
import csv
import os
import re
import sys

ELIGIBLE_FILE = os.path.join("..", "eligible.csv")
OUTPUT_FILE = "scalp_watchlist.csv"

MIN_PRICE = 20.0
MAX_PRICE = 1000.0
MIN_DOLLAR_VOLUME = 100_000_000   # dollars traded per day, approx
MAX_NAMES = 500
MEASURED_SPREADS_FILE = "measured_spreads.csv"
MAX_MEDIAN_SPREAD_PCT = 0.03      # round trip ~ <= $0.90 on a $3,000 trade


def load_measured_spreads() -> dict:
    if not os.path.exists(MEASURED_SPREADS_FILE):
        return {}
    table = {}
    with open(MEASURED_SPREADS_FILE, newline="") as f:
        for r in csv.DictReader(f):
            try:
                table[r["symbol"].strip().upper()] = float(r["median_pct"])
            except (KeyError, ValueError):
                continue
    return table


def main() -> int:
    if not os.path.exists(ELIGIBLE_FILE):
        print(f"{ELIGIBLE_FILE} not found -- run from the scalping/ folder.", file=sys.stderr)
        return 1

    with open(ELIGIBLE_FILE, newline="") as f:
        rows = list(csv.DictReader(f))

    spreads = load_measured_spreads()
    kept, skipped_symbol, dropped_wide = [], 0, 0
    for r in rows:
        sym = (r.get("symbol") or "").strip().upper()
        try:
            price = float(r["price"])
            avg_vol = float(r["avg_volume"])
        except (KeyError, ValueError, TypeError):
            continue
        if not re.fullmatch(r"[A-Z]{1,5}", sym):
            skipped_symbol += 1
            continue
        dollar_vol = price * avg_vol
        if MIN_PRICE <= price <= MAX_PRICE and dollar_vol >= MIN_DOLLAR_VOLUME:
            spread_pct = spreads.get(sym)
            if spread_pct is not None and spread_pct > MAX_MEDIAN_SPREAD_PCT:
                dropped_wide += 1
                continue
            kept.append({
                "symbol": sym,
                "name": r.get("name", ""),
                "exchange": r.get("exchange", ""),
                "price": round(price, 2),
                "avg_volume": int(avg_vol),
                "dollar_volume": int(dollar_vol),
                "median_spread_pct": "" if spread_pct is None else spread_pct,
                "spread_known": "no" if spread_pct is None else "yes",
            })

    kept.sort(key=lambda x: x["dollar_volume"], reverse=True)
    passed = len(kept)
    kept = kept[:MAX_NAMES]
    for i, k in enumerate(kept, 1):
        k["rank"] = i

    with open(OUTPUT_FILE, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "rank", "symbol", "name", "exchange", "price", "avg_volume", "dollar_volume",
            "median_spread_pct", "spread_known"])
        w.writeheader()
        w.writerows(kept)

    print(f"eligible rows: {len(rows)} | non-plain symbols skipped: {skipped_symbol} | "
          f"dropped for wide measured spread: {dropped_wide} | "
          f"passed filters: {passed} | written (cap {MAX_NAMES}): {len(kept)}")
    known = sum(1 for k in kept if k["spread_known"] == "yes")
    print(f"spread measured for {known} of {len(kept)} names; the rest still need logging")
    print(f"top 5: {', '.join(k['symbol'] for k in kept[:5])}")
    if kept:
        print(f"lowest included: {kept[-1]['symbol']} "
              f"(${kept[-1]['dollar_volume']/1e6:,.0f}M/day at ${kept[-1]['price']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
