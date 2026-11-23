# Scalp signal analysis (fixed exits)

_313 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 313 | 39% (34-44) | -0.11 | -1.51 | -471 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 253 | -485 | -1.92 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 309 | -450 | -1.46 | +21 |
| skip when SPY is down on the day | 143 | -196 | -1.37 | 170 | -275 | -1.62 | +196 |
| skip when SPY is below its VWAP | 138 | -204 | -1.48 | 175 | -267 | -1.53 | +204 |
| skip when SPY fell over the last 15 min | 103 | -136 | -1.32 | 210 | -335 | -1.59 | +136 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 77 | -195 | -2.53 | 236 | -276 | -1.17 | +195 |
| skip stock not beating SPY over 15 min | 49 | -70 | -1.42 | 264 | -402 | -1.52 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 246 | -227 | -0.92 | +244 |
| skip volume spikes above 5x average | 67 | -172 | -2.57 | 246 | -299 | -1.22 | +172 |
| skip when the stop is inside normal noise (range > stop) | 42 | -54 | -1.28 | 271 | -417 | -1.54 | +54 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 49 | -72 | -1.47 | 264 | -399 | -1.51 | +72 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 175 | -108 | -0.62 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 128 | 36% (28-45) | -0.58 | -1.75 | -223 |  |
| 240-375 | 86 | 30% (22-41) | -1.51 | -3.15 | -271 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 89 | 39% (30-50) | -0.01 | -1.00 | -89 |  |
| -0.2 to 0 | 54 | 41% (29-54) | +0.07 | -1.98 | -107 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.00 | -1.48 | -204 |  |
| above VWAP | 175 | 38% (31-45) | -0.20 | -1.53 | -267 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 105 | 38% (29-48) | -0.25 | -1.34 | -141 |  |
| (0.122, 0.374] | 104 | 42% (33-52) | +0.14 | -1.27 | -132 |  |
| (0.374, 5.591] | 104 | 37% (28-46) | -0.23 | -1.91 | -199 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 103 | 47% (37-56) | +0.66 | -0.44 | -45 |  |
| (0.135, 0.453] | 103 | 38% (29-48) | +0.00 | -1.69 | -174 |  |
| (0.453, 4.846] | 103 | 34% (26-44) | -0.82 | -2.24 | -231 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.572] | 105 | 42% (33-51) | +0.08 | -1.36 | -143 |  |
| (-0.572, 0.338] | 104 | 39% (31-49) | +0.28 | -0.87 | -91 |  |
| (0.338, 9.926] | 104 | 36% (27-45) | -0.70 | -2.28 | -238 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 105 | 39% (30-49) | -0.43 | -1.68 | -176 |  |
| (0.056, 0.127] | 105 | 44% (35-53) | +0.45 | -0.83 | -88 |  |
| (0.127, 0.924] | 103 | 34% (26-44) | -0.36 | -2.01 | -207 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 105 | 44% (35-53) | +0.37 | -0.62 | -65 |  |
| (0.218, 0.346] | 104 | 39% (31-49) | -0.03 | -1.63 | -169 |  |
| (0.346, 2.663] | 104 | 34% (25-43) | -0.69 | -2.28 | -237 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 105 | 34% (26-44) | -0.52 | -1.90 | -199 |  |
| (2.381, 3.637] | 104 | 49% (40-59) | +0.99 | -0.43 | -45 | ▲ |
| (3.637, 19.488] | 104 | 34% (25-43) | -0.80 | -2.19 | -227 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 105 | 45% (36-54) | +0.25 | -0.48 | -51 |  |
| (0.104, 0.166] | 104 | 37% (28-46) | -0.33 | -1.47 | -153 |  |
| (0.166, 0.76] | 104 | 36% (27-45) | -0.26 | -2.57 | -268 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.762] | 63 | 30% (20-42) | -1.32 | -2.11 | -133 |  |
| (-0.762, 0.658] | 63 | 48% (36-60) | +0.91 | +0.36 | +23 |  |
| (0.658, 8.282] | 61 | 43% (31-55) | +0.20 | -0.53 | -33 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.547] | 65 | 43% (32-55) | -0.03 | -0.64 | -42 |  |
| (0.547, 0.856] | 64 | 41% (29-53) | -0.20 | -0.90 | -58 |  |
| (0.856, 3.799] | 65 | 35% (25-48) | -0.24 | -1.04 | -68 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.9] | 65 | 42% (30-54) | -0.11 | -0.69 | -45 |  |
| (0.9, 1.621] | 64 | 47% (35-59) | +0.81 | +0.13 | +8 |  |
| (1.621, 9.058] | 65 | 31% (21-43) | -1.16 | -2.01 | -131 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.401] | 65 | 37% (26-49) | -0.45 | -1.01 | -66 |  |
| (0.401, 0.617] | 64 | 50% (38-62) | +0.91 | +0.20 | +13 |  |
| (0.617, 4.001] | 65 | 32% (22-44) | -0.92 | -1.76 | -114 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 160, target 76, time_stop 61, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 105 | 38% | 17% | 39% |
| (0.104, 0.166] | 104 | 56% | 25% | 12% |
| (0.166, 0.76] | 104 | 60% | 31% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
