# Random-entry baseline

Generated 2026-10-23T17:31:03+00:00. 16 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.841 | $0.057 | 43.8 | 31.2 |
| Random: A_same_symbol_day | $-0.595 (5-95%: -3.104 to 2.097) | $-1.379 | 35.6 | 19.4 |
| Random: B_within_15_min | $1.345 (5-95%: -1.207 to 3.886) | $0.561 | 49.0 | 31.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.182
- B_within_15_min: p = 0.611

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 16 | $0.841 | $0.057 | 43.8 | 31.2 | - |
| +1 min | 15 | $2.725 | $1.927 | 60.0 | 40.0 | +1.839 (+/- 1.162) |
| +2 min | 15 | $2.388 | $1.59 | 53.3 | 40.0 | +1.502 (+/- 2.17) |
| +3 min | 15 | $0.901 | $0.103 | 46.7 | 26.7 | +0.015 (+/- 1.636) |
| +5 min | 15 | $0.617 | $-0.181 | 40.0 | 26.7 | -0.269 (+/- 1.935) |
| +10 min | 14 | $-1.638 | $-2.463 | 21.4 | 14.3 | -1.853 (+/- 2.848) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

16 trades: avg gross $-1.905, avg net $-2.689, win 25.0%, target 12.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
