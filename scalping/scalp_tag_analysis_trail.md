# Scalp signal analysis (trail exits)

_320 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 320 | 44% (39-50) | -0.59 | -1.97 | -630 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 260 | -658 | -2.53 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 316 | -613 | -1.94 | +17 |
| skip when SPY is down on the day | 147 | -306 | -2.08 | 173 | -324 | -1.87 | +306 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 180 | -303 | -1.68 | +327 |
| skip when SPY fell over the last 15 min | 107 | -202 | -1.89 | 213 | -428 | -2.01 | +202 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -220 | -2.78 | 241 | -410 | -1.70 | +220 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 271 | -516 | -1.90 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -249 | -3.61 | 251 | -381 | -1.52 | +249 |
| skip volume spikes above 5x average | 69 | -230 | -3.34 | 251 | -400 | -1.59 | +230 |
| skip when the stop is inside normal noise (range > stop) | 45 | -55 | -1.23 | 275 | -575 | -2.09 | +55 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 50 | -77 | -1.54 | 270 | -553 | -2.05 | +77 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 182 | -211 | -1.16 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 133 | 41% (33-49) | -1.13 | -2.28 | -303 |  |
| 240-375 | 88 | 41% (31-51) | -1.52 | -3.13 | -276 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 56 | 41% (29-54) | -1.29 | -3.30 | -185 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 103 | 49% (39-58) | +0.21 | -1.22 | -125 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 180 | 46% (39-53) | -0.37 | -1.68 | -303 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 107 | 42% (33-52) | -0.30 | -1.39 | -148 |  |
| (0.123, 0.374] | 107 | 51% (42-61) | -0.31 | -1.69 | -181 |  |
| (0.374, 5.591] | 106 | 39% (30-48) | -1.17 | -2.83 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 106 | 52% (42-61) | +0.40 | -0.69 | -74 |  |
| (0.135, 0.451] | 105 | 41% (32-51) | -0.97 | -2.64 | -277 |  |
| (0.451, 4.846] | 105 | 40% (31-50) | -1.10 | -2.50 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.579] | 107 | 49% (39-58) | -0.33 | -1.69 | -181 |  |
| (-0.579, 0.332] | 106 | 44% (35-54) | -0.09 | -1.31 | -138 |  |
| (0.332, 9.926] | 107 | 39% (31-49) | -1.35 | -2.90 | -310 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0564] | 107 | 43% (34-52) | -1.01 | -2.25 | -240 |  |
| (0.0564, 0.127] | 107 | 50% (40-59) | +0.29 | -0.98 | -105 |  |
| (0.127, 0.924] | 106 | 40% (31-49) | -1.06 | -2.68 | -284 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.223] | 107 | 45% (36-54) | +0.01 | -0.98 | -105 |  |
| (0.223, 0.351] | 106 | 47% (38-57) | -0.57 | -2.23 | -237 |  |
| (0.351, 2.663] | 107 | 40% (31-50) | -1.21 | -2.70 | -289 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 107 | 44% (35-53) | -0.49 | -1.85 | -198 |  |
| (2.384, 3.635] | 106 | 52% (42-61) | +0.72 | -0.70 | -74 |  |
| (3.635, 19.488] | 107 | 36% (28-46) | -1.99 | -3.35 | -358 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 107 | 48% (38-57) | +0.11 | -0.62 | -66 |  |
| (0.104, 0.167] | 106 | 44% (35-54) | -0.98 | -2.16 | -229 |  |
| (0.167, 0.76] | 107 | 40% (31-50) | -0.91 | -3.13 | -335 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.748] | 65 | 43% (32-55) | -1.28 | -2.07 | -134 |  |
| (-0.748, 0.658] | 64 | 53% (41-65) | +0.03 | -0.52 | -34 |  |
| (0.658, 14.989] | 65 | 58% (46-70) | -0.14 | -0.87 | -56 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 67 | 49% (38-61) | -0.53 | -1.14 | -76 |  |
| (0.55, 0.885] | 67 | 55% (43-67) | -0.47 | -1.18 | -79 |  |
| (0.885, 3.799] | 67 | 49% (38-61) | -0.64 | -1.42 | -95 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.943] | 67 | 51% (39-62) | -1.05 | -1.62 | -109 |  |
| (0.943, 1.674] | 67 | 49% (38-61) | -0.60 | -1.29 | -87 |  |
| (1.674, 9.058] | 67 | 54% (42-65) | +0.01 | -0.83 | -55 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 67 | 45% (33-57) | -0.89 | -1.45 | -97 |  |
| (0.409, 0.633] | 67 | 61% (49-72) | -0.08 | -0.79 | -53 | ▲ |
| (0.633, 4.001] | 67 | 48% (36-60) | -0.67 | -1.50 | -101 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 138, stop 137, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 107 | 34% | 34% | 28% |
| (0.104, 0.167] | 106 | 47% | 46% | 3% |
| (0.167, 0.76] | 107 | 48% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
