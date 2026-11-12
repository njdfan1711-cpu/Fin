# Random-entry baseline

Generated 2026-11-12T20:30:55+00:00. 26 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $3.322 | $2.595 | 61.5 | 46.2 |
| Random: A_same_symbol_day | $-0.245 (5-95%: -2.263 to 1.758) | $-0.972 | 38.4 | 22.0 |
| Random: B_within_15_min | $1.922 (5-95%: -0.199 to 4.133) | $1.195 | 51.0 | 40.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.005
- B_within_15_min: p = 0.147

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 26 | $3.322 | $2.595 | 61.5 | 46.2 | - |
| +1 min | 26 | $1.179 | $0.451 | 46.2 | 30.8 | -2.144 (+/- 1.323) |
| +2 min | 25 | $2.97 | $2.275 | 60.0 | 40.0 | -0.076 (+/- 1.399) |
| +3 min | 25 | $2.006 | $1.31 | 52.0 | 32.0 | -1.04 (+/- 1.646) |
| +5 min | 23 | $0.883 | $0.202 | 43.5 | 26.1 | -2.727 (+/- 1.73) |
| +10 min | 23 | $-2.646 | $-3.327 | 21.7 | 8.7 | -6.256 (+/- 1.805) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

26 trades: avg gross $-2.246, avg net $-2.974, win 26.9%, target 15.4%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
