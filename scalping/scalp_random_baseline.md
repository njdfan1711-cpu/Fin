# Random-entry baseline

Generated 2026-11-03T14:31:14+00:00. 34 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.825 | $0.069 | 47.1 | 23.5 |
| Random: A_same_symbol_day | $0.04 (5-95%: -1.7 to 1.706) | $-0.72 | 40.7 | 20.0 |
| Random: B_within_15_min | $3.163 (5-95%: 1.525 to 4.863) | $2.402 | 61.3 | 43.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.223
- B_within_15_min: p = 0.989

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 34 | $0.825 | $0.069 | 47.1 | 23.5 | - |
| +1 min | 33 | $3.193 | $2.457 | 60.6 | 39.4 | +2.28 (+/- 1.163) |
| +2 min | 33 | $2.647 | $1.911 | 57.6 | 33.3 | +1.734 (+/- 1.206) |
| +3 min | 33 | $0.292 | $-0.444 | 45.5 | 21.2 | -0.621 (+/- 1.192) |
| +5 min | 32 | $1.216 | $0.469 | 53.1 | 25.0 | +0.26 (+/- 1.418) |
| +10 min | 26 | $-2.095 | $-2.809 | 23.1 | 11.5 | -2.521 (+/- 1.712) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

34 trades: avg gross $-0.673, avg net $-1.428, win 35.3%, target 20.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
