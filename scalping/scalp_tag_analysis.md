# Scalp signal analysis (fixed exits)

_335 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 335 | 39% (34-44) | -0.05 | -1.40 | -469 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 273 | -470 | -1.72 | -0 |
| skip first 30 min | 5 | -27 | -5.42 | 330 | -442 | -1.34 | +27 |
| skip when SPY is down on the day | 156 | -181 | -1.16 | 179 | -288 | -1.61 | +181 |
| skip when SPY is below its VWAP | 143 | -204 | -1.42 | 192 | -266 | -1.38 | +204 |
| skip when SPY fell over the last 15 min | 110 | -134 | -1.22 | 225 | -335 | -1.49 | +134 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 83 | -170 | -2.05 | 252 | -299 | -1.19 | +170 |
| skip stock not beating SPY over 15 min | 53 | -94 | -1.78 | 282 | -375 | -1.33 | +94 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 265 | -242 | -0.91 | +227 |
| skip volume spikes above 5x average | 72 | -173 | -2.40 | 263 | -297 | -1.13 | +173 |
| skip when the stop is inside normal noise (range > stop) | 51 | -49 | -0.97 | 284 | -420 | -1.48 | +49 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 54 | -56 | -1.04 | 281 | -413 | -1.47 | +56 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -366 | -2.60 | 194 | -103 | -0.53 | +366 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 48% (33-62) | +1.39 | -0.18 | -8 |  |
| 60-240 | 142 | 37% (30-46) | -0.34 | -1.47 | -209 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 39% (30-49) | -0.01 | -0.98 | -96 |  |
| -0.2 to 0 | 58 | 43% (31-56) | +0.50 | -1.46 | -85 |  |
| 0 to 0.2 | 72 | 32% (22-43) | -0.60 | -1.89 | -136 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (33-49) | +0.03 | -1.42 | -204 |  |
| above VWAP | 192 | 38% (31-45) | -0.11 | -1.38 | -266 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.115] | 112 | 37% (28-46) | -0.42 | -1.42 | -159 |  |
| (0.115, 0.37] | 111 | 42% (34-52) | +0.23 | -1.19 | -132 |  |
| (0.37, 5.591] | 112 | 38% (30-48) | +0.04 | -1.59 | -178 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 110 | 46% (37-56) | +0.74 | -0.33 | -37 |  |
| (0.135, 0.446] | 110 | 38% (30-48) | +0.02 | -1.60 | -176 |  |
| (0.446, 4.846] | 110 | 35% (26-44) | -0.70 | -2.08 | -229 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.574] | 112 | 43% (34-52) | +0.29 | -1.11 | -124 |  |
| (-0.574, 0.289] | 111 | 38% (29-47) | +0.13 | -1.00 | -111 |  |
| (0.289, 9.926] | 112 | 37% (28-46) | -0.57 | -2.09 | -234 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 112 | 38% (29-47) | -0.57 | -1.78 | -199 |  |
| (0.056, 0.125] | 111 | 43% (34-53) | +0.37 | -0.88 | -98 |  |
| (0.125, 0.924] | 112 | 37% (28-46) | +0.05 | -1.54 | -172 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 112 | 43% (34-52) | +0.29 | -0.69 | -78 |  |
| (0.222, 0.351] | 111 | 39% (30-48) | -0.10 | -1.71 | -190 |  |
| (0.351, 2.663] | 112 | 36% (27-45) | -0.35 | -1.80 | -202 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.392] | 112 | 36% (27-45) | -0.25 | -1.58 | -177 |  |
| (2.392, 3.625] | 111 | 48% (39-57) | +0.90 | -0.48 | -53 |  |
| (3.625, 19.488] | 112 | 34% (26-43) | -0.80 | -2.13 | -239 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 112 | 45% (36-54) | +0.29 | -0.43 | -48 |  |
| (0.104, 0.167] | 111 | 35% (27-44) | -0.51 | -1.67 | -185 |  |
| (0.167, 0.76] | 112 | 38% (29-47) | +0.06 | -2.10 | -236 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 70 | 31% (22-43) | -1.06 | -1.85 | -129 |  |
| (-0.912, 0.651] | 69 | 45% (34-57) | +0.59 | +0.02 | +1 |  |
| (0.651, 14.989] | 70 | 44% (33-56) | +0.54 | -0.19 | -13 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 72 | 43% (32-55) | +0.06 | -0.55 | -40 |  |
| (0.546, 0.888] | 72 | 42% (31-53) | -0.01 | -0.72 | -52 |  |
| (0.888, 3.799] | 72 | 35% (25-46) | -0.23 | -1.03 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.923] | 72 | 40% (30-52) | -0.27 | -0.87 | -63 |  |
| (0.923, 1.674] | 72 | 43% (32-55) | +0.39 | -0.29 | -21 |  |
| (1.674, 9.058] | 72 | 36% (26-48) | -0.30 | -1.14 | -82 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 72 | 36% (26-48) | -0.52 | -1.09 | -79 |  |
| (0.409, 0.625] | 72 | 47% (36-59) | +0.62 | -0.10 | -7 |  |
| (0.625, 4.001] | 72 | 36% (26-48) | -0.28 | -1.11 | -80 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 171, target 84, time_stop 64, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 112 | 38% | 18% | 38% |
| (0.104, 0.167] | 111 | 57% | 24% | 12% |
| (0.167, 0.76] | 112 | 58% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
