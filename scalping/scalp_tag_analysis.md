# Scalp signal analysis (fixed exits)

_268 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 268 | 41% (35-47) | +0.14 | -1.37 | -368 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -28 | -0.58 | 220 | -340 | -1.54 | +28 |
| skip first 30 min | 3 | -15 | -4.90 | 265 | -353 | -1.33 | +15 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 169 | -268 | -1.59 | +99 |
| skip when SPY is below its VWAP | 116 | -180 | -1.56 | 152 | -187 | -1.23 | +180 |
| skip when SPY fell over the last 15 min | 98 | -134 | -1.37 | 170 | -234 | -1.37 | +134 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 66 | -170 | -2.58 | 202 | -197 | -0.98 | +170 |
| skip stock not beating SPY over 15 min | 43 | -46 | -1.06 | 225 | -322 | -1.43 | +46 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -212 | -3.53 | 208 | -156 | -0.75 | +212 |
| skip volume spikes above 5x average | 53 | -111 | -2.09 | 215 | -257 | -1.20 | +111 |
| skip when the stop is inside normal noise (range > stop) | 27 | -13 | -0.48 | 241 | -355 | -1.47 | +13 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 37 | -22 | -0.59 | 231 | -346 | -1.50 | +22 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 144 | -41 | -0.29 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 107 | 40% (31-50) | +0.11 | -1.19 | -127 |  |
| 240-375 | 76 | 33% (23-44) | -1.16 | -2.89 | -220 |  |
| 375-390 | 48 | 46% (33-60) | +0.92 | -0.58 | -28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 101 | 43% (33-52) | +0.02 | -1.42 | -144 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 116 | 41% (33-50) | +0.07 | -1.56 | -180 |  |
| above VWAP | 152 | 40% (33-48) | +0.20 | -1.23 | -187 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 90 | 40% (30-50) | +0.12 | -1.09 | -98 |  |
| (0.132, 0.382] | 89 | 46% (36-56) | +0.56 | -0.97 | -86 |  |
| (0.382, 5.591] | 89 | 36% (27-46) | -0.24 | -2.06 | -183 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 89 | 46% (36-56) | +0.70 | -0.48 | -42 |  |
| (0.118, 0.44] | 88 | 42% (32-52) | +0.59 | -1.29 | -113 |  |
| (0.44, 4.846] | 88 | 35% (26-46) | -0.71 | -2.24 | -197 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 90 | 44% (35-55) | +0.58 | -1.13 | -101 |  |
| (-0.367, 0.426] | 89 | 45% (35-55) | +0.88 | -0.23 | -21 |  |
| (0.426, 9.926] | 89 | 33% (24-43) | -1.03 | -2.76 | -246 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 90 | 41% (32-51) | -0.11 | -1.45 | -131 |  |
| (0.056, 0.127] | 90 | 44% (35-55) | +0.55 | -0.87 | -79 |  |
| (0.127, 0.924] | 88 | 36% (27-47) | -0.02 | -1.80 | -159 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 90 | 44% (35-55) | +0.42 | -0.65 | -58 |  |
| (0.217, 0.34] | 89 | 42% (32-52) | +0.38 | -1.37 | -122 |  |
| (0.34, 2.663] | 89 | 36% (27-46) | -0.36 | -2.10 | -187 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 90 | 38% (28-48) | -0.04 | -1.50 | -135 |  |
| (2.356, 3.611] | 89 | 47% (37-57) | +0.76 | -0.77 | -68 |  |
| (3.611, 19.488] | 89 | 37% (28-47) | -0.29 | -1.85 | -165 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 90 | 48% (38-58) | +0.57 | -0.20 | -18 |  |
| (0.104, 0.164] | 89 | 35% (26-45) | -0.49 | -1.72 | -153 |  |
| (0.164, 0.76] | 89 | 39% (30-50) | +0.35 | -2.21 | -197 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 48 | 35% (23-50) | -0.52 | -1.30 | -62 |  |
| (-0.974, 0.613] | 47 | 51% (37-65) | +1.27 | +0.67 | +32 |  |
| (0.613, 7.522] | 47 | 45% (31-59) | +0.55 | -0.18 | -9 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.542] | 50 | 48% (35-61) | +0.57 | -0.07 | -4 |  |
| (0.542, 0.837] | 51 | 41% (29-55) | -0.01 | -0.71 | -36 |  |
| (0.837, 3.799] | 48 | 40% (27-54) | +0.32 | -0.50 | -24 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.852] | 50 | 44% (31-58) | +0.29 | -0.29 | -15 |  |
| (0.852, 1.463] | 49 | 45% (32-59) | +0.79 | +0.08 | +4 |  |
| (1.463, 9.058] | 50 | 40% (28-54) | -0.21 | -1.07 | -53 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.382] | 50 | 42% (29-56) | +0.05 | -0.53 | -27 |  |
| (0.382, 0.594] | 49 | 47% (34-61) | +0.66 | -0.08 | -4 |  |
| (0.594, 4.001] | 50 | 40% (28-54) | +0.16 | -0.67 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 131, target 69, time_stop 55, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 90 | 34% | 17% | 42% |
| (0.104, 0.164] | 89 | 57% | 26% | 11% |
| (0.164, 0.76] | 89 | 55% | 35% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
