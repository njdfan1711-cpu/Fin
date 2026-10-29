# Random-entry baseline

Generated 2026-10-29T19:31:11+00:00. 30 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.261 | $-0.49 | 43.3 | 23.3 |
| Random: A_same_symbol_day | $0.044 (5-95%: -1.864 to 2.031) | $-0.71 | 40.9 | 21.2 |
| Random: B_within_15_min | $2.726 (5-95%: 0.91 to 4.563) | $1.973 | 58.3 | 42.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.422
- B_within_15_min: p = 0.986

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 30 | $0.261 | $-0.49 | 43.3 | 23.3 | - |
| +1 min | 30 | $3.835 | $3.083 | 63.3 | 46.7 | +3.574 (+/- 1.234) |
| +2 min | 30 | $3.106 | $2.355 | 56.7 | 43.3 | +2.845 (+/- 1.321) |
| +3 min | 30 | $0.058 | $-0.694 | 40.0 | 26.7 | -0.203 (+/- 1.244) |
| +5 min | 29 | $1.356 | $0.593 | 51.7 | 24.1 | +1.071 (+/- 1.423) |
| +10 min | 27 | $-0.535 | $-1.295 | 37.0 | 18.5 | -0.082 (+/- 1.805) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

30 trades: avg gross $-1.207, avg net $-1.958, win 30.0%, target 20.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
