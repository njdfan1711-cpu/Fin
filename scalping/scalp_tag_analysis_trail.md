# Scalp signal analysis (trail exits)

_306 tagged trades, 37 trading days (2026-10-01 to 2026-11-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 306 | 42% (36-47) | -0.71 | -2.12 | -650 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 246 | -679 | -2.76 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 302 | -633 | -2.10 | +17 |
| skip when SPY is down on the day | 136 | -320 | -2.35 | 170 | -330 | -1.94 | +320 |
| skip when SPY is below its VWAP | 134 | -341 | -2.54 | 172 | -309 | -1.80 | +341 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 203 | -435 | -2.14 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 76 | -223 | -2.94 | 230 | -427 | -1.85 | +223 |
| skip stock not beating SPY over 15 min | 48 | -107 | -2.23 | 258 | -543 | -2.10 | +107 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -252 | -3.75 | 239 | -398 | -1.67 | +252 |
| skip volume spikes above 5x average | 64 | -242 | -3.77 | 242 | -408 | -1.69 | +242 |
| skip when the stop is inside normal noise (range > stop) | 39 | -68 | -1.73 | 267 | -582 | -2.18 | +68 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 47 | -90 | -1.92 | 259 | -560 | -2.16 | +90 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 137 | -419 | -3.06 | 169 | -231 | -1.37 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 124 | 37% (29-46) | -1.36 | -2.56 | -317 |  |
| 240-375 | 84 | 38% (28-49) | -1.68 | -3.33 | -280 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 85 | 44% (33-54) | -0.58 | -1.60 | -136 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 134 | 39% (31-47) | -1.04 | -2.54 | -341 |  |
| above VWAP | 172 | 44% (37-52) | -0.45 | -1.80 | -309 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 102 | 40% (31-50) | -0.34 | -1.45 | -148 |  |
| (0.123, 0.374] | 102 | 49% (40-59) | -0.44 | -1.87 | -190 |  |
| (0.374, 5.591] | 102 | 36% (28-46) | -1.35 | -3.05 | -311 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 101 | 50% (40-59) | +0.28 | -0.84 | -85 |  |
| (0.134, 0.449] | 100 | 40% (31-50) | -0.96 | -2.69 | -269 |  |
| (0.449, 4.846] | 101 | 37% (28-46) | -1.33 | -2.77 | -280 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.548] | 102 | 44% (35-54) | -0.67 | -2.14 | -218 |  |
| (-0.548, 0.348] | 102 | 45% (36-55) | +0.10 | -1.09 | -111 |  |
| (0.348, 9.926] | 102 | 36% (28-46) | -1.56 | -3.14 | -320 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0554] | 102 | 41% (32-51) | -1.20 | -2.46 | -251 |  |
| (0.0554, 0.127] | 102 | 47% (38-57) | +0.30 | -1.02 | -104 |  |
| (0.127, 0.924] | 102 | 37% (28-47) | -1.22 | -2.89 | -295 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 102 | 45% (36-55) | +0.11 | -0.89 | -91 |  |
| (0.217, 0.346] | 102 | 46% (37-56) | -0.65 | -2.28 | -232 |  |
| (0.346, 2.663] | 102 | 34% (26-44) | -1.59 | -3.20 | -326 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 102 | 42% (33-52) | -0.54 | -1.93 | -197 |  |
| (2.38, 3.618] | 102 | 50% (40-60) | +0.63 | -0.81 | -82 |  |
| (3.618, 19.488] | 102 | 33% (25-43) | -2.21 | -3.63 | -370 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 102 | 47% (38-57) | +0.11 | -0.63 | -64 |  |
| (0.104, 0.166] | 102 | 42% (33-52) | -1.07 | -2.23 | -228 |  |
| (0.166, 0.76] | 102 | 36% (28-46) | -1.16 | -3.51 | -358 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.773] | 60 | 40% (29-53) | -1.48 | -2.29 | -137 |  |
| (-0.773, 0.62] | 60 | 52% (39-64) | -0.00 | -0.56 | -33 |  |
| (0.62, 7.522] | 60 | 53% (41-65) | -0.47 | -1.23 | -74 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.545] | 63 | 48% (36-60) | -0.61 | -1.23 | -77 |  |
| (0.545, 0.843] | 62 | 53% (41-65) | -0.73 | -1.44 | -89 |  |
| (0.843, 3.799] | 62 | 44% (32-56) | -0.86 | -1.69 | -105 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 63 | 48% (36-60) | -1.26 | -1.86 | -117 |  |
| (0.891, 1.624] | 62 | 50% (38-62) | -0.45 | -1.14 | -71 |  |
| (1.624, 9.058] | 62 | 47% (35-59) | -0.48 | -1.34 | -83 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.397] | 63 | 44% (33-57) | -0.82 | -1.39 | -88 |  |
| (0.397, 0.616] | 62 | 60% (47-71) | -0.14 | -0.86 | -53 | ▲ |
| (0.616, 4.001] | 62 | 40% (29-53) | -1.24 | -2.10 | -130 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.16%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 136, trail_stop 125, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 102 | 33% | 32% | 29% |
| (0.104, 0.166] | 102 | 49% | 44% | 3% |
| (0.166, 0.76] | 102 | 51% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
