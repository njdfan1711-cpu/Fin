# Scalp signal analysis (trail exits)

_202 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 202 | 33% (27-40) | -0.70 | -2.58 | -521 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 79 | -75 | -0.95 | 123 | -446 | -3.63 | +75 |
| skip first 30 min | 59 | -86 | -1.46 | 143 | -435 | -3.04 | +86 |
| skip when SPY is down on the day | 73 | -206 | -2.82 | 129 | -316 | -2.45 | +206 |
| skip when SPY is below its VWAP | 67 | -190 | -2.83 | 135 | -332 | -2.46 | +190 |
| skip when SPY fell over the last 15 min | 57 | -167 | -2.92 | 145 | -355 | -2.45 | +167 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 36 | -181 | -5.02 | 166 | -341 | -2.05 | +181 |
| skip stock not beating SPY over 15 min | 19 | -59 | -3.11 | 183 | -462 | -2.53 | +59 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -370 | -3.30 | 90 | -151 | -1.68 | +370 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 58 | 31% (21-44) | -0.20 | -1.38 | -80 |  |
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 62 | 29% (19-41) | -1.36 | -3.13 | -194 |  |
| 240-375 | 41 | 32% (20-47) | -2.53 | -4.92 | -202 |  |
| 375-390 | 21 | 38% (21-59) | +2.69 | +0.23 | +5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 51 | 33% (22-47) | -0.41 | -2.64 | -135 |  |
| 0 to 0.2 | 82 | 28% (19-39) | -1.53 | -2.99 | -245 |  |
| > 0.2 | 47 | 43% (30-57) | +0.74 | -1.50 | -71 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 67 | 30% (20-42) | -0.60 | -2.83 | -190 |  |
| above VWAP | 135 | 35% (27-43) | -0.75 | -2.46 | -332 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 48 | 31% (20-45) | +0.13 | -1.63 | -78 |  |
| (0.135, 0.371] | 48 | 44% (31-58) | -1.14 | -3.29 | -158 |  |
| (0.371, 1.555] | 48 | 27% (17-41) | -1.71 | -4.27 | -205 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.152] | 48 | 35% (23-50) | +0.17 | -1.64 | -79 |  |
| (0.152, 0.406] | 47 | 38% (26-53) | -0.71 | -3.05 | -143 |  |
| (0.406, 1.192] | 48 | 29% (18-43) | -2.06 | -4.44 | -213 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 68 | 35% (25-47) | -1.07 | -3.25 | -221 |  |
| (-0.108, 0.374] | 67 | 43% (32-55) | +1.04 | -0.33 | -22 |  |
| (0.374, 2.726] | 67 | 21% (13-32) | -2.08 | -4.15 | -278 | ▼ |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0572] | 68 | 34% (24-46) | -1.71 | -3.38 | -230 |  |
| (0.0572, 0.136] | 67 | 39% (28-51) | +0.43 | -1.36 | -91 |  |
| (0.136, 0.786] | 67 | 27% (18-39) | -0.81 | -2.99 | -200 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.229] | 68 | 38% (28-50) | -0.33 | -1.60 | -109 |  |
| (0.229, 0.436] | 67 | 33% (23-45) | -1.36 | -4.02 | -269 |  |
| (0.436, 4.92] | 67 | 28% (19-40) | -0.42 | -2.14 | -144 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 68 | 38% (28-50) | -0.70 | -2.59 | -176 |  |
| (2.623, 4.845] | 67 | 34% (24-46) | -0.22 | -2.51 | -168 |  |
| (4.845, 18.76] | 67 | 27% (18-39) | -1.19 | -2.65 | -177 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 68 | 37% (26-49) | -0.37 | -1.12 | -76 |  |
| (0.0985, 0.162] | 67 | 36% (25-48) | -1.30 | -2.69 | -180 |  |
| (0.162, 0.395] | 67 | 27% (18-39) | -0.44 | -3.96 | -265 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 103, trail_stop 73, time_stop 26

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 68 | 40% | 29% | 31% |
| (0.0985, 0.162] | 67 | 54% | 42% | 4% |
| (0.162, 0.395] | 67 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
