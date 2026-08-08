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

# --- 52-week high / breakout quality checks ---
FIFTY_TWO_WEEK_HIGH_TOLERANCE = 0.999   # within 0.1% of the trailing high counts as "at" it
BREAKOUT_VOLUME_MULTIPLIER = 1.5        # lower bar than RELATIVE_VOLUME_TRIGGER --
                                         # a breakout only needs moderately elevated
                                         # volume to be "confirmed", not an extreme spike
MAX_MA50_EXTENSION_PCT = 25.0           # price this far above its 50-day MA = caution,
                                         # historically more prone to a sharp pullback
RS_NEW_HIGH_LOOKBACK_DAYS = 60          # window for checking if the stock's performance
                                         # relative to SPY is ALSO making a new high
                                         # (confirms genuine outperformance, not just
                                         # riding a broad market rally)

# --- Fundamentals trigger thresholds ---
EARNINGS_SURPRISE_PCT = 5.0       # actual EPS beat estimate by this % or more
EARNINGS_RECENCY_DAYS = 5         # only count an earnings beat if reported this recently
REVENUE_GROWTH_YOY_PCT = 10.0     # YoY revenue growth at or above this
EPS_GROWTH_YOY_PCT = 10.0         # YoY EPS growth at or above this

# --- Fundamental quality checklist (all from the same Finnhub 'metric'
# call already made for revenue/EPS growth -- zero extra API cost) ---
MAX_DEBT_TO_EQUITY = 1.0          # below this = low leverage
MIN_CURRENT_RATIO = 1.5           # above this = can cover short-term liabilities
MIN_ROE_PCT = 15.0                # above this = efficient use of capital
MIN_NET_MARGIN_PCT = 10.0         # simple stand-in for "healthy margins"
                                   # (true peer-relative margin comparison would need
                                   # industry-average data we don't have a free source for)
MIN_QUALITY_CHECKS_PASSED = 3     # out of 4 (D/E, current ratio, ROE, margin) --
                                   # require most, not all, to be lenient on edge cases

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
MIN_QUALIFYING_STRENGTH = 1.0   # ALSO require combined strength across those
                                 # categories to hit this floor -- without this,
                                 # two weak/borderline signals (e.g. RSI oversold +
                                 # a bare-minimum revenue growth reading) would
                                 # qualify exactly as easily as two strong ones
TOP_N_ALERTS = 20           # cap on a single push, ranked by confidence

# --- Conviction tiers (shown on every alert, so weak-but-qualifying and
# genuinely strong matches don't look identical at a glance) ---
STRONG_TIER_MIN_CATEGORIES = 3       # 3+ independent categories = automatically Strong
STRONG_TIER_STRENGTH_FOR_TWO = 1.5   # OR just 2 categories, but with combined
                                      # strength this high -- lets a genuinely
                                      # powerful 2-signal match still rank as
                                      # Strong rather than being capped by category
                                      # count alone

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
ALERT_LOG_FILE = "alert_log.json"              # composite-level "seen before" tracking
LATEST_ALERTS_FILE = "latest_alerts.md"        # human-readable full ranked list

# Auto-populated by the workflow (github.server_url + github.repository --
# no secret needed, GitHub provides this automatically) so the push
# notification can link straight to the full list in the repo.
REPO_URL = os.environ.get("REPO_URL", "")
TICKER_SECTORS_FILE = "sectors.json"           # {symbol: industry}
SECTOR_ALERTS_FILE = "sector_alerts.json"      # active sector-level news annotations

# --- Sector-level news (annotation only -- does NOT count toward the
# MIN_SIGNAL_CATEGORIES confluence requirement, per your preference to
# keep the confidence system as-is). A broad macro/sector story gets
# attached as context to any push where the ticker's industry matches,
# without inflating that ticker's actual signal count. Keyword list is
# intentionally modest and easy to extend -- these are rough matches
# against Finnhub's finnhubIndustry field, not precise classification. ---
SECTOR_ALERT_VALIDITY_HOURS = 8
SECTOR_KEYWORDS = {
    "tariff": ["Steel", "Auto", "Semiconductor", "Metals", "Aerospace", "Machinery"],
    "interest rate": ["Bank", "Real Estate", "Insurance", "Financial", "REIT"],
    "federal reserve": ["Bank", "Real Estate", "Insurance", "Financial", "REIT"],
    "rate cut": ["Bank", "Real Estate", "Insurance", "Financial", "REIT"],
    "rate hike": ["Bank", "Real Estate", "Insurance", "Financial", "REIT"],
    "oil price": ["Oil & Gas", "Energy"],
    "opec": ["Oil & Gas", "Energy"],
    "chip export": ["Semiconductor", "Technology", "Electronic"],
    "semiconductor export": ["Semiconductor", "Technology", "Electronic"],
    "fda approval": ["Biotechnology", "Pharmaceutical", "Health"],
    "drug pricing": ["Biotechnology", "Pharmaceutical", "Health"],
    "airline": ["Airlines"],
    "jet fuel": ["Airlines"],
    "housing market": ["Real Estate", "REIT", "Construction", "Homebuilding"],
    "retail sales": ["Retail", "Consumer"],
}

# --- Secrets (set these as GitHub Actions repo secrets, never hardcode) ---
FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY", "")
NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "")
