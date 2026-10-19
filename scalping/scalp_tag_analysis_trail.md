# Scalp signal analysis (trail exits)

_192 tagged trades, 13 trading days (2026-10-01 to 2026-10-19). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 192 | 34% (28-41) | -0.62 | -2.44 | -468 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 76 | -49 | -0.64 | 116 | -419 | -3.61 | +49 |
| skip first 30 min | 56 | -61 | -1.08 | 136 | -407 | -2.99 | +61 |
| skip when SPY is down on the day | 70 | -179 | -2.55 | 122 | -289 | -2.37 | +179 |
| skip when SPY is below its VWAP | 64 | -181 | -2.83 | 128 | -287 | -2.24 | +181 |
| skip when SPY fell over the last 15 min | 55 | -162 | -2.94 | 137 | -306 | -2.23 | +162 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 34 | -171 | -5.03 | 158 | -297 | -1.88 | +171 |
| skip stock not beating SPY over 15 min | 16 | -53 | -3.32 | 176 | -415 | -2.36 | +53 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -272 | -2.87 | 97 | -195 | -2.01 | +272 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 55 | 33% (22-46) | +0.11 | -0.99 | -54 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.49 | -50 |  |
| 60-240 | 56 | 29% (18-41) | -1.53 | -3.15 | -177 |  |
| 240-375 | 40 | 32% (20-48) | -2.46 | -4.81 | -192 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.26 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.18 | -70 |  |
| -0.2 to 0 | 48 | 35% (23-50) | -0.06 | -2.27 | -109 |  |
| 0 to 0.2 | 80 | 28% (19-38) | -1.62 | -2.99 | -239 |  |
| > 0.2 | 42 | 45% (31-60) | +1.03 | -1.19 | -50 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 30% (20-42) | -0.65 | -2.83 | -181 |  |
| above VWAP | 128 | 36% (28-45) | -0.61 | -2.24 | -287 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.139] | 46 | 30% (19-45) | -0.03 | -1.83 | -84 |  |
| (0.139, 0.374] | 46 | 46% (32-60) | -0.98 | -2.97 | -137 |  |
| (0.374, 1.555] | 45 | 27% (16-41) | -1.77 | -4.27 | -192 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.165] | 46 | 41% (28-56) | +0.65 | -0.97 | -44 |  |
| (0.165, 0.412] | 45 | 33% (21-48) | -1.16 | -3.63 | -164 |  |
| (0.412, 1.192] | 45 | 29% (18-43) | -2.17 | -4.42 | -199 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 64 | 36% (25-48) | -1.09 | -3.26 | -208 |  |
| (-0.108, 0.367] | 64 | 42% (31-54) | +1.07 | -0.27 | -17 |  |
| (0.367, 2.726] | 64 | 23% (15-35) | -1.85 | -3.78 | -242 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0593] | 64 | 34% (24-47) | -1.89 | -3.47 | -222 |  |
| (0.0593, 0.136] | 64 | 41% (29-53) | +0.73 | -0.94 | -60 |  |
| (0.136, 0.786] | 64 | 27% (17-38) | -0.71 | -2.89 | -185 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.231] | 64 | 42% (31-54) | +0.12 | -0.99 | -63 |  |
| (0.231, 0.439] | 64 | 30% (20-42) | -1.60 | -4.47 | -286 |  |
| (0.439, 4.92] | 64 | 30% (20-42) | -0.39 | -1.85 | -118 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.627] | 64 | 39% (28-51) | -0.75 | -2.58 | -165 |  |
| (2.627, 5.099] | 64 | 34% (24-47) | -0.15 | -2.40 | -153 |  |
| (5.099, 18.76] | 64 | 28% (19-40) | -0.97 | -2.33 | -149 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 64 | 39% (28-51) | -0.08 | -0.74 | -47 |  |
| (0.0985, 0.161] | 64 | 36% (25-48) | -1.46 | -2.73 | -175 |  |
| (0.161, 0.395] | 64 | 27% (17-38) | -0.33 | -3.83 | -245 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 97, trail_stop 70, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 64 | 38% | 31% | 31% |
| (0.0985, 0.161] | 64 | 55% | 41% | 5% |
| (0.161, 0.395] | 64 | 59% | 38% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
