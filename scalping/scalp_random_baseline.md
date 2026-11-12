# Random-entry baseline

Generated 2026-11-12T19:31:35+00:00. 32 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.337 | $0.67 | 50.0 | 34.4 |
| Random: A_same_symbol_day | $-0.149 (5-95%: -2.069 to 1.907) | $-0.815 | 39.1 | 22.6 |
| Random: B_within_15_min | $1.915 (5-95%: -0.043 to 3.929) | $1.248 | 50.3 | 41.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.117
- B_within_15_min: p = 0.677

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 32 | $1.337 | $0.67 | 50.0 | 34.4 | - |
| +1 min | 32 | $-0.465 | $-1.133 | 37.5 | 25.0 | -1.803 (+/- 1.453) |
| +2 min | 31 | $-0.273 | $-0.925 | 38.7 | 25.8 | -1.787 (+/- 1.47) |
| +3 min | 31 | $-0.366 | $-1.017 | 32.3 | 22.6 | -1.88 (+/- 1.542) |
| +5 min | 29 | $-0.231 | $-0.903 | 31.0 | 24.1 | -1.971 (+/- 1.487) |
| +10 min | 28 | $-2.861 | $-3.537 | 17.9 | 10.7 | -4.874 (+/- 1.734) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

32 trades: avg gross $-2.142, avg net $-2.81, win 25.0%, target 18.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
