# Scalp signal analysis (trail exits)

_297 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 297 | 42% (36-47) | -0.70 | -2.14 | -636 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 56 | +14 | +0.24 | 241 | -650 | -2.70 | -14 |
| skip first 30 min | 4 | -17 | -4.16 | 293 | -619 | -2.11 | +17 |
| skip when SPY is down on the day | 127 | -306 | -2.41 | 170 | -330 | -1.94 | +306 |
| skip when SPY is below its VWAP | 132 | -351 | -2.66 | 165 | -285 | -1.73 | +351 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 194 | -421 | -2.17 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 73 | -235 | -3.22 | 224 | -401 | -1.79 | +235 |
| skip stock not beating SPY over 15 min | 47 | -108 | -2.29 | 250 | -528 | -2.11 | +108 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -245 | -3.71 | 231 | -391 | -1.69 | +245 |
| skip volume spikes above 5x average | 60 | -219 | -3.65 | 237 | -417 | -1.76 | +219 |
| skip when the stop is inside normal noise (range > stop) | 37 | -77 | -2.09 | 260 | -559 | -2.15 | +77 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 45 | -100 | -2.23 | 252 | -536 | -2.13 | +100 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 135 | -429 | -3.18 | 162 | -207 | -1.28 | +429 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 120 | 38% (30-47) | -1.23 | -2.45 | -294 |  |
| 240-375 | 83 | 39% (29-49) | -1.62 | -3.30 | -274 |  |
| 375-390 | 56 | 50% (37-63) | +1.64 | +0.24 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 76 | 43% (33-55) | -0.54 | -1.61 | -122 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 132 | 38% (30-46) | -1.15 | -2.66 | -351 |  |
| above VWAP | 165 | 45% (37-52) | -0.35 | -1.73 | -285 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 99 | 40% (31-50) | -0.26 | -1.40 | -139 |  |
| (0.129, 0.375] | 99 | 49% (40-59) | -0.39 | -1.86 | -184 |  |
| (0.375, 5.591] | 99 | 35% (27-45) | -1.45 | -3.16 | -313 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.128] | 98 | 49% (39-59) | +0.31 | -0.83 | -81 |  |
| (0.128, 0.446] | 97 | 42% (33-52) | -0.73 | -2.50 | -243 |  |
| (0.446, 4.846] | 98 | 35% (26-45) | -1.56 | -3.02 | -296 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.506] | 99 | 43% (34-53) | -0.69 | -2.23 | -221 |  |
| (-0.506, 0.364] | 99 | 45% (36-55) | +0.09 | -1.08 | -107 |  |
| (0.364, 9.926] | 99 | 36% (28-46) | -1.50 | -3.12 | -308 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 99 | 42% (33-52) | -1.01 | -2.31 | -228 |  |
| (0.0558, 0.129] | 99 | 45% (36-55) | +0.17 | -1.18 | -116 |  |
| (0.129, 0.924] | 99 | 37% (28-47) | -1.26 | -2.94 | -291 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 99 | 45% (36-55) | +0.22 | -0.81 | -80 |  |
| (0.217, 0.346] | 99 | 46% (37-56) | -0.57 | -2.23 | -221 |  |
| (0.346, 2.663] | 99 | 33% (25-43) | -1.75 | -3.39 | -335 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 100 | 41% (32-51) | -0.58 | -1.98 | -198 |  |
| (2.377, 3.61] | 98 | 49% (39-59) | +0.54 | -0.93 | -91 |  |
| (3.61, 19.488] | 99 | 35% (27-45) | -2.05 | -3.50 | -347 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 99 | 47% (38-57) | +0.22 | -0.53 | -53 |  |
| (0.104, 0.166] | 99 | 42% (33-52) | -1.05 | -2.24 | -222 |  |
| (0.166, 0.76] | 99 | 35% (27-45) | -1.27 | -3.65 | -362 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.821] | 57 | 40% (29-53) | -1.38 | -2.20 | -126 |  |
| (-0.821, 0.615] | 57 | 53% (40-65) | +0.03 | -0.53 | -30 |  |
| (0.615, 7.522] | 57 | 53% (40-65) | -0.56 | -1.31 | -75 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.555] | 60 | 48% (36-61) | -0.55 | -1.19 | -71 |  |
| (0.555, 0.843] | 59 | 54% (42-66) | -0.59 | -1.31 | -77 |  |
| (0.843, 3.799] | 59 | 42% (31-55) | -1.02 | -1.84 | -109 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 60 | 47% (35-59) | -1.35 | -1.95 | -117 |  |
| (0.891, 1.624] | 59 | 53% (40-65) | -0.19 | -0.90 | -53 |  |
| (1.624, 9.058] | 59 | 46% (34-58) | -0.62 | -1.47 | -87 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 60 | 45% (33-58) | -0.70 | -1.29 | -77 |  |
| (0.408, 0.618] | 59 | 63% (50-74) | +0.09 | -0.64 | -38 | ▲ |
| (0.618, 4.001] | 59 | 37% (26-50) | -1.56 | -2.41 | -142 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 131, trail_stop 121, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 99 | 32% | 32% | 30% |
| (0.104, 0.166] | 99 | 48% | 44% | 3% |
| (0.166, 0.76] | 99 | 52% | 45% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
