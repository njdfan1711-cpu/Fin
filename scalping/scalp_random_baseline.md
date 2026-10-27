# Random-entry baseline

Generated 2026-10-27T16:31:12+00:00. 20 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.59 | $-0.111 | 45.0 | 25.0 |
| Random: A_same_symbol_day | $-0.177 (5-95%: -2.427 to 2.038) | $-0.88 | 39.3 | 19.7 |
| Random: B_within_15_min | $1.872 (5-95%: -0.297 to 4.045) | $1.17 | 53.5 | 34.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.292
- B_within_15_min: p = 0.833

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 20 | $0.59 | $-0.111 | 45.0 | 25.0 | - |
| +1 min | 19 | $3.24 | $2.532 | 63.2 | 42.1 | +2.627 (+/- 1.262) |
| +2 min | 19 | $2.305 | $1.598 | 52.6 | 36.8 | +1.693 (+/- 1.938) |
| +3 min | 19 | $1.046 | $0.338 | 47.4 | 26.3 | +0.434 (+/- 1.492) |
| +5 min | 18 | $2.32 | $1.598 | 61.1 | 27.8 | +1.648 (+/- 1.959) |
| +10 min | 17 | $-0.41 | $-1.149 | 35.3 | 17.6 | -0.516 (+/- 2.296) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

20 trades: avg gross $-1.117, avg net $-1.818, win 25.0%, target 20.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
