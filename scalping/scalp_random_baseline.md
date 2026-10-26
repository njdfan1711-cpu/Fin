# Random-entry baseline

Generated 2026-10-26T14:31:39+00:00. 17 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.875 | $0.14 | 41.2 | 35.3 |
| Random: A_same_symbol_day | $-0.465 (5-95%: -2.882 to 2.085) | $-1.201 | 36.2 | 21.1 |
| Random: B_within_15_min | $1.596 (5-95%: -0.879 to 4.103) | $0.861 | 51.5 | 33.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.186
- B_within_15_min: p = 0.683

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 17 | $0.875 | $0.14 | 41.2 | 35.3 | - |
| +1 min | 16 | $2.441 | $1.696 | 56.2 | 43.8 | +1.521 (+/- 1.093) |
| +2 min | 16 | $2.07 | $1.325 | 50.0 | 43.8 | +1.15 (+/- 2.025) |
| +3 min | 16 | $0.364 | $-0.38 | 43.8 | 25.0 | -0.555 (+/- 1.541) |
| +5 min | 16 | $1.097 | $0.352 | 50.0 | 25.0 | +0.177 (+/- 2.122) |
| +10 min | 14 | $-1.085 | $-1.9 | 28.6 | 14.3 | -0.693 (+/- 2.893) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

17 trades: avg gross $-1.365, avg net $-2.1, win 29.4%, target 17.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
