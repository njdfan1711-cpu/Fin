# Random-entry baseline

Generated 2026-11-03T20:31:42+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.357 | $-0.403 | 42.5 | 22.5 |
| Random: A_same_symbol_day | $0.043 (5-95%: -1.601 to 1.668) | $-0.721 | 40.6 | 20.1 |
| Random: B_within_15_min | $2.811 (5-95%: 1.228 to 4.46) | $2.047 | 58.7 | 41.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.369
- B_within_15_min: p = 0.996

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $0.357 | $-0.403 | 42.5 | 22.5 | - |
| +1 min | 39 | $1.81 | $1.067 | 51.3 | 33.3 | +1.39 (+/- 1.107) |
| +2 min | 39 | $1.769 | $1.025 | 51.3 | 30.8 | +1.349 (+/- 1.035) |
| +3 min | 39 | $-0.223 | $-0.967 | 41.0 | 20.5 | -0.643 (+/- 1.012) |
| +5 min | 38 | $0.541 | $-0.211 | 47.4 | 23.7 | +0.098 (+/- 1.198) |
| +10 min | 32 | $-1.677 | $-2.404 | 28.1 | 12.5 | -1.594 (+/- 1.631) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $-0.181, avg net $-0.94, win 40.0%, target 20.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
