# Scalp signal analysis (trail exits)

_264 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 264 | 42% (37-48) | -0.64 | -2.17 | -573 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -12 | -0.26 | 217 | -561 | -2.59 | +12 |
| skip first 30 min | 3 | -10 | -3.32 | 261 | -563 | -2.16 | +10 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 165 | -305 | -1.85 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 152 | -247 | -1.63 | +326 |
| skip when SPY fell over the last 15 min | 95 | -205 | -2.16 | 169 | -368 | -2.18 | +205 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 65 | -228 | -3.50 | 199 | -346 | -1.74 | +228 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 222 | -481 | -2.17 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 206 | -358 | -1.74 | +215 |
| skip volume spikes above 5x average | 50 | -171 | -3.41 | 214 | -403 | -1.88 | +171 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 238 | -533 | -2.24 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 36 | -57 | -1.59 | 228 | -516 | -2.26 | +57 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 140 | -158 | -1.13 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 106 | 40% (31-49) | -0.98 | -2.29 | -243 |  |
| 240-375 | 74 | 41% (30-52) | -1.51 | -3.28 | -243 |  |
| 375-390 | 47 | 47% (33-61) | +1.25 | -0.26 | -12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 97 | 48% (39-58) | +0.35 | -1.14 | -110 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 152 | 47% (39-55) | -0.20 | -1.63 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 88 | 40% (30-50) | -0.29 | -1.51 | -132 |  |
| (0.129, 0.375] | 88 | 53% (43-63) | -0.11 | -1.65 | -145 | ▲ |
| (0.375, 5.591] | 88 | 34% (25-44) | -1.53 | -3.36 | -296 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.117] | 87 | 48% (38-59) | +0.35 | -0.84 | -73 |  |
| (0.117, 0.44] | 87 | 43% (33-53) | -0.81 | -2.61 | -227 |  |
| (0.44, 4.846] | 87 | 37% (27-47) | -1.39 | -3.03 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 88 | 45% (35-56) | -0.76 | -2.49 | -219 |  |
| (-0.367, 0.4] | 88 | 48% (38-58) | +0.57 | -0.55 | -49 |  |
| (0.4, 5.005] | 88 | 34% (25-44) | -1.73 | -3.47 | -306 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 88 | 43% (33-54) | -0.89 | -2.25 | -198 |  |
| (0.0559, 0.125] | 88 | 44% (34-55) | +0.10 | -1.34 | -118 |  |
| (0.125, 0.924] | 88 | 40% (30-50) | -1.13 | -2.92 | -257 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.215] | 88 | 44% (34-55) | +0.08 | -0.99 | -87 |  |
| (0.215, 0.333] | 88 | 45% (35-56) | -0.63 | -2.40 | -211 |  |
| (0.333, 2.663] | 88 | 38% (28-48) | -1.37 | -3.13 | -276 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.35] | 88 | 41% (31-51) | -0.62 | -2.10 | -185 |  |
| (2.35, 3.538] | 88 | 50% (40-60) | +0.59 | -0.95 | -83 |  |
| (3.538, 18.762] | 88 | 36% (27-47) | -1.90 | -3.47 | -306 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 88 | 49% (39-59) | +0.44 | -0.33 | -29 |  |
| (0.103, 0.161] | 88 | 41% (31-51) | -1.26 | -2.43 | -214 |  |
| (0.161, 0.76] | 88 | 38% (28-48) | -1.10 | -3.76 | -331 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 46 | 43% (30-58) | -1.29 | -2.08 | -96 |  |
| (-0.938, 0.615] | 46 | 54% (40-68) | +0.18 | -0.42 | -19 |  |
| (0.615, 7.522] | 46 | 57% (42-70) | -0.41 | -1.15 | -53 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 49 | 51% (37-64) | -0.22 | -0.87 | -43 |  |
| (0.541, 0.832] | 48 | 52% (38-66) | -1.12 | -1.82 | -88 |  |
| (0.832, 3.799] | 48 | 50% (36-64) | -0.51 | -1.34 | -64 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.841] | 49 | 49% (36-63) | -1.21 | -1.80 | -88 |  |
| (0.841, 1.467] | 48 | 54% (40-67) | -0.14 | -0.84 | -41 |  |
| (1.467, 9.058] | 48 | 50% (36-64) | -0.49 | -1.38 | -66 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.377] | 49 | 47% (34-61) | -0.62 | -1.20 | -59 |  |
| (0.377, 0.587] | 48 | 58% (44-71) | -0.50 | -1.24 | -60 | ▲ |
| (0.587, 4.001] | 48 | 48% (34-62) | -0.74 | -1.59 | -76 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 115, trail_stop 110, time_stop 31, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 88 | 31% | 33% | 31% |
| (0.103, 0.161] | 88 | 51% | 44% | 2% |
| (0.161, 0.76] | 88 | 49% | 48% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
