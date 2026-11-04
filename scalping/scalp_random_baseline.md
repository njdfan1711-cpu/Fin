# Random-entry baseline

Generated 2026-11-04T15:31:22+00:00. 38 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.593 | $-0.209 | 44.7 | 23.7 |
| Random: A_same_symbol_day | $0.127 (5-95%: -1.562 to 1.835) | $-0.678 | 41.1 | 21.1 |
| Random: B_within_15_min | $3.305 (5-95%: 1.694 to 5.042) | $2.499 | 61.6 | 45.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.322
- B_within_15_min: p = 0.998

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 38 | $0.593 | $-0.209 | 44.7 | 23.7 | - |
| +1 min | 37 | $1.133 | $0.347 | 45.9 | 29.7 | +0.468 (+/- 1.169) |
| +2 min | 36 | $1.613 | $0.825 | 50.0 | 30.6 | +1.083 (+/- 1.018) |
| +3 min | 36 | $-0.342 | $-1.131 | 38.9 | 22.2 | -0.872 (+/- 1.128) |
| +5 min | 36 | $0.961 | $0.17 | 47.2 | 27.8 | +0.43 (+/- 1.216) |
| +10 min | 29 | $-1.64 | $-2.426 | 27.6 | 13.8 | -1.531 (+/- 1.771) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

38 trades: avg gross $-0.797, avg net $-1.599, win 36.8%, target 15.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
