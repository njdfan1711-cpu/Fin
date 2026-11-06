# Random-entry baseline

Generated 2026-11-06T17:31:04+00:00. 40 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.596 | $-0.065 | 45.0 | 27.5 |
| Random: A_same_symbol_day | $-0.281 (5-95%: -1.929 to 1.503) | $-0.945 | 37.5 | 22.1 |
| Random: B_within_15_min | $1.976 (5-95%: 0.227 to 3.744) | $1.312 | 51.9 | 39.4 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.183
- B_within_15_min: p = 0.896

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 40 | $0.596 | $-0.065 | 45.0 | 27.5 | - |
| +1 min | 38 | $-0.869 | $-1.51 | 34.2 | 21.1 | -1.496 (+/- 1.234) |
| +2 min | 38 | $-0.349 | $-0.99 | 36.8 | 26.3 | -0.977 (+/- 0.985) |
| +3 min | 38 | $-0.328 | $-0.97 | 31.6 | 26.3 | -0.955 (+/- 1.261) |
| +5 min | 37 | $-0.285 | $-0.933 | 32.4 | 27.0 | -0.869 (+/- 1.122) |
| +10 min | 32 | $-2.69 | $-3.336 | 25.0 | 9.4 | -3.707 (+/- 1.657) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

40 trades: avg gross $-0.384, avg net $-1.045, win 35.0%, target 27.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
