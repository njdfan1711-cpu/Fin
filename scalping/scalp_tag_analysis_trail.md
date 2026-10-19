# Scalp signal analysis (trail exits)

_193 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 193 | 34% (28-41) | -0.60 | -2.41 | -465 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -49 | -0.64 | 117 | -416 | -3.56 | +49 |
| skip first 30 min | 56 | -61 | -1.08 | 137 | -404 | -2.95 | +61 |
| skip when SPY is down on the day | 70 | -179 | -2.55 | 123 | -286 | -2.33 | +179 |
| skip when SPY is below its VWAP | 64 | -181 | -2.83 | 129 | -284 | -2.20 | +181 |
| skip when SPY fell over the last 15 min | 55 | -162 | -2.94 | 138 | -303 | -2.20 | +162 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 34 | -171 | -5.03 | 159 | -294 | -1.85 | +171 |
| skip stock not beating SPY over 15 min | 16 | -53 | -3.32 | 177 | -412 | -2.33 | +53 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -272 | -2.87 | 98 | -193 | -1.97 | +272 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 33% (22-46) | +0.11 | -0.99 | -54 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.49 | -50 |  |
| 60-240 | 57 | 30% (20-43) | -1.45 | -3.05 | -174 |  |
| 240-375 | 40 | 32% (20-48) | -2.46 | -4.81 | -192 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.26 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.18 | -70 |  |
| -0.2 to 0 | 48 | 35% (23-50) | -0.06 | -2.27 | -109 |  |
| 0 to 0.2 | 80 | 28% (19-38) | -1.62 | -2.99 | -239 |  |
| > 0.2 | 43 | 47% (33-61) | +1.08 | -1.10 | -47 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 30% (20-42) | -0.65 | -2.83 | -181 |  |
| above VWAP | 129 | 36% (29-45) | -0.58 | -2.20 | -284 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.142] | 46 | 30% (19-45) | -0.03 | -1.83 | -84 |  |
| (0.142, 0.374] | 47 | 47% (33-61) | -0.89 | -2.85 | -134 |  |
| (0.374, 1.555] | 45 | 27% (16-41) | -1.77 | -4.27 | -192 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 46 | 41% (28-56) | +0.65 | -0.97 | -44 |  |
| (0.165, 0.41] | 45 | 36% (23-50) | -0.95 | -3.33 | -150 |  |
| (0.41, 1.192] | 46 | 28% (17-43) | -2.25 | -4.57 | -210 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 65 | 37% (26-49) | -1.02 | -3.17 | -206 |  |
| (-0.108, 0.364] | 64 | 42% (31-54) | +1.07 | -0.27 | -17 |  |
| (0.364, 2.726] | 64 | 23% (15-35) | -1.85 | -3.78 | -242 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0604] | 65 | 35% (25-48) | -0.81 | -2.40 | -156 |  |
| (0.0604, 0.137] | 64 | 39% (28-51) | -0.42 | -2.08 | -133 |  |
| (0.137, 0.786] | 64 | 28% (19-40) | -0.57 | -2.75 | -176 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.231] | 65 | 42% (30-54) | +0.02 | -1.07 | -69 |  |
| (0.231, 0.439] | 64 | 31% (21-43) | -1.46 | -4.33 | -277 |  |
| (0.439, 4.92] | 64 | 30% (20-42) | -0.39 | -1.85 | -118 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.626] | 65 | 40% (29-52) | -0.69 | -2.50 | -162 |  |
| (2.626, 5.086] | 64 | 34% (24-47) | -0.15 | -2.40 | -153 |  |
| (5.086, 18.76] | 64 | 28% (19-40) | -0.97 | -2.33 | -149 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 65 | 38% (28-51) | -0.17 | -0.86 | -56 |  |
| (0.0985, 0.162] | 64 | 36% (25-48) | -1.46 | -2.73 | -175 |  |
| (0.162, 0.395] | 64 | 28% (19-40) | -0.18 | -3.66 | -234 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 97, trail_stop 71, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 65 | 38% | 31% | 31% |
| (0.0985, 0.162] | 64 | 55% | 41% | 5% |
| (0.162, 0.395] | 64 | 58% | 39% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
