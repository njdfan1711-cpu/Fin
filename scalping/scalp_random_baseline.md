# Random-entry baseline

Generated 2026-10-21T15:31:21+00:00. 12 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-1.318 | $-1.961 | 33.3 | 0.0 |
| Random: A_same_symbol_day | $-0.031 (5-95%: -2.644 to 2.869) | $-0.676 | 41.6 | 15.3 |
| Random: B_within_15_min | $2.093 (5-95%: -0.601 to 4.588) | $1.45 | 54.4 | 28.9 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.779
- B_within_15_min: p = 0.988

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
