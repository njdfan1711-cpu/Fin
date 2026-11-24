# Scalp signal analysis (trail exits)

_321 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 321 | 44% (39-49) | -0.60 | -1.97 | -632 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 261 | -660 | -2.53 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 317 | -615 | -1.94 | +17 |
| skip when SPY is down on the day | 147 | -306 | -2.08 | 174 | -326 | -1.88 | +306 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 181 | -305 | -1.69 | +327 |
| skip when SPY fell over the last 15 min | 107 | -202 | -1.89 | 214 | -430 | -2.01 | +202 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -220 | -2.78 | 242 | -412 | -1.70 | +220 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 272 | -518 | -1.90 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 251 | -381 | -1.52 | +251 |
| skip volume spikes above 5x average | 69 | -230 | -3.34 | 252 | -402 | -1.59 | +230 |
| skip when the stop is inside normal noise (range > stop) | 45 | -55 | -1.23 | 276 | -577 | -2.09 | +55 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 51 | -73 | -1.43 | 270 | -559 | -2.07 | +73 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 183 | -213 | -1.16 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 133 | 41% (33-49) | -1.13 | -2.28 | -303 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 56 | 41% (29-54) | -1.29 | -3.30 | -185 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 104 | 48% (39-58) | +0.19 | -1.23 | -127 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 181 | 46% (39-53) | -0.38 | -1.69 | -305 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 107 | 42% (33-52) | -0.30 | -1.39 | -148 |  |
| (0.123, 0.374] | 108 | 51% (42-60) | -0.32 | -1.69 | -183 |  |
| (0.374, 5.591] | 106 | 39% (30-48) | -1.17 | -2.83 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.134] | 106 | 51% (42-60) | +0.34 | -0.75 | -80 |  |
| (0.134, 0.449] | 105 | 42% (33-51) | -0.86 | -2.54 | -266 |  |
| (0.449, 4.846] | 106 | 40% (31-49) | -1.15 | -2.54 | -269 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.578] | 107 | 49% (39-58) | -0.33 | -1.69 | -181 |  |
| (-0.578, 0.339] | 107 | 45% (36-54) | -0.07 | -1.28 | -137 |  |
| (0.339, 9.926] | 107 | 38% (30-48) | -1.38 | -2.93 | -314 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 107 | 43% (34-52) | -0.97 | -2.21 | -236 |  |
| (0.0561, 0.127] | 108 | 49% (40-58) | +0.23 | -1.03 | -111 |  |
| (0.127, 0.924] | 106 | 40% (31-49) | -1.06 | -2.68 | -284 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.224] | 107 | 45% (36-54) | +0.01 | -0.98 | -105 |  |
| (0.224, 0.351] | 107 | 47% (38-56) | -0.58 | -2.23 | -239 |  |
| (0.351, 2.663] | 107 | 40% (31-50) | -1.21 | -2.70 | -289 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 107 | 44% (35-53) | -0.45 | -1.81 | -193 |  |
| (2.38, 3.634] | 107 | 51% (42-61) | +0.65 | -0.75 | -80 |  |
| (3.634, 19.488] | 107 | 36% (28-46) | -1.99 | -3.35 | -358 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 107 | 48% (38-57) | +0.15 | -0.58 | -63 |  |
| (0.104, 0.167] | 107 | 44% (35-53) | -1.02 | -2.19 | -235 |  |
| (0.167, 0.76] | 107 | 40% (31-50) | -0.91 | -3.13 | -335 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.773] | 65 | 43% (32-55) | -1.26 | -2.05 | -133 |  |
| (-0.773, 0.658] | 65 | 52% (40-64) | -0.02 | -0.57 | -37 |  |
| (0.658, 14.989] | 65 | 58% (46-70) | -0.14 | -0.87 | -56 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.545] | 68 | 49% (37-60) | -0.54 | -1.16 | -79 |  |
| (0.545, 0.884] | 67 | 55% (43-67) | -0.47 | -1.18 | -79 |  |
| (0.884, 3.799] | 67 | 49% (38-61) | -0.64 | -1.42 | -95 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 69 | 51% (39-62) | -1.00 | -1.56 | -108 |  |
| (0.952, 1.669] | 66 | 48% (37-60) | -0.66 | -1.36 | -90 |  |
| (1.669, 9.058] | 67 | 54% (42-65) | +0.01 | -0.83 | -55 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 68 | 44% (33-56) | -0.90 | -1.46 | -99 |  |
| (0.408, 0.628] | 67 | 61% (49-72) | -0.08 | -0.79 | -53 | ▲ |
| (0.628, 4.001] | 67 | 48% (36-60) | -0.67 | -1.50 | -101 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 138, stop 137, time_stop 36, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 107 | 33% | 34% | 29% |
| (0.104, 0.167] | 107 | 48% | 46% | 3% |
| (0.167, 0.76] | 107 | 48% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
