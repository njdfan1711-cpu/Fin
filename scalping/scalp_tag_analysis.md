# Scalp signal analysis (fixed exits)

_308 tagged trades, 37 trading days (2026-10-01 to 2026-11-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 308 | 39% (33-44) | -0.13 | -1.54 | -475 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 248 | -489 | -1.97 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 304 | -454 | -1.49 | +21 |
| skip when SPY is down on the day | 138 | -200 | -1.45 | 170 | -275 | -1.62 | +200 |
| skip when SPY is below its VWAP | 136 | -201 | -1.48 | 172 | -274 | -1.59 | +201 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 206 | -344 | -1.67 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 76 | -199 | -2.62 | 232 | -276 | -1.19 | +199 |
| skip stock not beating SPY over 15 min | 48 | -63 | -1.31 | 260 | -412 | -1.59 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 241 | -231 | -0.96 | +244 |
| skip volume spikes above 5x average | 64 | -178 | -2.78 | 244 | -297 | -1.22 | +178 |
| skip when the stop is inside normal noise (range > stop) | 40 | -65 | -1.63 | 268 | -410 | -1.53 | +65 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 47 | -86 | -1.83 | 261 | -389 | -1.49 | +86 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 170 | -112 | -0.66 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 124 | 35% (28-44) | -0.57 | -1.76 | -218 |  |
| 240-375 | 86 | 30% (22-41) | -1.51 | -3.15 | -271 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 87 | 38% (28-48) | -0.17 | -1.18 | -103 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 136 | 40% (33-49) | +0.01 | -1.48 | -201 |  |
| above VWAP | 172 | 37% (30-45) | -0.25 | -1.59 | -274 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 103 | 38% (29-48) | -0.22 | -1.33 | -137 |  |
| (0.126, 0.374] | 102 | 42% (33-52) | +0.11 | -1.32 | -135 |  |
| (0.374, 5.591] | 103 | 36% (27-46) | -0.28 | -1.97 | -203 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 102 | 47% (38-57) | +0.75 | -0.37 | -38 |  |
| (0.135, 0.451] | 101 | 38% (29-47) | +0.01 | -1.70 | -172 |  |
| (0.451, 4.846] | 101 | 33% (24-42) | -0.98 | -2.42 | -244 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.56] | 103 | 41% (32-50) | -0.05 | -1.52 | -157 |  |
| (-0.56, 0.34] | 102 | 40% (31-50) | +0.40 | -0.77 | -79 |  |
| (0.34, 9.926] | 103 | 35% (26-45) | -0.74 | -2.33 | -240 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0557] | 103 | 38% (29-48) | -0.57 | -1.83 | -188 |  |
| (0.0557, 0.128] | 102 | 44% (35-54) | +0.53 | -0.78 | -80 |  |
| (0.128, 0.924] | 103 | 34% (26-44) | -0.36 | -2.01 | -207 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 103 | 44% (35-53) | +0.42 | -0.58 | -60 |  |
| (0.217, 0.348] | 102 | 39% (30-49) | -0.07 | -1.71 | -174 |  |
| (0.348, 2.663] | 103 | 33% (25-43) | -0.74 | -2.34 | -241 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.377] | 104 | 35% (26-44) | -0.47 | -1.85 | -193 |  |
| (2.377, 3.611] | 101 | 48% (38-57) | +0.92 | -0.53 | -53 |  |
| (3.611, 19.488] | 103 | 34% (26-44) | -0.82 | -2.23 | -229 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 103 | 46% (36-55) | +0.37 | -0.37 | -38 |  |
| (0.104, 0.166] | 102 | 34% (26-44) | -0.63 | -1.79 | -183 |  |
| (0.166, 0.76] | 103 | 36% (27-46) | -0.14 | -2.47 | -255 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 62 | 31% (21-43) | -1.29 | -2.09 | -130 |  |
| (-0.793, 0.616] | 59 | 47% (35-60) | +1.01 | +0.46 | +27 |  |
| (0.616, 7.522] | 61 | 41% (30-54) | +0.03 | -0.72 | -44 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 63 | 43% (31-55) | -0.02 | -0.64 | -40 |  |
| (0.55, 0.847] | 63 | 41% (30-54) | -0.11 | -0.82 | -51 |  |
| (0.847, 3.799] | 63 | 33% (23-46) | -0.45 | -1.27 | -80 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 63 | 41% (30-54) | -0.17 | -0.77 | -49 |  |
| (0.909, 1.652] | 63 | 44% (33-57) | +0.62 | -0.08 | -5 |  |
| (1.652, 9.058] | 63 | 32% (22-44) | -1.02 | -1.87 | -118 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 63 | 38% (27-50) | -0.29 | -0.86 | -54 |  |
| (0.404, 0.62] | 63 | 49% (37-61) | +0.89 | +0.17 | +11 |  |
| (0.62, 4.001] | 63 | 30% (20-42) | -1.18 | -2.04 | -128 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 158, target 75, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 103 | 37% | 17% | 40% |
| (0.104, 0.166] | 102 | 58% | 24% | 11% |
| (0.166, 0.76] | 103 | 59% | 32% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
