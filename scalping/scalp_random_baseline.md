# Random-entry baseline

Generated 2026-11-05T19:31:17+00:00. 44 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.571 | $-0.132 | 43.2 | 27.3 |
| Random: A_same_symbol_day | $0.003 (5-95%: -1.589 to 1.62) | $-0.703 | 40.1 | 21.4 |
| Random: B_within_15_min | $2.266 (5-95%: 0.682 to 3.869) | $1.559 | 54.1 | 39.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.276
- B_within_15_min: p = 0.962

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 44 | $0.571 | $-0.132 | 43.2 | 27.3 | - |
| +1 min | 42 | $0.212 | $-0.475 | 40.5 | 26.2 | -0.386 (+/- 1.152) |
| +2 min | 42 | $0.755 | $0.068 | 45.2 | 31.0 | +0.156 (+/- 0.726) |
| +3 min | 42 | $-0.128 | $-0.817 | 33.3 | 26.2 | -0.726 (+/- 1.111) |
| +5 min | 42 | $-0.203 | $-0.892 | 33.3 | 26.2 | -0.801 (+/- 0.847) |
| +10 min | 37 | $-3.3 | $-3.995 | 18.9 | 5.4 | -4.276 (+/- 1.391) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

44 trades: avg gross $-0.592, avg net $-1.295, win 36.4%, target 22.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
