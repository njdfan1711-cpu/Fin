# Random-entry baseline

Generated 2026-11-10T18:30:54+00:00. 31 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $1.598 | $0.925 | 51.6 | 35.5 |
| Random: A_same_symbol_day | $-0.187 (5-95%: -2.127 to 1.737) | $-0.859 | 38.5 | 21.3 |
| Random: B_within_15_min | $1.628 (5-95%: -0.346 to 3.718) | $0.956 | 49.7 | 37.5 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.063
- B_within_15_min: p = 0.514

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 31 | $1.598 | $0.925 | 51.6 | 35.5 | - |
| +1 min | 30 | $-0.94 | $-1.613 | 33.3 | 23.3 | -2.522 (+/- 1.432) |
| +2 min | 29 | $-0.012 | $-0.667 | 37.9 | 27.6 | -1.791 (+/- 1.342) |
| +3 min | 29 | $-0.818 | $-1.473 | 27.6 | 20.7 | -2.597 (+/- 1.399) |
| +5 min | 28 | $-0.496 | $-1.159 | 28.6 | 25.0 | -2.258 (+/- 1.306) |
| +10 min | 27 | $-2.956 | $-3.63 | 22.2 | 7.4 | -4.681 (+/- 1.826) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

31 trades: avg gross $-1.661, avg net $-2.334, win 29.0%, target 16.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
