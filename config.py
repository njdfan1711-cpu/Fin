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
EARNINGS_PROXIMITY_DAYS = 5        # flag a caution if the NEXT scheduled report is within
                                    # this many days -- an ATR-based stop offers zero
                                    # protection against an overnight earnings gap, and a
                                    # multi-day swing hold can easily run right into one
EARNINGS_REACTION_DAYS = 3         # flag a caution when the company reported earnings within
                                    # this many calendar days (0 = reported today). A pick that
                                    # qualifies INSIDE the reaction window is often the earnings
                                    # gap-up itself, and post-earnings pops frequently fade over
                                    # the next sessions (2026-11 LIFE: +12% after hours, new
                                    # all-time high next day, then back below the pre-earnings
                                    # close within 48h). Flag only -- never excludes or re-ranks.
                                    # Must be <= EARNINGS_RECENCY_DAYS (that sets how far back
                                    # the earnings calendar is pulled).
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

# --- Analyst recommendation trend (Finnhub /stock/recommendation) ---
# Approximates the idea behind Zacks Rank (analysts getting more/less
# bullish lately) without needing a proprietary score: compares the two
# most recent monthly buy/hold/sell/strongBuy/strongSell periods for a
# meaningful swing in either direction. NOT the same call as /stock/metric
# above -- a genuinely separate API hit per ticker, so it shares the same
# cache/refresh cadence rather than adding an uncoordinated second budget.
# FINNHUB_KEY_CHECK -- unconfirmed whether this endpoint is free-tier or
# requires a paid plan; documentation on this was ambiguous. Built
# defensively (same fetch-failure handling as everything else here) so if
# it turns out to be premium-gated, it just fails quietly and this signal
# never fires rather than breaking the rest of the fundamentals scan.
RECOMMENDATION_TREND_MIN_ANALYSTS = 3   # ignore thinly-covered names -- a single
                                         # analyst flipping shouldn't swing this
RECOMMENDATION_TREND_MIN_SCORE_DELTA = 2   # minimum weighted-score swing (see
                                            # analyze_recommendation_trend) to
                                            # count as a meaningful improve/
                                            # deteriorate, not just noise
THIN_COVERAGE_MAX_ANALYSTS = 4   # 4 or fewer total ratings = flag as thin --
                                  # less price discovery/scrutiny than a
                                  # widely-covered name, real risk factor
                                  # independent of any trend direction

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
    "news_caution": 8,     # same cadence as "news" -- same underlying data source
    "news_neutral": 8,
    "fundamentals": EARNINGS_RECENCY_DAYS * 24,
    "earnings_reaction": EARNINGS_RECENCY_DAYS * 24,  # just-reported caution; cleared
                                                       # daily by fundamentals_scan once
                                                       # outside EARNINGS_REACTION_DAYS
    "earnings_quality": EARNINGS_RECENCY_DAYS * 24,  # same cadence as
                                                      # fundamentals -- tied
                                                      # to the same quarterly
                                                      # metrics, same cache
    "short_interest": 15 * 24,  # roughly matches FINRA's biweekly cadence
    "momentum": 4,         # low-float volume-spike setups go cold fast, same window as technical
    "caution": 4,          # technicals-derived cautions (extended above MA, light-volume high,
                           # weak market regime) are rewritten every technicals scan, so same
                           # window as "technical" -- previously fell through to the 24h default
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
# How far down the ranking latest_alerts.md gets live price/ATR, a trade plan, the
# chase caution and the recent-IPO flag. The top TOP_N_ALERTS are always fetched
# first, exactly as before; ranks TOP_N_ALERTS+1..PRICED_TOP_N are a best-effort
# second pass in small batches (a failed batch just leaves those entries without a
# plan -- it can never affect the top picks) and stops once the time budget below
# is spent. Set equal to TOP_N_ALERTS to turn the extra pass off.
PRICED_TOP_N = 60

