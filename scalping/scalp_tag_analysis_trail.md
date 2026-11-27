# Scalp signal analysis (trail exits)

_338 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 338 | 44% (39-49) | -0.64 | -1.98 | -670 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 276 | -695 | -2.52 | -24 |
| skip first 30 min | 5 | -22 | -4.48 | 333 | -648 | -1.95 | +22 |
| skip when SPY is down on the day | 156 | -324 | -2.08 | 182 | -347 | -1.90 | +324 |
| skip when SPY is below its VWAP | 143 | -339 | -2.37 | 195 | -332 | -1.70 | +339 |
| skip when SPY fell over the last 15 min | 113 | -211 | -1.87 | 225 | -460 | -2.04 | +211 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 83 | -219 | -2.64 | 255 | -451 | -1.77 | +219 |
| skip stock not beating SPY over 15 min | 53 | -124 | -2.34 | 285 | -546 | -1.92 | +124 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 268 | -420 | -1.57 | +251 |
| skip volume spikes above 5x average | 72 | -249 | -3.46 | 266 | -421 | -1.58 | +249 |
| skip when the stop is inside normal noise (range > stop) | 51 | -79 | -1.54 | 287 | -592 | -2.06 | +79 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 55 | -82 | -1.49 | 283 | -589 | -2.08 | +82 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -430 | -3.05 | 197 | -240 | -1.22 | +430 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 45% (31-60) | -0.73 | -2.30 | -97 |  |
| 60-240 | 145 | 42% (34-50) | -1.09 | -2.21 | -320 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 47% (37-57) | -0.47 | -1.45 | -142 |  |
| -0.2 to 0 | 58 | 43% (31-56) | -1.17 | -3.14 | -182 |  |
| 0 to 0.2 | 75 | 36% (26-47) | -1.52 | -2.78 | -209 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (34-49) | -0.92 | -2.37 | -339 |  |
| above VWAP | 195 | 46% (39-53) | -0.44 | -1.70 | -332 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.115] | 113 | 42% (33-51) | -0.53 | -1.52 | -172 |  |
| (0.115, 0.37] | 112 | 53% (43-62) | -0.15 | -1.56 | -175 |  |
| (0.37, 5.591] | 113 | 38% (30-47) | -1.24 | -2.87 | -324 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.13] | 111 | 51% (42-60) | +0.35 | -0.72 | -80 |  |
| (0.13, 0.445] | 111 | 42% (34-52) | -0.92 | -2.53 | -280 |  |
| (0.445, 4.846] | 111 | 40% (31-49) | -1.22 | -2.59 | -287 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.574] | 113 | 47% (38-56) | -0.55 | -1.94 | -220 |  |
| (-0.574, 0.31] | 112 | 45% (36-54) | -0.20 | -1.33 | -149 |  |
| (0.31, 9.926] | 113 | 41% (32-50) | -1.17 | -2.67 | -302 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 113 | 42% (33-51) | -1.13 | -2.33 | -264 |  |
| (0.0559, 0.125] | 112 | 48% (39-57) | +0.02 | -1.22 | -137 |  |
| (0.125, 0.924] | 113 | 42% (34-52) | -0.81 | -2.39 | -270 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 113 | 45% (36-54) | -0.08 | -1.06 | -119 |  |
| (0.222, 0.351] | 112 | 47% (38-57) | -0.58 | -2.18 | -244 |  |
| (0.351, 2.663] | 113 | 40% (31-49) | -1.27 | -2.72 | -307 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 113 | 43% (35-53) | -0.59 | -1.91 | -216 |  |
| (2.389, 3.611] | 112 | 54% (44-63) | +0.80 | -0.58 | -65 | ▲ |
| (3.611, 19.488] | 113 | 35% (27-45) | -2.13 | -3.45 | -390 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 113 | 47% (38-56) | -0.03 | -0.76 | -85 |  |
| (0.104, 0.167] | 112 | 46% (37-55) | -0.88 | -2.03 | -227 |  |
| (0.167, 0.76] | 113 | 40% (31-49) | -1.02 | -3.17 | -358 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.899] | 71 | 45% (34-57) | -1.24 | -2.02 | -144 |  |
| (-0.899, 0.658] | 70 | 51% (40-63) | -0.14 | -0.71 | -50 |  |
| (0.658, 14.989] | 71 | 56% (45-67) | -0.29 | -1.01 | -72 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 73 | 48% (37-59) | -0.70 | -1.31 | -95 |  |
| (0.546, 0.885] | 73 | 56% (45-67) | -0.36 | -1.06 | -77 | ▲ |
| (0.885, 3.799] | 73 | 48% (37-59) | -0.83 | -1.63 | -119 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 73 | 51% (39-62) | -1.00 | -1.60 | -117 |  |
| (0.909, 1.652] | 73 | 49% (38-61) | -0.63 | -1.31 | -95 |  |
| (1.652, 9.058] | 73 | 52% (41-63) | -0.25 | -1.09 | -80 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.402] | 73 | 45% (34-57) | -0.86 | -1.43 | -105 |  |
| (0.402, 0.624] | 73 | 62% (50-72) | -0.05 | -0.76 | -56 | ▲ |
| (0.624, 4.001] | 73 | 45% (34-57) | -0.98 | -1.80 | -131 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 146, stop 145, time_stop 37, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 113 | 35% | 34% | 27% |
| (0.104, 0.167] | 112 | 46% | 47% | 4% |
| (0.167, 0.76] | 113 | 49% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
