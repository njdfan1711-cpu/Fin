# Random-entry baseline

Generated 2026-11-17T17:31:08+00:00. 34 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.767 | $-2.429 | 29.4 | 14.7 |
| Random: A_same_symbol_day | $-0.036 (5-95%: -1.806 to 1.744) | $-0.697 | 39.3 | 22.5 |
| Random: B_within_15_min | $2.075 (5-95%: 0.095 to 3.934) | $1.414 | 53.2 | 39.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.947
- B_within_15_min: p = 1.0

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 34 | $-1.767 | $-2.429 | 29.4 | 14.7 | - |
| +1 min | 34 | $-2.994 | $-3.655 | 20.6 | 8.8 | -1.227 (+/- 0.929) |
| +2 min | 34 | $-2.167 | $-2.828 | 29.4 | 11.8 | -0.4 (+/- 1.113) |
| +3 min | 34 | $-1.269 | $-1.93 | 32.4 | 17.6 | +0.498 (+/- 1.39) |
| +5 min | 31 | $-0.029 | $-0.705 | 35.5 | 22.6 | +2.011 (+/- 1.568) |
| +10 min | 30 | $0.485 | $-0.196 | 43.3 | 26.7 | +2.394 (+/- 1.747) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

34 trades: avg gross $1.639, avg net $0.977, win 50.0%, target 38.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
