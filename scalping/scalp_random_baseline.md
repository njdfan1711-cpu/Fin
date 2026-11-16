# Random-entry baseline

Generated 2026-11-16T15:31:05+00:00. 21 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.229 | $-0.99 | 42.9 | 19.0 |
| Random: A_same_symbol_day | $-0.036 (5-95%: -2.232 to 2.225) | $-0.796 | 40.9 | 18.3 |
| Random: B_within_15_min | $2.304 (5-95%: -0.011 to 4.592) | $1.544 | 56.1 | 35.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.544
- B_within_15_min: p = 0.96

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 21 | $-0.229 | $-0.99 | 42.9 | 19.0 | - |
| +1 min | 21 | $-0.339 | $-1.099 | 42.9 | 19.0 | -0.11 (+/- 1.219) |
| +2 min | 21 | $-0.05 | $-0.811 | 42.9 | 19.0 | +0.179 (+/- 1.46) |
| +3 min | 20 | $0.619 | $-0.146 | 40.0 | 25.0 | +0.567 (+/- 1.906) |
| +5 min | 20 | $-0.184 | $-0.948 | 35.0 | 15.0 | -0.236 (+/- 1.946) |
| +10 min | 19 | $-2.528 | $-3.27 | 26.3 | 5.3 | -2.895 (+/- 1.95) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

21 trades: avg gross $0.308, avg net $-0.453, win 47.6%, target 23.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
