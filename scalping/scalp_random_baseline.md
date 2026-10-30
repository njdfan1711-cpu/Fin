# Random-entry baseline

Generated 2026-10-30T19:31:24+00:00. 33 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.716 | $-0.026 | 45.5 | 27.3 |
| Random: A_same_symbol_day | $-0.063 (5-95%: -1.791 to 1.837) | $-0.807 | 39.9 | 20.7 |
| Random: B_within_15_min | $2.731 (5-95%: 1.006 to 4.474) | $1.988 | 58.2 | 42.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.245
- B_within_15_min: p = 0.972

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 33 | $0.716 | $-0.026 | 45.5 | 27.3 | - |
| +1 min | 33 | $3.77 | $3.029 | 63.6 | 45.5 | +3.054 (+/- 1.181) |
| +2 min | 33 | $2.905 | $2.163 | 57.6 | 39.4 | +2.189 (+/- 1.286) |
| +3 min | 32 | $0.194 | $-0.534 | 43.8 | 25.0 | -0.727 (+/- 1.224) |
| +5 min | 31 | $1.175 | $0.436 | 51.6 | 22.6 | +0.209 (+/- 1.468) |
| +10 min | 27 | $-1.492 | $-2.219 | 29.6 | 14.8 | -1.679 (+/- 1.815) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

32 trades: avg gross $-1.476, avg net $-2.204, win 28.1%, target 18.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
