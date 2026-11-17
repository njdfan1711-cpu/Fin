# Random-entry baseline

Generated 2026-11-17T20:31:06+00:00. 37 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-2.012 | $-2.683 | 27.0 | 13.5 |
| Random: A_same_symbol_day | $-0.145 (5-95%: -1.791 to 1.56) | $-0.816 | 38.5 | 21.4 |
| Random: B_within_15_min | $2.118 (5-95%: 0.353 to 3.867) | $1.448 | 53.3 | 38.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.969
- B_within_15_min: p = 1.0

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 37 | $-2.012 | $-2.683 | 27.0 | 13.5 | - |
| +1 min | 37 | $-2.988 | $-3.659 | 18.9 | 8.1 | -0.976 (+/- 0.866) |
| +2 min | 37 | $-2.25 | $-2.92 | 27.0 | 10.8 | -0.238 (+/- 1.027) |
| +3 min | 37 | $-1.413 | $-2.083 | 29.7 | 16.2 | +0.599 (+/- 1.278) |
| +5 min | 34 | $-0.201 | $-0.887 | 35.3 | 20.6 | +2.081 (+/- 1.432) |
| +10 min | 33 | $0.452 | $-0.237 | 42.4 | 24.2 | +2.624 (+/- 1.592) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

37 trades: avg gross $2.013, avg net $1.342, win 54.1%, target 37.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
