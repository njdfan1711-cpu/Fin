## 2026-10-20 -- Day-boundary fixes, one-position account sim, ranking v1, random-entry baseline, new tags

Base file: scalp_backtest.py (main, 2026-10-19, sha256 d01a6dbba5ca...)
Files: scalping/scalp_backtest.py, scalping/gate_check.py, scalping/analyze_tags.py,
scalping/scalp_random_baseline.py (new), .github/workflows/scalp_backtest.yml
(new baseline step; new output files added to the commit list)

**Bugs fixed (scalp_backtest.py)**
- Momentum, the 20-bar volume average and range20 ran across the overnight gap. At
  9:30 the "3-minute momentum" was yesterday's close -> today's gap and the "volume
  spike" was the opening bar vs yesterday's quiet last minutes. All indicators are
  now computed within one trading day; no entry before MIN_MINUTES_AFTER_OPEN = 20.
- Positions could roll overnight (16 stored trades "exited" at the next day's 9:30 at
  the stop/target price, ignoring the gap). Open positions now close at the last bar
  of the day ("eod"); no entry on the last bar.
- Stored trades that break these rules are ignored (row_is_valid), not deleted;
  compliant trades are unchanged. 96 of 281 stored trades ignored, 185 valid.
- analyze_tags.py ignores tagged signals entered before minute 20 for the same reason.

**New: account simulation (scalp_backtest.py)**
- Replays valid stored trades under the LIVE rule: one open position, cost gate on,
  max 40 entries/day; same-minute ties go to the best-ranked signal.
  RANK_MODE = "least_extended" (smallest 30-min run-up, else move since the open;
  then tighter spread, then symbol) is a declared hypothesis, NOT tuned.
- Writes scalp_account_trades.csv, scalp_account_skipped.csv (reason + hypothetical
  result of each skipped signal) and scalp_account_summary.json (incl. picked-vs-outranked).
- gate_check.py Gate 1 reads scalp_account_trades.csv when present (else the old file)
  and prints which file it used.

**New: random-entry baseline (scalp_random_baseline.py)**
- Same symbols, days, exits and sizing; only the entry time is random (1,000 draws,
  two versions: same symbol-day, and within +/-15 min of the real entry). Writes
  scalp_random_baseline.json / .md with the real signals' average vs the random range
  and a p-value. Uses only the current ~7-day Yahoo window. Exit logic verified identical
  to find_trades on 127 synthetic trades. Runs as a new workflow step.

**New tags (tagging only, no effect on entries/exits)**
- gap_open_pct, range_to_stop, dist_from_day_high_pct, burst_pct, minutes_to_close,
  weekday. record_tags now back-fills blank tag fields on existing rows when the same
  signal is found again (never overwrites existing values).
- analyze_tags.py: buckets for the new tags and what-if rules for afternoon entries,
  volume spikes > 5x, stop-inside-noise and post-burst entries.

**Results (in-sample, 2026-09-24 to 2026-10-19)**
- 185 valid trades, symbols independent: gross -$82.71, cost $413.82, net -$496.53.
- Cost-gate passing: 115 trades, gross -$16.33, net -$100.18 (-$0.87/trade).
- Account sim (one position, least_extended): 81 trades / 18 days (4.5/day), gross -$16.52,
  cost $64.57, net -$81.09 (-$1.00/trade), win rate 39.5%. 11 ties: pick averaged
  $3.76 worse than outranked (std error $2.04) -- too few to act on.
- The first-bar "edge" (66 trades, +$94 gross) came from the day-boundary bug.

**Not changed:** entry thresholds, stop/target, hold time, position size, cost model.
FREEZE_DATE stays unset.
