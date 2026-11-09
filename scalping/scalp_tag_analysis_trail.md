# Scalp signal analysis (trail exits)

_252 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 252 | 42% (36-48) | -0.67 | -2.25 | -567 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -3 | -0.07 | 208 | -564 | -2.71 | +3 |
| skip first 30 min | 2 | -3 | -1.70 | 250 | -564 | -2.25 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 153 | -298 | -1.95 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 140 | -241 | -1.72 | +326 |
| skip when SPY fell over the last 15 min | 93 | -200 | -2.16 | 159 | -366 | -2.30 | +200 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 63 | -230 | -3.65 | 189 | -337 | -1.78 | +230 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 210 | -474 | -2.26 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 55 | -226 | -4.10 | 197 | -341 | -1.73 | +226 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 204 | -400 | -1.96 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 226 | -526 | -2.33 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 33 | -48 | -1.46 | 219 | -519 | -2.37 | +48 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 122 | -421 | -3.45 | 130 | -146 | -1.13 | +421 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 101 | 39% (30-48) | -1.04 | -2.39 | -242 |  |
| 240-375 | 71 | 38% (28-50) | -1.76 | -3.57 | -254 |  |
| 375-390 | 44 | 48% (34-62) | +1.52 | -0.07 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 67 | 34% (24-46) | -1.60 | -2.92 | -196 |  |
| > 0.2 | 86 | 48% (37-58) | +0.41 | -1.19 | -103 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 140 | 46% (38-54) | -0.22 | -1.72 | -241 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 84 | 40% (31-51) | -0.14 | -1.40 | -117 |  |
| (0.133, 0.379] | 84 | 51% (41-62) | -0.32 | -1.89 | -159 |  |
| (0.379, 5.591] | 84 | 33% (24-44) | -1.57 | -3.47 | -291 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.11] | 84 | 49% (38-59) | +0.48 | -0.72 | -60 |  |
| (0.11, 0.422] | 83 | 41% (31-52) | -0.97 | -2.84 | -236 |  |
| (0.422, 4.846] | 83 | 35% (26-46) | -1.54 | -3.22 | -267 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.371] | 84 | 45% (35-56) | -0.79 | -2.58 | -217 |  |
| (-0.371, 0.396] | 84 | 46% (36-57) | +0.46 | -0.68 | -57 |  |
| (0.396, 5.005] | 84 | 33% (24-44) | -1.69 | -3.49 | -293 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 84 | 43% (33-54) | -0.94 | -2.33 | -196 |  |
| (0.0561, 0.126] | 84 | 44% (34-55) | +0.21 | -1.28 | -108 |  |
| (0.126, 0.924] | 84 | 38% (28-49) | -1.29 | -3.13 | -263 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 84 | 45% (35-56) | +0.26 | -0.84 | -70 |  |
| (0.212, 0.333] | 84 | 43% (33-54) | -0.90 | -2.71 | -228 |  |
| (0.333, 2.663] | 84 | 37% (27-48) | -1.38 | -3.20 | -269 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.305] | 84 | 40% (31-51) | -0.72 | -2.22 | -187 |  |
| (2.305, 3.618] | 84 | 49% (38-59) | +0.60 | -1.00 | -84 |  |
| (3.618, 18.762] | 84 | 36% (26-46) | -1.90 | -3.53 | -296 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 84 | 49% (38-59) | +0.35 | -0.42 | -35 |  |
| (0.102, 0.158] | 84 | 40% (31-51) | -1.23 | -2.38 | -200 |  |
| (0.158, 0.76] | 84 | 36% (26-46) | -1.14 | -3.95 | -332 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 42 | 40% (27-56) | -1.59 | -2.41 | -101 |  |
| (-0.938, 0.589] | 42 | 57% (42-71) | +0.30 | -0.31 | -13 | ▲ |
| (0.589, 7.522] | 42 | 55% (40-69) | -0.39 | -1.13 | -47 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 46 | 48% (34-62) | -0.68 | -1.33 | -61 |  |
| (0.533, 0.832] | 43 | 53% (39-67) | -0.91 | -1.61 | -69 |  |
| (0.832, 3.799] | 44 | 50% (36-64) | -0.46 | -1.31 | -58 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 45 | 47% (33-61) | -1.40 | -1.97 | -89 |  |
| (0.822, 1.457] | 44 | 55% (40-68) | -0.15 | -0.88 | -39 |  |
| (1.457, 9.058] | 44 | 50% (36-64) | -0.47 | -1.38 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.369] | 45 | 47% (33-61) | -0.63 | -1.21 | -54 |  |
| (0.369, 0.594] | 44 | 59% (44-72) | -0.52 | -1.27 | -56 | ▲ |
| (0.594, 4.001] | 44 | 45% (32-60) | -0.89 | -1.77 | -78 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 110, trail_stop 105, time_stop 29, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 84 | 31% | 33% | 30% |
| (0.102, 0.158] | 84 | 50% | 45% | 2% |
| (0.158, 0.76] | 84 | 50% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
