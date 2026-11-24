# Scalp signal analysis (fixed exits)

_319 tagged trades, 39 trading days (2026-10-01 to 2026-11-24). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 319 | 40% (35-46) | +0.08 | -1.30 | -415 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +13 | +0.22 | 259 | -428 | -1.65 | -13 |
| skip first 30 min | 4 | -21 | -5.34 | 315 | -394 | -1.25 | +21 |
| skip when SPY is down on the day | 147 | -158 | -1.07 | 172 | -257 | -1.50 | +158 |
| skip when SPY is below its VWAP | 140 | -185 | -1.32 | 179 | -230 | -1.29 | +185 |
| skip when SPY fell over the last 15 min | 106 | -109 | -1.03 | 213 | -306 | -1.44 | +109 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 79 | -176 | -2.23 | 240 | -239 | -1.00 | +176 |
| skip stock not beating SPY over 15 min | 49 | -70 | -1.42 | 270 | -345 | -1.28 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 69 | -225 | -3.26 | 250 | -190 | -0.76 | +225 |
| skip volume spikes above 5x average | 69 | -154 | -2.23 | 250 | -261 | -1.04 | +154 |
| skip when the stop is inside normal noise (range > stop) | 45 | -26 | -0.59 | 274 | -389 | -1.42 | +26 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.73%) | 50 | -55 | -1.11 | 269 | -360 | -1.34 | +55 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -363 | -2.63 | 181 | -52 | -0.29 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 51% (36-66) | +1.88 | +0.24 | +9 |  |
| 60-240 | 132 | 38% (30-46) | -0.26 | -1.41 | -186 |  |
| 240-375 | 88 | 32% (23-42) | -1.25 | -2.86 | -252 |  |
| 375-390 | 60 | 50% (38-62) | +1.59 | +0.22 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 91 | 41% (31-51) | +0.22 | -0.76 | -69 |  |
| -0.2 to 0 | 56 | 43% (31-56) | +0.43 | -1.57 | -88 |  |
| 0 to 0.2 | 70 | 33% (23-44) | -0.44 | -1.75 | -122 |  |
| > 0.2 | 102 | 43% (34-53) | +0.12 | -1.32 | -135 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 140 | 41% (34-50) | +0.14 | -1.32 | -185 |  |
| above VWAP | 179 | 39% (32-46) | +0.03 | -1.29 | -230 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 107 | 38% (30-48) | -0.21 | -1.29 | -138 |  |
| (0.123, 0.374] | 106 | 44% (35-54) | +0.47 | -0.92 | -98 |  |
| (0.374, 5.591] | 106 | 38% (29-47) | -0.03 | -1.69 | -179 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.135] | 105 | 48% (38-57) | +0.84 | -0.25 | -27 |  |
| (0.135, 0.453] | 105 | 39% (30-49) | +0.19 | -1.48 | -155 |  |
| (0.453, 4.846] | 105 | 35% (27-45) | -0.62 | -2.02 | -212 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.581] | 107 | 45% (36-54) | +0.57 | -0.78 | -84 |  |
| (-0.581, 0.319] | 106 | 39% (30-48) | +0.24 | -0.98 | -104 |  |
| (0.319, 9.926] | 106 | 37% (28-46) | -0.59 | -2.15 | -228 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 107 | 39% (31-49) | -0.38 | -1.62 | -173 |  |
| (0.0561, 0.127] | 106 | 45% (36-55) | +0.68 | -0.60 | -63 |  |
| (0.127, 0.924] | 106 | 36% (27-45) | -0.06 | -1.69 | -179 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.223] | 107 | 43% (34-52) | +0.25 | -0.73 | -79 |  |
| (0.223, 0.351] | 106 | 40% (31-49) | +0.02 | -1.64 | -174 |  |
| (0.351, 2.663] | 106 | 38% (29-47) | -0.04 | -1.53 | -162 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.381] | 107 | 36% (27-45) | -0.33 | -1.69 | -180 |  |
| (2.381, 3.637] | 106 | 50% (41-59) | +1.17 | -0.24 | -26 | ▲ |
| (3.637, 19.488] | 106 | 35% (27-44) | -0.60 | -1.97 | -209 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 107 | 45% (36-54) | +0.29 | -0.46 | -49 |  |
| (0.105, 0.167] | 106 | 37% (28-46) | -0.28 | -1.44 | -153 |  |
| (0.167, 0.76] | 106 | 39% (30-48) | +0.23 | -2.01 | -213 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.762] | 65 | 32% (22-44) | -0.98 | -1.78 | -115 |  |
| (-0.762, 0.658] | 64 | 48% (37-60) | +0.98 | +0.43 | +28 |  |
| (0.658, 14.989] | 64 | 45% (34-57) | +0.75 | +0.02 | +1 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.553] | 67 | 43% (32-55) | +0.04 | -0.57 | -39 |  |
| (0.553, 0.887] | 66 | 44% (33-56) | +0.24 | -0.47 | -31 |  |
| (0.887, 3.799] | 67 | 37% (27-49) | +0.16 | -0.62 | -42 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.934] | 67 | 43% (32-55) | -0.02 | -0.60 | -40 |  |
| (0.934, 1.68] | 66 | 44% (33-56) | +0.60 | -0.09 | -6 |  |
| (1.68, 9.058] | 67 | 37% (27-49) | -0.13 | -0.97 | -65 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 67 | 36% (25-48) | -0.61 | -1.18 | -79 |  |
| (0.409, 0.638] | 66 | 52% (40-63) | +1.19 | +0.48 | +32 |  |
| (0.638, 4.001] | 67 | 37% (27-49) | -0.13 | -0.95 | -64 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 160, target 82, time_stop 61, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 107 | 38% | 18% | 38% |
| (0.105, 0.167] | 106 | 56% | 25% | 11% |
| (0.167, 0.76] | 106 | 57% | 34% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
