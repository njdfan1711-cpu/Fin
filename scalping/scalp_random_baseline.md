# Random-entry baseline

Generated 2026-11-05T15:31:23+00:00. 42 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.143 | $-0.57 | 40.5 | 23.8 |
| Random: A_same_symbol_day | $0.026 (5-95%: -1.556 to 1.734) | $-0.69 | 40.3 | 20.9 |
| Random: B_within_15_min | $2.245 (5-95%: 0.642 to 3.859) | $1.529 | 54.2 | 38.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.433
- B_within_15_min: p = 0.984

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 42 | $0.143 | $-0.57 | 40.5 | 23.8 | - |
| +1 min | 40 | $0.496 | $-0.199 | 42.5 | 27.5 | +0.346 (+/- 1.084) |
| +2 min | 40 | $0.704 | $0.009 | 45.0 | 30.0 | +0.554 (+/- 0.647) |
| +3 min | 40 | $0.139 | $-0.558 | 35.0 | 27.5 | -0.011 (+/- 1.042) |
| +5 min | 40 | $0.06 | $-0.638 | 35.0 | 27.5 | -0.09 (+/- 0.721) |
| +10 min | 35 | $-3.176 | $-3.881 | 20.0 | 5.7 | -3.661 (+/- 1.4) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

42 trades: avg gross $-0.36, avg net $-1.072, win 38.1%, target 23.8%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
