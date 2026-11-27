# Scalp signal analysis (fixed exits)

_338 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 338 | 39% (34-45) | -0.01 | -1.35 | -456 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 276 | -457 | -1.66 | -0 |
| skip first 30 min | 5 | -27 | -5.42 | 333 | -429 | -1.29 | +27 |
| skip when SPY is down on the day | 156 | -181 | -1.16 | 182 | -275 | -1.51 | +181 |
| skip when SPY is below its VWAP | 143 | -204 | -1.42 | 195 | -253 | -1.30 | +204 |
| skip when SPY fell over the last 15 min | 112 | -115 | -1.03 | 226 | -341 | -1.51 | +115 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 83 | -170 | -2.05 | 255 | -286 | -1.12 | +170 |
| skip stock not beating SPY over 15 min | 53 | -94 | -1.78 | 285 | -362 | -1.27 | +94 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 268 | -229 | -0.86 | +227 |
| skip volume spikes above 5x average | 72 | -173 | -2.40 | 266 | -284 | -1.07 | +173 |
| skip when the stop is inside normal noise (range > stop) | 51 | -49 | -0.97 | 287 | -407 | -1.42 | +49 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 55 | -46 | -0.84 | 283 | -410 | -1.45 | +46 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -366 | -2.60 | 197 | -91 | -0.46 | +366 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 48% (33-62) | +1.39 | -0.18 | -8 |  |
| 60-240 | 145 | 38% (30-46) | -0.24 | -1.35 | -196 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 39% (30-49) | -0.01 | -0.98 | -96 |  |
| -0.2 to 0 | 58 | 43% (31-56) | +0.50 | -1.46 | -85 |  |
| 0 to 0.2 | 75 | 33% (24-45) | -0.38 | -1.64 | -123 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (33-49) | +0.03 | -1.42 | -204 |  |
| above VWAP | 195 | 38% (32-45) | -0.04 | -1.30 | -253 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.115] | 113 | 37% (29-46) | -0.33 | -1.32 | -149 |  |
| (0.115, 0.37] | 112 | 43% (34-52) | +0.32 | -1.09 | -122 |  |
| (0.37, 5.591] | 113 | 38% (30-47) | -0.01 | -1.64 | -185 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.13] | 111 | 47% (38-56) | +0.83 | -0.25 | -27 |  |
| (0.13, 0.445] | 111 | 39% (30-48) | +0.11 | -1.50 | -166 |  |
| (0.445, 4.846] | 111 | 34% (26-43) | -0.75 | -2.13 | -236 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.574] | 113 | 42% (34-52) | +0.23 | -1.15 | -130 |  |
| (-0.574, 0.31] | 112 | 38% (29-47) | +0.08 | -1.05 | -118 |  |
| (0.31, 9.926] | 113 | 38% (30-47) | -0.34 | -1.84 | -208 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 113 | 37% (29-46) | -0.55 | -1.75 | -198 |  |
| (0.0559, 0.125] | 112 | 44% (35-53) | +0.39 | -0.85 | -96 |  |
| (0.125, 0.924] | 113 | 37% (29-46) | +0.13 | -1.44 | -163 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 113 | 42% (34-52) | +0.24 | -0.74 | -84 |  |
| (0.222, 0.351] | 112 | 39% (31-49) | -0.01 | -1.61 | -180 |  |
| (0.351, 2.663] | 113 | 36% (28-45) | -0.26 | -1.70 | -193 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 113 | 35% (27-45) | -0.30 | -1.62 | -183 |  |
| (2.389, 3.611] | 112 | 48% (39-57) | +1.05 | -0.33 | -37 |  |
| (3.611, 19.488] | 113 | 35% (26-44) | -0.77 | -2.09 | -237 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 113 | 44% (35-53) | +0.24 | -0.48 | -55 |  |
| (0.104, 0.167] | 112 | 37% (28-46) | -0.28 | -1.42 | -160 |  |
| (0.167, 0.76] | 113 | 37% (29-46) | +0.01 | -2.14 | -242 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.899] | 71 | 31% (21-42) | -1.12 | -1.91 | -136 |  |
| (-0.899, 0.658] | 70 | 46% (35-57) | +0.68 | +0.11 | +8 |  |
| (0.658, 14.989] | 71 | 45% (34-57) | +0.72 | -0.01 | -0 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 73 | 42% (32-54) | -0.02 | -0.63 | -46 |  |
| (0.546, 0.885] | 73 | 42% (32-54) | +0.13 | -0.58 | -42 |  |
| (0.885, 3.799] | 73 | 36% (26-47) | -0.09 | -0.89 | -65 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 73 | 41% (31-53) | -0.03 | -0.63 | -46 |  |
| (0.909, 1.652] | 73 | 44% (33-55) | +0.42 | -0.25 | -18 |  |
| (1.652, 9.058] | 73 | 36% (26-47) | -0.37 | -1.22 | -89 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.402] | 73 | 37% (27-48) | -0.37 | -0.94 | -68 |  |
| (0.402, 0.624] | 73 | 48% (37-59) | +0.74 | +0.02 | +2 |  |
| (0.624, 4.001] | 73 | 36% (26-47) | -0.36 | -1.18 | -86 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 172, target 86, time_stop 64, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 113 | 39% | 18% | 38% |
| (0.104, 0.167] | 112 | 55% | 26% | 12% |
| (0.167, 0.76] | 113 | 58% | 33% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
