# Scalp signal analysis (trail exits)

_174 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 174 | 36% (29-43) | -0.46 | -2.31 | -401 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | -1 | -0.01 | 112 | -401 | -3.58 | +1 |
| skip first 30 min | 43 | -14 | -0.34 | 131 | -387 | -2.95 | +14 |
| skip when SPY is down on the day | 65 | -152 | -2.34 | 109 | -250 | -2.29 | +152 |
| skip when SPY is below its VWAP | 59 | -154 | -2.61 | 115 | -248 | -2.15 | +154 |
| skip when SPY fell over the last 15 min | 53 | -149 | -2.81 | 121 | -252 | -2.08 | +149 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 33 | -169 | -5.13 | 141 | -232 | -1.65 | +169 |
| skip stock not beating SPY over 15 min | 15 | -47 | -3.13 | 159 | -354 | -2.23 | +47 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 89 | -267 | -3.00 | 85 | -134 | -1.58 | +267 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 37% (24-52) | +0.63 | -0.34 | -14 |  |
| 15-60 | 18 | 50% (29-71) | +0.36 | -2.45 | -44 |  |
| 60-240 | 55 | 29% (19-42) | -1.45 | -3.10 | -171 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 18 | 39% (20-61) | -0.90 | -2.74 | -49 |  |
| -0.2 to 0 | 47 | 36% (24-50) | +0.07 | -2.18 | -103 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 42 | 45% (31-60) | +1.03 | -1.19 | -50 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 32% (22-45) | -0.37 | -2.61 | -154 |  |
| above VWAP | 115 | 37% (29-47) | -0.50 | -2.15 | -248 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.139] | 44 | 32% (20-47) | +0.23 | -1.64 | -72 |  |
| (0.139, 0.369] | 43 | 47% (33-61) | -0.99 | -2.93 | -126 |  |
| (0.369, 1.555] | 44 | 27% (16-42) | -1.69 | -4.30 | -189 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.157] | 44 | 41% (28-56) | +0.77 | -0.89 | -39 |  |
| (0.157, 0.41] | 43 | 35% (22-50) | -0.94 | -3.39 | -146 |  |
| (0.41, 1.192] | 44 | 30% (18-44) | -2.28 | -4.59 | -202 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.104] | 58 | 38% (27-51) | -0.72 | -3.11 | -180 |  |
| (-0.104, 0.374] | 58 | 47% (34-59) | +1.13 | -0.02 | -1 |  |
| (0.374, 2.726] | 58 | 22% (14-35) | -1.78 | -3.79 | -220 | ▼ |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 58 | 40% (28-53) | -0.47 | -2.09 | -121 |  |
| (0.0605, 0.136] | 58 | 40% (28-53) | -0.58 | -2.31 | -134 |  |
| (0.136, 0.786] | 58 | 28% (18-40) | -0.32 | -2.52 | -146 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.229] | 58 | 43% (31-56) | +0.29 | -0.82 | -47 |  |
| (0.229, 0.419] | 58 | 31% (21-44) | -1.62 | -4.30 | -249 |  |
| (0.419, 3.871] | 58 | 33% (22-46) | -0.05 | -1.81 | -105 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.624] | 58 | 40% (28-53) | -0.57 | -2.49 | -145 |  |
| (2.624, 5.006] | 58 | 38% (27-51) | +0.21 | -1.98 | -115 |  |
| (5.006, 18.76] | 58 | 29% (19-42) | -1.02 | -2.45 | -142 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 58 | 43% (31-56) | +0.28 | -0.39 | -22 |  |
| (0.0964, 0.146] | 58 | 36% (25-49) | -1.28 | -2.61 | -151 |  |
| (0.146, 0.392] | 58 | 28% (18-40) | -0.38 | -3.93 | -228 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 12% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 85, trail_stop 66, time_stop 23

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 58 | 36% | 33% | 31% |
| (0.0964, 0.146] | 58 | 53% | 41% | 5% |
| (0.146, 0.392] | 58 | 57% | 40% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
