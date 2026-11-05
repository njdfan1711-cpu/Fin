# Random-entry baseline

Generated 2026-11-05T14:31:17+00:00. 41 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.886 | $0.098 | 43.9 | 26.8 |
| Random: A_same_symbol_day | $-0.054 (5-95%: -1.668 to 1.634) | $-0.846 | 39.4 | 21.2 |
| Random: B_within_15_min | $3.073 (5-95%: 1.464 to 4.671) | $2.281 | 59.5 | 44.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.162
- B_within_15_min: p = 0.982

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 41 | $0.886 | $0.098 | 43.9 | 26.8 | - |
| +1 min | 40 | $1.077 | $0.304 | 45.0 | 27.5 | +0.116 (+/- 1.064) |
| +2 min | 38 | $1.681 | $0.926 | 50.0 | 31.6 | +1.084 (+/- 0.968) |
| +3 min | 38 | $0.006 | $-0.749 | 39.5 | 23.7 | -0.591 (+/- 1.055) |
| +5 min | 37 | $0.915 | $0.17 | 45.9 | 29.7 | +0.266 (+/- 1.183) |
| +10 min | 30 | $-2.32 | $-3.05 | 23.3 | 10.0 | -2.379 (+/- 1.828) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

41 trades: avg gross $-0.986, avg net $-1.774, win 36.6%, target 14.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
