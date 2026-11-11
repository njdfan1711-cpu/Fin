# Random-entry baseline

Generated 2026-11-11T15:31:03+00:00. 30 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.855 | $1.195 | 53.3 | 36.7 |
| Random: A_same_symbol_day | $-0.071 (5-95%: -2.095 to 1.87) | $-0.729 | 39.6 | 23.1 |
| Random: B_within_15_min | $2.026 (5-95%: -0.142 to 4.049) | $1.367 | 51.6 | 42.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.052
- B_within_15_min: p = 0.554

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 30 | $1.855 | $1.195 | 53.3 | 36.7 | - |
| +1 min | 29 | $-0.762 | $-1.421 | 34.5 | 24.1 | -2.609 (+/- 1.48) |
| +2 min | 28 | $0.206 | $-0.435 | 39.3 | 28.6 | -1.855 (+/- 1.389) |
| +3 min | 28 | $-0.605 | $-1.245 | 28.6 | 21.4 | -2.666 (+/- 1.449) |
| +5 min | 26 | $-0.238 | $-0.9 | 30.8 | 26.9 | -2.592 (+/- 1.382) |
| +10 min | 24 | $-2.769 | $-3.449 | 25.0 | 8.3 | -5.452 (+/- 1.996) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

30 trades: avg gross $-2.526, avg net $-3.185, win 23.3%, target 13.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
