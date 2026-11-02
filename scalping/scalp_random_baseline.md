# Random-entry baseline

Generated 2026-11-02T17:31:08+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.276 | $-0.494 | 43.2 | 21.6 |
| Random: A_same_symbol_day | $-0.097 (5-95%: -1.878 to 1.605) | $-0.873 | 39.4 | 19.9 |
| Random: B_within_15_min | $3.007 (5-95%: 1.337 to 4.701) | $2.232 | 60.3 | 42.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.354
- B_within_15_min: p = 0.996

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $0.276 | $-0.494 | 43.2 | 21.6 | - |
| +1 min | 36 | $2.888 | $2.135 | 58.3 | 38.9 | +2.546 (+/- 1.14) |
| +2 min | 36 | $2.387 | $1.635 | 55.6 | 33.3 | +2.046 (+/- 1.18) |
| +3 min | 36 | $-0.228 | $-0.981 | 41.7 | 19.4 | -0.57 (+/- 1.091) |
| +5 min | 35 | $1.48 | $0.718 | 54.3 | 25.7 | +1.115 (+/- 1.428) |
| +10 min | 29 | $-1.642 | $-2.379 | 27.6 | 13.8 | -1.41 (+/- 1.701) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

37 trades: avg gross $-0.66, avg net $-1.43, win 35.1%, target 21.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
