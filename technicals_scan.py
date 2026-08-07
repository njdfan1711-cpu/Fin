"""
technicals_scan.py

Runs every 30 minutes during market hours. Scans eligible.csv (the
liquidity/quality-filtered subset) for:
  - RSI extremes (low-weight signal per your preference -- kept as
    oversold/overbought mean-reversion, deliberately NOT changed to a
    momentum-confirmation range)
  - 20/50-day moving average crossovers (momentum signal)
  - Relative volume spikes (today's volume vs 20-day average)
  - MACD bullish crossover (12/26 EMA, 9-day signal line)
  - 50/200-day MA alignment (price above both, both trending up)
  - Relative strength vs SPY (outperforming the broader market over the
    last 20 trading days)

BUG FIX (post-launch): the original version called record_signal() up to
three times per ticker, and since each call overwrote the previous one in
the same "technical" category slot, only the LAST finding ever actually
got recorded -- the others were silently lost. This version collects all
findings for a ticker first, then records them as ONE combined signal.

Signals are RECORDED via signals_store.py, not pushed directly --
compose_alerts.py decides what's push-worthy by requiring agreement
across multiple signal categories.

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
SPY_LOOKBACK_DAYS = 20  # for relative strength comparison


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


def compute_macd(closes: pd.Series):
    """Returns (macd_line, signal_line) as pandas Series."""
    ema12 = closes.ewm(span=12, adjust=False).mean()
    ema26 = closes.ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    return macd_line, signal_line


def get_spy_return(days: int = SPY_LOOKBACK_DAYS) -> float | None:
    """Fetched ONCE per cycle, not per ticker -- cheap."""
    try:
        df = yf.download("SPY", period="2mo", interval="1d", progress=False)
        closes = df["Close"].dropna()
        if len(closes) < days + 1:
            return None
        return float((closes.iloc[-1] / closes.iloc[-1 - days] - 1) * 100)
    except Exception as e:
        print(f"[SPY fetch error] {e}", file=sys.stderr)
        return None


def evaluate_symbol(df: pd.DataFrame, spy_return: float | None):
    """Returns a list of (detail, strength) tuples for every signal found."""
    findings = []
    df = df.dropna()
    if len(df) < 200:
        # Not enough history for the 200-day MA check -- still evaluate
        # the shorter-window signals rather than skipping entirely.
        pass

    closes = df["Close"]
    volumes = df["Volume"]

    if len(closes) < MA_LONG + 1:
        return findings  # too little history for anything meaningful

    # RSI -- kept as mean-reversion (oversold/overbought), unchanged
    rsi = compute_rsi(closes)
    if rsi <= RSI_OVERSOLD:
        findings.append((f"RSI oversold ({rsi:.1f})", 0.4))
    elif rsi >= RSI_OVERBOUGHT:
        findings.append((f"RSI overbought ({rsi:.1f})", 0.4))

    # 20/50-day MA crossover
    ma_short = closes.rolling(MA_SHORT).mean()
    ma_long = closes.rolling(MA_LONG).mean()
    if len(ma_short.dropna()) >= 2 and len(ma_long.dropna()) >= 2:
        prev_short, prev_long = ma_short.iloc[-2], ma_long.iloc[-2]
        cur_short, cur_long = ma_short.iloc[-1], ma_long.iloc[-1]
        if prev_short <= prev_long and cur_short > cur_long:
            findings.append((f"{MA_SHORT}/{MA_LONG}-day MA bullish crossover", 0.8))

    # Relative volume spike
    avg_volume = volumes.iloc[:-1].tail(20).mean()
    today_volume = volumes.iloc[-1]
    if avg_volume > 0 and today_volume / avg_volume >= RELATIVE_VOLUME_TRIGGER:
        ratio = today_volume / avg_volume
        findings.append((f"Volume spike ({ratio:.1f}x average)", min(ratio / 5, 1.0)))

    # MACD bullish crossover
    macd_line, signal_line = compute_macd(closes)
    if len(macd_line.dropna()) >= 2:
        prev_macd, prev_signal = macd_line.iloc[-2], signal_line.iloc[-2]
        cur_macd, cur_signal = macd_line.iloc[-1], signal_line.iloc[-1]
        if prev_macd <= prev_signal and cur_macd > cur_signal:
            findings.append(("MACD bullish crossover", 0.7))

    # 50/200-day MA alignment (price above both, both trending up)
    if len(closes) >= 200:
        ma50 = closes.rolling(50).mean()
        ma200 = closes.rolling(200).mean()
        cur_price = closes.iloc[-1]
        if (
            cur_price > ma50.iloc[-1] > ma200.iloc[-1]
            and ma50.iloc[-1] > ma50.iloc[-6]      # 50-day MA rising over the last week
            and ma200.iloc[-1] > ma200.iloc[-21]   # 200-day MA rising over the last month
        ):
            findings.append(("Price above rising 50/200-day MAs", 0.6))

    # Relative strength vs SPY
    if spy_return is not None and len(closes) >= SPY_LOOKBACK_DAYS + 1:
        ticker_return = float((closes.iloc[-1] / closes.iloc[-1 - SPY_LOOKBACK_DAYS] - 1) * 100)
        if ticker_return > spy_return:
            outperformance = ticker_return - spy_return
            findings.append((f"Outperforming S&P 500 by {outperformance:.1f}pts (20d)",
                            min(outperformance / 15, 1.0)))

    return findings


def main():
    symbols = load_eligible()
    print(f"Running technical scan on {len(symbols)} eligible tickers...", file=sys.stderr)

    spy_return = get_spy_return()
    print(f"  SPY {SPY_LOOKBACK_DAYS}-day return: "
          f"{spy_return:.2f}%" if spy_return is not None else "  SPY return unavailable",
          file=sys.stderr)

    total_signals = 0
    total_tickers_with_signals = 0

    for i, batch in enumerate(chunk(symbols, BATCH_SIZE), start=1):
        print(f"  Batch {i}...", file=sys.stderr)
        try:
            data = yf.download(
                tickers=" ".join(batch),
                period="1y",   # need a full year for the 200-day MA check
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
                findings = evaluate_symbol(df, spy_return)
            except Exception:
                continue

            if findings:
                combined_detail = "; ".join(d for d, _ in findings)
                combined_strength = max(s for _, s in findings)
                record_signal(sym, "technical", combined_detail, strength=combined_strength)
                total_signals += len(findings)
                total_tickers_with_signals += 1

    print(f"\n{total_signals} technical signal(s) across {total_tickers_with_signals} ticker(s) recorded.",
          file=sys.stderr)


if __name__ == "__main__":
    main()
