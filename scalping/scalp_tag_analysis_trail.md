# Scalp signal analysis (trail exits)

_200 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 200 | 34% (27-40) | -0.67 | -2.56 | -512 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 79 | -75 | -0.95 | 121 | -436 | -3.61 | +75 |
| skip first 30 min | 59 | -86 | -1.46 | 141 | -425 | -3.01 | +86 |
| skip when SPY is down on the day | 73 | -206 | -2.82 | 127 | -306 | -2.41 | +206 |
| skip when SPY is below its VWAP | 66 | -187 | -2.83 | 134 | -325 | -2.42 | +187 |
| skip when SPY fell over the last 15 min | 57 | -167 | -2.92 | 143 | -345 | -2.41 | +167 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 35 | -174 | -4.98 | 165 | -337 | -2.04 | +174 |
| skip stock not beating SPY over 15 min | 18 | -56 | -3.12 | 182 | -455 | -2.50 | +56 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -363 | -3.27 | 89 | -148 | -1.67 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 58 | 31% (21-44) | -0.20 | -1.38 | -80 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 61 | 30% (20-42) | -1.34 | -3.13 | -191 |  |
| 240-375 | 40 | 32% (20-48) | -2.46 | -4.87 | -195 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.23 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 51 | 33% (22-47) | -0.41 | -2.64 | -135 |  |
| 0 to 0.2 | 82 | 28% (19-39) | -1.53 | -2.99 | -245 |  |
| > 0.2 | 45 | 44% (31-59) | +0.95 | -1.35 | -61 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 30% (21-42) | -0.57 | -2.83 | -187 |  |
| above VWAP | 134 | 35% (28-43) | -0.72 | -2.42 | -325 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 48 | 31% (20-45) | +0.06 | -1.85 | -89 |  |
| (0.136, 0.374] | 48 | 46% (33-60) | -0.82 | -2.85 | -137 |  |
| (0.374, 1.555] | 46 | 26% (16-40) | -1.86 | -4.47 | -206 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 47 | 38% (26-53) | +0.48 | -1.33 | -63 |  |
| (0.153, 0.408] | 47 | 38% (26-53) | -0.80 | -3.16 | -149 |  |
| (0.408, 1.192] | 47 | 28% (17-42) | -2.15 | -4.55 | -214 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 67 | 36% (25-48) | -1.04 | -3.25 | -218 |  |
| (-0.108, 0.374] | 66 | 44% (33-56) | +1.15 | -0.22 | -14 |  |
| (0.374, 2.726] | 67 | 21% (13-32) | -2.09 | -4.17 | -279 | ▼ |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 67 | 36% (25-48) | -0.60 | -2.30 | -154 |  |
| (0.0605, 0.136] | 66 | 38% (27-50) | -0.59 | -2.38 | -157 |  |
| (0.136, 0.786] | 67 | 27% (18-39) | -0.81 | -2.99 | -200 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.23] | 67 | 40% (29-52) | -0.09 | -1.39 | -93 |  |
| (0.23, 0.436] | 66 | 32% (22-44) | -1.51 | -4.17 | -275 |  |
| (0.436, 4.92] | 67 | 28% (19-40) | -0.42 | -2.14 | -144 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.625] | 67 | 39% (28-51) | -0.68 | -2.61 | -175 |  |
| (2.625, 4.926] | 66 | 35% (24-47) | -0.13 | -2.42 | -160 |  |
| (4.926, 18.76] | 67 | 27% (18-39) | -1.19 | -2.65 | -177 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 67 | 39% (28-51) | -0.21 | -0.95 | -64 |  |
| (0.0987, 0.163] | 66 | 35% (24-47) | -1.36 | -2.77 | -183 |  |
| (0.163, 0.395] | 67 | 27% (18-39) | -0.44 | -3.96 | -265 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 14% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 102, trail_stop 73, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 67 | 39% | 31% | 30% |
| (0.0987, 0.163] | 66 | 55% | 41% | 5% |
| (0.163, 0.395] | 67 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
