# Random-entry baseline

Generated 2026-11-24T17:31:31+00:00. 23 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.126 | $0.493 | 47.8 | 39.1 |
| Random: A_same_symbol_day | $-0.174 (5-95%: -2.489 to 2.131) | $-0.805 | 37.7 | 25.7 |
| Random: B_within_15_min | $1.16 (5-95%: -1.081 to 3.503) | $0.528 | 45.8 | 36.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.173
- B_within_15_min: p = 0.502

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 23 | $1.126 | $0.493 | 47.8 | 39.1 | - |
| +1 min | 23 | $-2.348 | $-2.982 | 26.1 | 13.0 | -3.474 (+/- 1.344) |
| +2 min | 23 | $-2.128 | $-2.762 | 26.1 | 13.0 | -3.254 (+/- 1.274) |
| +3 min | 23 | $-1.863 | $-2.497 | 30.4 | 13.0 | -2.989 (+/- 1.259) |
| +5 min | 18 | $-3.095 | $-3.679 | 16.7 | 11.1 | -2.197 (+/- 1.952) |
| +10 min | 18 | $-0.758 | $-1.34 | 33.3 | 16.7 | +0.141 (+/- 2.462) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

23 trades: avg gross $1.432, avg net $0.799, win 47.8%, target 34.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
