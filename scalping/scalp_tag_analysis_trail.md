# Scalp signal analysis (trail exits)

_335 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 335 | 44% (39-49) | -0.66 | -2.01 | -674 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 273 | -698 | -2.56 | -24 |
| skip first 30 min | 5 | -22 | -4.48 | 330 | -652 | -1.98 | +22 |
| skip when SPY is down on the day | 156 | -324 | -2.08 | 179 | -351 | -1.96 | +324 |
| skip when SPY is below its VWAP | 143 | -339 | -2.37 | 192 | -335 | -1.75 | +339 |
| skip when SPY fell over the last 15 min | 111 | -221 | -1.99 | 224 | -453 | -2.02 | +221 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 83 | -219 | -2.64 | 252 | -455 | -1.81 | +219 |
| skip stock not beating SPY over 15 min | 53 | -124 | -2.34 | 282 | -550 | -1.95 | +124 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 265 | -423 | -1.60 | +251 |
| skip volume spikes above 5x average | 72 | -249 | -3.46 | 263 | -425 | -1.62 | +249 |
| skip when the stop is inside normal noise (range > stop) | 51 | -79 | -1.54 | 284 | -596 | -2.10 | +79 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 54 | -84 | -1.56 | 281 | -590 | -2.10 | +84 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -430 | -3.05 | 194 | -244 | -1.26 | +430 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 45% (31-60) | -0.73 | -2.30 | -97 |  |
| 60-240 | 142 | 42% (34-50) | -1.16 | -2.28 | -324 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 47% (37-57) | -0.47 | -1.45 | -142 |  |
| -0.2 to 0 | 58 | 43% (31-56) | -1.17 | -3.14 | -182 |  |
| 0 to 0.2 | 72 | 35% (25-46) | -1.66 | -2.95 | -213 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (34-49) | -0.92 | -2.37 | -339 |  |
| above VWAP | 192 | 46% (39-53) | -0.47 | -1.75 | -335 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.115] | 112 | 41% (32-50) | -0.60 | -1.59 | -178 |  |
| (0.115, 0.37] | 111 | 52% (43-61) | -0.19 | -1.60 | -178 |  |
| (0.37, 5.591] | 112 | 38% (30-48) | -1.20 | -2.84 | -318 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 110 | 51% (42-60) | +0.28 | -0.80 | -88 |  |
| (0.135, 0.446] | 110 | 42% (33-51) | -0.95 | -2.57 | -283 |  |
| (0.446, 4.846] | 110 | 40% (31-49) | -1.17 | -2.55 | -281 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.574] | 112 | 47% (38-57) | -0.51 | -1.90 | -213 |  |
| (-0.574, 0.289] | 111 | 44% (35-53) | -0.22 | -1.35 | -150 |  |
| (0.289, 9.926] | 112 | 40% (32-49) | -1.27 | -2.78 | -311 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 112 | 42% (33-51) | -1.10 | -2.31 | -258 |  |
| (0.056, 0.125] | 111 | 48% (39-57) | -0.00 | -1.25 | -139 |  |
| (0.125, 0.924] | 112 | 42% (33-51) | -0.89 | -2.47 | -277 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 112 | 46% (37-55) | -0.02 | -1.01 | -113 |  |
| (0.222, 0.351] | 111 | 47% (38-56) | -0.62 | -2.23 | -247 |  |
| (0.351, 2.663] | 112 | 39% (31-49) | -1.35 | -2.80 | -314 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.392] | 112 | 44% (35-53) | -0.57 | -1.89 | -212 |  |
| (2.392, 3.625] | 111 | 53% (44-62) | +0.74 | -0.65 | -72 | ▲ |
| (3.625, 19.488] | 112 | 35% (27-44) | -2.15 | -3.49 | -391 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 112 | 47% (38-57) | +0.02 | -0.71 | -79 |  |
| (0.104, 0.167] | 111 | 44% (35-53) | -1.04 | -2.20 | -244 |  |
| (0.167, 0.76] | 112 | 40% (32-49) | -0.98 | -3.14 | -352 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 70 | 46% (35-57) | -1.17 | -1.96 | -137 |  |
| (-0.912, 0.651] | 69 | 51% (39-62) | -0.25 | -0.81 | -56 |  |
| (0.651, 14.989] | 70 | 56% (44-67) | -0.35 | -1.08 | -76 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 72 | 49% (37-60) | -0.62 | -1.24 | -89 |  |
| (0.546, 0.888] | 72 | 56% (44-66) | -0.49 | -1.19 | -86 | ▲ |
| (0.888, 3.799] | 72 | 47% (36-59) | -0.88 | -1.67 | -121 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.923] | 72 | 50% (39-61) | -1.13 | -1.73 | -124 |  |
| (0.923, 1.674] | 72 | 49% (37-60) | -0.68 | -1.36 | -98 |  |
| (1.674, 9.058] | 72 | 53% (41-64) | -0.17 | -1.02 | -73 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 72 | 44% (34-56) | -0.93 | -1.50 | -108 |  |
| (0.409, 0.625] | 72 | 61% (50-72) | -0.15 | -0.86 | -62 | ▲ |
| (0.625, 4.001] | 72 | 46% (35-57) | -0.91 | -1.74 | -125 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 144, stop 144, time_stop 37, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 112 | 34% | 34% | 28% |
| (0.104, 0.167] | 111 | 47% | 46% | 4% |
| (0.167, 0.76] | 112 | 48% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
