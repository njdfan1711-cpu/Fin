# Random-entry baseline

Generated 2026-10-28T14:31:27+00:00. 18 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.555 | $-0.014 | 50.0 | 16.7 |
| Random: A_same_symbol_day | $-0.08 (5-95%: -2.158 to 2.253) | $-0.651 | 40.8 | 15.5 |
| Random: B_within_15_min | $2.187 (5-95%: -0.388 to 4.709) | $1.618 | 55.4 | 35.8 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.3
- B_within_15_min: p = 0.849

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 18 | $0.555 | $-0.014 | 50.0 | 16.7 | - |
| +1 min | 18 | $2.502 | $1.933 | 61.1 | 33.3 | +1.947 (+/- 1.586) |
| +2 min | 17 | $1.749 | $1.179 | 52.9 | 23.5 | +1.491 (+/- 1.616) |
| +3 min | 17 | $0.634 | $0.063 | 47.1 | 23.5 | +0.376 (+/- 1.229) |
| +5 min | 17 | $2.126 | $1.555 | 64.7 | 29.4 | +1.868 (+/- 1.599) |
| +10 min | 17 | $0.14 | $-0.431 | 41.2 | 17.6 | -0.118 (+/- 1.779) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

18 trades: avg gross $-0.318, avg net $-0.887, win 38.9%, target 22.2%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
