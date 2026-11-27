# Random-entry baseline

Generated 2026-11-27T14:31:15+00:00. 24 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.762 | $-1.353 | 33.3 | 25.0 |
| Random: A_same_symbol_day | $0.052 (5-95%: -2.232 to 2.363) | $-0.539 | 39.6 | 26.5 |
| Random: B_within_15_min | $1.8 (5-95%: -0.378 to 3.82) | $1.209 | 51.2 | 39.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.707
- B_within_15_min: p = 0.98

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 24 | $-0.762 | $-1.353 | 33.3 | 25.0 | - |
| +1 min | 24 | $-1.968 | $-2.559 | 25.0 | 12.5 | -1.206 (+/- 0.848) |
| +2 min | 24 | $-2.215 | $-2.806 | 25.0 | 12.5 | -1.453 (+/- 0.911) |
| +3 min | 24 | $-2.102 | $-2.692 | 29.2 | 12.5 | -1.341 (+/- 1.341) |
| +5 min | 22 | $0.432 | $-0.136 | 45.5 | 27.3 | +1.399 (+/- 1.66) |
| +10 min | 21 | $-0.302 | $-0.876 | 38.1 | 23.8 | +0.447 (+/- 1.667) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

24 trades: avg gross $0.271, avg net $-0.32, win 41.7%, target 29.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
