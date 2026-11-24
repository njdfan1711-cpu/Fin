# Random-entry baseline

Generated 2026-11-24T16:31:28+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.745 | $0.113 | 45.5 | 36.4 |
| Random: A_same_symbol_day | $-0.363 (5-95%: -2.722 to 1.955) | $-0.993 | 36.6 | 24.3 |
| Random: B_within_15_min | $1.257 (5-95%: -1.159 to 3.544) | $0.626 | 46.7 | 36.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.234
- B_within_15_min: p = 0.631

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $0.745 | $0.113 | 45.5 | 36.4 | - |
| +1 min | 22 | $-2.208 | $-2.841 | 27.3 | 13.6 | -2.953 (+/- 1.297) |
| +2 min | 22 | $-2.657 | $-3.29 | 22.7 | 9.1 | -3.402 (+/- 1.324) |
| +3 min | 22 | $-1.701 | $-2.334 | 31.8 | 13.6 | -2.446 (+/- 1.189) |
| +5 min | 17 | $-2.957 | $-3.537 | 17.6 | 11.8 | -1.447 (+/- 1.912) |
| +10 min | 17 | $-0.482 | $-1.061 | 35.3 | 17.6 | +1.027 (+/- 2.437) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $1.744, avg net $1.111, win 50.0%, target 36.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
