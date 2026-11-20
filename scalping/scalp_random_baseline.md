# Random-entry baseline

Generated 2026-11-20T18:31:09+00:00. 25 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.981 | $-1.691 | 36.0 | 20.0 |
| Random: A_same_symbol_day | $-0.356 (5-95%: -2.377 to 1.733) | $-1.063 | 37.1 | 21.4 |
| Random: B_within_15_min | $2.608 (5-95%: 0.187 to 4.848) | $1.899 | 55.8 | 41.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.683
- B_within_15_min: p = 0.995

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 25 | $-0.981 | $-1.691 | 36.0 | 20.0 | - |
| +1 min | 25 | $-1.625 | $-2.335 | 32.0 | 12.0 | -0.644 (+/- 1.156) |
| +2 min | 25 | $-1.493 | $-2.203 | 32.0 | 12.0 | -0.511 (+/- 1.063) |
| +3 min | 24 | $-1.034 | $-1.745 | 33.3 | 16.7 | -0.255 (+/- 1.426) |
| +5 min | 19 | $-1.204 | $-1.887 | 26.3 | 15.8 | +1.994 (+/- 1.752) |
| +10 min | 18 | $-0.225 | $-0.879 | 33.3 | 22.2 | +2.82 (+/- 1.913) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

25 trades: avg gross $2.484, avg net $1.774, win 60.0%, target 36.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
