# Scalp signal analysis (fixed exits)

_314 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 314 | 39% (34-45) | -0.08 | -1.47 | -462 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 254 | -475 | -1.87 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 310 | -440 | -1.42 | +21 |
| skip when SPY is down on the day | 144 | -186 | -1.29 | 170 | -275 | -1.62 | +186 |
| skip when SPY is below its VWAP | 138 | -204 | -1.48 | 176 | -257 | -1.46 | +204 |
| skip when SPY fell over the last 15 min | 103 | -136 | -1.32 | 211 | -325 | -1.54 | +136 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 78 | -185 | -2.38 | 236 | -276 | -1.17 | +185 |
| skip stock not beating SPY over 15 min | 49 | -70 | -1.42 | 265 | -392 | -1.48 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 68 | -234 | -3.45 | 246 | -227 | -0.92 | +234 |
| skip volume spikes above 5x average | 67 | -172 | -2.57 | 247 | -289 | -1.17 | +172 |
| skip when the stop is inside normal noise (range > stop) | 42 | -54 | -1.28 | 272 | -408 | -1.50 | +54 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 49 | -72 | -1.46 | 265 | -390 | -1.47 | +72 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 176 | -99 | -0.56 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 128 | 36% (28-45) | -0.58 | -1.75 | -223 |  |
| 240-375 | 87 | 31% (22-41) | -1.37 | -3.00 | -261 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 89 | 39% (30-50) | -0.01 | -1.00 | -89 |  |
| -0.2 to 0 | 55 | 42% (30-55) | +0.26 | -1.77 | -97 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.00 | -1.48 | -204 |  |
| above VWAP | 176 | 38% (31-45) | -0.14 | -1.46 | -257 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 105 | 38% (29-48) | -0.25 | -1.34 | -141 |  |
| (0.123, 0.374] | 104 | 42% (33-52) | +0.14 | -1.27 | -132 |  |
| (0.374, 5.591] | 105 | 37% (29-47) | -0.13 | -1.80 | -189 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 104 | 47% (38-57) | +0.76 | -0.34 | -35 |  |
| (0.133, 0.451] | 103 | 38% (29-48) | +0.00 | -1.69 | -174 |  |
| (0.451, 4.846] | 103 | 34% (26-44) | -0.82 | -2.24 | -231 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.574] | 105 | 43% (34-52) | +0.24 | -1.21 | -127 |  |
| (-0.574, 0.332] | 104 | 38% (30-48) | +0.21 | -0.94 | -98 |  |
| (0.332, 9.926] | 105 | 36% (28-46) | -0.68 | -2.25 | -237 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 105 | 39% (30-49) | -0.43 | -1.68 | -176 |  |
| (0.056, 0.127] | 105 | 44% (35-53) | +0.45 | -0.83 | -88 |  |
| (0.127, 0.924] | 104 | 35% (26-44) | -0.25 | -1.90 | -198 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.219] | 105 | 44% (35-53) | +0.37 | -0.62 | -65 |  |
| (0.219, 0.348] | 104 | 39% (31-49) | -0.03 | -1.63 | -169 |  |
| (0.348, 2.663] | 105 | 34% (26-44) | -0.58 | -2.16 | -227 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.378] | 105 | 35% (27-45) | -0.37 | -1.74 | -183 |  |
| (2.378, 3.635] | 104 | 48% (39-58) | +0.91 | -0.51 | -53 |  |
| (3.635, 19.488] | 105 | 34% (26-44) | -0.77 | -2.15 | -225 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 105 | 45% (36-54) | +0.25 | -0.48 | -51 |  |
| (0.104, 0.166] | 104 | 37% (28-46) | -0.33 | -1.47 | -153 |  |
| (0.166, 0.76] | 105 | 36% (28-46) | -0.16 | -2.46 | -258 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.748] | 63 | 30% (20-42) | -1.32 | -2.11 | -133 |  |
| (-0.748, 0.658] | 63 | 48% (36-60) | +0.91 | +0.36 | +23 |  |
| (0.658, 14.989] | 62 | 44% (32-56) | +0.37 | -0.37 | -23 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 65 | 43% (32-55) | -0.03 | -0.64 | -42 |  |
| (0.55, 0.859] | 65 | 42% (30-54) | -0.06 | -0.77 | -50 |  |
| (0.859, 3.799] | 65 | 35% (25-48) | -0.22 | -1.02 | -66 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 65 | 42% (30-54) | -0.11 | -0.69 | -45 |  |
| (0.909, 1.631] | 65 | 46% (35-58) | +0.71 | +0.03 | +2 |  |
| (1.631, 9.058] | 65 | 32% (22-44) | -0.92 | -1.77 | -115 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 65 | 37% (26-49) | -0.45 | -1.01 | -66 |  |
| (0.404, 0.62] | 65 | 51% (39-63) | +1.05 | +0.34 | +22 |  |
| (0.62, 4.001] | 65 | 32% (22-44) | -0.91 | -1.75 | -114 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 160, target 77, time_stop 61, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 105 | 38% | 17% | 39% |
| (0.104, 0.166] | 104 | 56% | 25% | 12% |
| (0.166, 0.76] | 105 | 59% | 31% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
