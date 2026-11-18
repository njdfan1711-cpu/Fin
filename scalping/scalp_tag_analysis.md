# Scalp signal analysis (fixed exits)

_301 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 301 | 39% (34-45) | -0.05 | -1.48 | -446 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +18 | +0.32 | 244 | -464 | -1.90 | -18 |
| skip first 30 min | 4 | -21 | -5.34 | 297 | -424 | -1.43 | +21 |
| skip when SPY is down on the day | 131 | -171 | -1.30 | 170 | -275 | -1.62 | +171 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 168 | -263 | -1.57 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 199 | -315 | -1.58 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 74 | -187 | -2.52 | 227 | -259 | -1.14 | +187 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 254 | -389 | -1.53 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -238 | -3.60 | 235 | -208 | -0.88 | +238 |
| skip volume spikes above 5x average | 63 | -172 | -2.74 | 238 | -273 | -1.15 | +172 |
| skip when the stop is inside normal noise (range > stop) | 38 | -53 | -1.39 | 263 | -393 | -1.49 | +53 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 46 | -64 | -1.39 | 255 | -382 | -1.50 | +64 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -351 | -2.58 | 165 | -95 | -0.58 | +351 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 123 | 36% (28-45) | -0.52 | -1.73 | -213 |  |
| 240-375 | 83 | 31% (22-42) | -1.36 | -3.04 | -252 |  |
| 375-390 | 57 | 51% (38-63) | +1.72 | +0.32 | +18 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 80 | 40% (30-51) | +0.13 | -0.91 | -73 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 168 | 38% (31-45) | -0.20 | -1.57 | -263 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 101 | 39% (30-48) | -0.11 | -1.24 | -125 |  |
| (0.123, 0.374] | 100 | 42% (33-52) | +0.08 | -1.38 | -138 |  |
| (0.374, 5.591] | 100 | 37% (28-47) | -0.12 | -1.83 | -183 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 99 | 47% (38-57) | +0.84 | -0.29 | -29 |  |
| (0.135, 0.448] | 99 | 39% (30-49) | +0.24 | -1.50 | -149 |  |
| (0.448, 4.846] | 99 | 32% (24-42) | -1.04 | -2.49 | -246 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.526] | 101 | 43% (33-52) | +0.21 | -1.32 | -133 |  |
| (-0.526, 0.34] | 100 | 40% (31-50) | +0.38 | -0.77 | -77 |  |
| (0.34, 9.926] | 100 | 35% (26-45) | -0.75 | -2.35 | -235 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 101 | 40% (31-49) | -0.30 | -1.58 | -160 |  |
| (0.0558, 0.131] | 100 | 44% (35-54) | +0.51 | -0.83 | -83 |  |
| (0.131, 0.924] | 100 | 34% (25-44) | -0.36 | -2.03 | -203 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 101 | 45% (35-54) | +0.55 | -0.47 | -47 |  |
| (0.217, 0.346] | 100 | 40% (31-50) | +0.04 | -1.61 | -161 |  |
| (0.346, 2.663] | 100 | 33% (25-43) | -0.74 | -2.37 | -237 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 101 | 36% (27-45) | -0.32 | -1.72 | -174 |  |
| (2.381, 3.632] | 100 | 48% (38-58) | +0.93 | -0.53 | -53 |  |
| (3.632, 19.488] | 100 | 34% (25-44) | -0.76 | -2.19 | -219 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 101 | 46% (36-55) | +0.35 | -0.41 | -42 |  |
| (0.105, 0.166] | 101 | 37% (28-46) | -0.27 | -1.41 | -143 |  |
| (0.166, 0.76] | 99 | 35% (27-45) | -0.24 | -2.64 | -261 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 59 | 32% (22-45) | -1.07 | -1.89 | -111 |  |
| (-0.793, 0.617] | 58 | 47% (34-59) | +0.94 | +0.39 | +23 |  |
| (0.617, 7.522] | 58 | 43% (31-56) | +0.27 | -0.49 | -29 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.559] | 61 | 43% (31-55) | -0.07 | -0.70 | -42 |  |
| (0.559, 0.851] | 60 | 43% (32-56) | +0.18 | -0.53 | -32 |  |
| (0.851, 3.799] | 61 | 34% (24-47) | -0.29 | -1.11 | -68 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 61 | 41% (30-54) | -0.23 | -0.82 | -50 |  |
| (0.9, 1.638] | 60 | 47% (35-59) | +0.94 | +0.23 | +14 |  |
| (1.638, 9.058] | 61 | 33% (22-45) | -0.88 | -1.74 | -106 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 61 | 39% (28-52) | -0.10 | -0.69 | -42 |  |
| (0.408, 0.617] | 60 | 48% (36-61) | +0.73 | +0.00 | +0 |  |
| (0.617, 4.001] | 61 | 33% (22-45) | -0.79 | -1.64 | -100 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 152, target 74, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 101 | 37% | 17% | 41% |
| (0.105, 0.166] | 101 | 55% | 26% | 11% |
| (0.166, 0.76] | 99 | 60% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
