# Scalp signal analysis (trail exits)

_336 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 336 | 44% (39-49) | -0.68 | -2.03 | -681 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 274 | -705 | -2.57 | -24 |
| skip first 30 min | 5 | -22 | -4.48 | 331 | -658 | -1.99 | +22 |
| skip when SPY is down on the day | 156 | -324 | -2.08 | 180 | -357 | -1.98 | +324 |
| skip when SPY is below its VWAP | 143 | -339 | -2.37 | 193 | -342 | -1.77 | +339 |
| skip when SPY fell over the last 15 min | 111 | -221 | -1.99 | 225 | -460 | -2.04 | +221 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 83 | -219 | -2.64 | 253 | -462 | -1.82 | +219 |
| skip stock not beating SPY over 15 min | 53 | -124 | -2.34 | 283 | -557 | -1.97 | +124 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 266 | -430 | -1.62 | +251 |
| skip volume spikes above 5x average | 72 | -249 | -3.46 | 264 | -431 | -1.63 | +249 |
| skip when the stop is inside normal noise (range > stop) | 51 | -79 | -1.54 | 285 | -602 | -2.11 | +79 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 54 | -84 | -1.56 | 282 | -597 | -2.12 | +84 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -430 | -3.05 | 195 | -250 | -1.28 | +430 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 45% (31-60) | -0.73 | -2.30 | -97 |  |
| 60-240 | 143 | 41% (34-49) | -1.19 | -2.31 | -330 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 47% (37-57) | -0.47 | -1.45 | -142 |  |
| -0.2 to 0 | 58 | 43% (31-56) | -1.17 | -3.14 | -182 |  |
| 0 to 0.2 | 73 | 34% (24-46) | -1.72 | -3.00 | -219 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (34-49) | -0.92 | -2.37 | -339 |  |
| above VWAP | 193 | 46% (39-53) | -0.50 | -1.77 | -342 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.116] | 112 | 41% (32-50) | -0.60 | -1.59 | -178 |  |
| (0.116, 0.372] | 112 | 52% (43-61) | -0.23 | -1.64 | -184 |  |
| (0.372, 5.591] | 112 | 38% (30-48) | -1.21 | -2.84 | -318 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 111 | 51% (42-60) | +0.32 | -0.76 | -84 |  |
| (0.135, 0.446] | 110 | 41% (32-50) | -1.06 | -2.67 | -293 |  |
| (0.446, 4.846] | 110 | 40% (31-49) | -1.17 | -2.55 | -281 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.577] | 112 | 47% (38-57) | -0.51 | -1.83 | -205 |  |
| (-0.577, 0.287] | 112 | 44% (35-53) | -0.27 | -1.47 | -164 |  |
| (0.287, 9.926] | 112 | 40% (32-49) | -1.27 | -2.78 | -311 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 112 | 41% (32-50) | -1.18 | -2.38 | -267 |  |
| (0.0559, 0.125] | 112 | 48% (39-57) | +0.02 | -1.22 | -137 |  |
| (0.125, 0.924] | 112 | 42% (33-51) | -0.89 | -2.47 | -277 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.22] | 112 | 46% (37-55) | -0.02 | -1.01 | -113 |  |
| (0.22, 0.351] | 112 | 46% (37-56) | -0.67 | -2.27 | -254 |  |
| (0.351, 2.663] | 112 | 39% (31-49) | -1.35 | -2.80 | -314 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 112 | 43% (34-52) | -0.63 | -1.95 | -219 |  |
| (2.39, 3.618] | 112 | 54% (44-63) | +0.74 | -0.63 | -71 | ▲ |
| (3.618, 19.488] | 112 | 35% (27-44) | -2.15 | -3.49 | -391 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 112 | 47% (38-57) | +0.02 | -0.71 | -79 |  |
| (0.104, 0.167] | 112 | 44% (35-53) | -1.08 | -2.23 | -250 |  |
| (0.167, 0.76] | 112 | 40% (32-49) | -0.98 | -3.14 | -352 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 70 | 46% (35-57) | -1.17 | -1.96 | -137 |  |
| (-0.912, 0.658] | 71 | 51% (39-62) | -0.22 | -0.79 | -56 |  |
| (0.658, 14.989] | 69 | 55% (43-66) | -0.46 | -1.19 | -82 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.545] | 73 | 48% (37-59) | -0.70 | -1.31 | -95 |  |
| (0.545, 0.888] | 72 | 56% (44-66) | -0.49 | -1.19 | -86 | ▲ |
| (0.888, 3.799] | 72 | 47% (36-59) | -0.88 | -1.67 | -121 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.925] | 73 | 51% (39-62) | -1.09 | -1.68 | -123 |  |
| (0.925, 1.669] | 72 | 47% (36-59) | -0.79 | -1.47 | -106 |  |
| (1.669, 9.058] | 72 | 53% (41-64) | -0.17 | -1.02 | -73 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 73 | 44% (33-55) | -1.00 | -1.57 | -115 |  |
| (0.408, 0.624] | 72 | 61% (50-72) | -0.15 | -0.86 | -62 | ▲ |
| (0.624, 4.001] | 72 | 46% (35-57) | -0.91 | -1.74 | -125 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: stop 145, trail_stop 144, time_stop 37, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 112 | 34% | 34% | 28% |
| (0.104, 0.167] | 112 | 47% | 46% | 4% |
| (0.167, 0.76] | 112 | 48% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