# --- Extension-aware ranking and relative tiers (2026-11) -------------------------
# Backed by scorecard.py findings, NOT yet validated going forward: picks carrying
# "extension" flags did clearly worse than clean ones, and raw strength did not
# predict results. Both raw and adjusted scores are logged (see compose_alerts.py
# record_push / scorecard.py "Shadow score check") so this can be checked and undone.
# Extension flags: extended above 50-day MA, RSI overbought, just reported earnings,
# stale alert (Day >= STALE_ALERT_DAY) -- known for every ticker, so they affect the
# RANKING -- plus chase risk and "already up EXTENSION_RUNUP_PCT since first alert",
# which need a live price, so they affect only the TIER and the Extended filter.
EXTENSION_PENALTY = 0.5        # strength subtracted per flag when ranking (0 = off)
STALE_ALERT_DAY = 5            # "Day N" streak at/after which an alert counts as stale
EXTENSION_RUNUP_PCT = 5.0      # already up this much since the first alert = extended
# Tiers are relative, computed each run among CLEAN (flag-free) tickers only:
# Strong = top STRONG_TOP_PCT, Moderate = on to MODERATE_TOP_PCT (cumulative), rest
# Watch. Any flagged ticker is "Extended" whatever its score. Strong also needs the old
# absolute floor (conviction_tier) AND a live price check, so a missing check can never
# produce a Strong.
STRONG_TOP_PCT = 0.10
MODERATE_TOP_PCT = 0.40
PRICED_BATCH_SIZE = 30
PRICED_EXTRA_TIME_BUDGET_SECONDS = 120

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

# Show the "Day N" streak tag on a ticker once it has been pushed on this many
# consecutive trading days (counting today). Display only.
STREAK_TAG_MIN_DAYS = 3

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
LATEST_ALERTS_FILE = "latest_alerts.md"        # human-readable full ranked list -- always
                                                # the CURRENT/most-recent run; overwritten
                                                # each run, same as before
ALERTS_HISTORY_DIR = "alerts_history"          # one timestamped snapshot per run, ET,
                                                # e.g. alerts_history/latest_alerts_2026-08-19_0933.md
                                                # -- never overwritten, for trade-plan lookback
DAILY_PUSHES_FILE = "daily_pushes.json"        # running log of actual pushes, per ET trading day
DAILY_PUSHES_RETENTION_DAYS = 10               # how many days of history to keep

# --- Outcome tracking ---
# Revisits past pushes N days later and records what the price actually
# did -- did it hit the recorded target, the recorded stop, or neither --
# so the system's thresholds can eventually be validated/tuned against
# real results instead of guesses. Each push is evaluated EXACTLY ONCE
# (the first run where it's old enough), then marked resolved and never
# touched again -- keeps API usage bounded regardless of how long this
# runs for.
OUTCOME_LOOKBACK_DAYS = 7          # comfortably inside DAILY_PUSHES_RETENTION_DAYS
                                    # above, so a push can't get pruned before
                                    # it's old enough to be evaluated
OUTCOME_HISTORY_FILE = "outcome_history.json"

# --- Position monitor -------------------------------------------------
# Checks OPEN_POSITIONS_FILE (synced from the trade log) against the
# trade_plan Fin generated when each symbol was originally pushed --
# the feedback loop that was missing between "here's a stop/target" at
# signal time and what actually happens to a position afterward.
# Trade data lives in a SEPARATE PRIVATE repo (checked out into FIN_PRIVATE_DIR by the
# workflows) so it never appears in this public repo or its history. When FIN_PRIVATE_DIR
# is unset (local runs) everything behaves exactly as before: files in the repo root.
# While it IS set, scripts also stay quiet about trade details in their console output,
# because GitHub Actions logs of a public repo are publicly readable.
FIN_PRIVATE_DIR = os.environ.get("FIN_PRIVATE_DIR", "")
QUIET_TRADE_LOGS = bool(FIN_PRIVATE_DIR)
OPEN_POSITIONS_FILE = (os.path.join(FIN_PRIVATE_DIR, "open_positions.json")
                       if FIN_PRIVATE_DIR else "open_positions.json")
POSITION_MONITOR_STATE_FILE = "position_monitor_state.json"
# How many days back to search daily_pushes.json for the trade_plan that
# was active on/before a position's entry_date. 21 covers a full push
# retention cycle with room to spare (DAILY_PUSHES_RETENTION_DAYS below).
POSITION_PLAN_LOOKBACK_DAYS = 21
# If a position has been held this many multiples of the empirical
# median days-to-resolution (from outcome_history.json) without hitting
# either its stop or target, flag it as overdue -- the "this trade has
# outrun its own thesis" alert.
OVERDUE_HOLD_MULTIPLIER = 2.0
# Independent of the stop -- a position can be down a lot without ever
# touching its (often wider, ATR-based) stop. This is a faster "hey,
# pay attention" check: % loss from entry price, regardless of where
# the stop actually sits. Checked on the intraday cadence (see
# intraday.yml) specifically so a fast midday move surfaces same-day
# rather than waiting for the next morning's daily scan.
POSITION_DRAWDOWN_ALERT_PCT = 10.0

