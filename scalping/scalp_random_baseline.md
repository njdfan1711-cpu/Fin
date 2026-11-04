# Random-entry baseline

Generated 2026-11-04T18:31:02+00:00. 42 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.386 | $-0.347 | 42.9 | 26.2 |
| Random: A_same_symbol_day | $0.02 (5-95%: -1.598 to 1.64) | $-0.718 | 40.2 | 20.7 |
| Random: B_within_15_min | $2.364 (5-95%: 0.683 to 4.058) | $1.626 | 54.9 | 40.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.363
- B_within_15_min: p = 0.98

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 42 | $0.386 | $-0.347 | 42.9 | 26.2 | - |
| +1 min | 40 | $0.868 | $0.15 | 42.5 | 32.5 | +0.462 (+/- 1.109) |
| +2 min | 40 | $1.082 | $0.364 | 47.5 | 32.5 | +0.676 (+/- 0.651) |
| +3 min | 40 | $0.32 | $-0.4 | 37.5 | 30.0 | -0.085 (+/- 1.052) |
| +5 min | 40 | $0.495 | $-0.226 | 40.0 | 30.0 | +0.089 (+/- 0.716) |
| +10 min | 35 | $-2.841 | $-3.572 | 22.9 | 8.6 | -3.618 (+/- 1.4) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

42 trades: avg gross $-0.548, avg net $-1.282, win 38.1%, target 21.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
