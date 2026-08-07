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
EARNINGS_RECENCY_DAYS = 5         # only count an earnings beat if reported this recently
                                   # -- without this, a beat from months ago would
                                   # match forever, which is what caused the 329-ticker alert
REVENUE_GROWTH_YOY_PCT = 10.0     # YoY revenue growth at or above this

# --- Short interest ---
SHORT_INTEREST_SPIKE_PCT = 20.0   # % increase in short interest since last report

# --- Signal validity windows (how long a detected signal "counts" toward
# confluence before it's considered stale) ---
SIGNAL_VALIDITY_HOURS = {
    "technical": 4,       # RSI/MA/volume -- intraday, goes stale fast
    "news": 8,             # catalyst relevance fades but not instantly
    "fundamentals": EARNINGS_RECENCY_DAYS * 24,
    "short_interest": 15 * 24,  # roughly matches FINRA's biweekly cadence
}

# --- Composite alert rules ---
MIN_SIGNAL_CATEGORIES = 2   # require agreement across at least this many
                             # distinct categories before it's push-worthy
TOP_N_ALERTS = 20           # cap on a single push, ranked by confidence

# --- Alert de-duplication (applied at the composite level -- once a ticker
# has been pushed, don't push it again for this long even if it's still
# top-ranked, so the same names don't spam every 30 min) ---
DEDUPE_HOURS = 12

# --- Files ---
UNIVERSE_FILE = "universe.csv"
ELIGIBLE_FILE = "eligible.csv"
DELISTING_RISK_FILE = "delisting_risk.json"
FUNDAMENTALS_SIGNALS_FILE = "fundamentals_signals.json"
SIGNALS_STATE_FILE = "signals_state.json"      # rolling raw signals, all categories
ALERT_LOG_FILE = "alert_log.json"              # composite-level push dedupe
LATEST_ALERTS_FILE = "latest_alerts.md"        # human-readable full ranked list

# --- Secrets (set these as GitHub Actions repo secrets, never hardcode) ---
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY", "")
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "")
