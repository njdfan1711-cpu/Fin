# Random-entry baseline

Generated 2026-11-24T18:31:34+00:00. 24 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.266 | $0.638 | 50.0 | 37.5 |
| Random: A_same_symbol_day | $-0.238 (5-95%: -2.493 to 2.04) | $-0.864 | 37.1 | 25.4 |
| Random: B_within_15_min | $1.522 (5-95%: -0.77 to 3.888) | $0.896 | 48.4 | 37.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.13
- B_within_15_min: p = 0.573

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 24 | $1.266 | $0.638 | 50.0 | 37.5 | - |
| +1 min | 24 | $-2.115 | $-2.743 | 29.2 | 12.5 | -3.38 (+/- 1.29) |
| +2 min | 24 | $-1.883 | $-2.511 | 29.2 | 12.5 | -3.149 (+/- 1.224) |
| +3 min | 24 | $-1.639 | $-2.268 | 33.3 | 12.5 | -2.905 (+/- 1.208) |
| +5 min | 19 | $-2.389 | $-2.967 | 21.1 | 15.8 | -1.773 (+/- 1.894) |
| +10 min | 19 | $-0.174 | $-0.752 | 36.8 | 21.1 | +0.441 (+/- 2.348) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

24 trades: avg gross $1.126, avg net $0.499, win 45.8%, target 33.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
