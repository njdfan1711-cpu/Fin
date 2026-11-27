# Random-entry baseline

Generated 2026-11-27T17:31:21+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.082 | $0.45 | 45.5 | 36.4 |
| Random: A_same_symbol_day | $0.065 (5-95%: -2.28 to 2.495) | $-0.567 | 39.8 | 24.9 |
| Random: B_within_15_min | $1.699 (5-95%: -0.438 to 3.813) | $1.067 | 50.6 | 37.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.227
- B_within_15_min: p = 0.684

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $1.082 | $0.45 | 45.5 | 36.4 | - |
| +1 min | 22 | $-1.911 | $-2.544 | 27.3 | 18.2 | -2.994 (+/- 1.251) |
| +2 min | 22 | $-1.656 | $-2.29 | 27.3 | 18.2 | -2.739 (+/- 1.289) |
| +3 min | 22 | $-1.443 | $-2.075 | 31.8 | 18.2 | -2.525 (+/- 1.317) |
| +5 min | 21 | $-1.474 | $-2.103 | 33.3 | 19.0 | -2.197 (+/- 1.611) |
| +10 min | 20 | $0.077 | $-0.539 | 40.0 | 25.0 | -0.977 (+/- 2.049) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $1.475, avg net $0.842, win 50.0%, target 36.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
