"""
technicals_scan.py

Runs every 30 minutes during market hours. Scans eligible.csv (the
liquidity/quality-filtered subset) for:
  - RSI extremes (low-weight signal per your preference)
  - 20/50-day moving average crossovers (momentum signal)
  - Relative volume spikes (today's volume vs 20-day average -- often the
    earliest sign something is happening, good swing-entry catalyst)

Any ONE condition matching is enough to alert (your OR-logic preference).
Alerts are de-duplicated via alert_log.py so a condition staying true
doesn't re-ping you every single cycle.

NOTE: needs yfinance and outbound network access. Test in your actual
deployment, not in a network-restricted sandbox.
"""

import csv
import sys

import pandas as pd
import yfinance as yf

from config import (
    ELIGIBLE_FILE,
    RSI_PERIOD,
    RSI_OVERSOLD,
    RSI_OVERBOUGHT,
    MA_SHORT,
    MA_LONG,
    RELATIVE_VOLUME_TRIGGER,
)
from alert_log import filter_new
from notify import send_batch_alert

BATCH_SIZE = 150


def load_eligible() -> list[str]:
    with open(ELIGIBLE_FILE, newline="") as f:
        return [row["symbol"] for row in csv.DictReader(f)]


def chunk(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def compute_rsi(closes: pd.Series, period: int = RSI_PERIOD) -> float:
    delta = closes.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss.replace(0, float("nan"))
    rsi = 100 - (100 / (1 + rs))
    return float(rsi.iloc[-1])


def evaluate_symbol(df: pd.DataFrame) -> list[str]:
    reasons = []
    df = df.dropna()
    if len(df) < MA_LONG + 1:
        return reasons  # not enough history to evaluate MA_LONG yet

    closes = df["Close"]
    volumes = df["Volume"]

    # RSI (low priority per your preference, but still included)
    rsi = compute_rsi(closes)
    if rsi <= RSI_OVERSOLD:
        reasons.append(f"RSI oversold ({rsi:.1f})")
    elif rsi >= RSI_OVERBOUGHT:
        reasons.append(f"RSI overbought ({rsi:.1f})")

    # Moving average crossover (20 over 50 = bullish momentum)
    ma_short = closes.rolling(MA_SHORT).mean()
    ma_long = closes.rolling(MA_LONG).mean()
    if len(ma_short.dropna()) >= 2 and len(ma_long.dropna()) >= 2:
        prev_short, prev_long = ma_short.iloc[-2], ma_long.iloc[-2]
        cur_short, cur_long = ma_short.iloc[-1], ma_long.iloc[-1]
        if prev_short <= prev_long and cur_short > cur_long:
            reasons.append(f"{MA_SHORT}/{MA_LONG}-day MA bullish crossover")

    # Relative volume spike
    avg_volume = volumes.iloc[:-1].tail(20).mean()  # baseline excludes today
    today_volume = volumes.iloc[-1]
    if avg_volume > 0 and today_volume / avg_volume >= RELATIVE_VOLUME_TRIGGER:
        ratio = today_volume / avg_volume
        reasons.append(f"Volume spike ({ratio:.1f}x average)")

    return reasons


def main():
    symbols = load_eligible()
    print(f"Running technical scan on {len(symbols)} eligible tickers...", file=sys.stderr)

    all_matches = []

    for i, batch in enumerate(chunk(symbols, BATCH_SIZE), start=1):
        print(f"  Batch {i}...", file=sys.stderr)
        try:
            data = yf.download(
                tickers=" ".join(batch),
                period="3mo",
                interval="1d",
                group_by="ticker",
                threads=True,
                progress=False,
            )
        except Exception as e:
            print(f"    [batch error] {e}", file=sys.stderr)
            continue

        for sym in batch:
            try:
                df = data if len(batch) == 1 else data[sym]
                reasons = evaluate_symbol(df)
            except Exception:
                continue

            if reasons:
                fresh = filter_new(sym, reasons)
                if fresh:
                    all_matches.append({"symbol": sym, "reasons": fresh})

    print(f"\n{len(all_matches)} ticker(s) matched (after de-dup).", file=sys.stderr)
    send_batch_alert(all_matches)


if __name__ == "__main__":
    main()
