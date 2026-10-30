# Random-entry baseline

Generated 2026-10-30T14:30:58+00:00. 30 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.468 | $-0.278 | 43.3 | 26.7 |
| Random: A_same_symbol_day | $-0.06 (5-95%: -2.015 to 1.852) | $-0.808 | 40.2 | 20.1 |
| Random: B_within_15_min | $2.737 (5-95%: 0.992 to 4.519) | $1.989 | 58.5 | 42.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.334
- B_within_15_min: p = 0.985

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 30 | $0.468 | $-0.278 | 43.3 | 26.7 | - |
| +1 min | 30 | $4.065 | $3.319 | 63.3 | 50.0 | +3.597 (+/- 1.232) |
| +2 min | 30 | $3.478 | $2.731 | 60.0 | 43.3 | +3.01 (+/- 1.275) |
| +3 min | 30 | $0.36 | $-0.387 | 43.3 | 26.7 | -0.108 (+/- 1.222) |
| +5 min | 29 | $1.617 | $0.859 | 55.2 | 24.1 | +1.117 (+/- 1.411) |
| +10 min | 25 | $-1.256 | $-2.005 | 32.0 | 16.0 | -0.841 (+/- 1.859) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

30 trades: avg gross $-1.204, avg net $-1.95, win 30.0%, target 20.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
