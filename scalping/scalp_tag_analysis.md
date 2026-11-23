# Scalp signal analysis (fixed exits)

_309 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 309 | 39% (34-44) | -0.10 | -1.51 | -466 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 249 | -480 | -1.93 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 305 | -445 | -1.46 | +21 |
| skip when SPY is down on the day | 139 | -191 | -1.38 | 170 | -275 | -1.62 | +191 |
| skip when SPY is below its VWAP | 136 | -201 | -1.48 | 173 | -265 | -1.53 | +201 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 207 | -335 | -1.62 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 76 | -200 | -2.63 | 233 | -267 | -1.14 | +200 |
| skip stock not beating SPY over 15 min | 48 | -63 | -1.31 | 261 | -403 | -1.54 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 242 | -222 | -0.92 | +244 |
| skip volume spikes above 5x average | 65 | -169 | -2.60 | 244 | -297 | -1.22 | +169 |
| skip when the stop is inside normal noise (range > stop) | 41 | -56 | -1.37 | 268 | -410 | -1.53 | +56 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 48 | -77 | -1.59 | 261 | -390 | -1.49 | +77 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 171 | -103 | -0.60 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 124 | 35% (28-44) | -0.57 | -1.76 | -218 |  |
| 240-375 | 86 | 30% (22-41) | -1.51 | -3.15 | -271 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 88 | 39% (29-49) | -0.07 | -1.07 | -94 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 136 | 40% (33-49) | +0.01 | -1.48 | -201 |  |
| above VWAP | 173 | 38% (31-45) | -0.19 | -1.53 | -265 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 103 | 38% (29-48) | -0.22 | -1.33 | -137 |  |
| (0.129, 0.374] | 103 | 43% (34-52) | +0.20 | -1.22 | -126 |  |
| (0.374, 5.591] | 103 | 36% (27-46) | -0.28 | -1.97 | -203 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.137] | 102 | 47% (38-57) | +0.75 | -0.37 | -38 |  |
| (0.137, 0.455] | 101 | 38% (29-47) | +0.01 | -1.70 | -172 |  |
| (0.455, 4.846] | 102 | 33% (25-43) | -0.88 | -2.31 | -235 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.573] | 103 | 42% (33-51) | +0.09 | -1.38 | -142 |  |
| (-0.573, 0.339] | 103 | 40% (31-49) | +0.34 | -0.82 | -85 |  |
| (0.339, 9.926] | 103 | 35% (26-45) | -0.74 | -2.33 | -240 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0558] | 103 | 38% (29-48) | -0.57 | -1.83 | -188 |  |
| (0.0558, 0.127] | 103 | 45% (35-54) | +0.62 | -0.69 | -71 |  |
| (0.127, 0.924] | 103 | 34% (26-44) | -0.36 | -2.01 | -207 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 103 | 44% (35-53) | +0.42 | -0.58 | -60 |  |
| (0.218, 0.347] | 103 | 40% (31-49) | +0.01 | -1.60 | -165 |  |
| (0.347, 2.663] | 103 | 33% (25-43) | -0.74 | -2.34 | -241 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 104 | 35% (26-44) | -0.47 | -1.85 | -193 |  |
| (2.377, 3.618] | 102 | 48% (39-58) | +0.94 | -0.50 | -51 |  |
| (3.618, 19.488] | 103 | 34% (26-44) | -0.76 | -2.16 | -223 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 103 | 46% (36-55) | +0.37 | -0.37 | -38 |  |
| (0.104, 0.166] | 104 | 36% (27-45) | -0.43 | -1.57 | -164 |  |
| (0.166, 0.76] | 102 | 35% (27-45) | -0.24 | -2.59 | -264 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 62 | 31% (21-43) | -1.29 | -2.09 | -130 |  |
| (-0.793, 0.62] | 60 | 47% (35-59) | +0.95 | +0.40 | +24 |  |
| (0.62, 7.53] | 61 | 43% (31-55) | +0.22 | -0.52 | -32 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 64 | 42% (31-54) | -0.11 | -0.73 | -47 |  |
| (0.552, 0.855] | 63 | 41% (30-54) | -0.11 | -0.82 | -52 |  |
| (0.855, 3.799] | 63 | 35% (24-47) | -0.21 | -1.03 | -65 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.891] | 64 | 42% (31-54) | -0.03 | -0.62 | -40 |  |
| (0.891, 1.644] | 63 | 44% (33-57) | +0.62 | -0.08 | -5 |  |
| (1.644, 9.058] | 63 | 32% (22-44) | -1.02 | -1.87 | -118 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.408] | 64 | 38% (27-50) | -0.37 | -0.95 | -61 |  |
| (0.408, 0.618] | 63 | 51% (39-63) | +1.13 | +0.42 | +26 |  |
| (0.618, 4.001] | 63 | 30% (20-42) | -1.18 | -2.04 | -128 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 158, target 76, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 103 | 37% | 17% | 40% |
| (0.104, 0.166] | 104 | 57% | 25% | 11% |
| (0.166, 0.76] | 102 | 60% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
