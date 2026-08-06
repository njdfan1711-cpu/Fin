"""
config.py - all tunable thresholds live here so the whole system can be
adjusted from one place after the few-weeks review.
"""

import os

# --- Liquidity / quality floor (applied daily to build eligible.csv) ---
MIN_PRICE = 3.00
MIN_AVG_VOLUME = 500_000          # 20-day average daily share volume

# --- Technical trigger thresholds ---
RSI_PERIOD = 14
RSI_OVERSOLD = 30                 # low-weight signal, per your preference
RSI_OVERBOUGHT = 70
MA_SHORT = 20
MA_LONG = 50
RELATIVE_VOLUME_TRIGGER = 2.5     # today's volume >= 2.5x the 20-day average
                                   # -- this is the "something is happening" signal

# --- Fundamentals trigger thresholds ---
EARNINGS_SURPRISE_PCT = 5.0       # actual EPS beat estimate by this % or more
REVENUE_GROWTH_YOY_PCT = 10.0     # YoY revenue growth at or above this

# --- Short interest ---
SHORT_INTEREST_SPIKE_PCT = 20.0   # % increase in short interest since last report
                                   # (potential squeeze signal)

# --- Alert de-duplication ---
# Don't re-alert the same ticker+reason more than once within this window
DEDUPE_HOURS = 12

# --- Files ---
UNIVERSE_FILE = "universe.csv"
ELIGIBLE_FILE = "eligible.csv"
DELISTING_RISK_FILE = "delisting_risk.json"
FUNDAMENTALS_SIGNALS_FILE = "fundamentals_signals.json"
ALERT_LOG_FILE = "alert_log.json"

# --- Secrets (set these as GitHub Actions repo secrets, never hardcode) ---
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY", "")
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "")
