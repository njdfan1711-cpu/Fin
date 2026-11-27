# Scalp signal analysis (trail exits)

_334 tagged trades, 41 trading days (2026-10-01 to 2026-11-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 334 | 44% (39-49) | -0.65 | -2.00 | -668 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +24 | +0.39 | 272 | -692 | -2.54 | -24 |
| skip first 30 min | 5 | -22 | -4.48 | 329 | -646 | -1.96 | +22 |
| skip when SPY is down on the day | 156 | -324 | -2.08 | 178 | -344 | -1.93 | +324 |
| skip when SPY is below its VWAP | 143 | -339 | -2.37 | 191 | -329 | -1.72 | +339 |
| skip when SPY fell over the last 15 min | 111 | -221 | -1.99 | 223 | -447 | -2.00 | +221 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 82 | -224 | -2.74 | 252 | -444 | -1.76 | +224 |
| skip stock not beating SPY over 15 min | 52 | -118 | -2.26 | 282 | -550 | -1.95 | +118 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -251 | -3.58 | 264 | -417 | -1.58 | +251 |
| skip volume spikes above 5x average | 72 | -249 | -3.46 | 262 | -419 | -1.60 | +249 |
| skip when the stop is inside normal noise (range > stop) | 51 | -79 | -1.54 | 283 | -589 | -2.08 | +79 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 54 | -84 | -1.56 | 280 | -584 | -2.09 | +84 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 141 | -430 | -3.05 | 193 | -238 | -1.23 | +430 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 42 | 45% (31-60) | -0.73 | -2.30 | -97 |  |
| 60-240 | 141 | 42% (34-50) | -1.12 | -2.25 | -318 |  |
| 240-375 | 89 | 40% (31-51) | -1.52 | -3.12 | -278 |  |
| 375-390 | 62 | 53% (41-65) | +1.74 | +0.39 | +24 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 98 | 47% (37-57) | -0.47 | -1.45 | -142 |  |
| -0.2 to 0 | 58 | 43% (31-56) | -1.17 | -3.14 | -182 |  |
| 0 to 0.2 | 71 | 35% (25-47) | -1.60 | -2.90 | -206 |  |
| > 0.2 | 107 | 48% (38-57) | +0.10 | -1.29 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 143 | 41% (34-49) | -0.92 | -2.37 | -339 |  |
| above VWAP | 191 | 46% (39-53) | -0.45 | -1.72 | -329 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.117] | 112 | 42% (33-51) | -0.52 | -1.51 | -169 |  |
| (0.117, 0.37] | 111 | 51% (42-60) | -0.26 | -1.69 | -187 |  |
| (0.37, 5.591] | 111 | 39% (30-48) | -1.17 | -2.81 | -312 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.137] | 110 | 52% (43-61) | +0.38 | -0.71 | -78 |  |
| (0.137, 0.446] | 109 | 41% (32-51) | -1.01 | -2.63 | -287 |  |
| (0.446, 4.846] | 110 | 40% (31-49) | -1.17 | -2.55 | -281 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.576] | 112 | 47% (38-57) | -0.51 | -1.90 | -213 |  |
| (-0.576, 0.291] | 111 | 45% (36-54) | -0.15 | -1.29 | -143 |  |
| (0.291, 9.926] | 111 | 40% (31-49) | -1.29 | -2.81 | -312 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 113 | 42% (33-51) | -1.13 | -2.34 | -264 |  |
| (0.0561, 0.126] | 110 | 49% (40-58) | +0.15 | -1.11 | -122 |  |
| (0.126, 0.924] | 111 | 41% (33-51) | -0.95 | -2.54 | -282 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.221] | 112 | 46% (37-55) | -0.02 | -1.01 | -113 |  |
| (0.221, 0.351] | 111 | 47% (38-56) | -0.62 | -2.23 | -248 |  |
| (0.351, 2.663] | 111 | 40% (31-49) | -1.31 | -2.77 | -307 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 112 | 44% (35-53) | -0.57 | -1.89 | -212 |  |
| (2.39, 3.611] | 111 | 53% (44-62) | +0.74 | -0.65 | -72 |  |
| (3.611, 19.488] | 111 | 35% (27-44) | -2.12 | -3.46 | -384 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 112 | 47% (38-57) | +0.02 | -0.73 | -81 |  |
| (0.105, 0.168] | 111 | 45% (36-54) | -0.96 | -2.10 | -233 |  |
| (0.168, 0.76] | 111 | 40% (31-49) | -1.01 | -3.18 | -353 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.913] | 70 | 46% (35-57) | -1.17 | -1.96 | -137 |  |
| (-0.913, 0.638] | 69 | 51% (39-62) | -0.25 | -0.81 | -56 |  |
| (0.638, 14.989] | 69 | 57% (45-68) | -0.27 | -1.00 | -69 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.549] | 72 | 50% (39-61) | -0.50 | -1.12 | -80 |  |
| (0.549, 0.889] | 71 | 55% (43-66) | -0.53 | -1.24 | -88 |  |
| (0.889, 3.799] | 72 | 47% (36-59) | -0.88 | -1.67 | -121 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.934] | 72 | 51% (40-63) | -1.02 | -1.62 | -117 |  |
| (0.934, 1.68] | 71 | 48% (37-59) | -0.72 | -1.40 | -99 |  |
| (1.68, 9.058] | 72 | 53% (41-64) | -0.17 | -1.02 | -73 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 72 | 44% (34-56) | -0.93 | -1.51 | -109 |  |
| (0.409, 0.627] | 71 | 62% (50-72) | -0.07 | -0.78 | -55 | ▲ |
| (0.627, 4.001] | 72 | 46% (35-57) | -0.91 | -1.74 | -125 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.15%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 43%
- Exit mix: trail_stop 144, stop 143, time_stop 37, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 112 | 34% | 34% | 28% |
| (0.105, 0.168] | 111 | 46% | 47% | 4% |
| (0.168, 0.76] | 111 | 49% | 49% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
