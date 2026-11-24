# Scalp signal analysis (trail exits)

_319 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 319 | 44% (39-49) | -0.60 | -1.98 | -631 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 259 | -659 | -2.55 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 315 | -614 | -1.95 | +17 |
| skip when SPY is down on the day | 147 | -306 | -2.08 | 172 | -325 | -1.89 | +306 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 179 | -304 | -1.70 | +327 |
| skip when SPY fell over the last 15 min | 107 | -202 | -1.89 | 212 | -429 | -2.02 | +202 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -220 | -2.78 | 240 | -411 | -1.71 | +220 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 270 | -517 | -1.92 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -249 | -3.61 | 250 | -382 | -1.53 | +249 |
| skip volume spikes above 5x average | 69 | -230 | -3.34 | 250 | -401 | -1.60 | +230 |
| skip when the stop is inside normal noise (range > stop) | 45 | -55 | -1.23 | 274 | -576 | -2.10 | +55 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.73%) | 50 | -77 | -1.54 | 269 | -554 | -2.06 | +77 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 181 | -212 | -1.17 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 132 | 40% (32-49) | -1.15 | -2.30 | -304 |  |
| 240-375 | 88 | 41% (31-51) | -1.52 | -3.13 | -276 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 56 | 41% (29-54) | -1.29 | -3.30 | -185 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 102 | 48% (39-58) | +0.20 | -1.24 | -126 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 179 | 46% (39-53) | -0.38 | -1.70 | -304 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 107 | 41% (32-51) | -0.37 | -1.46 | -156 |  |
| (0.123, 0.374] | 106 | 52% (42-61) | -0.25 | -1.65 | -174 |  |
| (0.374, 5.591] | 106 | 39% (30-48) | -1.17 | -2.83 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 105 | 51% (42-61) | +0.36 | -0.74 | -78 |  |
| (0.135, 0.453] | 105 | 41% (32-51) | -0.94 | -2.61 | -274 |  |
| (0.453, 4.846] | 105 | 40% (31-50) | -1.10 | -2.50 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.581] | 107 | 49% (39-58) | -0.33 | -1.69 | -181 |  |
| (-0.581, 0.319] | 106 | 44% (35-54) | -0.09 | -1.31 | -138 |  |
| (0.319, 9.926] | 106 | 39% (30-48) | -1.38 | -2.94 | -311 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 107 | 43% (34-52) | -1.01 | -2.25 | -240 |  |
| (0.0561, 0.127] | 106 | 49% (40-58) | +0.28 | -1.00 | -106 |  |
| (0.127, 0.924] | 106 | 40% (31-49) | -1.06 | -2.68 | -284 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.223] | 107 | 45% (36-54) | +0.01 | -0.98 | -105 |  |
| (0.223, 0.351] | 106 | 46% (37-56) | -0.64 | -2.31 | -244 |  |
| (0.351, 2.663] | 106 | 41% (32-50) | -1.17 | -2.66 | -282 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 107 | 44% (35-53) | -0.49 | -1.85 | -198 |  |
| (2.381, 3.637] | 106 | 52% (42-61) | +0.72 | -0.69 | -73 |  |
| (3.637, 19.488] | 106 | 36% (27-45) | -2.03 | -3.40 | -360 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 107 | 47% (38-56) | +0.04 | -0.71 | -76 |  |
| (0.105, 0.167] | 106 | 44% (35-54) | -0.98 | -2.14 | -227 |  |
| (0.167, 0.76] | 106 | 41% (32-50) | -0.86 | -3.10 | -328 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.762] | 65 | 43% (32-55) | -1.28 | -2.07 | -134 |  |
| (-0.762, 0.658] | 64 | 53% (41-65) | +0.04 | -0.51 | -33 |  |
| (0.658, 14.989] | 64 | 58% (46-69) | -0.17 | -0.91 | -58 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.553] | 67 | 48% (36-60) | -0.64 | -1.25 | -84 |  |
| (0.553, 0.887] | 66 | 56% (44-67) | -0.39 | -1.10 | -73 | ▲ |
| (0.887, 3.799] | 67 | 49% (38-61) | -0.64 | -1.42 | -95 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.934] | 67 | 51% (39-62) | -1.05 | -1.62 | -109 |  |
| (0.934, 1.68] | 66 | 48% (37-60) | -0.64 | -1.33 | -88 |  |
| (1.68, 9.058] | 67 | 54% (42-65) | +0.01 | -0.83 | -55 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 67 | 43% (32-55) | -0.99 | -1.57 | -105 |  |
| (0.409, 0.638] | 66 | 62% (50-73) | +0.01 | -0.70 | -46 | ▲ |
| (0.638, 4.001] | 67 | 48% (36-60) | -0.67 | -1.50 | -101 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 137, stop 137, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 107 | 35% | 33% | 28% |
| (0.105, 0.167] | 106 | 47% | 46% | 3% |
| (0.167, 0.76] | 106 | 47% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
