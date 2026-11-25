# Scalp signal analysis (trail exits)

_325 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 325 | 44% (39-49) | -0.61 | -1.97 | -641 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 263 | -665 | -2.53 | -24 |
| skip first 30 min | 4 | -17 | -4.16 | 321 | -624 | -1.94 | +17 |
| skip when SPY is down on the day | 148 | -304 | -2.05 | 177 | -337 | -1.90 | +304 |
| skip when SPY is below its VWAP | 140 | -327 | -2.33 | 185 | -314 | -1.70 | +327 |
| skip when SPY fell over the last 15 min | 108 | -208 | -1.93 | 217 | -432 | -1.99 | +208 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 80 | -218 | -2.73 | 245 | -423 | -1.72 | +218 |
| skip stock not beating SPY over 15 min | 51 | -118 | -2.31 | 274 | -523 | -1.91 | +118 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 255 | -390 | -1.53 | +251 |
| skip volume spikes above 5x average | 70 | -236 | -3.38 | 255 | -404 | -1.59 | +236 |
| skip when the stop is inside normal noise (range > stop) | 47 | -59 | -1.26 | 278 | -581 | -2.09 | +59 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 52 | -79 | -1.52 | 273 | -561 | -2.06 | +79 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 187 | -222 | -1.18 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 48% (33-63) | -0.54 | -2.15 | -86 |  |
| 60-240 | 134 | 41% (33-50) | -1.10 | -2.25 | -301 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 47% (37-57) | -0.34 | -1.33 | -121 |  |
| -0.2 to 0 | 57 | 42% (30-55) | -1.23 | -3.21 | -183 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | -0.87 | -2.33 | -327 |  |
| above VWAP | 185 | 46% (39-53) | -0.41 | -1.70 | -314 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.12] | 109 | 42% (33-52) | -0.46 | -1.46 | -159 |  |
| (0.12, 0.37] | 108 | 51% (42-60) | -0.25 | -1.68 | -181 |  |
| (0.37, 5.591] | 108 | 39% (30-48) | -1.12 | -2.78 | -300 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.139] | 107 | 51% (42-61) | +0.38 | -0.71 | -76 |  |
| (0.139, 0.448] | 107 | 41% (32-51) | -0.98 | -2.63 | -281 |  |
| (0.448, 4.846] | 107 | 40% (31-50) | -1.11 | -2.50 | -267 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.581] | 109 | 49% (39-58) | -0.36 | -1.70 | -185 |  |
| (-0.581, 0.319] | 108 | 44% (35-54) | -0.12 | -1.32 | -143 |  |
| (0.319, 9.926] | 108 | 39% (30-48) | -1.35 | -2.89 | -313 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 109 | 43% (34-52) | -0.99 | -2.21 | -241 |  |
| (0.056, 0.126] | 108 | 48% (39-57) | +0.17 | -1.10 | -118 |  |
| (0.126, 0.924] | 108 | 41% (32-50) | -1.00 | -2.61 | -282 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.225] | 109 | 45% (36-54) | -0.03 | -1.01 | -110 |  |
| (0.225, 0.35] | 108 | 47% (38-57) | -0.54 | -2.18 | -236 |  |
| (0.35, 2.663] | 108 | 40% (31-49) | -1.26 | -2.73 | -295 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 109 | 44% (35-53) | -0.48 | -1.83 | -199 |  |
| (2.389, 3.632] | 108 | 52% (43-61) | +0.68 | -0.71 | -77 |  |
| (3.632, 19.488] | 108 | 36% (28-46) | -2.02 | -3.37 | -364 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 109 | 47% (38-56) | +0.04 | -0.69 | -75 |  |
| (0.104, 0.167] | 108 | 44% (35-54) | -0.99 | -2.16 | -233 |  |
| (0.167, 0.76] | 108 | 41% (32-50) | -0.87 | -3.08 | -332 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.864] | 67 | 43% (32-55) | -1.26 | -2.04 | -137 |  |
| (-0.864, 0.658] | 67 | 52% (40-64) | -0.08 | -0.63 | -42 |  |
| (0.658, 14.989] | 65 | 58% (46-70) | -0.14 | -0.87 | -56 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 69 | 48% (36-59) | -0.62 | -1.24 | -85 |  |
| (0.546, 0.887] | 68 | 56% (44-67) | -0.43 | -1.13 | -77 | ▲ |
| (0.887, 3.799] | 69 | 49% (38-61) | -0.67 | -1.44 | -100 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.954] | 69 | 51% (39-62) | -1.00 | -1.56 | -108 |  |
| (0.954, 1.68] | 68 | 49% (37-60) | -0.69 | -1.39 | -94 |  |
| (1.68, 9.058] | 69 | 54% (42-65) | -0.04 | -0.86 | -60 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 69 | 43% (32-55) | -0.97 | -1.54 | -106 |  |
| (0.409, 0.627] | 68 | 63% (51-74) | +0.08 | -0.63 | -43 | ▲ |
| (0.627, 4.001] | 69 | 46% (35-58) | -0.82 | -1.64 | -113 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 140, stop 139, time_stop 36, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 109 | 34% | 33% | 28% |
| (0.104, 0.167] | 108 | 47% | 46% | 3% |
| (0.167, 0.76] | 108 | 47% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
