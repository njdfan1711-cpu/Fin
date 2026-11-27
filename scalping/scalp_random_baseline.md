# Random-entry baseline

Generated 2026-11-27T15:31:27+00:00. 19 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $2.082 | $1.507 | 52.6 | 42.1 |
| Random: A_same_symbol_day | $-0.026 (5-95%: -2.356 to 2.416) | $-0.6 | 39.3 | 24.8 |
| Random: B_within_15_min | $2.019 (5-95%: -0.168 to 4.338) | $1.445 | 52.8 | 39.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.08
- B_within_15_min: p = 0.468

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 19 | $2.082 | $1.507 | 52.6 | 42.1 | - |
| +1 min | 19 | $-1.274 | $-1.849 | 31.6 | 21.1 | -3.356 (+/- 1.432) |
| +2 min | 19 | $-1.224 | $-1.799 | 31.6 | 21.1 | -3.306 (+/- 1.45) |
| +3 min | 19 | $-1.013 | $-1.586 | 36.8 | 21.1 | -3.095 (+/- 1.48) |
| +5 min | 18 | $-0.727 | $-1.293 | 38.9 | 22.2 | -2.445 (+/- 1.879) |
| +10 min | 17 | $-0.133 | $-0.681 | 41.2 | 23.5 | -2.299 (+/- 2.139) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

19 trades: avg gross $0.41, avg net $-0.165, win 42.1%, target 31.6%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
