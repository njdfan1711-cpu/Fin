# Random-entry baseline

Generated 2026-11-23T18:31:12+00:00. 24 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.213 | $-1.922 | 33.3 | 20.8 |
| Random: A_same_symbol_day | $-0.198 (5-95%: -2.405 to 2.029) | $-0.903 | 38.4 | 22.3 |
| Random: B_within_15_min | $1.764 (5-95%: -0.409 to 3.93) | $1.057 | 51.3 | 35.0 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.782
- B_within_15_min: p = 0.986

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 24 | $-1.213 | $-1.922 | 33.3 | 20.8 | - |
| +1 min | 24 | $-2.7 | $-3.409 | 25.0 | 8.3 | -1.487 (+/- 0.883) |
| +2 min | 24 | $-2.547 | $-3.256 | 25.0 | 8.3 | -1.334 (+/- 0.757) |
| +3 min | 24 | $-1.81 | $-2.519 | 29.2 | 12.5 | -0.597 (+/- 0.986) |
| +5 min | 19 | $-1.718 | $-2.398 | 26.3 | 15.8 | +2.028 (+/- 1.244) |
| +10 min | 18 | $-0.178 | $-0.83 | 38.9 | 16.7 | +3.446 (+/- 1.74) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

24 trades: avg gross $3.214, avg net $2.506, win 62.5%, target 41.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
