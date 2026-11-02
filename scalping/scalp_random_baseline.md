# Random-entry baseline

Generated 2026-11-02T16:31:24+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.182 | $-0.899 | 40.0 | 22.5 |
| Random: A_same_symbol_day | $-0.01 (5-95%: -1.526 to 1.69) | $-0.733 | 40.4 | 19.2 |
| Random: B_within_15_min | $2.335 (5-95%: 0.649 to 3.964) | $1.614 | 55.5 | 38.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.54
- B_within_15_min: p = 0.996

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $-0.182 | $-0.899 | 40.0 | 22.5 | - |
| +1 min | 39 | $2.288 | $1.589 | 53.8 | 38.5 | +2.422 (+/- 1.085) |
| +2 min | 38 | $1.461 | $0.758 | 52.6 | 31.6 | +1.745 (+/- 0.864) |
| +3 min | 38 | $0.925 | $0.22 | 44.7 | 31.6 | +1.21 (+/- 1.071) |
| +5 min | 38 | $1.147 | $0.441 | 50.0 | 31.6 | +1.432 (+/- 0.944) |
| +10 min | 34 | $-1.863 | $-2.567 | 29.4 | 11.8 | -1.949 (+/- 1.427) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $-0.005, avg net $-0.722, win 40.0%, target 27.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
