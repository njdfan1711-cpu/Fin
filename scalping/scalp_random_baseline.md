# Random-entry baseline

Generated 2026-10-29T14:31:21+00:00. 27 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.361 | $-0.405 | 44.4 | 25.9 |
| Random: A_same_symbol_day | $0.048 (5-95%: -2.014 to 2.14) | $-0.721 | 40.5 | 20.9 |
| Random: B_within_15_min | $2.674 (5-95%: 0.74 to 4.593) | $1.907 | 57.9 | 41.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.395
- B_within_15_min: p = 0.972

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 27 | $0.361 | $-0.405 | 44.4 | 25.9 | - |
| +1 min | 27 | $3.864 | $3.099 | 63.0 | 48.1 | +3.503 (+/- 1.252) |
| +2 min | 27 | $3.021 | $2.256 | 55.6 | 44.4 | +2.66 (+/- 1.358) |
| +3 min | 27 | $-0.257 | $-1.023 | 37.0 | 25.9 | -0.618 (+/- 1.226) |
| +5 min | 26 | $1.833 | $1.054 | 53.8 | 26.9 | +1.441 (+/- 1.571) |
| +10 min | 24 | $-1.031 | $-1.808 | 33.3 | 16.7 | -0.6 (+/- 1.904) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

27 trades: avg gross $-0.683, avg net $-1.448, win 33.3%, target 22.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
