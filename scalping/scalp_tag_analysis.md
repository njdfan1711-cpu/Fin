# Scalp signal analysis (fixed exits)

_306 tagged trades, 37 trading days (2026-10-01 to 2026-11-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 306 | 39% (34-44) | -0.10 | -1.51 | -463 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 246 | -476 | -1.94 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 302 | -442 | -1.46 | +21 |
| skip when SPY is down on the day | 136 | -188 | -1.38 | 170 | -275 | -1.62 | +188 |
| skip when SPY is below its VWAP | 134 | -189 | -1.41 | 172 | -274 | -1.59 | +189 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 204 | -332 | -1.63 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 76 | -191 | -2.51 | 230 | -273 | -1.19 | +191 |
| skip stock not beating SPY over 15 min | 48 | -63 | -1.31 | 258 | -400 | -1.55 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 239 | -219 | -0.92 | +244 |
| skip volume spikes above 5x average | 64 | -178 | -2.78 | 242 | -285 | -1.18 | +178 |
| skip when the stop is inside normal noise (range > stop) | 39 | -59 | -1.52 | 267 | -404 | -1.51 | +59 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 47 | -70 | -1.50 | 259 | -393 | -1.52 | +70 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 137 | -357 | -2.61 | 169 | -106 | -0.63 | +357 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 124 | 35% (28-44) | -0.57 | -1.76 | -218 |  |
| 240-375 | 84 | 31% (22-41) | -1.42 | -3.08 | -258 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 85 | 39% (29-49) | -0.05 | -1.07 | -91 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 134 | 41% (33-50) | +0.10 | -1.41 | -189 |  |
| above VWAP | 172 | 37% (30-45) | -0.25 | -1.59 | -274 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 102 | 38% (29-48) | -0.17 | -1.28 | -131 |  |
| (0.123, 0.374] | 102 | 42% (33-52) | +0.11 | -1.32 | -135 |  |
| (0.374, 5.591] | 102 | 36% (28-46) | -0.23 | -1.94 | -198 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.134] | 101 | 47% (37-56) | +0.70 | -0.42 | -42 |  |
| (0.134, 0.449] | 100 | 39% (30-49) | +0.18 | -1.55 | -155 |  |
| (0.449, 4.846] | 101 | 33% (24-42) | -0.99 | -2.43 | -245 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.548] | 102 | 41% (32-51) | -0.00 | -1.48 | -151 |  |
| (-0.548, 0.348] | 102 | 41% (32-51) | +0.56 | -0.63 | -64 |  |
| (0.348, 9.926] | 102 | 34% (26-44) | -0.85 | -2.43 | -248 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0554] | 102 | 37% (28-47) | -0.67 | -1.93 | -197 |  |
| (0.0554, 0.127] | 102 | 45% (36-55) | +0.69 | -0.63 | -64 |  |
| (0.127, 0.924] | 102 | 34% (26-44) | -0.31 | -1.98 | -202 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 102 | 43% (34-53) | +0.32 | -0.68 | -70 |  |
| (0.217, 0.346] | 102 | 40% (31-50) | +0.09 | -1.54 | -157 |  |
| (0.346, 2.663] | 102 | 33% (25-43) | -0.70 | -2.32 | -236 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 102 | 35% (27-45) | -0.38 | -1.77 | -180 |  |
| (2.38, 3.618] | 102 | 48% (39-58) | +0.94 | -0.50 | -51 |  |
| (3.618, 19.488] | 102 | 33% (25-43) | -0.86 | -2.27 | -232 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 102 | 45% (36-55) | +0.27 | -0.47 | -48 |  |
| (0.104, 0.166] | 102 | 35% (27-45) | -0.47 | -1.63 | -166 |  |
| (0.166, 0.76] | 102 | 36% (28-46) | -0.10 | -2.44 | -249 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.773] | 60 | 32% (21-44) | -1.16 | -1.96 | -118 |  |
| (-0.773, 0.62] | 60 | 47% (35-59) | +0.95 | +0.40 | +24 |  |
| (0.62, 7.522] | 60 | 42% (30-54) | +0.07 | -0.68 | -41 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.545] | 63 | 43% (31-55) | -0.02 | -0.64 | -40 |  |
| (0.545, 0.843] | 62 | 42% (30-54) | -0.02 | -0.73 | -45 |  |
| (0.843, 3.799] | 62 | 34% (23-46) | -0.38 | -1.20 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 63 | 41% (30-54) | -0.17 | -0.77 | -49 |  |
| (0.891, 1.624] | 62 | 45% (33-57) | +0.72 | +0.03 | +2 |  |
| (1.624, 9.058] | 62 | 32% (22-45) | -0.95 | -1.82 | -113 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.397] | 63 | 38% (27-50) | -0.29 | -0.86 | -54 |  |
| (0.397, 0.616] | 62 | 48% (36-61) | +0.75 | +0.02 | +1 |  |
| (0.616, 4.001] | 62 | 32% (22-45) | -0.87 | -1.72 | -107 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 156, target 75, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 102 | 37% | 17% | 40% |
| (0.104, 0.166] | 102 | 57% | 25% | 11% |
| (0.166, 0.76] | 102 | 59% | 32% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
