# Random-entry baseline

Generated 2026-10-23T15:31:04+00:00. 13 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.991 | $-2.622 | 23.1 | 7.7 |
| Random: A_same_symbol_day | $-0.226 (5-95%: -2.666 to 2.446) | $-0.861 | 40.0 | 16.5 |
| Random: B_within_15_min | $1.606 (5-95%: -1.03 to 4.426) | $0.973 | 50.3 | 29.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.861
- B_within_15_min: p = 0.986

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 13 | $-1.991 | $-2.622 | 23.1 | 7.7 | - |
| +1 min | 12 | $-0.027 | $-0.677 | 41.7 | 16.7 | +2.025 (+/- 1.915) |
| +2 min | 12 | $0.648 | $-0.001 | 33.3 | 16.7 | +2.7 (+/- 2.231) |
| +3 min | 12 | $-0.062 | $-0.711 | 41.7 | 16.7 | +1.99 (+/- 0.88) |
| +5 min | 12 | $0.409 | $-0.24 | 33.3 | 33.3 | +2.461 (+/- 1.853) |
| +10 min | 12 | $-0.285 | $-0.936 | 33.3 | 25.0 | +1.767 (+/- 2.027) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

13 trades: avg gross $-0.704, avg net $-1.335, win 46.2%, target 7.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
