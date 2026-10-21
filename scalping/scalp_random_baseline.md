# Random-entry baseline

Generated 2026-10-21T12:47:17+00:00. 24 real signals vs 1000 random draws (same symbols and days, same exits and sizing). Symbols: AAPL, AMD, AMZN, AVGO, BAC, GOOGL, HOOD, INTC, JPM, META, MSFT, MU, NFLX, NVDA, PLTR, QQQ, SMCI, SPY, T, TSLA, UBER, XOM.

| | Avg gross / trade | Avg net / trade | Win % | Target hit % |
|---|---|---|---|---|
| Real signals | $-0.409 | $-1.197 | 37.5 | 20.8 |
| Random: A_same_symbol_day | $-0.435 (5-95%: -2.332 to 1.616) | $-1.221 | 37.4 | 15.1 |
| Random: B_within_15_min | $2.034 (5-95%: 0.122 to 3.975) | $1.248 | 54.2 | 31.2 |

p-value = share of random draws whose average gross was at least as good as the real signals' (small = the signal beat random timing):
- A_same_symbol_day: p = 0.477
- B_within_15_min: p = 0.979

Read it as: if the real average gross sits inside the random 5-95% range, the entry signal is adding nothing beyond the exit rules. Small sample: this can show 'no edge' far more easily than it can prove one.
