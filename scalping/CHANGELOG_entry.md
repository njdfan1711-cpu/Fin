## 2026-10-21 -- Timing diagnostics added to scalp_random_baseline.py

Files: scalping/scalp_random_baseline.py (replace). No other files change.

**Added**
- Delay sweep: the real signals re-entered 0, 1, 2, 3, 5 and 10 minutes AFTER the
  signal minute with the same exits and sizing, with the paired gross difference vs
  the signal minute (+/- standard error). Tests whether the signal fires at the top
  of a burst (waiting would then do better).
- Mirror (short) test: the opposite side at the signal minute with mirrored
  stop/target. Diagnostic only -- the bot is long-only; a clearly positive result
  would mean the signal tends to mark exhaustion.
- Both are written to scalp_random_baseline.json / .md. Same ~7-day Yahoo window
  and the same few real signals as the random-entry baseline, so treat as clues.

**Why:** the 2026-10-21 baseline (24 signals) had the real signals at -$0.41 gross per
trade vs +$2.03 for random entries within +/-15 min of each signal (p = 0.98), which
suggests entering at the signal minute is worse than nearby minutes.

**Verified on synthetic data:** a burst-then-fade pattern makes the signal minute lose,
later entries win and the mirror short win; a burst-then-continue pattern does the
opposite. Exit logic still identical to find_trades.

**Not changed:** entry rules, exits, sizing, cost model, ranking.
