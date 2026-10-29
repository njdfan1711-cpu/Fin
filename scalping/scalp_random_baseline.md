# Random-entry baseline

Generated 2026-10-29T17:31:20+00:00. 29 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.029 | $-0.732 | 41.4 | 24.1 |
| Random: A_same_symbol_day | $-0.033 (5-95%: -1.908 to 1.969) | $-0.798 | 40.2 | 21.0 |
| Random: B_within_15_min | $2.558 (5-95%: 0.663 to 4.407) | $1.794 | 56.7 | 41.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.461
- B_within_15_min: p = 0.991

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 29 | $0.029 | $-0.732 | 41.4 | 24.1 | - |
| +1 min | 29 | $3.75 | $2.988 | 62.1 | 48.3 | +3.72 (+/- 1.269) |
| +2 min | 29 | $2.965 | $2.203 | 55.2 | 44.8 | +2.936 (+/- 1.364) |
| +3 min | 29 | $-0.087 | $-0.849 | 37.9 | 27.6 | -0.117 (+/- 1.285) |
| +5 min | 28 | $1.276 | $0.502 | 50.0 | 25.0 | +1.229 (+/- 1.466) |
| +10 min | 26 | $-0.78 | $-1.553 | 34.6 | 19.2 | -0.041 (+/- 1.875) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

29 trades: avg gross $-1.045, avg net $-1.807, win 31.0%, target 20.7%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
