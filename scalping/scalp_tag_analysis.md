# Scalp signal analysis (fixed exits)

_317 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 317 | 40% (35-45) | +0.02 | -1.37 | -433 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 257 | -446 | -1.74 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 313 | -411 | -1.31 | +21 |
| skip when SPY is down on the day | 147 | -158 | -1.07 | 170 | -275 | -1.62 | +158 |
| skip when SPY is below its VWAP | 140 | -185 | -1.32 | 177 | -248 | -1.40 | +185 |
| skip when SPY fell over the last 15 min | 104 | -127 | -1.22 | 213 | -306 | -1.44 | +127 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 78 | -170 | -2.18 | 239 | -263 | -1.10 | +170 |
| skip stock not beating SPY over 15 min | 49 | -70 | -1.42 | 268 | -363 | -1.36 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -225 | -3.26 | 248 | -208 | -0.84 | +225 |
| skip volume spikes above 5x average | 68 | -163 | -2.39 | 249 | -270 | -1.08 | +163 |
| skip when the stop is inside normal noise (range > stop) | 43 | -44 | -1.03 | 274 | -389 | -1.42 | +44 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 50 | -63 | -1.25 | 267 | -370 | -1.39 | +63 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 179 | -70 | -0.39 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 130 | 37% (29-45) | -0.41 | -1.57 | -204 |  |
| 240-375 | 88 | 32% (23-42) | -1.25 | -2.86 | -252 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 41% (31-51) | +0.22 | -0.76 | -69 |  |
| -0.2 to 0 | 56 | 43% (31-56) | +0.43 | -1.57 | -88 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | +0.14 | -1.32 | -185 |  |
| above VWAP | 177 | 38% (32-46) | -0.08 | -1.40 | -248 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 106 | 38% (29-47) | -0.30 | -1.39 | -147 |  |
| (0.126, 0.374] | 105 | 44% (35-53) | +0.39 | -1.01 | -106 |  |
| (0.374, 5.591] | 106 | 38% (29-47) | -0.03 | -1.69 | -179 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.135] | 105 | 48% (38-57) | +0.80 | -0.30 | -31 |  |
| (0.135, 0.458] | 104 | 38% (29-47) | +0.03 | -1.65 | -171 |  |
| (0.458, 4.846] | 104 | 36% (27-45) | -0.60 | -2.01 | -209 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.585] | 106 | 45% (36-55) | +0.64 | -0.73 | -77 |  |
| (-0.585, 0.308] | 105 | 38% (29-48) | +0.15 | -1.07 | -112 |  |
| (0.308, 9.926] | 106 | 36% (27-45) | -0.73 | -2.29 | -243 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 106 | 40% (31-49) | -0.33 | -1.57 | -167 |  |
| (0.056, 0.127] | 106 | 44% (35-54) | +0.54 | -0.74 | -78 |  |
| (0.127, 0.924] | 105 | 35% (27-45) | -0.15 | -1.79 | -188 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 106 | 43% (34-53) | +0.31 | -0.68 | -72 |  |
| (0.222, 0.35] | 105 | 40% (31-50) | +0.08 | -1.51 | -159 |  |
| (0.35, 2.663] | 106 | 36% (27-45) | -0.34 | -1.90 | -202 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.384] | 106 | 35% (27-44) | -0.42 | -1.79 | -189 |  |
| (2.384, 3.635] | 105 | 50% (40-59) | +1.15 | -0.27 | -28 | ▲ |
| (3.635, 19.488] | 106 | 35% (27-44) | -0.67 | -2.03 | -216 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 106 | 45% (36-55) | +0.35 | -0.38 | -41 |  |
| (0.104, 0.167] | 105 | 36% (28-46) | -0.38 | -1.57 | -164 |  |
| (0.167, 0.76] | 106 | 38% (29-47) | +0.09 | -2.15 | -228 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.711] | 64 | 30% (20-42) | -1.39 | -2.18 | -140 |  |
| (-0.711, 0.669] | 63 | 49% (37-61) | +1.09 | +0.54 | +34 |  |
| (0.669, 14.989] | 64 | 45% (34-57) | +0.75 | +0.02 | +1 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 66 | 44% (33-56) | +0.13 | -0.49 | -32 |  |
| (0.55, 0.871] | 66 | 42% (31-54) | +0.10 | -0.61 | -40 |  |
| (0.871, 3.799] | 66 | 36% (26-48) | -0.07 | -0.86 | -57 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.923] | 66 | 42% (31-54) | -0.06 | -0.64 | -43 |  |
| (0.923, 1.652] | 66 | 45% (34-57) | +0.73 | +0.04 | +3 |  |
| (1.652, 9.058] | 66 | 35% (24-47) | -0.51 | -1.35 | -89 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 66 | 36% (26-48) | -0.53 | -1.10 | -73 |  |
| (0.409, 0.625] | 66 | 52% (40-63) | +1.19 | +0.48 | +31 |  |
| (0.625, 4.001] | 66 | 35% (24-47) | -0.50 | -1.33 | -88 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 160, target 80, time_stop 61, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 106 | 38% | 18% | 39% |
| (0.104, 0.167] | 105 | 56% | 25% | 11% |
| (0.167, 0.76] | 106 | 58% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
