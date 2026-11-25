# Random-entry baseline

Generated 2026-11-25T20:31:12+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.64 | $-1.258 | 35.0 | 22.5 |
| Random: A_same_symbol_day | $-0.191 (5-95%: -1.936 to 1.649) | $-0.807 | 37.5 | 25.6 |
| Random: B_within_15_min | $2.072 (5-95%: 0.396 to 3.655) | $1.455 | 52.8 | 40.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.638
- B_within_15_min: p = 0.999

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $-0.64 | $-1.258 | 35.0 | 22.5 | - |
| +1 min | 40 | $-1.855 | $-2.473 | 27.5 | 10.0 | -1.215 (+/- 0.66) |
| +2 min | 40 | $-1.894 | $-2.512 | 27.5 | 10.0 | -1.254 (+/- 0.624) |
| +3 min | 39 | $-1.578 | $-2.171 | 33.3 | 10.3 | -0.655 (+/- 0.958) |
| +5 min | 33 | $0.056 | $-0.526 | 42.4 | 24.2 | +2.155 (+/- 1.255) |
| +10 min | 32 | $0.929 | $0.343 | 46.9 | 28.1 | +2.92 (+/- 1.447) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $1.173, avg net $0.555, win 47.5%, target 35.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
