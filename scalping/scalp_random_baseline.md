# Random-entry baseline

Generated 2026-11-12T17:31:27+00:00. 31 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.326 | $0.651 | 48.4 | 35.5 |
| Random: A_same_symbol_day | $0.001 (5-95%: -1.984 to 1.937) | $-0.673 | 40.0 | 23.9 |
| Random: B_within_15_min | $1.847 (5-95%: -0.23 to 3.96) | $1.173 | 50.0 | 41.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.141
- B_within_15_min: p = 0.647

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 31 | $1.326 | $0.651 | 48.4 | 35.5 | - |
| +1 min | 31 | $-0.399 | $-1.075 | 38.7 | 25.8 | -1.725 (+/- 1.499) |
| +2 min | 30 | $-0.219 | $-0.878 | 40.0 | 26.7 | -1.728 (+/- 1.519) |
| +3 min | 30 | $-0.72 | $-1.379 | 30.0 | 20.0 | -2.228 (+/- 1.553) |
| +5 min | 28 | $-0.09 | $-0.771 | 32.1 | 25.0 | -1.831 (+/- 1.535) |
| +10 min | 27 | $-2.749 | $-3.434 | 18.5 | 11.1 | -4.775 (+/- 1.796) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

31 trades: avg gross $-2.022, avg net $-2.698, win 25.8%, target 19.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
