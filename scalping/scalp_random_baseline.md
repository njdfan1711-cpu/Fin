# Random-entry baseline

Generated 2026-10-29T15:31:11+00:00. 31 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.536 | $-0.139 | 45.2 | 25.8 |
| Random: A_same_symbol_day | $0.099 (5-95%: -1.696 to 2.029) | $-0.579 | 41.3 | 19.0 |
| Random: B_within_15_min | $2.288 (5-95%: 0.43 to 4.179) | $1.611 | 54.5 | 39.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.338
- B_within_15_min: p = 0.933

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 31 | $0.536 | $-0.139 | 45.2 | 25.8 | - |
| +1 min | 31 | $2.801 | $2.125 | 58.1 | 41.9 | +2.265 (+/- 1.368) |
| +2 min | 30 | $1.828 | $1.148 | 53.3 | 33.3 | +1.461 (+/- 1.061) |
| +3 min | 30 | $1.292 | $0.613 | 46.7 | 33.3 | +0.925 (+/- 1.078) |
| +5 min | 30 | $1.52 | $0.839 | 53.3 | 33.3 | +1.153 (+/- 0.911) |
| +10 min | 30 | $-1.361 | $-2.043 | 30.0 | 16.7 | -1.728 (+/- 1.534) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

31 trades: avg gross $-0.948, avg net $-1.624, win 35.5%, target 19.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
