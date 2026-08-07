"""
compose_alerts.py

The final step of each intraday cycle. Reads everything recorded by
technicals_scan.py, news_scan.py, fundamentals_scan.py, and
short_interest_scan.py (via signals_store.py), and decides what's
actually worth pushing to your phone:

  1. Only tickers with signals from >= MIN_SIGNAL_CATEGORIES DISTINCT
     categories qualify (per your preference: require 2+ signals to agree
     before it counts as a real opportunity, not noise).
  2. Qualifying tickers are ranked by a confidence score: category count
     first (agreement across more independent signal types matters most),
     then combined signal strength as a tiebreaker.
  3. Already-recently-alerted tickers are skipped (alert_log.py) so the
     same names don't repeat every 30 minutes.
  4. For the top TOP_N_ALERTS, fetches a live price and Finnhub's analyst
     consensus price target -- giving each alert an actual "why" and a
     defensible target, rather than a bare list of tickers.
  5. Sends ONE push with the top-ranked picks (push length is limited, so
     everything qualifying -- not just the top N -- gets written to
     latest_alerts.md in the repo for full reference).

Run this as the last step of the intraday workflow, after technicals_scan
and news_scan. Fundamentals/short-interest signals recorded earlier that
day remain active per their validity window and get pulled in here too.
"""

import json
import sys
import urllib.request

import yfinance as yf

from config import (
    FINNHUB_API_KEY,
    MIN_SIGNAL_CATEGORIES,
    TOP_N_ALERTS,
    LATEST_ALERTS_FILE,
)
from signals_store import get_active_signals
from alert_log import was_recently_alerted, mark_alerted
from notify import send_alert

CATEGORY_LABELS = {
    "technical": "Technical",
    "news": "News",
    "fundamentals": "Fundamentals",
    "short_interest": "Short Interest",
}


def score_ticker(categories: dict) -> tuple:
    """Returns (category_count, total_strength) -- used as a sort key."""
    count = len(categories)
    total_strength = sum(info.get("strength", 0.5) for info in categories.values())
    return (count, total_strength)


def fetch_price_target(symbol: str):
    if not FINNHUB_API_KEY:
        return None
    url = f"https://finnhub.io/api/v1/stock/price-target?symbol={symbol}&token={FINNHUB_API_KEY}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "personal-stock-scanner"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("targetMean")
    except Exception:
        return None


def fetch_current_prices(symbols: list[str]) -> dict:
    """Live-ish prices for just the shortlist -- cheap since it's a small batch."""
    if not symbols:
        return {}
    try:
        data = yf.download(
            tickers=" ".join(symbols),
            period="1d",
            interval="1d",
            group_by="ticker",
            threads=True,
            progress=False,
        )
    except Exception as e:
        print(f"[price fetch error] {e}", file=sys.stderr)
        return {}

    prices = {}
    for sym in symbols:
        try:
            df = data if len(symbols) == 1 else data[sym]
            prices[sym] = float(df["Close"].dropna().iloc[-1])
        except Exception:
            continue
    return prices


def format_ticker_line(symbol: str, categories: dict, price, target) -> str:
    reason_bits = []
    for cat, info in categories.items():
        label = CATEGORY_LABELS.get(cat, cat)
        reason_bits.append(f"{label}: {info['detail']}")
    reasons_text = " | ".join(reason_bits)

    price_bit = ""
    if price and target:
        upside = ((target - price) / price) * 100
        direction = "upside" if upside >= 0 else "downside"
        price_bit = f" | ${price:.2f} -> target ${target:.2f} ({upside:+.1f}% {direction})"
    elif price:
        price_bit = f" | ${price:.2f}"

    return f"{symbol} ({len(categories)} signals){price_bit}\n  {reasons_text}"


def main():
    active = get_active_signals()

    # Require confluence
    qualifying = {
        sym: cats for sym, cats in active.items()
        if len(cats) >= MIN_SIGNAL_CATEGORIES
    }
    print(f"{len(active)} ticker(s) have active signals; "
          f"{len(qualifying)} qualify with {MIN_SIGNAL_CATEGORIES}+ categories.", file=sys.stderr)

    # Rank by confidence
    ranked = sorted(qualifying.items(), key=lambda kv: score_ticker(kv[1]), reverse=True)

    # Write the FULL ranked list to the repo regardless of push cap
    with open(LATEST_ALERTS_FILE, "w") as f:
        f.write(f"# Latest Alerts ({len(ranked)} qualifying tickers)\n\n")
        for rank, (sym, cats) in enumerate(ranked, start=1):
            count, strength = score_ticker(cats)
            f.write(f"## {rank}. {sym} -- {count} signals, strength {strength:.2f}\n")
            for cat, info in cats.items():
                f.write(f"- **{CATEGORY_LABELS.get(cat, cat)}**: {info['detail']}\n")
            f.write("\n")

    # Filter out recently-alerted, then cap to top N for the actual push
    fresh_ranked = [(sym, cats) for sym, cats in ranked if not was_recently_alerted(sym)]
    push_list = fresh_ranked[:TOP_N_ALERTS]

    if not push_list:
        print("Nothing new to push (either no qualifying tickers, or all "
              "recently alerted already).", file=sys.stderr)
        return

    symbols_to_price = [sym for sym, _ in push_list]
    prices = fetch_current_prices(symbols_to_price)

    lines = []
    for sym, cats in push_list:
        price = prices.get(sym)
        target = fetch_price_target(sym)
        lines.append(format_ticker_line(sym, cats, price, target))

    message = "\n\n".join(lines)
    if len(message) > 3800:
        message = message[:3800] + "\n...(see latest_alerts.md in the repo for the rest)"

    title = f"{len(push_list)} high-confidence pick(s)"
    if len(fresh_ranked) > len(push_list):
        title += f" (+{len(fresh_ranked) - len(push_list)} more in repo)"

    send_alert(title, message, priority="high", tags=["chart_with_upwards_trend"])
    mark_alerted(symbols_to_price)

    print(f"\nPushed {len(push_list)} ticker(s). "
          f"Full ranked list ({len(ranked)} total) written to {LATEST_ALERTS_FILE}.", file=sys.stderr)


if __name__ == "__main__":
    main()
