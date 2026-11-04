# Random-entry baseline

Generated 2026-11-04T19:30:59+00:00. 41 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.961 | $0.181 | 46.3 | 26.8 |
| Random: A_same_symbol_day | $0.019 (5-95%: -1.502 to 1.688) | $-0.765 | 39.9 | 21.2 |
| Random: B_within_15_min | $3.179 (5-95%: 1.609 to 4.76) | $2.395 | 60.3 | 45.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.167
- B_within_15_min: p = 0.988

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 41 | $0.961 | $0.181 | 46.3 | 26.8 | - |
| +1 min | 40 | $1.407 | $0.642 | 47.5 | 32.5 | +0.369 (+/- 1.083) |
| +2 min | 39 | $2.049 | $1.282 | 53.8 | 33.3 | +1.127 (+/- 0.945) |
| +3 min | 39 | $0.162 | $-0.605 | 41.0 | 25.6 | -0.76 (+/- 1.043) |
| +5 min | 39 | $1.256 | $0.487 | 48.7 | 30.8 | +0.334 (+/- 1.124) |
| +10 min | 32 | $-2.037 | $-2.797 | 25.0 | 12.5 | -2.465 (+/- 1.721) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

41 trades: avg gross $-1.166, avg net $-1.946, win 34.1%, target 14.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
