# Scalp signal analysis (trail exits)

_331 tagged trades, 40 trading days (2026-10-01 to 2026-11-25). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 331 | 44% (39-50) | -0.61 | -1.96 | -650 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 269 | -674 | -2.51 | -24 |
| skip first 30 min | 4 | -17 | -4.16 | 327 | -633 | -1.94 | +17 |
| skip when SPY is down on the day | 154 | -313 | -2.03 | 177 | -337 | -1.90 | +313 |
| skip when SPY is below its VWAP | 142 | -333 | -2.35 | 189 | -317 | -1.68 | +333 |
| skip when SPY fell over the last 15 min | 110 | -215 | -1.96 | 221 | -435 | -1.97 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 82 | -212 | -2.58 | 249 | -438 | -1.76 | +212 |
| skip stock not beating SPY over 15 min | 52 | -118 | -2.26 | 279 | -532 | -1.91 | +118 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 261 | -399 | -1.53 | +251 |
| skip volume spikes above 5x average | 71 | -243 | -3.43 | 260 | -406 | -1.56 | +243 |
| skip when the stop is inside normal noise (range > stop) | 49 | -66 | -1.34 | 282 | -584 | -2.07 | +66 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 53 | -78 | -1.48 | 278 | -571 | -2.06 | +78 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 140 | -425 | -3.04 | 191 | -225 | -1.18 | +425 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 48% (33-63) | -0.54 | -2.15 | -86 |  |
| 60-240 | 140 | 42% (34-50) | -1.09 | -2.22 | -310 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 96 | 48% (38-58) | -0.39 | -1.36 | -131 |  |
| -0.2 to 0 | 58 | 43% (31-56) | -1.17 | -3.14 | -182 |  |
| 0 to 0.2 | 70 | 36% (26-47) | -1.54 | -2.84 | -199 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 142 | 42% (34-50) | -0.89 | -2.35 | -333 |  |
| above VWAP | 189 | 47% (40-54) | -0.40 | -1.68 | -317 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.117] | 111 | 42% (34-52) | -0.49 | -1.48 | -164 |  |
| (0.117, 0.37] | 110 | 52% (43-61) | -0.21 | -1.64 | -180 |  |
| (0.37, 5.591] | 110 | 39% (30-48) | -1.13 | -2.78 | -306 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.139] | 109 | 52% (43-61) | +0.42 | -0.67 | -73 |  |
| (0.139, 0.446] | 109 | 41% (32-51) | -1.01 | -2.63 | -287 |  |
| (0.446, 4.846] | 109 | 40% (32-50) | -1.13 | -2.51 | -274 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.576] | 111 | 48% (39-57) | -0.46 | -1.86 | -206 |  |
| (-0.576, 0.291] | 110 | 45% (36-55) | -0.11 | -1.25 | -137 |  |
| (0.291, 9.926] | 110 | 40% (31-49) | -1.27 | -2.79 | -307 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 111 | 42% (34-52) | -1.07 | -2.28 | -253 |  |
| (0.0561, 0.126] | 110 | 49% (40-58) | +0.15 | -1.11 | -122 |  |
| (0.126, 0.924] | 110 | 42% (33-51) | -0.90 | -2.49 | -274 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.221] | 111 | 46% (37-55) | +0.01 | -0.97 | -108 |  |
| (0.221, 0.35] | 110 | 47% (38-57) | -0.57 | -2.19 | -241 |  |
| (0.35, 2.663] | 110 | 40% (31-49) | -1.27 | -2.74 | -301 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 111 | 44% (35-53) | -0.52 | -1.84 | -205 |  |
| (2.39, 3.611] | 110 | 54% (44-63) | +0.78 | -0.61 | -67 |  |
| (3.611, 19.488] | 110 | 35% (27-45) | -2.09 | -3.44 | -379 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 111 | 48% (39-57) | +0.07 | -0.66 | -73 |  |
| (0.104, 0.167] | 110 | 45% (36-54) | -1.01 | -2.17 | -239 |  |
| (0.167, 0.76] | 110 | 41% (32-50) | -0.89 | -3.08 | -339 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.92] | 69 | 46% (35-58) | -1.10 | -1.90 | -131 |  |
| (-0.92, 0.624] | 68 | 51% (40-63) | -0.19 | -0.74 | -51 |  |
| (0.624, 14.989] | 68 | 57% (46-68) | -0.20 | -0.92 | -63 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 71 | 49% (38-61) | -0.55 | -1.17 | -83 |  |
| (0.546, 0.887] | 70 | 56% (44-67) | -0.48 | -1.18 | -82 |  |
| (0.887, 3.799] | 71 | 49% (38-61) | -0.70 | -1.49 | -106 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 72 | 53% (41-64) | -0.88 | -1.45 | -105 |  |
| (0.952, 1.68] | 69 | 48% (36-59) | -0.76 | -1.46 | -100 |  |
| (1.68, 9.058] | 71 | 54% (42-65) | -0.09 | -0.93 | -66 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 71 | 45% (34-57) | -0.88 | -1.46 | -104 |  |
| (0.409, 0.624] | 70 | 63% (51-73) | +0.01 | -0.70 | -49 | ▲ |
| (0.624, 4.001] | 71 | 46% (35-58) | -0.85 | -1.67 | -118 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 144, stop 141, time_stop 36, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 111 | 33% | 34% | 28% |
| (0.104, 0.167] | 110 | 47% | 46% | 3% |
| (0.167, 0.76] | 110 | 47% | 50% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
