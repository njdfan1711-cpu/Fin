# Random-entry baseline

Generated 2026-11-10T14:31:32+00:00. 30 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.849 | $1.169 | 53.3 | 36.7 |
| Random: A_same_symbol_day | $-0.224 (5-95%: -2.064 to 1.698) | $-0.902 | 38.3 | 21.5 |
| Random: B_within_15_min | $1.768 (5-95%: -0.229 to 3.776) | $1.089 | 50.3 | 38.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.032
- B_within_15_min: p = 0.484

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 30 | $1.849 | $1.169 | 53.3 | 36.7 | - |
| +1 min | 29 | $-0.768 | $-1.448 | 34.5 | 24.1 | -2.609 (+/- 1.48) |
| +2 min | 28 | $0.2 | $-0.462 | 39.3 | 28.6 | -1.855 (+/- 1.389) |
| +3 min | 28 | $-0.713 | $-1.375 | 28.6 | 21.4 | -2.767 (+/- 1.439) |
| +5 min | 27 | $-0.295 | $-0.965 | 29.6 | 25.9 | -2.342 (+/- 1.353) |
| +10 min | 26 | $-2.841 | $-3.523 | 23.1 | 7.7 | -4.861 (+/- 1.888) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

30 trades: avg gross $-1.857, avg net $-2.537, win 26.7%, target 16.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
