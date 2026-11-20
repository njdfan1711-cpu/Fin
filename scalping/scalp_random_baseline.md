# Random-entry baseline

Generated 2026-11-20T16:31:20+00:00. 39 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.03 | $-1.668 | 33.3 | 17.9 |
| Random: A_same_symbol_day | $-0.22 (5-95%: -1.818 to 1.48) | $-0.855 | 37.9 | 22.3 |
| Random: B_within_15_min | $2.007 (5-95%: 0.251 to 3.79) | $1.371 | 52.3 | 38.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.781
- B_within_15_min: p = 0.998

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 39 | $-1.03 | $-1.668 | 33.3 | 17.9 | - |
| +1 min | 39 | $-2.441 | $-3.079 | 23.1 | 7.7 | -1.411 (+/- 0.883) |
| +2 min | 39 | $-1.768 | $-2.406 | 30.8 | 10.3 | -0.738 (+/- 0.896) |
| +3 min | 38 | $-1.236 | $-1.848 | 34.2 | 13.2 | +0.096 (+/- 1.172) |
| +5 min | 30 | $-0.458 | $-1.063 | 33.3 | 20.0 | +2.634 (+/- 1.487) |
| +10 min | 30 | $0.641 | $0.037 | 43.3 | 26.7 | +3.733 (+/- 1.411) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

39 trades: avg gross $1.726, avg net $1.089, win 51.3%, target 35.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
