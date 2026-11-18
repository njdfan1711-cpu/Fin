# Scalp signal analysis (fixed exits)

_299 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 299 | 39% (34-45) | -0.02 | -1.45 | -435 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +18 | +0.32 | 242 | -453 | -1.87 | -18 |
| skip first 30 min | 4 | -21 | -5.34 | 295 | -414 | -1.40 | +21 |
| skip when SPY is down on the day | 129 | -160 | -1.24 | 170 | -275 | -1.62 | +160 |
| skip when SPY is below its VWAP | 133 | -182 | -1.37 | 166 | -253 | -1.52 | +182 |
| skip when SPY fell over the last 15 min | 102 | -131 | -1.29 | 197 | -304 | -1.54 | +131 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 74 | -187 | -2.52 | 225 | -248 | -1.10 | +187 |
| skip stock not beating SPY over 15 min | 47 | -57 | -1.20 | 252 | -378 | -1.50 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -238 | -3.60 | 233 | -197 | -0.85 | +238 |
| skip volume spikes above 5x average | 61 | -162 | -2.65 | 238 | -273 | -1.15 | +162 |
| skip when the stop is inside normal noise (range > stop) | 38 | -53 | -1.39 | 261 | -382 | -1.46 | +53 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 45 | -58 | -1.29 | 254 | -377 | -1.48 | +58 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -351 | -2.58 | 163 | -84 | -0.52 | +351 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 50% (35-65) | +1.69 | +0.01 | +0 |  |
| 60-240 | 121 | 36% (28-45) | -0.45 | -1.67 | -202 |  |
| 240-375 | 83 | 31% (22-42) | -1.36 | -3.04 | -252 |  |
| 375-390 | 57 | 51% (38-63) | +1.72 | +0.32 | +18 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 78 | 41% (31-52) | +0.27 | -0.80 | -62 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 41% (33-50) | +0.14 | -1.37 | -182 |  |
| above VWAP | 166 | 38% (31-46) | -0.14 | -1.52 | -253 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 100 | 40% (31-50) | +0.09 | -1.05 | -105 |  |
| (0.133, 0.376] | 99 | 41% (32-51) | -0.02 | -1.48 | -147 |  |
| (0.376, 5.591] | 100 | 37% (28-47) | -0.12 | -1.83 | -183 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 99 | 47% (38-57) | +0.84 | -0.29 | -29 |  |
| (0.133, 0.451] | 98 | 40% (31-50) | +0.29 | -1.47 | -144 |  |
| (0.451, 4.846] | 98 | 33% (24-42) | -0.99 | -2.45 | -240 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.557] | 100 | 42% (33-52) | +0.11 | -1.39 | -139 |  |
| (-0.557, 0.356] | 99 | 41% (32-51) | +0.59 | -0.62 | -62 |  |
| (0.356, 9.926] | 100 | 35% (26-45) | -0.75 | -2.35 | -235 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 100 | 40% (31-50) | -0.26 | -1.54 | -154 |  |
| (0.0559, 0.133] | 99 | 44% (35-54) | +0.57 | -0.78 | -78 |  |
| (0.133, 0.924] | 100 | 34% (25-44) | -0.36 | -2.03 | -203 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 100 | 45% (36-55) | +0.60 | -0.42 | -42 |  |
| (0.217, 0.346] | 99 | 40% (31-50) | +0.10 | -1.56 | -154 |  |
| (0.346, 2.663] | 100 | 33% (25-43) | -0.75 | -2.39 | -239 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.378] | 100 | 36% (27-46) | -0.27 | -1.67 | -167 |  |
| (2.378, 3.611] | 99 | 47% (38-57) | +0.91 | -0.56 | -55 |  |
| (3.611, 19.488] | 100 | 35% (26-45) | -0.68 | -2.13 | -213 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 100 | 46% (37-56) | +0.40 | -0.36 | -36 |  |
| (0.105, 0.166] | 100 | 37% (28-47) | -0.22 | -1.38 | -138 |  |
| (0.166, 0.76] | 99 | 35% (27-45) | -0.24 | -2.64 | -261 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 59 | 32% (22-45) | -1.07 | -1.89 | -111 |  |
| (-0.793, 0.622] | 56 | 48% (36-61) | +1.15 | +0.59 | +33 |  |
| (0.622, 7.522] | 58 | 43% (31-56) | +0.27 | -0.49 | -29 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.563] | 60 | 43% (32-56) | +0.02 | -0.62 | -37 |  |
| (0.563, 0.855] | 60 | 43% (32-56) | +0.17 | -0.55 | -33 |  |
| (0.855, 3.799] | 60 | 35% (24-48) | -0.20 | -1.02 | -61 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 60 | 42% (30-54) | -0.14 | -0.74 | -45 |  |
| (0.909, 1.652] | 60 | 47% (35-59) | +0.93 | +0.21 | +13 |  |
| (1.652, 9.058] | 60 | 33% (23-46) | -0.80 | -1.66 | -99 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 60 | 40% (29-53) | -0.02 | -0.61 | -37 |  |
| (0.409, 0.62] | 60 | 50% (38-62) | +0.98 | +0.25 | +15 |  |
| (0.62, 4.001] | 60 | 32% (21-44) | -0.97 | -1.83 | -110 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 150, target 74, time_stop 59, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 100 | 36% | 17% | 41% |
| (0.105, 0.166] | 100 | 55% | 26% | 11% |
| (0.166, 0.76] | 99 | 60% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
