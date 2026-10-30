# Random-entry baseline

Generated 2026-10-30T16:31:28+00:00. 31 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $0.627 | $-0.11 | 45.2 | 25.8 |
| Random: A_same_symbol_day | $0.015 (5-95%: -1.771 to 1.951) | $-0.724 | 40.4 | 20.7 |
| Random: B_within_15_min | $2.709 (5-95%: 0.804 to 4.439) | $1.97 | 58.3 | 42.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.303
- B_within_15_min: p = 0.972

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 31 | $0.627 | $-0.11 | 45.2 | 25.8 | - |
| +1 min | 31 | $4.152 | $3.415 | 64.5 | 48.4 | +3.525 (+/- 1.193) |
| +2 min | 31 | $3.418 | $2.681 | 61.3 | 41.9 | +2.791 (+/- 1.253) |
| +3 min | 31 | $0.158 | $-0.579 | 41.9 | 25.8 | -0.469 (+/- 1.235) |
| +5 min | 30 | $1.405 | $0.657 | 53.3 | 23.3 | +0.742 (+/- 1.414) |
| +10 min | 26 | $-1.434 | $-2.172 | 30.8 | 15.4 | -1.242 (+/- 1.831) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

31 trades: avg gross $-1.339, avg net $-2.076, win 29.0%, target 19.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
