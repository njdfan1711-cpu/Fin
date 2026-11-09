# Random-entry baseline

Generated 2026-11-09T16:31:23+00:00. 38 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.259 | $-0.471 | 42.1 | 26.3 |
| Random: A_same_symbol_day | $-0.254 (5-95%: -1.971 to 1.53) | $-0.986 | 37.5 | 22.7 |
| Random: B_within_15_min | $1.724 (5-95%: -0.082 to 3.508) | $0.99 | 49.7 | 38.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.32
- B_within_15_min: p = 0.908

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 38 | $0.259 | $-0.471 | 42.1 | 26.3 | - |
| +1 min | 36 | $-1.334 | $-2.047 | 30.6 | 19.4 | -1.607 (+/- 1.307) |
| +2 min | 35 | $-0.722 | $-1.422 | 34.3 | 22.9 | -1.122 (+/- 1.228) |
| +3 min | 35 | $-1.239 | $-1.94 | 25.7 | 20.0 | -1.638 (+/- 1.396) |
| +5 min | 34 | $-0.786 | $-1.494 | 26.5 | 23.5 | -1.131 (+/- 1.324) |
| +10 min | 30 | $-2.966 | $-3.676 | 23.3 | 6.7 | -3.819 (+/- 1.69) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

38 trades: avg gross $-0.347, avg net $-1.076, win 36.8%, target 26.3%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
