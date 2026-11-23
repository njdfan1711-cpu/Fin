# Scalp signal analysis (fixed exits)

_311 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 311 | 39% (34-44) | -0.11 | -1.51 | -470 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 251 | -483 | -1.92 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 307 | -448 | -1.46 | +21 |
| skip when SPY is down on the day | 141 | -194 | -1.38 | 170 | -275 | -1.62 | +194 |
| skip when SPY is below its VWAP | 138 | -204 | -1.48 | 173 | -265 | -1.53 | +204 |
| skip when SPY fell over the last 15 min | 103 | -136 | -1.32 | 208 | -333 | -1.60 | +136 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 77 | -190 | -2.47 | 234 | -280 | -1.19 | +190 |
| skip stock not beating SPY over 15 min | 48 | -63 | -1.31 | 263 | -406 | -1.55 | +63 |
| skip afternoon entries (2:00-3:45 PM) | 67 | -244 | -3.64 | 244 | -225 | -0.92 | +244 |
| skip volume spikes above 5x average | 67 | -172 | -2.57 | 244 | -297 | -1.22 | +172 |
| skip when the stop is inside normal noise (range > stop) | 42 | -54 | -1.28 | 269 | -416 | -1.55 | +54 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 48 | -77 | -1.59 | 263 | -393 | -1.49 | +77 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 173 | -107 | -0.62 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 126 | 36% (28-44) | -0.58 | -1.76 | -222 |  |
| 240-375 | 86 | 30% (22-41) | -1.51 | -3.15 | -271 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 88 | 39% (29-49) | -0.07 | -1.07 | -94 |  |
| -0.2 to 0 | 53 | 42% (29-55) | +0.19 | -1.90 | -101 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.00 | -1.48 | -204 |  |
| above VWAP | 173 | 38% (31-45) | -0.19 | -1.53 | -265 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 104 | 38% (30-48) | -0.19 | -1.29 | -134 |  |
| (0.123, 0.374] | 103 | 42% (33-51) | +0.04 | -1.38 | -142 |  |
| (0.374, 5.591] | 104 | 37% (28-46) | -0.18 | -1.86 | -194 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 103 | 47% (37-56) | +0.66 | -0.44 | -45 |  |
| (0.133, 0.451] | 102 | 38% (29-48) | +0.06 | -1.64 | -167 |  |
| (0.451, 4.846] | 102 | 33% (25-43) | -0.88 | -2.31 | -235 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.566] | 104 | 41% (32-51) | +0.04 | -1.42 | -148 |  |
| (-0.566, 0.34] | 103 | 40% (31-49) | +0.34 | -0.82 | -84 |  |
| (0.34, 9.926] | 104 | 36% (27-45) | -0.70 | -2.28 | -238 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 104 | 38% (30-48) | -0.46 | -1.72 | -179 |  |
| (0.0559, 0.127] | 104 | 44% (35-54) | +0.49 | -0.80 | -83 |  |
| (0.127, 0.924] | 103 | 34% (26-44) | -0.36 | -2.01 | -207 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.219] | 104 | 44% (35-54) | +0.43 | -0.57 | -59 |  |
| (0.219, 0.346] | 103 | 40% (31-49) | +0.03 | -1.57 | -162 |  |
| (0.346, 2.663] | 104 | 33% (24-42) | -0.79 | -2.39 | -248 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.378] | 104 | 35% (26-44) | -0.47 | -1.85 | -193 |  |
| (2.378, 3.635] | 103 | 48% (38-57) | +0.87 | -0.56 | -58 |  |
| (3.635, 19.488] | 104 | 35% (26-44) | -0.72 | -2.11 | -219 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 104 | 45% (36-55) | +0.31 | -0.42 | -44 |  |
| (0.104, 0.166] | 103 | 36% (27-46) | -0.38 | -1.53 | -158 |  |
| (0.166, 0.76] | 104 | 36% (27-45) | -0.26 | -2.57 | -268 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.783] | 62 | 31% (21-43) | -1.29 | -2.09 | -130 |  |
| (-0.783, 0.633] | 61 | 48% (36-60) | +0.97 | +0.42 | +26 |  |
| (0.633, 8.282] | 62 | 42% (30-54) | +0.14 | -0.60 | -37 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.554] | 64 | 42% (31-54) | -0.11 | -0.73 | -47 |  |
| (0.554, 0.859] | 64 | 42% (31-54) | +0.03 | -0.68 | -43 |  |
| (0.859, 3.799] | 64 | 34% (24-47) | -0.39 | -1.19 | -76 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.889] | 64 | 41% (29-53) | -0.14 | -0.72 | -46 |  |
| (0.889, 1.631] | 64 | 47% (35-59) | +0.77 | +0.08 | +5 |  |
| (1.631, 9.058] | 64 | 31% (21-43) | -1.09 | -1.95 | -125 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 64 | 38% (27-50) | -0.36 | -0.93 | -59 |  |
| (0.404, 0.616] | 64 | 50% (38-62) | +0.91 | +0.20 | +13 |  |
| (0.616, 4.001] | 64 | 31% (21-43) | -1.01 | -1.86 | -119 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 159, target 76, time_stop 60, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 104 | 38% | 17% | 39% |
| (0.104, 0.166] | 103 | 56% | 25% | 11% |
| (0.166, 0.76] | 104 | 60% | 31% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
