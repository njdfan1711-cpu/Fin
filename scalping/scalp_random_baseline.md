# Random-entry baseline

Generated 2026-10-26T19:31:22+00:00. 17 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.858 | $-1.319 | 35.3 | 11.8 |
| Random: A_same_symbol_day | $-0.536 (5-95%: -2.552 to 1.738) | $-0.999 | 38.4 | 11.9 |
| Random: B_within_15_min | $1.783 (5-95%: -0.597 to 4.189) | $1.321 | 53.0 | 29.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.575
- B_within_15_min: p = 0.959

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 17 | $-0.858 | $-1.319 | 35.3 | 11.8 | - |
| +1 min | 16 | $1.594 | $1.13 | 56.2 | 25.0 | +2.427 (+/- 1.714) |
| +2 min | 15 | $1.634 | $1.176 | 46.7 | 26.7 | +2.896 (+/- 2.017) |
| +3 min | 14 | $-0.002 | $-0.461 | 42.9 | 14.3 | +0.924 (+/- 0.822) |
| +5 min | 13 | $0.813 | $0.354 | 53.8 | 23.1 | +1.35 (+/- 1.689) |
| +10 min | 13 | $0.573 | $0.113 | 46.2 | 15.4 | +1.11 (+/- 2.155) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

17 trades: avg gross $0.453, avg net $-0.008, win 47.1%, target 23.5%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
