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

BREAKOUT-QUALITY CHECKS (added to address the risk of buying purely
because a stock hit a new high, with nothing else confirming it):
  - Volume-confirmed breakout: new 52-week high on above-average volume
  - Relative strength line at a new high: the stock's performance vs SPY
    is ALSO at a new high, not just its raw price -- confirms genuine
    outperformance rather than just riding a broad market rally
  - New all-time high vs. new 52-week-high-but-still-below-ATH: these are
    different risk profiles. A true all-time high has no "trapped" sellers
    waiting to exit above the price; a 52-week high that's still below the
    all-time high can face overhead resistance from people selling once
    they're back to breakeven.
  - 50-day MA extension (CAUTION flag, not a bullish signal): price too
    far above its 50-day MA is historically more prone to a sharp
    pullback. Recorded in a separate "caution" category that does NOT
    count toward the 2+ signal confluence requirement, but still shows up
    as an explicit warning on the alert.
  - Market regime check (CAUTION flag): if SPY itself is below its own
    200-day MA, breakouts are statistically less reliable -- flagged as
    caution rather than suppressed, so you still see the opportunity but
    with the added context.

Signals are RECORDED via signals_store.py, not pushed directly --
compose_alerts.py decides what's push-worthy by requiring agreement
across multiple signal categories (caution-category signals are excluded
from that count -- they're context, not confirmation).

NOTE: needs yfinance and outbound network access. Test in your actual
deployment, not in a network-restricted sandbox.
"""

import csv
import sys
import time

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
    FIFTY_TWO_WEEK_HIGH_TOLERANCE,
    BREAKOUT_VOLUME_MULTIPLIER,
    MAX_MA50_EXTENSION_PCT,
    RS_NEW_HIGH_LOOKBACK_DAYS,
)
from signals_store import record_signal

BATCH_SIZE = 75
BATCH_PAUSE_SECONDS = 4
SPY_LOOKBACK_DAYS = 20  # for the existing 20-day relative-strength-vs-SPY check
ATH_BATCH_SIZE = 50     # for the targeted all-time-high follow-up pass


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
    ema12 = closes.ewm(span=12, adjust=False).mean()
    ema26 = closes.ewm(span=26, adjust=False).mean()
    macd_line = ema12 - ema26
    signal_line = macd_line.ewm(span=9, adjust=False).mean()
    return macd_line, signal_line


def fetch_spy_data():
    """
    Fetched ONCE per cycle, not per ticker. Returns a dict with the 20-day
    return (existing check), the daily close series (for RS-new-high
    comparisons), and whether SPY itself is in a healthy regime (above its
    own 200-day MA).
    """
    try:
        df = yf.download("SPY", period="1y", interval="1d", progress=False)
        closes = df["Close"].dropna()
        if len(closes) < SPY_LOOKBACK_DAYS + 1:
            return {"return_20d": None, "closes": closes, "bullish_regime": None}

        return_20d = float((closes.iloc[-1] / closes.iloc[-1 - SPY_LOOKBACK_DAYS] - 1) * 100)

        bullish_regime = None
        if len(closes) >= 200:
            ma200 = closes.rolling(200).mean()
            bullish_regime = bool(closes.iloc[-1] > ma200.iloc[-1])

        return {"return_20d": return_20d, "closes": closes, "bullish_regime": bullish_regime}
    except Exception as e:
        print(f"[SPY fetch error] {e}", file=sys.stderr)
        return {"return_20d": None, "closes": None, "bullish_regime": None}


def evaluate_symbol(df: pd.DataFrame, spy_data: dict):
    """
    Returns (findings, caution, hit_52wk_high, current_price) where
    findings/caution are lists of (detail, strength) tuples.
    """
    findings = []
    caution = []
    df = df.dropna()

    closes = df["Close"]
    volumes = df["Volume"]

    if len(closes) < MA_LONG + 1:
        return findings, caution, False, None

    current_price = float(closes.iloc[-1])

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

    # Relative volume (today vs 20-day average) -- reused below for breakout confirmation
    avg_volume = volumes.iloc[:-1].tail(20).mean()
    today_volume = volumes.iloc[-1]
    rel_volume_ratio = (today_volume / avg_volume) if avg_volume > 0 else 0

    if rel_volume_ratio >= RELATIVE_VOLUME_TRIGGER:
        findings.append((f"Volume spike ({rel_volume_ratio:.1f}x average)",
                         min(rel_volume_ratio / 5, 1.0)))

    # MACD bullish crossover
    macd_line, signal_line = compute_macd(closes)
    if len(macd_line.dropna()) >= 2:
        prev_macd, prev_signal = macd_line.iloc[-2], signal_line.iloc[-2]
        cur_macd, cur_signal = macd_line.iloc[-1], signal_line.iloc[-1]
        if prev_macd <= prev_signal and cur_macd > cur_signal:
            findings.append(("MACD bullish crossover", 0.7))

    # 50/200-day MA alignment (price above both, both trending up)
    ma50 = closes.rolling(50).mean()
    if len(closes) >= 200:
        ma200 = closes.rolling(200).mean()
        if (
            current_price > ma50.iloc[-1] > ma200.iloc[-1]
            and ma50.iloc[-1] > ma50.iloc[-6]
            and ma200.iloc[-1] > ma200.iloc[-21]
        ):
            findings.append(("Price above rising 50/200-day MAs", 0.6))

    # Relative strength vs SPY (20-day return comparison)
    spy_return = spy_data.get("return_20d")
    if spy_return is not None and len(closes) >= SPY_LOOKBACK_DAYS + 1:
        ticker_return = float((closes.iloc[-1] / closes.iloc[-1 - SPY_LOOKBACK_DAYS] - 1) * 100)
        if ticker_return > spy_return:
            outperformance = ticker_return - spy_return
            findings.append((f"Outperforming S&P 500 by {outperformance:.1f}pts (20d)",
                            min(outperformance / 15, 1.0)))

    # --- 52-week high / breakout quality checks ---
    fifty_two_wk_high = float(closes.tail(252).max())
    hit_52wk_high = current_price >= fifty_two_wk_high * FIFTY_TWO_WEEK_HIGH_TOLERANCE

    if hit_52wk_high:
        # 1. Volume-confirmed breakout
        if rel_volume_ratio >= BREAKOUT_VOLUME_MULTIPLIER:
            findings.append((f"52-week high confirmed by volume ({rel_volume_ratio:.1f}x average)", 0.75))
        else:
            caution.append((f"New 52-week high but on light volume ({rel_volume_ratio:.1f}x average) "
                            f"-- unconfirmed breakout", 0.3))

        # 3. Relative strength line at a new high (not just raw price)
        spy_closes = spy_data.get("closes")
        if spy_closes is not None:
            aligned_spy = spy_closes.reindex(closes.index).ffill().bfill()
            rs_ratio = closes / aligned_spy
            rs_recent = rs_ratio.dropna().tail(RS_NEW_HIGH_LOOKBACK_DAYS)
            if len(rs_recent) >= RS_NEW_HIGH_LOOKBACK_DAYS // 2:
                if rs_recent.iloc[-1] >= rs_recent.max() - 1e-9:
                    findings.append((
                        f"Relative strength line also at a {RS_NEW_HIGH_LOOKBACK_DAYS}-day high "
                        f"(genuine outperformance, not just riding the market)", 0.65))

    # 2. Extension above 50-day MA -- CAUTION, not a bullish signal
    if len(ma50.dropna()) > 0 and ma50.iloc[-1] > 0:
        extension_pct = ((current_price - ma50.iloc[-1]) / ma50.iloc[-1]) * 100
        if extension_pct >= MAX_MA50_EXTENSION_PCT:
            caution.append((f"Extended {extension_pct:.0f}% above 50-day MA "
                            f"-- elevated pullback risk", 0.5))

    # 4. Market regime -- CAUTION, not suppression
    if spy_data.get("bullish_regime") is False:
        caution.append(("Broader market (S&P 500) below its 200-day MA -- "
                        "breakouts less reliable in this regime", 0.4))

    return findings, caution, hit_52wk_high, current_price


def check_all_time_high(symbol: str, current_price: float):
    """
    5. Distinguishes a true all-time high (no overhead resistance from
    trapped sellers) from a 52-week high that's still below the all-time
    high (potential resistance from people selling once back to breakeven).
    Only called for tickers that already hit a 52-week high this cycle --
    keeps this targeted fetch cheap rather than pulling max-history for
    the whole universe.
    """
    try:
        df = yf.download(symbol, period="max", interval="1d", progress=False)
        closes = df["Close"].dropna()
        if closes.empty:
            return None
        all_time_high = float(closes.max())
    except Exception:
        return None

    if current_price >= all_time_high * FIFTY_TWO_WEEK_HIGH_TOLERANCE:
        return ("New ALL-TIME high -- no overhead resistance from prior sellers", 0.7)
    else:
        pct_below = ((all_time_high - current_price) / all_time_high) * 100
        return (f"52-week high, but still {pct_below:.1f}% below all-time high "
                f"(${all_time_high:.2f}) -- possible overhead resistance", 0.3)


def main():
    symbols = load_eligible()
    print(f"Running technical scan on {len(symbols)} eligible tickers...", file=sys.stderr)

    spy_data = fetch_spy_data()
    if spy_data.get("return_20d") is not None:
        print(f"  SPY {SPY_LOOKBACK_DAYS}-day return: {spy_data['return_20d']:.2f}%", file=sys.stderr)
    regime = spy_data.get("bullish_regime")
    print(f"  Market regime: {'bullish' if regime else 'BEARISH/caution' if regime is False else 'unknown'}",
          file=sys.stderr)

    all_findings = {}   # symbol -> list of (detail, strength)
    all_caution = {}    # symbol -> list of (detail, strength)
    ath_candidates = {} # symbol -> current_price, for the targeted follow-up pass

    total_batches = (len(symbols) + BATCH_SIZE - 1) // BATCH_SIZE

    for i, batch in enumerate(chunk(symbols, BATCH_SIZE), start=1):
        if i % 5 == 0 or i == total_batches:
            print(f"  Batch {i}/{total_batches}...", file=sys.stderr)
        try:
            data = yf.download(
                tickers=" ".join(batch),
                period="1y",
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
                findings, caution, hit_52wk_high, price = evaluate_symbol(df, spy_data)
            except Exception:
                continue

            if findings:
                all_findings[sym] = findings
            if caution:
                all_caution[sym] = caution
            if hit_52wk_high and price:
                ath_candidates[sym] = price

        time.sleep(BATCH_PAUSE_SECONDS)

    # Targeted all-time-high follow-up -- only for tickers that hit a
    # 52-week high this cycle, keeping this cheap rather than pulling
    # max-history for the whole universe.
    if ath_candidates:
        print(f"\nChecking all-time-high status for {len(ath_candidates)} "
              f"52-week-high candidate(s)...", file=sys.stderr)
        for sym, price in ath_candidates.items():
            result = check_all_time_high(sym, price)
            if result:
                all_findings.setdefault(sym, []).append(result)
            time.sleep(1)  # light pacing for this smaller, separate batch of calls

    # Record everything -- ONE combined signal per category per symbol
    total_signals = 0
    for sym, findings in all_findings.items():
        combined_detail = "; ".join(d for d, _ in findings)
        combined_strength = max(s for _, s in findings)
        record_signal(sym, "technical", combined_detail, strength=combined_strength)
        total_signals += len(findings)

    total_caution = 0
    for sym, cautions in all_caution.items():
        combined_detail = "; ".join(d for d, _ in cautions)
        combined_strength = max(s for _, s in cautions)
        record_signal(sym, "caution", combined_detail, strength=combined_strength)
        total_caution += len(cautions)

    print(f"\n{total_signals} technical signal(s) across {len(all_findings)} ticker(s), "
          f"{total_caution} caution flag(s) across {len(all_caution)} ticker(s) recorded.",
          file=sys.stderr)


if __name__ == "__main__":
    main()
