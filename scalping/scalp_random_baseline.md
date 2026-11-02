# Random-entry baseline

Generated 2026-11-02T14:31:32+00:00. 36 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.448 | $-0.327 | 44.4 | 22.2 |
| Random: A_same_symbol_day | $-0.057 (5-95%: -1.837 to 1.655) | $-0.837 | 40.0 | 20.3 |
| Random: B_within_15_min | $3.046 (5-95%: 1.247 to 4.759) | $2.265 | 60.5 | 43.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.323
- B_within_15_min: p = 0.994

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 36 | $0.448 | $-0.327 | 44.4 | 22.2 | - |
| +1 min | 35 | $3.14 | $2.382 | 60.0 | 40.0 | +2.619 (+/- 1.17) |
| +2 min | 35 | $2.625 | $1.867 | 57.1 | 34.3 | +2.104 (+/- 1.213) |
| +3 min | 35 | $-0.133 | $-0.891 | 42.9 | 20.0 | -0.654 (+/- 1.12) |
| +5 min | 34 | $1.576 | $0.808 | 55.9 | 26.5 | +1.026 (+/- 1.468) |
| +10 min | 28 | $-1.648 | $-2.391 | 28.6 | 14.3 | -1.619 (+/- 1.75) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

36 trades: avg gross $-0.891, avg net $-1.666, win 33.3%, target 22.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
