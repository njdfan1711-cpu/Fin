"""
momentum_scan.py

Runs every 30 minutes during market hours, alongside technicals_scan.py.

A deliberately SEPARATE, opposite-philosophy track from the rest of the
screener: instead of quality + multi-signal confluence, this looks for the
setup behind fast, violent moves -- a low-float stock seeing an unusually
large, price-confirmed volume spike. This is almost certainly the actual
mechanism behind paid "AI signal" products (see the Reddit thread on the
"Oracle Trading Platform" that prompted this: $2,500-$5,000+ for what one
user described as "an algorithm that helps identify stocks that are
showing signs of likely moves... dependably tradable low floats").
There's no need to pay for that -- it's a straightforward, disclosed
screen, not a black box.

IMPORTANT: this signal is recorded under its own "momentum" category and
is EXCLUDED from the main confluence scoring in compose_alerts.py (see
MOMENTUM_CATEGORY there). It never counts toward MIN_SIGNAL_CATEGORIES or
the STRONG/MODERATE tier used by your quality-backed picks -- it gets its
own small, separately-capped section of the push instead, so it can never
crowd out or dilute your main list.

Two-stage filter, cheapest checks first:
  1. Float proxy (shares outstanding, from float_data.json -- written
     daily by fundamentals_scan.py at zero extra API cost) narrows
     eligible.csv down to a small low-float candidate set BEFORE any
     price data is fetched.
  2. Only that small candidate set gets a batched yfinance pull to check
     today's relative volume AND today's price change -- both required,
     so a volume spike with no price follow-through (which could just be
     institutional rebalancing, not a genuine breakout) doesn't qualify.

NOTE: needs yfinance and outbound network access, like technicals_scan.py.
"""

import csv
import json
import sys
import time

import yfinance as yf

from config import (
    ELIGIBLE_FILE,
    FLOAT_DATA_FILE,
    MAX_SHARES_OUTSTANDING_MOMENTUM,
    MOMENTUM_RELATIVE_VOLUME_TRIGGER,
    MOMENTUM_MIN_DAY_CHANGE_PCT,
)
from signals_store import record_signal

BATCH_SIZE = 75
BATCH_PAUSE_SECONDS = 4


def load_eligible() -> list[str]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return [row["symbol"] for row in csv.DictReader(f)]


def load_float_data() -> dict:
    try:
        with open(FLOAT_DATA_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def chunk(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def evaluate_symbol(df, share_outstanding: float):
    """Returns (detail, strength) or None."""
    df = df.dropna()
    closes = df["Close"]
    volumes = df["Volume"]

    if len(closes) < 21:
        return None

    current_price = float(closes.iloc[-1])
    prev_close = float(closes.iloc[-2])
    if prev_close <= 0:
        return None
    day_change_pct = ((current_price - prev_close) / prev_close) * 100

    avg_volume = volumes.iloc[:-1].tail(20).mean()
    today_volume = volumes.iloc[-1]
    rel_volume_ratio = (today_volume / avg_volume) if avg_volume > 0 else 0

    if rel_volume_ratio < MOMENTUM_RELATIVE_VOLUME_TRIGGER:
        return None
    if day_change_pct < MOMENTUM_MIN_DAY_CHANGE_PCT:
        return None

    detail = (
        f"Low float ({share_outstanding:.1f}M shares out) + "
        f"{rel_volume_ratio:.1f}x volume + {day_change_pct:+.1f}% today"
    )
    # Strength scales with how far past the (already tight) thresholds
    # this candidate is -- a 20x-volume, +30%-day name should rank above
    # one that just barely cleared the bar.
    strength = min(
        (rel_volume_ratio / MOMENTUM_RELATIVE_VOLUME_TRIGGER) *
        (day_change_pct / MOMENTUM_MIN_DAY_CHANGE_PCT) / 2,
        1.0,
    )
    return (detail, strength)


def main():
    eligible = set(load_eligible())
    float_data = load_float_data()

    candidates = [
        sym for sym, shares in float_data.items()
        if sym in eligible and shares is not None
        and shares <= MAX_SHARES_OUTSTANDING_MOMENTUM
    ]

    print(f"{len(candidates)} low-float candidate(s) (<= "
          f"{MAX_SHARES_OUTSTANDING_MOMENTUM / 1_000_000:.0f}M shares out) "
          f"out of {len(eligible)} eligible tickers.", file=sys.stderr)

    if not candidates:
        print("Nothing to scan -- no low-float candidates today "
              "(or float_data.json hasn't run yet).", file=sys.stderr)
        return

    total_signals = 0
    total_batches = (len(candidates) + BATCH_SIZE - 1) // BATCH_SIZE

    for i, batch in enumerate(chunk(candidates, BATCH_SIZE), start=1):
        if i % 5 == 0 or i == total_batches:
            print(f"  Batch {i}/{total_batches}...", file=sys.stderr)
        try:
            data = yf.download(
                tickers=" ".join(batch),
                period="1mo",
                interval="1d",
                group_by="ticker",
                threads=True,
                progress=False,
            )
        except Exception as e:
            print(f"    [batch error] {e}", file=sys.stderr)
            time.sleep(BATCH_PAUSE_SECONDS)
            continue

        for sym in batch:
            try:
                df = data if len(batch) == 1 else data[sym]
                result = evaluate_symbol(df, float_data[sym])
            except Exception:
                continue
            if result:
                detail, strength = result
                record_signal(sym, "momentum", detail, strength=strength)
                total_signals += 1

        time.sleep(BATCH_PAUSE_SECONDS)

    print(f"\n{total_signals} momentum signal(s) recorded.", file=sys.stderr)


if __name__ == "__main__":
    main()
