# Random-entry baseline

Generated 2026-11-19T14:31:04+00:00. 26 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.837 | $-1.559 | 38.5 | 19.2 |
| Random: A_same_symbol_day | $-0.296 (5-95%: -2.357 to 1.723) | $-1.015 | 37.2 | 22.5 |
| Random: B_within_15_min | $2.39 (5-95%: 0.174 to 4.503) | $1.668 | 54.7 | 39.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.669
- B_within_15_min: p = 0.993

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 26 | $-0.837 | $-1.559 | 38.5 | 19.2 | - |
| +1 min | 26 | $-1.51 | $-2.232 | 34.6 | 11.5 | -0.673 (+/- 1.111) |
| +2 min | 26 | $-1.664 | $-2.386 | 30.8 | 11.5 | -0.827 (+/- 1.069) |
| +3 min | 25 | $-1.231 | $-1.954 | 32.0 | 16.0 | -0.594 (+/- 1.409) |
| +5 min | 20 | $-0.928 | $-1.629 | 30.0 | 15.0 | +1.971 (+/- 1.663) |
| +10 min | 19 | $0.15 | $-0.525 | 36.8 | 21.1 | +2.889 (+/- 1.984) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

26 trades: avg gross $2.165, avg net $1.442, win 57.7%, target 34.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
