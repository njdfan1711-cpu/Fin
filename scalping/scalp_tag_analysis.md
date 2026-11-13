# Scalp signal analysis (fixed exits)

_269 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 269 | 41% (35-46) | +0.12 | -1.39 | -374 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -28 | -0.58 | 221 | -346 | -1.57 | +28 |
| skip first 30 min | 3 | -15 | -4.90 | 266 | -360 | -1.35 | +15 |
| skip when SPY is down on the day | 100 | -106 | -1.06 | 169 | -268 | -1.59 | +106 |
| skip when SPY is below its VWAP | 117 | -187 | -1.60 | 152 | -187 | -1.23 | +187 |
| skip when SPY fell over the last 15 min | 99 | -141 | -1.42 | 170 | -234 | -1.37 | +141 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 67 | -177 | -2.65 | 202 | -197 | -0.97 | +177 |
| skip stock not beating SPY over 15 min | 43 | -46 | -1.06 | 226 | -328 | -1.45 | +46 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -212 | -3.53 | 209 | -162 | -0.78 | +212 |
| skip volume spikes above 5x average | 54 | -117 | -2.17 | 215 | -257 | -1.20 | +117 |
| skip when the stop is inside normal noise (range > stop) | 27 | -13 | -0.48 | 242 | -361 | -1.49 | +13 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 38 | -29 | -0.76 | 231 | -345 | -1.50 | +29 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 145 | -48 | -0.33 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 108 | 40% (31-49) | +0.06 | -1.24 | -134 |  |
| 240-375 | 76 | 33% (23-44) | -1.16 | -2.89 | -220 |  |
| 375-390 | 48 | 46% (33-60) | +0.92 | -0.58 | -28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 49 | 47% (34-61) | +1.08 | -0.17 | -8 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 117 | 41% (33-50) | +0.02 | -1.60 | -187 |  |
| above VWAP | 152 | 40% (33-48) | +0.20 | -1.23 | -187 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 90 | 40% (30-50) | +0.12 | -1.09 | -98 |  |
| (0.133, 0.38] | 89 | 45% (35-55) | +0.39 | -1.14 | -101 |  |
| (0.38, 5.591] | 90 | 37% (27-47) | -0.14 | -1.95 | -175 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 89 | 46% (36-56) | +0.70 | -0.48 | -42 |  |
| (0.118, 0.442] | 88 | 42% (32-52) | +0.59 | -1.29 | -113 |  |
| (0.442, 4.846] | 89 | 35% (26-45) | -0.77 | -2.29 | -204 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 90 | 44% (35-55) | +0.57 | -1.13 | -101 |  |
| (-0.367, 0.418] | 89 | 45% (35-55) | +0.88 | -0.24 | -21 |  |
| (0.418, 9.926] | 90 | 32% (23-42) | -1.08 | -2.79 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 90 | 40% (30-50) | -0.21 | -1.55 | -140 |  |
| (0.0559, 0.127] | 89 | 46% (36-56) | +0.69 | -0.75 | -66 |  |
| (0.127, 0.924] | 90 | 36% (26-46) | -0.11 | -1.87 | -168 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.216] | 90 | 43% (34-54) | +0.23 | -0.83 | -75 |  |
| (0.216, 0.339] | 89 | 43% (33-53) | +0.53 | -1.22 | -109 |  |
| (0.339, 2.663] | 90 | 36% (26-46) | -0.39 | -2.12 | -191 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.36] | 90 | 38% (28-48) | -0.04 | -1.50 | -135 |  |
| (2.36, 3.625] | 89 | 47% (37-57) | +0.76 | -0.77 | -68 |  |
| (3.625, 19.488] | 90 | 37% (27-47) | -0.35 | -1.90 | -171 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 91 | 47% (37-57) | +0.50 | -0.27 | -25 |  |
| (0.104, 0.163] | 88 | 35% (26-46) | -0.43 | -1.61 | -142 |  |
| (0.163, 0.76] | 90 | 39% (29-49) | +0.28 | -2.31 | -208 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.956] | 48 | 35% (23-50) | -0.52 | -1.30 | -62 |  |
| (-0.956, 0.616] | 47 | 51% (37-65) | +1.27 | +0.67 | +32 |  |
| (0.616, 7.522] | 48 | 44% (31-58) | +0.42 | -0.32 | -15 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.538] | 50 | 46% (33-60) | +0.25 | -0.40 | -20 |  |
| (0.538, 0.837] | 52 | 42% (30-56) | +0.18 | -0.51 | -26 |  |
| (0.837, 3.799] | 48 | 40% (27-54) | +0.32 | -0.50 | -24 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.846] | 50 | 44% (31-58) | +0.29 | -0.30 | -15 |  |
| (0.846, 1.46] | 50 | 44% (31-58) | +0.65 | -0.05 | -2 |  |
| (1.46, 9.058] | 50 | 40% (28-54) | -0.21 | -1.07 | -53 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.38] | 50 | 42% (29-56) | +0.05 | -0.53 | -27 |  |
| (0.38, 0.594] | 50 | 46% (33-60) | +0.53 | -0.20 | -10 |  |
| (0.594, 4.001] | 50 | 40% (28-54) | +0.16 | -0.67 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 132, target 69, time_stop 55, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 91 | 35% | 16% | 42% |
| (0.104, 0.163] | 88 | 57% | 26% | 11% |
| (0.163, 0.76] | 90 | 56% | 34% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
