# Scalp signal analysis (trail exits)

_250 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 250 | 42% (36-48) | -0.67 | -2.25 | -561 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -3 | -0.07 | 206 | -558 | -2.71 | +3 |
| skip first 30 min | 2 | -3 | -1.70 | 248 | -558 | -2.25 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 151 | -293 | -1.94 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 138 | -235 | -1.71 | +326 |
| skip when SPY fell over the last 15 min | 92 | -202 | -2.20 | 158 | -359 | -2.27 | +202 |
| skip over-extended (30-min run in top quarter, > 0.51%) | 62 | -233 | -3.75 | 188 | -329 | -1.75 | +233 |
| skip stock not beating SPY over 15 min | 41 | -85 | -2.08 | 209 | -476 | -2.28 | +85 |
| skip afternoon entries (2:00-3:45 PM) | 54 | -228 | -4.21 | 196 | -334 | -1.70 | +228 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 202 | -394 | -1.95 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 224 | -521 | -2.32 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 33 | -48 | -1.46 | 217 | -513 | -2.37 | +48 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 121 | -413 | -3.41 | 129 | -148 | -1.15 | +413 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 100 | 39% (30-49) | -1.00 | -2.34 | -234 |  |
| 240-375 | 70 | 37% (27-49) | -1.82 | -3.65 | -256 |  |
| 375-390 | 44 | 48% (34-62) | +1.52 | -0.07 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 67 | 34% (24-46) | -1.60 | -2.92 | -196 |  |
| > 0.2 | 84 | 48% (37-58) | +0.46 | -1.16 | -97 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 138 | 46% (38-54) | -0.20 | -1.71 | -235 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 84 | 40% (31-51) | -0.06 | -1.31 | -110 |  |
| (0.133, 0.382] | 83 | 52% (41-62) | -0.28 | -1.86 | -154 |  |
| (0.382, 5.591] | 83 | 33% (23-43) | -1.67 | -3.58 | -297 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.108] | 83 | 48% (38-59) | +0.46 | -0.74 | -62 |  |
| (0.108, 0.433] | 82 | 41% (31-52) | -0.91 | -2.79 | -229 |  |
| (0.433, 4.846] | 83 | 35% (26-46) | -1.54 | -3.22 | -267 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.379] | 84 | 45% (35-56) | -0.79 | -2.58 | -217 |  |
| (-0.379, 0.394] | 83 | 47% (37-58) | +0.53 | -0.60 | -50 |  |
| (0.394, 4.204] | 83 | 33% (23-43) | -1.74 | -3.56 | -295 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 84 | 43% (33-54) | -0.94 | -2.33 | -196 |  |
| (0.056, 0.127] | 84 | 45% (35-56) | +0.30 | -1.18 | -99 |  |
| (0.127, 0.924] | 82 | 37% (27-47) | -1.37 | -3.24 | -266 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 84 | 44% (34-55) | +0.16 | -0.92 | -78 |  |
| (0.212, 0.335] | 83 | 45% (34-55) | -0.73 | -2.57 | -213 |  |
| (0.335, 2.663] | 83 | 36% (27-47) | -1.44 | -3.26 | -271 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.318] | 84 | 42% (32-52) | -0.55 | -2.04 | -172 |  |
| (2.318, 3.632] | 83 | 47% (37-58) | +0.40 | -1.21 | -101 |  |
| (3.632, 18.762] | 83 | 36% (27-47) | -1.85 | -3.48 | -289 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 47% (37-58) | +0.27 | -0.51 | -43 |  |
| (0.102, 0.16] | 82 | 43% (33-53) | -1.02 | -2.21 | -181 |  |
| (0.16, 0.76] | 83 | 35% (26-46) | -1.28 | -4.06 | -337 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 42 | 40% (27-56) | -1.59 | -2.41 | -101 |  |
| (-0.974, 0.613] | 41 | 56% (41-70) | +0.40 | -0.19 | -8 |  |
| (0.613, 7.522] | 41 | 56% (41-70) | -0.41 | -1.14 | -47 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.536] | 44 | 48% (34-62) | -0.63 | -1.27 | -56 |  |
| (0.536, 0.835] | 43 | 53% (39-67) | -0.91 | -1.61 | -69 |  |
| (0.835, 3.799] | 44 | 50% (36-64) | -0.46 | -1.31 | -58 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.832] | 44 | 48% (34-62) | -1.29 | -1.86 | -82 |  |
| (0.832, 1.463] | 43 | 53% (39-67) | -0.21 | -0.93 | -40 |  |
| (1.463, 9.058] | 44 | 50% (36-64) | -0.47 | -1.38 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.375] | 44 | 48% (34-62) | -0.50 | -1.07 | -47 |  |
| (0.375, 0.594] | 43 | 58% (43-72) | -0.59 | -1.35 | -58 | ▲ |
| (0.594, 4.001] | 44 | 45% (32-60) | -0.89 | -1.77 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 109, trail_stop 104, time_stop 29, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 32% | 33% | 29% |
| (0.102, 0.16] | 82 | 49% | 46% | 2% |
| (0.16, 0.76] | 83 | 51% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
