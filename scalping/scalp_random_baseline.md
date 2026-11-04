# Random-entry baseline

Generated 2026-11-04T16:31:14+00:00. 39 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.011 | $-0.767 | 41.0 | 23.1 |
| Random: A_same_symbol_day | $0.007 (5-95%: -1.669 to 1.734) | $-0.753 | 40.2 | 20.0 |
| Random: B_within_15_min | $2.43 (5-95%: 0.734 to 4.049) | $1.67 | 55.5 | 40.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.491
- B_within_15_min: p = 0.989

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 39 | $-0.011 | $-0.767 | 41.0 | 23.1 | - |
| +1 min | 37 | $0.557 | $-0.183 | 40.5 | 29.7 | +0.568 (+/- 1.198) |
| +2 min | 37 | $0.585 | $-0.155 | 43.2 | 29.7 | +0.597 (+/- 0.694) |
| +3 min | 37 | $0.024 | $-0.718 | 35.1 | 29.7 | +0.036 (+/- 1.124) |
| +5 min | 37 | $0.416 | $-0.327 | 40.5 | 29.7 | +0.428 (+/- 0.72) |
| +10 min | 32 | $-2.561 | $-3.318 | 25.0 | 9.4 | -2.891 (+/- 1.426) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

39 trades: avg gross $-0.145, avg net $-0.9, win 41.0%, target 23.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
