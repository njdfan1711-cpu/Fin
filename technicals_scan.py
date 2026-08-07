"""
technicals_scan.py

Runs every 30 minutes during market hours. Scans eligible.csv (the
liquidity/quality-filtered subset) for:
  - RSI extremes (low-weight signal per your preference)
  - 20/50-day moving average crossovers (momentum signal)
  - Relative volume spikes (today's volume vs 20-day average -- often the
    earliest sign something is happening, good swing-entry catalyst)

Signals are RECORDED via signals_store.py, not pushed directly -- a
separate compose_alerts.py step decides what's actually push-worthy by
requiring agreement across multiple signal categories.

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
from signals_store import record_signal

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


def evaluate_symbol(symbol: str, df: pd.DataFrame):
    """Records any matching signals directly; returns count of signals found."""
    df = df.dropna()
    if len(df) < MA_LONG + 1:
        return 0

    closes = df["Close"]
    volumes = df["Volume"]
    found = 0

    # RSI -- low priority per your preference (low strength weight), but
    # still recorded so it can contribute to confluence with other signals
    rsi = compute_rsi(closes)
    if rsi <= RSI_OVERSOLD:
        record_signal(symbol, "technical", f"RSI oversold ({rsi:.1f})", strength=0.4)
        found += 1
    elif rsi >= RSI_OVERBOUGHT:
        record_signal(symbol, "technical", f"RSI overbought ({rsi:.1f})", strength=0.4)
        found += 1

    # Moving average crossover (20 over 50 = bullish momentum)
    ma_short = closes.rolling(MA_SHORT).mean()
    ma_long = closes.rolling(MA_LONG).mean()
    if len(ma_short.dropna()) >= 2 and len(ma_long.dropna()) >= 2:
        prev_short, prev_long = ma_short.iloc[-2], ma_long.iloc[-2]
        cur_short, cur_long = ma_short.iloc[-1], ma_long.iloc[-1]
        if prev_short <= prev_long and cur_short > cur_long:
            record_signal(symbol, "technical",
                          f"{MA_SHORT}/{MA_LONG}-day MA bullish crossover", strength=0.8)
            found += 1

    # Relative volume spike -- often the earliest tell of a real catalyst
    avg_volume = volumes.iloc[:-1].tail(20).mean()
    today_volume = volumes.iloc[-1]
    if avg_volume > 0 and today_volume / avg_volume >= RELATIVE_VOLUME_TRIGGER:
        ratio = today_volume / avg_volume
        record_signal(symbol, "technical", f"Volume spike ({ratio:.1f}x average)",
                      strength=min(ratio / 5, 1.0))
        found += 1

    return found


def main():
    symbols = load_eligible()
    print(f"Running technical scan on {len(symbols)} eligible tickers...", file=sys.stderr)

    total_signals = 0

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
                total_signals += evaluate_symbol(sym, df)
            except Exception:
                continue

    print(f"\n{total_signals} technical signal(s) recorded. "
          f"Run compose_alerts.py to send any push-worthy results.", file=sys.stderr)


if __name__ == "__main__":
    main()

