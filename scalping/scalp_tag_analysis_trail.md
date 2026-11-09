# Scalp signal analysis (trail exits)

_251 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 251 | 41% (36-48) | -0.69 | -2.27 | -569 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -3 | -0.07 | 207 | -566 | -2.73 | +3 |
| skip first 30 min | 2 | -3 | -1.70 | 249 | -565 | -2.27 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 152 | -300 | -1.98 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 139 | -243 | -1.75 | +326 |
| skip when SPY fell over the last 15 min | 92 | -202 | -2.20 | 159 | -366 | -2.30 | +202 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 62 | -233 | -3.75 | 189 | -336 | -1.78 | +233 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 209 | -476 | -2.28 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 54 | -228 | -4.21 | 197 | -341 | -1.73 | +228 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 203 | -402 | -1.98 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 225 | -528 | -2.35 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 33 | -48 | -1.46 | 218 | -521 | -2.39 | +48 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 122 | -421 | -3.45 | 129 | -148 | -1.15 | +421 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 101 | 39% (30-48) | -1.04 | -2.39 | -242 |  |
| 240-375 | 70 | 37% (27-49) | -1.82 | -3.65 | -256 |  |
| 375-390 | 44 | 48% (34-62) | +1.52 | -0.07 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 67 | 34% (24-46) | -1.60 | -2.92 | -196 |  |
| > 0.2 | 85 | 47% (37-58) | +0.39 | -1.23 | -105 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 139 | 45% (37-54) | -0.24 | -1.75 | -243 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 84 | 40% (31-51) | -0.14 | -1.40 | -117 |  |
| (0.133, 0.38] | 83 | 51% (40-61) | -0.35 | -1.93 | -161 |  |
| (0.38, 5.591] | 84 | 33% (24-44) | -1.57 | -3.47 | -291 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.109] | 83 | 48% (38-59) | +0.46 | -0.74 | -62 |  |
| (0.109, 0.428] | 83 | 41% (31-52) | -0.97 | -2.85 | -236 |  |
| (0.428, 4.846] | 83 | 35% (26-46) | -1.54 | -3.22 | -267 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.375] | 84 | 45% (35-56) | -0.79 | -2.58 | -217 |  |
| (-0.375, 0.39] | 83 | 46% (35-56) | +0.45 | -0.70 | -58 |  |
| (0.39, 4.204] | 84 | 33% (24-44) | -1.71 | -3.50 | -294 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 84 | 43% (33-54) | -0.94 | -2.33 | -196 |  |
| (0.056, 0.127] | 83 | 43% (33-54) | +0.18 | -1.32 | -110 |  |
| (0.127, 0.924] | 84 | 38% (28-49) | -1.29 | -3.13 | -263 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 84 | 44% (34-55) | +0.16 | -0.93 | -78 |  |
| (0.212, 0.334] | 83 | 43% (33-54) | -0.84 | -2.67 | -222 |  |
| (0.334, 2.663] | 84 | 37% (27-48) | -1.38 | -3.20 | -269 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.293] | 84 | 40% (31-51) | -0.72 | -2.22 | -187 |  |
| (2.293, 3.625] | 83 | 48% (38-59) | +0.57 | -1.04 | -86 |  |
| (3.625, 18.762] | 84 | 36% (26-46) | -1.90 | -3.53 | -296 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 47% (37-58) | +0.27 | -0.51 | -43 |  |
| (0.102, 0.159] | 82 | 41% (31-52) | -1.21 | -2.36 | -194 |  |
| (0.159, 0.76] | 84 | 36% (26-46) | -1.14 | -3.95 | -332 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.956] | 42 | 40% (27-56) | -1.59 | -2.41 | -101 |  |
| (-0.956, 0.601] | 41 | 56% (41-70) | +0.25 | -0.36 | -15 |  |
| (0.601, 7.522] | 42 | 55% (40-69) | -0.39 | -1.13 | -47 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 45 | 47% (33-61) | -0.75 | -1.41 | -63 |  |
| (0.533, 0.834] | 43 | 53% (39-67) | -0.91 | -1.61 | -69 |  |
| (0.834, 3.799] | 44 | 50% (36-64) | -0.46 | -1.31 | -58 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.826] | 44 | 45% (32-60) | -1.49 | -2.06 | -91 |  |
| (0.826, 1.46] | 44 | 55% (40-68) | -0.15 | -0.88 | -39 |  |
| (1.46, 9.058] | 44 | 50% (36-64) | -0.47 | -1.38 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.372] | 44 | 45% (32-60) | -0.70 | -1.28 | -56 |  |
| (0.372, 0.594] | 44 | 59% (44-72) | -0.52 | -1.27 | -56 | ▲ |
| (0.594, 4.001] | 44 | 45% (32-60) | -0.89 | -1.77 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 110, trail_stop 104, time_stop 29, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 32% | 33% | 29% |
| (0.102, 0.159] | 82 | 50% | 45% | 2% |
| (0.159, 0.76] | 84 | 50% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
