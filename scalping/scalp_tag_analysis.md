# Scalp signal analysis (fixed exits)

_318 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 318 | 40% (35-45) | +0.05 | -1.33 | -424 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 258 | -437 | -1.69 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 314 | -402 | -1.28 | +21 |
| skip when SPY is down on the day | 147 | -158 | -1.07 | 171 | -266 | -1.56 | +158 |
| skip when SPY is below its VWAP | 140 | -185 | -1.32 | 178 | -239 | -1.34 | +185 |
| skip when SPY fell over the last 15 min | 105 | -118 | -1.12 | 213 | -306 | -1.44 | +118 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -176 | -2.23 | 239 | -248 | -1.04 | +176 |
| skip stock not beating SPY over 15 min | 49 | -70 | -1.42 | 269 | -354 | -1.32 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -225 | -3.26 | 249 | -199 | -0.80 | +225 |
| skip volume spikes above 5x average | 68 | -163 | -2.39 | 250 | -261 | -1.04 | +163 |
| skip when the stop is inside normal noise (range > stop) | 44 | -35 | -0.80 | 274 | -389 | -1.42 | +35 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.73%) | 50 | -55 | -1.11 | 268 | -368 | -1.37 | +55 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 180 | -61 | -0.34 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 131 | 37% (30-46) | -0.33 | -1.49 | -195 |  |
| 240-375 | 88 | 32% (23-42) | -1.25 | -2.86 | -252 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 41% (31-51) | +0.22 | -0.76 | -69 |  |
| -0.2 to 0 | 56 | 43% (31-56) | +0.43 | -1.57 | -88 |  |
| 0 to 0.2 | 69 | 32% (22-44) | -0.59 | -1.90 | -131 |  |
| > 0.2 | 102 | 43% (34-53) | +0.12 | -1.32 | -135 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | +0.14 | -1.32 | -185 |  |
| above VWAP | 178 | 39% (32-46) | -0.03 | -1.34 | -239 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 106 | 38% (29-47) | -0.30 | -1.39 | -147 |  |
| (0.129, 0.374] | 106 | 44% (35-54) | +0.47 | -0.92 | -98 |  |
| (0.374, 5.591] | 106 | 38% (29-47) | -0.03 | -1.69 | -179 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.134] | 105 | 48% (38-57) | +0.84 | -0.25 | -27 |  |
| (0.134, 0.455] | 104 | 38% (30-48) | +0.10 | -1.58 | -164 |  |
| (0.455, 4.846] | 105 | 35% (27-45) | -0.62 | -2.02 | -212 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.583] | 106 | 45% (36-55) | +0.64 | -0.73 | -77 |  |
| (-0.583, 0.325] | 106 | 38% (29-47) | +0.10 | -1.12 | -119 |  |
| (0.325, 9.926] | 106 | 37% (28-46) | -0.59 | -2.15 | -228 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 106 | 40% (31-49) | -0.33 | -1.57 | -167 |  |
| (0.0561, 0.127] | 106 | 44% (35-54) | +0.54 | -0.74 | -78 |  |
| (0.127, 0.924] | 106 | 36% (27-45) | -0.06 | -1.69 | -179 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.222] | 106 | 43% (34-53) | +0.31 | -0.68 | -72 |  |
| (0.222, 0.351] | 106 | 40% (31-49) | +0.02 | -1.64 | -174 |  |
| (0.351, 2.663] | 106 | 37% (28-46) | -0.19 | -1.68 | -178 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.38] | 106 | 36% (27-45) | -0.28 | -1.64 | -174 |  |
| (2.38, 3.634] | 106 | 49% (40-58) | +1.09 | -0.32 | -34 |  |
| (3.634, 19.488] | 106 | 35% (27-44) | -0.67 | -2.03 | -216 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 106 | 45% (36-55) | +0.35 | -0.38 | -41 |  |
| (0.104, 0.167] | 106 | 37% (28-46) | -0.28 | -1.46 | -155 |  |
| (0.167, 0.76] | 106 | 38% (29-47) | +0.08 | -2.15 | -228 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.734] | 64 | 31% (21-43) | -1.15 | -1.94 | -124 |  |
| (-0.734, 0.664] | 64 | 48% (37-60) | +0.98 | +0.43 | +28 |  |
| (0.664, 14.989] | 64 | 45% (34-57) | +0.75 | +0.02 | +1 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.552] | 67 | 43% (32-55) | +0.04 | -0.57 | -39 |  |
| (0.552, 0.884] | 66 | 44% (33-56) | +0.24 | -0.47 | -31 |  |
| (0.884, 3.799] | 66 | 36% (26-48) | +0.02 | -0.77 | -51 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.925] | 67 | 43% (32-55) | -0.02 | -0.60 | -40 |  |
| (0.925, 1.669] | 66 | 44% (33-56) | +0.60 | -0.09 | -6 |  |
| (1.669, 9.058] | 66 | 36% (26-48) | -0.28 | -1.12 | -74 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 67 | 36% (25-48) | -0.61 | -1.18 | -79 |  |
| (0.409, 0.628] | 66 | 52% (40-63) | +1.19 | +0.48 | +32 |  |
| (0.628, 4.001] | 66 | 36% (26-48) | -0.27 | -1.10 | -73 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 160, target 81, time_stop 61, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 106 | 38% | 18% | 39% |
| (0.104, 0.167] | 106 | 56% | 25% | 11% |
| (0.167, 0.76] | 106 | 58% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
