# Scalp signal analysis (fixed exits)

_263 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 263 | 40% (35-46) | +0.11 | -1.42 | -374 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -21 | -0.45 | 216 | -353 | -1.63 | +21 |
| skip first 30 min | 3 | -15 | -4.90 | 260 | -360 | -1.38 | +15 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 164 | -275 | -1.68 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 151 | -196 | -1.30 | +178 |
| skip when SPY fell over the last 15 min | 94 | -132 | -1.40 | 169 | -243 | -1.44 | +132 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 65 | -180 | -2.77 | 198 | -194 | -0.98 | +180 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 221 | -335 | -1.51 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 205 | -159 | -0.78 | +215 |
| skip volume spikes above 5x average | 49 | -124 | -2.53 | 214 | -251 | -1.17 | +124 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 237 | -368 | -1.55 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 36 | -31 | -0.87 | 227 | -343 | -1.51 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 139 | -48 | -0.35 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 105 | 39% (30-49) | +0.01 | -1.31 | -138 |  |
| 240-375 | 74 | 32% (23-44) | -1.24 | -3.01 | -222 |  |
| 375-390 | 47 | 47% (33-61) | +1.07 | -0.45 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 96 | 42% (32-52) | -0.07 | -1.57 | -150 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 151 | 40% (32-48) | +0.14 | -1.30 | -196 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 88 | 40% (30-50) | +0.08 | -1.15 | -101 |  |
| (0.133, 0.376] | 87 | 45% (35-55) | +0.40 | -1.14 | -100 |  |
| (0.376, 5.591] | 88 | 36% (27-47) | -0.14 | -1.98 | -174 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.117] | 87 | 46% (36-56) | +0.68 | -0.52 | -45 |  |
| (0.117, 0.44] | 86 | 42% (32-52) | +0.65 | -1.16 | -100 |  |
| (0.44, 4.846] | 87 | 34% (25-45) | -0.83 | -2.47 | -215 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 88 | 44% (34-55) | +0.64 | -1.09 | -96 |  |
| (-0.367, 0.398] | 87 | 45% (35-55) | +0.85 | -0.28 | -24 |  |
| (0.398, 5.005] | 88 | 32% (23-42) | -1.14 | -2.89 | -254 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 88 | 41% (31-51) | -0.08 | -1.44 | -127 |  |
| (0.0559, 0.126] | 87 | 45% (35-55) | +0.51 | -0.94 | -82 |  |
| (0.126, 0.924] | 88 | 35% (26-46) | -0.09 | -1.88 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.214] | 88 | 43% (33-54) | +0.27 | -0.80 | -70 |  |
| (0.214, 0.334] | 87 | 41% (32-52) | +0.29 | -1.49 | -130 |  |
| (0.334, 2.663] | 88 | 36% (27-47) | -0.22 | -1.98 | -174 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.348] | 88 | 38% (28-48) | +0.01 | -1.47 | -130 |  |
| (2.348, 3.475] | 87 | 47% (37-58) | +0.74 | -0.81 | -70 |  |
| (3.475, 18.762] | 88 | 36% (27-47) | -0.40 | -1.98 | -174 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 88 | 48% (38-58) | +0.63 | -0.14 | -13 |  |
| (0.103, 0.161] | 87 | 36% (26-46) | -0.36 | -1.53 | -133 |  |
| (0.161, 0.76] | 88 | 38% (28-48) | +0.06 | -2.60 | -228 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.918] | 46 | 35% (23-49) | -0.76 | -1.57 | -72 |  |
| (-0.918, 0.616] | 45 | 49% (35-63) | +1.22 | +0.63 | +28 |  |
| (0.616, 7.522] | 46 | 46% (32-60) | +0.69 | -0.05 | -2 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.538] | 48 | 46% (33-60) | +0.35 | -0.30 | -15 |  |
| (0.538, 0.834] | 48 | 40% (27-54) | -0.15 | -0.84 | -41 |  |
| (0.834, 3.799] | 48 | 42% (29-56) | +0.50 | -0.32 | -16 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.837] | 48 | 44% (31-58) | +0.29 | -0.30 | -14 |  |
| (0.837, 1.475] | 48 | 44% (31-58) | +0.55 | -0.15 | -7 |  |
| (1.475, 9.058] | 48 | 40% (27-54) | -0.14 | -1.02 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.376] | 48 | 42% (29-56) | +0.03 | -0.55 | -27 |  |
| (0.376, 0.576] | 48 | 46% (33-60) | +0.54 | -0.21 | -10 |  |
| (0.576, 4.001] | 48 | 40% (27-54) | +0.14 | -0.71 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 3% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 129, target 67, time_stop 54, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 88 | 34% | 17% | 42% |
| (0.103, 0.161] | 87 | 56% | 26% | 11% |
| (0.161, 0.76] | 88 | 57% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
