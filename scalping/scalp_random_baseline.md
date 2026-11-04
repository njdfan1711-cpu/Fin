# Random-entry baseline

Generated 2026-11-04T17:31:03+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.069 | $0.287 | 47.5 | 27.5 |
| Random: A_same_symbol_day | $0.073 (5-95%: -1.593 to 1.839) | $-0.712 | 40.4 | 21.5 |
| Random: B_within_15_min | $3.325 (5-95%: 1.73 to 4.937) | $2.539 | 61.5 | 46.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.176
- B_within_15_min: p = 0.987

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $1.069 | $0.287 | 47.5 | 27.5 | - |
| +1 min | 39 | $1.595 | $0.828 | 48.7 | 33.3 | +0.445 (+/- 1.109) |
| +2 min | 38 | $2.062 | $1.294 | 52.6 | 34.2 | +1.027 (+/- 0.965) |
| +3 min | 38 | $0.212 | $-0.557 | 42.1 | 26.3 | -0.824 (+/- 1.069) |
| +5 min | 38 | $1.445 | $0.675 | 50.0 | 31.6 | +0.41 (+/- 1.151) |
| +10 min | 30 | $-1.776 | $-2.544 | 26.7 | 13.3 | -2.001 (+/- 1.775) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $-1.047, avg net $-1.829, win 35.0%, target 15.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
