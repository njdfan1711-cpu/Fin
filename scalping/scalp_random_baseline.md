# Random-entry baseline

Generated 2026-11-23T14:31:49+00:00. 21 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.78 | $-2.54 | 28.6 | 19.0 |
| Random: A_same_symbol_day | $-0.276 (5-95%: -2.645 to 2.168) | $-1.033 | 37.2 | 22.4 |
| Random: B_within_15_min | $1.724 (5-95%: -0.754 to 4.069) | $0.966 | 50.4 | 34.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.847
- B_within_15_min: p = 0.994

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 21 | $-1.78 | $-2.54 | 28.6 | 19.0 | - |
| +1 min | 21 | $-3.308 | $-4.069 | 19.0 | 4.8 | -1.528 (+/- 1.001) |
| +2 min | 21 | $-3.17 | $-3.931 | 19.0 | 4.8 | -1.39 (+/- 0.859) |
| +3 min | 21 | $-2.413 | $-3.173 | 23.8 | 9.5 | -0.633 (+/- 1.129) |
| +5 min | 16 | $-2.317 | $-3.06 | 18.8 | 12.5 | +2.648 (+/- 1.415) |
| +10 min | 15 | $-0.363 | $-1.076 | 33.3 | 20.0 | +4.537 (+/- 1.956) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

21 trades: avg gross $3.704, avg net $2.944, win 66.7%, target 42.9%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
