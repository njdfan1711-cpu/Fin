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

# Earnings-quality caution -- Finnhub's growth metrics (EPS/revenue YoY)
# are documented as non-GAAP: adjusted to exclude one-time/unusual items.
# That means a stock can show solid "EPS growth" from the same quarter it
# posted a GAAP net loss from a large one-time charge (impairment,
# write-down, restructuring) -- the adjusted number and the headline
# number are answering different questions. netProfitMarginTTM/Annual is
# GAAP-based, so a deeply negative margin here is a genuine red flag that
# the adjusted-EPS growth signal alone won't catch.
NET_MARGIN_CAUTION_PCT = -5.0      # below this = flag regardless of what the
                                    # adjusted EPS/revenue growth figures say
                                   # (true peer-relative margin comparison would need
                                   # industry-average data we don't have a free source for)
MIN_QUALITY_CHECKS_PASSED = 3     # out of 4 (D/E, current ratio, ROE, margin) --
                                   # require most, not all, to be lenient on edge cases

# --- Fundamentals metrics caching (Actions-minutes optimization) ---
# The /stock/metric call (revenue/EPS growth, quality checklist, float
# proxy) has no bulk equivalent on Finnhub's free tier, so it's still one
# call per eligible ticker -- but revenue/EPS growth and balance-sheet
# ratios only change when a company reports, not daily. Rather than
# re-pull every ticker every single day, each ticker's metrics are cached
# for METRICS_REFRESH_DAYS and only re-fetched once stale. This spreads
# ~2,400 calls/day down to roughly (universe size / METRICS_REFRESH_DAYS)
# calls/day on average once the cache is warm -- the first run after
# adding this still costs the full per-ticker pass, since everything
# starts stale.
METRICS_CACHE_FILE = "metrics_cache.json"     # {symbol: {checked_at, findings, share_outstanding}}
METRICS_REFRESH_DAYS = 5                       # roughly matches earnings-cycle cadence;
                                                # lower = fresher data but more daily API cost

# --- Short interest ---
SHORT_INTEREST_SPIKE_PCT = 20.0   # % increase in short interest since last report

# --- Signal validity windows (how long a detected signal "counts" toward
# confluence before it's considered stale) ---
SIGNAL_VALIDITY_HOURS = {
    "technical": 4,       # RSI/MA/volume -- intraday, goes stale fast
    "news": 8,             # catalyst relevance fades but not instantly
    "fundamentals": EARNINGS_RECENCY_DAYS * 24,
    "earnings_quality": EARNINGS_RECENCY_DAYS * 24,  # same cadence as
                                                      # fundamentals -- tied
                                                      # to the same quarterly
                                                      # metrics, same cache
    "short_interest": 15 * 24,  # roughly matches FINRA's biweekly cadence
    "momentum": 4,         # low-float volume-spike setups go cold fast, same window as technical
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

# --- ntfy message size (https://docs.ntfy.sh/publish/#limitations) --
# messages over this many BYTES (not Python string length -- see the note
# at truncate_to_whole_entries in compose_alerts.py) get silently
# converted to a downloadable .txt attachment instead of shown inline, no
# error raised. Discovered the hard way: emoji (STRONG tier tags, caution
# warnings) are 3-4 bytes each in UTF-8 but 1-2 Python characters, so a
# budget measured in characters quietly under-counts the real size.
NTFY_MESSAGE_BYTE_LIMIT = 4096
# Stay comfortably under the hard limit -- ntfy's own server docs say
# ">4K NOT RECOMMENDED, and largely untested" even for exactly 4096.
NTFY_SAFE_BODY_BYTE_BUDGET = 3600

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

# --- Momentum / speculative low-float scan -- a SEPARATE track from the
# main confluence system, deliberately NOT blended into
# MIN_SIGNAL_CATEGORIES/STRONG-tier scoring. This targets the opposite
# philosophy from the rest of the screener on purpose: instead of
# quality + multi-signal agreement, it looks for low-float stocks
# showing an unusually large, price-confirmed volume spike -- the classic
# setup behind fast, violent moves (and the mechanism paid "AI signal"
# services like the Reddit-discussed "Oracle" platform are almost
# certainly just repackaging). Kept in its own reserved section of the
# push so it can never displace your main quality-backed picks.
#
# NOTE: Finnhub's free-tier 'shareOutstanding' field is used as a proxy
# for float. True float (shares outstanding MINUS insider/locked-up
# holdings) isn't available without a paid data source, so this will
# occasionally be looser than a real float screener -- e.g. a company
# with a large insider stake but low shares outstanding could slip in.
# Documented tradeoff, not a bug; tighten MAX_SHARES_OUTSTANDING_MOMENTUM
# further if that turns out to matter in practice.
MAX_SHARES_OUTSTANDING_MOMENTUM = 15_000_000   # tight: genuinely low float/share count
MOMENTUM_RELATIVE_VOLUME_TRIGGER = 5.0         # well above the main 2.5x technical trigger
MOMENTUM_MIN_DAY_CHANGE_PCT = 8.0              # requires real price follow-through,
                                                # not just volume noise with no direction
MOMENTUM_MAX_PICKS_IN_PUSH = 3                 # hard cap on push entries, regardless of
                                                # remaining character budget -- keeps this
                                                # section small and skimmable by design
MOMENTUM_PUSH_CHAR_BUDGET = 900                # reserved slice of the momentum push's own
                                                # NTFY_SAFE_BODY_BYTE_BUDGET -- now measured
                                                # in bytes despite the name (kept for backwards
                                                # compat with anything reading this constant)
FLOAT_DATA_FILE = "float_data.json"            # {symbol: shares_outstanding}, refreshed daily

# --- Files ---
UNIVERSE_FILE = "universe.csv"
ELIGIBLE_FILE = "eligible.csv"
DELISTING_RISK_FILE = "delisting_risk.json"
FUNDAMENTALS_SIGNALS_FILE = "fundamentals_signals.json"
SIGNALS_STATE_FILE = "signals_state.json"      # rolling raw signals, all categories
ALERT_LOG_FILE = "alert_log.json"              # composite-level "seen before" tracking
LATEST_ALERTS_FILE = "latest_alerts.md"        # human-readable full ranked list
DAILY_PUSHES_FILE = "daily_pushes.json"        # running log of actual pushes, per ET trading day
DAILY_PUSHES_RETENTION_DAYS = 10               # how many days of history to keep

# --- Trade plan (entry/stop/target) -- ATR-based volatility-scaled levels,
# computed live for just the small already-shortlisted push candidates.
# No new daily state file (avoids the merge-conflict class of bug that
# signals_state.json had) -- this is purely a display layer on top of
# the existing price fetch.
ATR_PERIOD = 14                       # standard ATR lookback, in daily bars
ENTRY_BAND_ATR_MULT = 0.25            # entry zone = price +/- this * ATR
STOP_ATR_MULT = 1.5                   # main-list stop distance, in ATRs
MOMENTUM_STOP_ATR_MULT = 1.0          # tighter stop for the momentum track --
                                       # low-float/volume-spike setups move
                                       # fast, a 1.5x-ATR stop is too loose
REWARD_RISK_RATIO = 2.0               # target = entry + this * (entry - stop)
DEFAULT_POSITION_SIZE_USD = 3000      # used to size the suggested share count

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
