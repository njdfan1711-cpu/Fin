# Random-entry baseline

Generated 2026-11-24T19:31:24+00:00. 25 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.151 | $0.53 | 48.0 | 36.0 |
| Random: A_same_symbol_day | $-0.23 (5-95%: -2.405 to 1.938) | $-0.849 | 37.1 | 25.0 |
| Random: B_within_15_min | $1.571 (5-95%: -0.624 to 3.835) | $0.951 | 49.2 | 36.3 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.157
- B_within_15_min: p = 0.632

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 25 | $1.151 | $0.53 | 48.0 | 36.0 | - |
| +1 min | 25 | $-2.067 | $-2.688 | 28.0 | 12.0 | -3.217 (+/- 1.248) |
| +2 min | 25 | $-1.845 | $-2.466 | 28.0 | 12.0 | -2.995 (+/- 1.184) |
| +3 min | 25 | $-1.491 | $-2.112 | 36.0 | 12.0 | -2.642 (+/- 1.188) |
| +5 min | 20 | $-2.223 | $-2.796 | 25.0 | 15.0 | -1.558 (+/- 1.81) |
| +10 min | 20 | $-0.225 | $-0.798 | 35.0 | 20.0 | +0.44 (+/- 2.228) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

25 trades: avg gross $1.146, avg net $0.525, win 48.0%, target 32.0%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
