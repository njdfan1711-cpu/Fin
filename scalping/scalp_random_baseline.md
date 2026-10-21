# Random-entry baseline

Generated 2026-10-21T16:31:21+00:00. 12 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.318 | $-1.961 | 33.3 | 0.0 |
| Random: A_same_symbol_day | $-0.121 (5-95%: -2.665 to 2.597) | $-0.766 | 41.0 | 14.2 |
| Random: B_within_15_min | $2.097 (5-95%: -0.6 to 4.573) | $1.454 | 54.5 | 28.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.762
- B_within_15_min: p = 0.988

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
