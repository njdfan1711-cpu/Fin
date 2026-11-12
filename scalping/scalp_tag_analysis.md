# Scalp signal analysis (fixed exits)

_264 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 264 | 41% (35-47) | +0.15 | -1.38 | -365 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -21 | -0.45 | 217 | -344 | -1.59 | +21 |
| skip first 30 min | 3 | -15 | -4.90 | 261 | -351 | -1.34 | +15 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 165 | -266 | -1.61 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 152 | -187 | -1.23 | +178 |
| skip when SPY fell over the last 15 min | 94 | -132 | -1.40 | 170 | -234 | -1.37 | +132 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 65 | -180 | -2.77 | 199 | -185 | -0.93 | +180 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 222 | -326 | -1.47 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 206 | -150 | -0.73 | +215 |
| skip volume spikes above 5x average | 50 | -115 | -2.30 | 214 | -251 | -1.17 | +115 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 238 | -359 | -1.51 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 36 | -31 | -0.87 | 228 | -334 | -1.46 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 140 | -39 | -0.28 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 106 | 40% (31-49) | +0.10 | -1.21 | -129 |  |
| 240-375 | 74 | 32% (23-44) | -1.24 | -3.01 | -222 |  |
| 375-390 | 47 | 47% (33-61) | +1.07 | -0.45 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 97 | 42% (33-52) | +0.03 | -1.46 | -141 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 152 | 40% (33-48) | +0.20 | -1.23 | -187 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 88 | 40% (30-50) | +0.07 | -1.15 | -101 |  |
| (0.129, 0.375] | 88 | 45% (35-56) | +0.52 | -1.03 | -90 |  |
| (0.375, 5.591] | 88 | 36% (27-47) | -0.14 | -1.98 | -174 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.117] | 87 | 46% (36-56) | +0.68 | -0.52 | -45 |  |
| (0.117, 0.44] | 87 | 43% (33-53) | +0.76 | -1.04 | -91 |  |
| (0.44, 4.846] | 87 | 34% (25-45) | -0.83 | -2.47 | -215 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 88 | 44% (34-55) | +0.64 | -1.09 | -96 |  |
| (-0.367, 0.4] | 88 | 45% (35-56) | +0.96 | -0.16 | -15 |  |
| (0.4, 5.005] | 88 | 32% (23-42) | -1.15 | -2.89 | -255 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 88 | 41% (31-51) | -0.08 | -1.44 | -127 |  |
| (0.0559, 0.125] | 88 | 45% (35-56) | +0.61 | -0.83 | -73 |  |
| (0.125, 0.924] | 88 | 35% (26-46) | -0.09 | -1.88 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.215] | 88 | 43% (33-54) | +0.27 | -0.80 | -70 |  |
| (0.215, 0.333] | 88 | 42% (32-52) | +0.39 | -1.37 | -121 |  |
| (0.333, 2.663] | 88 | 36% (27-47) | -0.22 | -1.98 | -174 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.35] | 88 | 38% (28-48) | +0.01 | -1.47 | -130 |  |
| (2.35, 3.538] | 88 | 48% (38-58) | +0.83 | -0.71 | -63 |  |
| (3.538, 18.762] | 88 | 36% (27-47) | -0.39 | -1.97 | -173 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 88 | 48% (38-58) | +0.63 | -0.14 | -13 |  |
| (0.103, 0.161] | 88 | 35% (26-46) | -0.42 | -1.59 | -140 |  |
| (0.161, 0.76] | 88 | 39% (29-49) | +0.24 | -2.41 | -212 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 46 | 35% (23-49) | -0.63 | -1.42 | -65 |  |
| (-0.938, 0.615] | 46 | 50% (36-64) | +1.26 | +0.66 | +30 |  |
| (0.615, 7.522] | 46 | 46% (32-60) | +0.69 | -0.05 | -2 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 49 | 47% (34-61) | +0.55 | -0.10 | -5 |  |
| (0.541, 0.832] | 48 | 40% (27-54) | -0.16 | -0.86 | -41 |  |
| (0.832, 3.799] | 48 | 42% (29-56) | +0.50 | -0.32 | -16 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.841] | 49 | 45% (32-59) | +0.42 | -0.17 | -8 |  |
| (0.841, 1.467] | 48 | 44% (31-58) | +0.61 | -0.09 | -4 |  |
| (1.467, 9.058] | 48 | 40% (27-54) | -0.14 | -1.02 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.377] | 49 | 43% (30-57) | +0.17 | -0.41 | -20 |  |
| (0.377, 0.587] | 48 | 46% (33-60) | +0.59 | -0.15 | -7 |  |
| (0.587, 4.001] | 48 | 40% (27-54) | +0.14 | -0.71 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 3% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 129, target 68, time_stop 54, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 88 | 34% | 17% | 42% |
| (0.103, 0.161] | 88 | 57% | 26% | 11% |
| (0.161, 0.76] | 88 | 56% | 34% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
