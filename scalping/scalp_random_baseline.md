# Random-entry baseline

Generated 2026-10-21T19:31:23+00:00. 13 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.67 | $-2.296 | 30.8 | 0.0 |
| Random: A_same_symbol_day | $-0.137 (5-95%: -2.723 to 2.408) | $-0.766 | 41.4 | 13.5 |
| Random: B_within_15_min | $2.139 (5-95%: -0.632 to 4.935) | $1.512 | 53.5 | 30.7 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.855
- B_within_15_min: p = 0.989

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
