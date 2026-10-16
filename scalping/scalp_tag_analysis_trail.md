# Scalp signal analysis (trail exits)

_171 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 171 | 35% (28-42) | -0.47 | -2.33 | -398 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | -1 | -0.01 | 109 | -397 | -3.64 | +1 |
| skip first 30 min | 43 | -14 | -0.34 | 128 | -383 | -2.99 | +14 |
| skip when SPY is down on the day | 62 | -148 | -2.39 | 109 | -250 | -2.29 | +148 |
| skip when SPY is below its VWAP | 57 | -159 | -2.78 | 114 | -239 | -2.10 | +159 |
| skip when SPY fell over the last 15 min | 53 | -149 | -2.81 | 118 | -248 | -2.11 | +149 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 32 | -163 | -5.08 | 139 | -235 | -1.69 | +163 |
| skip stock not beating SPY over 15 min | 15 | -47 | -3.13 | 156 | -351 | -2.25 | +47 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 87 | -260 | -2.99 | 84 | -137 | -1.64 | +260 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 37% (24-52) | +0.63 | -0.34 | -14 |  |
| 15-60 | 18 | 50% (29-71) | +0.36 | -2.45 | -44 |  |
| 60-240 | 52 | 27% (17-40) | -1.55 | -3.21 | -167 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 16 | 31% (14-56) | -1.43 | -3.37 | -54 |  |
| -0.2 to 0 | 46 | 37% (25-51) | +0.20 | -2.05 | -94 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 42 | 45% (31-60) | +1.03 | -1.19 | -50 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 57 | 30% (20-43) | -0.50 | -2.78 | -159 |  |
| above VWAP | 114 | 38% (29-47) | -0.46 | -2.10 | -239 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 43 | 33% (20-47) | +0.37 | -1.54 | -66 |  |
| (0.136, 0.372] | 42 | 43% (29-58) | -1.30 | -3.31 | -139 |  |
| (0.372, 1.555] | 43 | 28% (17-43) | -1.59 | -4.14 | -178 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 43 | 40% (26-54) | +0.70 | -0.95 | -41 |  |
| (0.153, 0.41] | 42 | 36% (23-51) | -0.78 | -3.27 | -137 |  |
| (0.41, 1.192] | 43 | 28% (17-43) | -2.43 | -4.77 | -205 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 57 | 37% (26-50) | -0.75 | -3.17 | -181 |  |
| (-0.1, 0.374] | 57 | 46% (33-58) | +1.05 | -0.10 | -5 |  |
| (0.374, 2.726] | 57 | 23% (14-35) | -1.71 | -3.71 | -212 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0593] | 57 | 39% (27-52) | -1.67 | -3.29 | -188 |  |
| (0.0593, 0.136] | 57 | 39% (27-52) | +0.48 | -1.27 | -72 |  |
| (0.136, 0.786] | 57 | 28% (18-41) | -0.22 | -2.42 | -138 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.226] | 57 | 44% (32-57) | +0.34 | -0.78 | -44 |  |
| (0.226, 0.419] | 57 | 30% (20-43) | -1.66 | -4.34 | -247 |  |
| (0.419, 3.871] | 57 | 32% (21-44) | -0.10 | -1.86 | -106 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.624] | 57 | 39% (27-52) | -0.65 | -2.59 | -148 |  |
| (2.624, 5.006] | 57 | 39% (27-52) | +0.32 | -1.86 | -106 |  |
| (5.006, 18.76] | 57 | 28% (18-41) | -1.08 | -2.52 | -144 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0958] | 57 | 44% (32-57) | +0.39 | -0.28 | -16 |  |
| (0.0958, 0.145] | 58 | 36% (25-49) | -1.28 | -2.58 | -150 |  |
| (0.145, 0.392] | 56 | 25% (16-38) | -0.51 | -4.15 | -232 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 12% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 84, trail_stop 64, time_stop 23

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0958] | 57 | 35% | 33% | 32% |
| (0.0958, 0.145] | 58 | 53% | 41% | 5% |
| (0.145, 0.392] | 56 | 59% | 38% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
