# Random-entry baseline

Generated 2026-11-18T14:31:24+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.337 | $-1.984 | 32.5 | 15.0 |
| Random: A_same_symbol_day | $-0.099 (5-95%: -1.858 to 1.651) | $-0.745 | 38.6 | 23.1 |
| Random: B_within_15_min | $2.037 (5-95%: 0.233 to 3.79) | $1.391 | 52.7 | 39.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.888
- B_within_15_min: p = 0.999

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $-1.337 | $-1.984 | 32.5 | 15.0 | - |
| +1 min | 40 | $-2.408 | $-3.055 | 25.0 | 7.5 | -1.071 (+/- 0.803) |
| +2 min | 40 | $-1.935 | $-2.583 | 30.0 | 10.0 | -0.599 (+/- 0.835) |
| +3 min | 39 | $-1.288 | $-1.911 | 33.3 | 12.8 | +0.351 (+/- 1.112) |
| +5 min | 32 | $-0.525 | $-1.168 | 34.4 | 18.8 | +2.516 (+/- 1.395) |
| +10 min | 31 | $0.543 | $-0.103 | 41.9 | 25.8 | +3.491 (+/- 1.449) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $1.487, avg net $0.839, win 50.0%, target 35.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