# --- Trade plan (entry/stop/target) -- ATR-based volatility-scaled levels,
# computed live for just the small already-shortlisted push candidates.
# No new daily state file (avoids the merge-conflict class of bug that
# signals_state.json had) -- this is purely a display layer on top of
# the existing price fetch.
ATR_PERIOD = 14                       # standard ATR lookback, in daily bars
LOW_ATR_PCT_CAUTION = 3.0             # ATR below this % of price rarely resolves to
                                       # target within the tracking window (0/171 in a
                                       # 515-sample backtest of daily_pushes.json vs.
                                       # outcome_history.json) -- flagged, not excluded,
                                       # since the sample is still thin (14 target hits
                                       # total across all ATR levels).
ENTRY_BAND_ATR_MULT = 0.25            # entry zone = price +/- this * ATR
STOP_ATR_MULT = 1.5                   # main-list stop distance, in ATRs
MOMENTUM_STOP_ATR_MULT = 1.0          # tighter stop for the momentum track --
                                       # low-float/volume-spike setups move
                                       # fast, a 1.5x-ATR stop is too loose
REWARD_RISK_RATIO = 2.0               # target = entry + this * (entry - stop)
DEFAULT_POSITION_SIZE_USD = 5000      # used to size the suggested share count

# Take-profit level (shown in the trade plan + watched by position_monitor).
# The full target (REWARD_RISK_RATIO x a 1.5-ATR stop = 3 ATR, ~12% for a
# typical pick) was hit by only ~5% of pushes inside the 7-day window
# (58 of 1,075 unique ticker-days in outcome_history.json, 2026-10-03).
# Real exits have clustered near +2% (~0.5 ATR at the median 3.8% ATR),
# so this is the "realistic" level. Lower-bound hit rate for 0.5 ATR from
# that same history is ~29% (stop_hit paths are unknown, so the true rate
# is higher). track_outcomes.py now records tp1_outcome so this multiple
# can be re-tuned against real paths instead of that lower bound.
TAKE_PROFIT_ATR_MULT = 0.5

# "Chase" caution -- flags a pick that has already run today or this week,
# since the entry zone is built off the CURRENT price and so moves up with
# the run. Volatility-scaled like everything else here. Display-only (no
# effect on ranking). Back-test on 526 consecutive-day push pairs was
# weak/inconclusive (stop rate ~35% for >=1 ATR run-ups vs ~35% flat), so
# this is logged per push (the "chase" field in daily_pushes/outcome
# history) and should be re-validated once there's more data.
# "Recent IPO" caution -- flags (never excludes) a pick whose first trade date
# is within RECENT_IPO_DAYS. Newly public names have a short price history, a
# valuation still being discovered, and a lock-up expiry (typically ~180 days
# after the IPO) when insiders/early holders can first sell. Seasoned large
# caps are far less exposed. Age comes from the first bar in yfinance's
# full-history download for the shortlist only (no API key, no state file).
# 365 is a starting point, not a tested threshold -- the scorecard tags
# (caut:recent_ipo) will show whether it separates outcomes.
RECENT_IPO_DAYS = 365
IPO_LOCKUP_DAYS = 180        # inside this window the caution also mentions the lock-up

CHASE_DAY_ATR_MULT = 1.0     # up >= this many ATRs vs prior close
CHASE_5D_ATR_MULT = 2.0      # or up >= this many ATRs vs ~5 bars ago

# position_monitor "review" checkpoint: fires when a position has been
# held longer than this multiple of the empirical median days-to-target
# (earlier and softer than OVERDUE_HOLD_MULTIPLIER, which stays the
# stronger second alert).
REVIEW_HOLD_MULTIPLIER = 1.0

# Auto-populated by the workflow (github.server_url + github.repository --
# no secret needed, GitHub provides this automatically) so the push
# notification can link straight to the full list in the repo.
REPO_URL = os.environ.get("REPO_URL", "")
# Optional: where latest_alerts.html is served (e.g. a GitHub Pages URL). When
# set, tapping an ntfy alert opens the styled page instead of the raw .md file.
ALERTS_PAGE_URL = os.environ.get("ALERTS_PAGE_URL", "")
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
