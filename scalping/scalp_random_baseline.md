# Random-entry baseline

Generated 2026-10-28T17:31:21+00:00. 25 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.82 | $0.152 | 48.0 | 24.0 |
| Random: A_same_symbol_day | $-0.24 (5-95%: -2.098 to 1.706) | $-0.911 | 39.2 | 15.4 |
| Random: B_within_15_min | $2.184 (5-95%: 0.19 to 4.238) | $1.514 | 54.6 | 36.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.18
- B_within_15_min: p = 0.846

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 25 | $0.82 | $0.152 | 48.0 | 24.0 | - |
| +1 min | 25 | $3.129 | $2.46 | 60.0 | 40.0 | +2.309 (+/- 1.284) |
| +2 min | 24 | $1.941 | $1.267 | 54.2 | 29.2 | +1.32 (+/- 1.148) |
| +3 min | 24 | $0.579 | $-0.095 | 41.7 | 25.0 | -0.042 (+/- 0.953) |
| +5 min | 24 | $2.054 | $1.379 | 58.3 | 33.3 | +1.434 (+/- 1.137) |
| +10 min | 24 | $-0.751 | $-1.427 | 33.3 | 16.7 | -1.372 (+/- 1.542) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

25 trades: avg gross $-0.377, avg net $-1.046, win 40.0%, target 20.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
