# Random-entry baseline

Generated 2026-10-28T13:31:09+00:00. 17 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.141 | $-0.894 | 41.2 | 17.6 |
| Random: A_same_symbol_day | $-0.408 (5-95%: -2.804 to 2.255) | $-1.162 | 37.6 | 18.1 |
| Random: B_within_15_min | $1.732 (5-95%: -0.609 to 4.184) | $0.979 | 53.2 | 31.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.42
- B_within_15_min: p = 0.914

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 17 | $-0.141 | $-0.894 | 41.2 | 17.6 | - |
| +1 min | 16 | $2.512 | $1.749 | 56.2 | 37.5 | +2.672 (+/- 1.459) |
| +2 min | 16 | $1.845 | $1.081 | 50.0 | 31.2 | +2.005 (+/- 1.772) |
| +3 min | 16 | $-0.199 | $-0.963 | 37.5 | 18.8 | -0.039 (+/- 1.692) |
| +5 min | 15 | $1.691 | $0.907 | 60.0 | 20.0 | +1.831 (+/- 2.359) |
| +10 min | 14 | $0.75 | $-0.059 | 42.9 | 21.4 | +1.634 (+/- 2.224) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

17 trades: avg gross $-0.441, avg net $-1.194, win 29.4%, target 23.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
