# Random-entry baseline

Generated 2026-10-26T18:31:10+00:00. 18 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.942 | $0.234 | 44.4 | 33.3 |
| Random: A_same_symbol_day | $-0.449 (5-95%: -2.772 to 1.931) | $-1.157 | 36.8 | 19.8 |
| Random: B_within_15_min | $1.695 (5-95%: -0.631 to 4.045) | $0.987 | 52.9 | 32.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.167
- B_within_15_min: p = 0.704

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 18 | $0.942 | $0.234 | 44.4 | 33.3 | - |
| +1 min | 17 | $2.503 | $1.788 | 58.8 | 41.2 | +1.516 (+/- 1.026) |
| +2 min | 17 | $2.196 | $1.481 | 52.9 | 41.2 | +1.209 (+/- 1.903) |
| +3 min | 17 | $0.587 | $-0.129 | 47.1 | 23.5 | -0.401 (+/- 1.456) |
| +5 min | 17 | $1.246 | $0.53 | 52.9 | 23.5 | +0.259 (+/- 1.995) |
| +10 min | 16 | $-1.037 | $-1.77 | 31.2 | 12.5 | -1.443 (+/- 2.696) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

18 trades: avg gross $-1.405, avg net $-2.113, win 27.8%, target 16.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
