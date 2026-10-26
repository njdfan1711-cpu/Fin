# Random-entry baseline

Generated 2026-10-26T13:31:10+00:00. 12 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.486 | $-2.03 | 25.0 | 8.3 |
| Random: A_same_symbol_day | $-0.738 (5-95%: -3.263 to 1.784) | $-1.286 | 36.1 | 12.3 |
| Random: B_within_15_min | $1.882 (5-95%: -1.081 to 4.87) | $1.336 | 51.5 | 32.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.683
- B_within_15_min: p = 0.975

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 12 | $-1.486 | $-2.03 | 25.0 | 8.3 | - |
| +1 min | 11 | $0.254 | $-0.303 | 45.5 | 18.2 | +1.76 (+/- 2.114) |
| +2 min | 10 | $0.146 | $-0.411 | 30.0 | 20.0 | +2.364 (+/- 2.688) |
| +3 min | 10 | $-0.816 | $-1.372 | 30.0 | 20.0 | +1.402 (+/- 0.938) |
| +5 min | 10 | $0.309 | $-0.248 | 40.0 | 30.0 | +2.527 (+/- 1.864) |
| +10 min | 10 | $0.612 | $0.054 | 40.0 | 20.0 | +2.83 (+/- 2.14) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

12 trades: avg gross $-0.189, avg net $-0.733, win 50.0%, target 16.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
