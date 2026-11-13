# Random-entry baseline

Generated 2026-11-13T15:31:12+00:00. 27 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.803 | $0.136 | 48.1 | 33.3 |
| Random: A_same_symbol_day | $-0.105 (5-95%: -2.142 to 1.874) | $-0.771 | 38.8 | 23.0 |
| Random: B_within_15_min | $1.926 (5-95%: -0.234 to 4.091) | $1.26 | 50.5 | 42.6 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.234
- B_within_15_min: p = 0.799

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 27 | $0.803 | $0.136 | 48.1 | 33.3 | - |
| +1 min | 27 | $-0.744 | $-1.411 | 33.3 | 25.9 | -1.547 (+/- 1.659) |
| +2 min | 26 | $-1.141 | $-1.788 | 30.8 | 23.1 | -2.134 (+/- 1.734) |
| +3 min | 26 | $-0.799 | $-1.446 | 30.8 | 23.1 | -1.792 (+/- 1.836) |
| +5 min | 24 | $-0.291 | $-0.962 | 33.3 | 25.0 | -1.513 (+/- 2.002) |
| +10 min | 23 | $-1.76 | $-2.436 | 26.1 | 17.4 | -3.293 (+/- 1.941) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

27 trades: avg gross $-0.907, avg net $-1.574, win 33.3%, target 25.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
