# Random-entry baseline

Generated 2026-11-12T14:31:36+00:00. 22 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $3.34 | $2.566 | 59.1 | 50.0 |
| Random: A_same_symbol_day | $-0.332 (5-95%: -2.522 to 2.174) | $-1.105 | 37.3 | 22.9 |
| Random: B_within_15_min | $1.425 (5-95%: -1.109 to 3.893) | $0.653 | 48.0 | 37.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.008
- B_within_15_min: p = 0.102

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 22 | $3.34 | $2.566 | 59.1 | 50.0 | - |
| +1 min | 22 | $0.392 | $-0.382 | 40.9 | 27.3 | -2.948 (+/- 1.292) |
| +2 min | 21 | $2.457 | $1.719 | 57.1 | 38.1 | -0.555 (+/- 1.446) |
| +3 min | 21 | $1.433 | $0.695 | 47.6 | 28.6 | -1.579 (+/- 1.559) |
| +5 min | 19 | $0.625 | $-0.1 | 42.1 | 26.3 | -3.066 (+/- 1.688) |
| +10 min | 19 | $-2.975 | $-3.699 | 21.1 | 5.3 | -6.666 (+/- 2.132) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

22 trades: avg gross $-2.284, avg net $-3.058, win 27.3%, target 13.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
