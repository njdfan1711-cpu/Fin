# Random-entry baseline

Generated 2026-11-25T15:31:13+00:00. 35 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.843 | $-1.421 | 34.3 | 20.0 |
| Random: A_same_symbol_day | $-0.379 (5-95%: -2.169 to 1.494) | $-0.955 | 36.5 | 24.3 |
| Random: B_within_15_min | $1.785 (5-95%: -0.031 to 3.527) | $1.208 | 51.4 | 38.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.65
- B_within_15_min: p = 0.994

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 35 | $-0.843 | $-1.421 | 34.3 | 20.0 | - |
| +1 min | 35 | $-2.232 | $-2.811 | 25.7 | 5.7 | -1.389 (+/- 0.751) |
| +2 min | 35 | $-2.276 | $-2.855 | 25.7 | 5.7 | -1.434 (+/- 0.709) |
| +3 min | 34 | $-2.388 | $-2.937 | 29.4 | 2.9 | -1.213 (+/- 0.976) |
| +5 min | 28 | $-0.637 | $-1.164 | 39.3 | 17.9 | +1.976 (+/- 1.384) |
| +10 min | 27 | $0.367 | $-0.163 | 44.4 | 22.2 | +2.871 (+/- 1.631) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

35 trades: avg gross $1.305, avg net $0.727, win 48.6%, target 37.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
