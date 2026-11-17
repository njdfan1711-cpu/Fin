# Scalp signal analysis (fixed exits)

_288 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 288 | 39% (33-45) | -0.11 | -1.57 | -452 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 51 | -27 | -0.53 | 237 | -424 | -1.79 | +27 |
| skip first 30 min | 4 | -21 | -5.34 | 284 | -430 | -1.52 | +21 |
| skip when SPY is down on the day | 118 | -177 | -1.50 | 170 | -275 | -1.62 | +177 |
| skip when SPY is below its VWAP | 123 | -205 | -1.67 | 165 | -247 | -1.50 | +205 |
| skip when SPY fell over the last 15 min | 100 | -147 | -1.47 | 188 | -305 | -1.62 | +147 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 71 | -188 | -2.65 | 217 | -264 | -1.22 | +188 |
| skip stock not beating SPY over 15 min | 46 | -63 | -1.38 | 242 | -388 | -1.61 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 62 | -215 | -3.46 | 226 | -237 | -1.05 | +215 |
| skip volume spikes above 5x average | 59 | -149 | -2.53 | 229 | -303 | -1.32 | +149 |
| skip when the stop is inside normal noise (range > stop) | 35 | -64 | -1.82 | 253 | -388 | -1.53 | +64 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 42 | -68 | -1.61 | 246 | -384 | -1.56 | +68 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 132 | -370 | -2.81 | 156 | -81 | -0.52 | +370 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 120 | 37% (29-46) | -0.41 | -1.63 | -196 |  |
| 240-375 | 79 | 33% (24-44) | -1.18 | -2.90 | -229 |  |
| 375-390 | 51 | 45% (32-59) | +0.93 | -0.53 | -27 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 67 | 39% (28-51) | -0.07 | -1.18 | -79 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 123 | 40% (32-49) | -0.10 | -1.67 | -205 |  |
| above VWAP | 165 | 38% (31-46) | -0.11 | -1.50 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 96 | 38% (28-47) | -0.22 | -1.38 | -133 |  |
| (0.129, 0.374] | 96 | 43% (33-53) | +0.12 | -1.36 | -130 |  |
| (0.374, 5.591] | 96 | 36% (28-46) | -0.22 | -1.96 | -188 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.128] | 95 | 45% (36-55) | +0.55 | -0.61 | -58 |  |
| (0.128, 0.446] | 94 | 41% (32-52) | +0.51 | -1.29 | -121 |  |
| (0.446, 4.846] | 95 | 32% (23-41) | -1.18 | -2.65 | -252 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.444] | 96 | 42% (32-52) | +0.10 | -1.46 | -140 |  |
| (-0.444, 0.384] | 96 | 42% (32-52) | +0.48 | -0.71 | -68 |  |
| (0.384, 9.926] | 96 | 33% (25-43) | -0.90 | -2.54 | -244 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 96 | 40% (30-50) | -0.29 | -1.59 | -153 |  |
| (0.0559, 0.127] | 96 | 44% (34-54) | +0.45 | -0.92 | -88 |  |
| (0.127, 0.924] | 96 | 33% (25-43) | -0.48 | -2.20 | -211 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 96 | 44% (34-54) | +0.37 | -0.67 | -64 |  |
| (0.218, 0.346] | 96 | 41% (31-51) | +0.18 | -1.50 | -144 |  |
| (0.346, 2.663] | 96 | 32% (24-42) | -0.88 | -2.54 | -243 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 96 | 36% (28-46) | -0.21 | -1.64 | -157 |  |
| (2.374, 3.634] | 96 | 45% (35-55) | +0.46 | -1.03 | -99 |  |
| (3.634, 19.488] | 96 | 35% (27-45) | -0.56 | -2.04 | -196 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 96 | 47% (37-57) | +0.47 | -0.29 | -27 |  |
| (0.104, 0.166] | 96 | 34% (26-44) | -0.54 | -1.74 | -167 |  |
| (0.166, 0.76] | 96 | 35% (27-45) | -0.25 | -2.68 | -257 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.915] | 54 | 33% (22-47) | -0.93 | -1.76 | -95 |  |
| (-0.915, 0.589] | 54 | 46% (34-59) | +0.72 | +0.16 | +8 |  |
| (0.589, 7.522] | 54 | 41% (29-54) | +0.05 | -0.68 | -37 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.555] | 57 | 44% (32-57) | +0.00 | -0.64 | -37 |  |
| (0.555, 0.843] | 56 | 43% (31-56) | +0.20 | -0.52 | -29 |  |
| (0.843, 3.799] | 56 | 32% (21-45) | -0.67 | -1.47 | -82 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.884] | 57 | 40% (29-53) | -0.21 | -0.81 | -46 |  |
| (0.884, 1.613] | 56 | 48% (36-61) | +1.04 | +0.31 | +18 |  |
| (1.613, 9.058] | 56 | 30% (20-43) | -1.30 | -2.13 | -119 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.397] | 57 | 39% (27-52) | -0.20 | -0.80 | -46 |  |
| (0.397, 0.618] | 56 | 50% (37-63) | +0.93 | +0.20 | +11 |  |
| (0.618, 4.001] | 56 | 30% (20-43) | -1.19 | -2.03 | -114 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 3% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 146, target 70, time_stop 58, eod 14

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 96 | 35% | 17% | 42% |
| (0.104, 0.166] | 96 | 57% | 25% | 11% |
| (0.166, 0.76] | 96 | 59% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
