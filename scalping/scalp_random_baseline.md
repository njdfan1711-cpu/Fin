# Random-entry baseline

Generated 2026-11-25T16:31:09+00:00. 27 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.637 | $0.01 | 44.4 | 33.3 |
| Random: A_same_symbol_day | $-0.191 (5-95%: -2.283 to 1.909) | $-0.816 | 37.4 | 26.1 |
| Random: B_within_15_min | $1.895 (5-95%: -0.184 to 4.045) | $1.268 | 51.3 | 39.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.27
- B_within_15_min: p = 0.822

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 27 | $0.637 | $0.01 | 44.4 | 33.3 | - |
| +1 min | 27 | $-2.334 | $-2.961 | 25.9 | 11.1 | -2.971 (+/- 1.167) |
| +2 min | 26 | $-1.979 | $-2.614 | 26.9 | 11.5 | -2.863 (+/- 1.146) |
| +3 min | 26 | $-1.648 | $-2.283 | 34.6 | 11.5 | -2.532 (+/- 1.148) |
| +5 min | 21 | $-2.035 | $-2.627 | 28.6 | 14.3 | -1.126 (+/- 1.831) |
| +10 min | 20 | $-0.524 | $-1.103 | 35.0 | 20.0 | +0.135 (+/- 2.217) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

26 trades: avg gross $1.122, avg net $0.488, win 46.2%, target 34.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
