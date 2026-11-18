# Scalp signal analysis (fixed exits)

_298 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 298 | 40% (34-45) | +0.00 | -1.44 | -429 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +18 | +0.32 | 241 | -448 | -1.86 | -18 |
| skip first 30 min | 4 | -21 | -5.34 | 294 | -408 | -1.39 | +21 |
| skip when SPY is down on the day | 128 | -154 | -1.20 | 170 | -275 | -1.62 | +154 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 165 | -247 | -1.50 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 196 | -298 | -1.52 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 74 | -187 | -2.52 | 224 | -242 | -1.08 | +187 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 251 | -373 | -1.48 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -238 | -3.60 | 232 | -191 | -0.82 | +238 |
| skip volume spikes above 5x average | 60 | -156 | -2.59 | 238 | -273 | -1.15 | +156 |
| skip when the stop is inside normal noise (range > stop) | 38 | -53 | -1.39 | 260 | -376 | -1.45 | +53 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 45 | -58 | -1.29 | 253 | -371 | -1.47 | +58 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -351 | -2.58 | 162 | -78 | -0.48 | +351 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 120 | 37% (29-46) | -0.41 | -1.63 | -196 |  |
| 240-375 | 83 | 31% (22-42) | -1.36 | -3.04 | -252 |  |
| 375-390 | 57 | 51% (38-63) | +1.72 | +0.32 | +18 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 77 | 42% (31-53) | +0.34 | -0.73 | -56 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 165 | 38% (31-46) | -0.11 | -1.50 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 100 | 40% (31-50) | +0.09 | -1.05 | -105 |  |
| (0.132, 0.377] | 99 | 42% (33-52) | +0.09 | -1.37 | -136 |  |
| (0.377, 5.591] | 99 | 36% (28-46) | -0.18 | -1.90 | -188 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.13] | 98 | 47% (37-57) | +0.74 | -0.40 | -39 |  |
| (0.13, 0.448] | 98 | 41% (32-51) | +0.46 | -1.31 | -128 |  |
| (0.448, 4.846] | 98 | 33% (24-42) | -1.00 | -2.45 | -241 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.526] | 100 | 43% (34-53) | +0.27 | -1.27 | -127 |  |
| (-0.526, 0.364] | 99 | 40% (31-50) | +0.43 | -0.74 | -73 |  |
| (0.364, 9.926] | 99 | 35% (27-45) | -0.70 | -2.31 | -229 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 100 | 40% (31-50) | -0.26 | -1.54 | -154 |  |
| (0.0558, 0.131] | 99 | 44% (35-54) | +0.57 | -0.78 | -78 |  |
| (0.131, 0.924] | 99 | 34% (26-44) | -0.31 | -1.99 | -197 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 100 | 45% (36-55) | +0.60 | -0.42 | -42 |  |
| (0.217, 0.346] | 99 | 40% (31-50) | +0.09 | -1.57 | -156 |  |
| (0.346, 2.663] | 99 | 33% (25-43) | -0.70 | -2.34 | -232 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 100 | 36% (27-46) | -0.27 | -1.67 | -167 |  |
| (2.377, 3.61] | 99 | 47% (38-57) | +0.91 | -0.56 | -55 |  |
| (3.61, 19.488] | 99 | 35% (27-45) | -0.64 | -2.09 | -207 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 100 | 46% (37-56) | +0.40 | -0.36 | -36 |  |
| (0.105, 0.166] | 100 | 37% (28-47) | -0.22 | -1.38 | -138 |  |
| (0.166, 0.76] | 98 | 36% (27-46) | -0.18 | -2.61 | -255 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 59 | 32% (22-45) | -1.07 | -1.89 | -111 |  |
| (-0.793, 0.617] | 56 | 48% (36-61) | +1.15 | +0.59 | +33 |  |
| (0.617, 7.522] | 57 | 44% (32-57) | +0.37 | -0.40 | -23 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.559] | 60 | 43% (32-56) | +0.02 | -0.62 | -37 |  |
| (0.559, 0.851] | 59 | 44% (32-57) | +0.27 | -0.45 | -26 |  |
| (0.851, 3.799] | 60 | 35% (24-48) | -0.20 | -1.03 | -62 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 60 | 42% (30-54) | -0.14 | -0.74 | -45 |  |
| (0.9, 1.638] | 59 | 47% (35-60) | +1.04 | +0.33 | +20 |  |
| (1.638, 9.058] | 60 | 33% (23-46) | -0.80 | -1.67 | -100 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 60 | 40% (29-53) | -0.02 | -0.61 | -37 |  |
| (0.408, 0.622] | 59 | 51% (38-63) | +1.08 | +0.35 | +21 |  |
| (0.622, 4.001] | 60 | 32% (21-44) | -0.97 | -1.83 | -110 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 149, target 74, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 100 | 36% | 17% | 41% |
| (0.105, 0.166] | 100 | 55% | 26% | 11% |
| (0.166, 0.76] | 98 | 59% | 32% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
