# Random-entry baseline

Generated 2026-10-30T18:31:21+00:00. 32 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.921 | $0.193 | 46.9 | 28.1 |
| Random: A_same_symbol_day | $0.035 (5-95%: -1.714 to 1.969) | $-0.695 | 40.6 | 20.9 |
| Random: B_within_15_min | $2.689 (5-95%: 0.857 to 4.415) | $1.96 | 58.2 | 41.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.2
- B_within_15_min: p = 0.939

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 32 | $0.921 | $0.193 | 46.9 | 28.1 | - |
| +1 min | 32 | $4.071 | $3.343 | 65.6 | 46.9 | +3.15 (+/- 1.215) |
| +2 min | 32 | $3.178 | $2.45 | 59.4 | 40.6 | +2.257 (+/- 1.325) |
| +3 min | 32 | $0.194 | $-0.534 | 43.8 | 25.0 | -0.727 (+/- 1.224) |
| +5 min | 31 | $1.175 | $0.436 | 51.6 | 22.6 | +0.209 (+/- 1.468) |
| +10 min | 27 | $-1.492 | $-2.219 | 29.6 | 14.8 | -1.679 (+/- 1.815) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

32 trades: avg gross $-1.476, avg net $-2.204, win 28.1%, target 18.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
