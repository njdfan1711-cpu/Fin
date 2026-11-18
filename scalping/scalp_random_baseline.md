# Random-entry baseline

Generated 2026-11-18T19:30:59+00:00. 42 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.519 | $-2.146 | 31.0 | 14.3 |
| Random: A_same_symbol_day | $-0.095 (5-95%: -1.772 to 1.562) | $-0.721 | 38.6 | 23.5 |
| Random: B_within_15_min | $1.866 (5-95%: 0.271 to 3.662) | $1.24 | 51.4 | 38.1 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.921
- B_within_15_min: p = 1.0

## Delay sweep (long, same exits): enter N minutes AFTER the signal

| Entry | Trades | Avg gross | Avg net | Win % | Target % | Gross vs signal minute (+/- std err) |
|---|---|---|---|---|---|---|
| +0 min | 42 | $-1.519 | $-2.146 | 31.0 | 14.3 | - |
| +1 min | 42 | $-2.538 | $-3.166 | 23.8 | 7.1 | -1.02 (+/- 0.765) |
| +2 min | 42 | $-2.088 | $-2.716 | 28.6 | 9.5 | -0.57 (+/- 0.795) |
| +3 min | 41 | $-1.476 | $-2.08 | 31.7 | 12.2 | +0.334 (+/- 1.057) |
| +5 min | 34 | $-0.797 | $-1.415 | 32.4 | 17.6 | +2.369 (+/- 1.316) |
| +10 min | 33 | $0.199 | $-0.421 | 39.4 | 24.2 | +3.28 (+/- 1.368) |

## Mirror test (SHORT at the signal minute; diagnostic only, the bot is long-only)

42 trades: avg gross $1.845, avg net $1.218, win 52.4%, target 38.1%.

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
