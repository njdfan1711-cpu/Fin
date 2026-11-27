# Scalp signal analysis (fixed exits)

_336 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 336 | 39% (34-44) | -0.07 | -1.42 | -476 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 274 | -476 | -1.74 | -0 |
| skip first 30 min | 5 | -27 | -5.42 | 331 | -449 | -1.36 | +27 |
| skip when SPY is down on the day | 156 | -181 | -1.16 | 180 | -294 | -1.63 | +181 |
| skip when SPY is below its VWAP | 143 | -204 | -1.42 | 193 | -272 | -1.41 | +204 |
| skip when SPY fell over the last 15 min | 110 | -134 | -1.22 | 226 | -341 | -1.51 | +134 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 83 | -170 | -2.05 | 253 | -305 | -1.21 | +170 |
| skip stock not beating SPY over 15 min | 53 | -94 | -1.78 | 283 | -381 | -1.35 | +94 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 266 | -248 | -0.93 | +227 |
| skip volume spikes above 5x average | 72 | -173 | -2.40 | 264 | -303 | -1.15 | +173 |
| skip when the stop is inside normal noise (range > stop) | 51 | -49 | -0.97 | 285 | -426 | -1.50 | +49 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 54 | -56 | -1.04 | 282 | -419 | -1.49 | +56 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -366 | -2.60 | 195 | -110 | -0.56 | +366 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 48% (33-62) | +1.39 | -0.18 | -8 |  |
| 60-240 | 143 | 37% (30-45) | -0.38 | -1.50 | -215 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 39% (30-49) | -0.01 | -0.98 | -96 |  |
| -0.2 to 0 | 58 | 43% (31-56) | +0.50 | -1.46 | -85 |  |
| 0 to 0.2 | 73 | 32% (22-43) | -0.67 | -1.95 | -142 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (33-49) | +0.03 | -1.42 | -204 |  |
| above VWAP | 193 | 38% (31-45) | -0.14 | -1.41 | -272 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.116] | 112 | 37% (28-46) | -0.42 | -1.42 | -159 |  |
| (0.116, 0.372] | 112 | 42% (33-51) | +0.18 | -1.23 | -138 |  |
| (0.372, 5.591] | 112 | 38% (30-48) | +0.04 | -1.60 | -179 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 111 | 47% (38-56) | +0.79 | -0.29 | -33 |  |
| (0.135, 0.446] | 110 | 37% (29-47) | -0.08 | -1.70 | -187 |  |
| (0.446, 4.846] | 110 | 35% (26-44) | -0.70 | -2.08 | -229 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.577] | 112 | 43% (34-52) | +0.29 | -1.03 | -116 |  |
| (-0.577, 0.287] | 112 | 38% (29-47) | +0.07 | -1.12 | -126 |  |
| (0.287, 9.926] | 112 | 37% (28-46) | -0.57 | -2.09 | -234 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 112 | 37% (28-46) | -0.65 | -1.86 | -208 |  |
| (0.0559, 0.125] | 112 | 44% (35-53) | +0.39 | -0.85 | -96 |  |
| (0.125, 0.924] | 112 | 37% (28-46) | +0.05 | -1.54 | -172 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.22] | 112 | 43% (34-52) | +0.29 | -0.69 | -77 |  |
| (0.22, 0.351] | 112 | 38% (30-48) | -0.16 | -1.76 | -197 |  |
| (0.351, 2.663] | 112 | 36% (27-45) | -0.35 | -1.80 | -202 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 112 | 35% (27-44) | -0.39 | -1.72 | -193 |  |
| (2.39, 3.618] | 112 | 48% (39-57) | +0.98 | -0.39 | -44 | ▲ |
| (3.618, 19.488] | 112 | 34% (26-43) | -0.80 | -2.13 | -239 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 112 | 45% (36-54) | +0.29 | -0.44 | -49 |  |
| (0.104, 0.167] | 112 | 35% (27-44) | -0.56 | -1.71 | -191 |  |
| (0.167, 0.76] | 112 | 38% (29-47) | +0.06 | -2.10 | -236 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 70 | 31% (22-43) | -1.06 | -1.85 | -129 |  |
| (-0.912, 0.658] | 71 | 45% (34-57) | +0.59 | +0.02 | +2 |  |
| (0.658, 14.989] | 69 | 43% (32-55) | +0.44 | -0.28 | -20 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.545] | 73 | 42% (32-54) | -0.02 | -0.63 | -46 |  |
| (0.545, 0.888] | 72 | 42% (31-53) | -0.01 | -0.72 | -52 |  |
| (0.888, 3.799] | 72 | 35% (25-46) | -0.23 | -1.03 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.925] | 73 | 41% (31-53) | -0.23 | -0.82 | -60 |  |
| (0.925, 1.669] | 72 | 42% (31-53) | +0.27 | -0.41 | -30 |  |
| (1.669, 9.058] | 72 | 36% (26-48) | -0.30 | -1.14 | -82 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 73 | 36% (26-47) | -0.59 | -1.16 | -85 |  |
| (0.408, 0.624] | 72 | 47% (36-59) | +0.62 | -0.10 | -7 |  |
| (0.624, 4.001] | 72 | 36% (26-48) | -0.28 | -1.11 | -80 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 172, target 84, time_stop 64, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 112 | 38% | 18% | 38% |
| (0.104, 0.167] | 112 | 57% | 24% | 12% |
| (0.167, 0.76] | 112 | 58% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
