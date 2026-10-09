# Scalp Trader — Ideas Backlog

Candidate rules and improvements. **Nothing on this list is implemented.**
Items move to the changelog only after they've been tested against the
baseline and kept.

## Guiding principle: don't over-filter

Every extra rule removes trades, including some good ones. The goal is a
bot that still finds truly good opportunities, so:

1. **Add one idea at a time** and compare against the baseline on the same
   data (same approach as the fixed vs. trailing-stop comparison).
2. **Tag, don't just filter.** (IMPLEMENTED 2026-10: `scalp_signals_tagged.csv` +
   `analyze_tags.py` -> `scalp_tag_analysis.md`.) Have the backtest record every signal with
   labels (minutes since open, SPY trend, how extended the price was,
   etc.) and keep the filtered-out trades too. Then each idea can be judged
   by what the *removed* trades would have earned. A good rule removes
   mostly losers; a bad rule removes winners along with them.
3. **Watch the trade count.** A rule that improves average profit per trade
   but cuts trades sharply may reduce total profit.
4. **Be wary of small samples.** With only dozens of trades, rules can look
   good by luck (overfitting). Prefer simple rules with a clear market
   logic, and confirm on fresh data before trusting them.

## Entry filter ideas

| # | Idea | Why it might help | Risk / what to watch |
|---|------|-------------------|----------------------|
| 1 | **Skip the first 15 and last 15 minutes** of the session (9:30-9:45, 3:45-4:00 ET) | Open and close are erratic: wide spreads, sudden swings, unpredictable moves | Some of the best moves happen at the open; the spread logger will show how much wider spreads really are then |
| 2 | **Avoid entries while SPY is down** (e.g. SPY below its day open/VWAP, or falling over the last N minutes) | Limits losses when the broad market is bearish, since most stocks follow it | "Down" needs a precise definition; too strict and it blocks good trades in stocks moving independently |
| 3 | **Skip entries that are already too extended** (price already up more than X% over the last N minutes, or far above VWAP) | Avoids buying the top of a move that has mostly played out | Threshold needs testing; too tight kills real breakouts |

## Other filter ideas (lower priority)

| # | Idea | Notes |
|---|------|-------|
| 4 | Trend filter (price above a short moving average) | Avoids catching bounces in falling stocks |
| 5 | Candle shape (signal candle closes near its high) | Shows buyers held control into the close of the minute |
| 6 | Overbought check (RSI or similar) | Overlaps with idea 3; test whether both are needed |
| 7 | Measured-spread filter | Drop stocks whose real median spread (from spread_logger.py) is above roughly 1-2 cents |
| 8 | Remove or downweight low-priced tickers | First backtest: NIO alone lost about $205; the daily watchlist already excludes sub-$20 names |
| 9 | Real-time news trigger | Needs a much faster feed than the swing screener's 30-minute news scan |

## Exit and sizing ideas

| # | Idea | Notes |
|---|------|-------|
| 10 | Tune trailing-stop parameters | Currently arms at +0.175% and trails 0.15%; try about 0.25% if normal 1-minute noise stops it out early |
| 11 | Per-symbol cooldown after a missed entry or a stop-out | Starting guess: 5-10 min after a miss, about 30 min after a stop-out |
| 12 | Multiple simultaneous positions | Only after consistent one-at-a-time results and account growth |

## Operations

| # | Idea | Notes |
|---|------|-------|
| 13 | Point `guardrails.py` ALLOWED_SYMBOLS at the daily watchlist | Required before the live bot can trade anything beyond the original 30 names |
| 14 | Extend `spread_logger.py` to the full watchlist | After the first clean trading-day run on the 30-name list |
| 15 | Reconsider MAX_TRADES_PER_DAY (currently 40) | Revisit once real signal frequency is known |
