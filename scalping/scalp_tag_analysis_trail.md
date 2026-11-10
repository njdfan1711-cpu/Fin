# Scalp signal analysis (trail exits)

_255 tagged trades, 29 trading days (2026-10-01 to 2026-11-10). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 255 | 42% (36-48) | -0.65 | -2.21 | -564 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -3 | -0.07 | 211 | -561 | -2.66 | +3 |
| skip first 30 min | 2 | -3 | -1.70 | 253 | -561 | -2.22 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 156 | -296 | -1.90 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 143 | -238 | -1.67 | +326 |
| skip when SPY fell over the last 15 min | 94 | -207 | -2.20 | 161 | -358 | -2.22 | +207 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 63 | -216 | -3.42 | 192 | -349 | -1.82 | +216 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 213 | -472 | -2.22 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.80 | 198 | -348 | -1.76 | +217 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 207 | -397 | -1.92 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 229 | -524 | -2.29 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 34 | -44 | -1.30 | 221 | -520 | -2.35 | +44 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 123 | -417 | -3.39 | 132 | -148 | -1.12 | +417 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 102 | 38% (29-48) | -1.09 | -2.43 | -248 |  |
| 240-375 | 73 | 40% (29-51) | -1.57 | -3.35 | -245 |  |
| 375-390 | 44 | 48% (34-62) | +1.52 | -0.07 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 67 | 34% (24-46) | -1.60 | -2.92 | -196 |  |
| > 0.2 | 89 | 48% (38-59) | +0.45 | -1.12 | -100 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 143 | 46% (38-54) | -0.18 | -1.67 | -238 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 85 | 40% (30-51) | -0.13 | -1.38 | -118 |  |
| (0.135, 0.382] | 85 | 53% (42-63) | -0.19 | -1.75 | -148 | ▲ |
| (0.382, 5.591] | 85 | 33% (24-43) | -1.63 | -3.51 | -298 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.116] | 85 | 48% (38-59) | +0.40 | -0.81 | -69 |  |
| (0.116, 0.439] | 84 | 40% (31-51) | -1.03 | -2.86 | -240 |  |
| (0.439, 4.846] | 84 | 37% (27-48) | -1.32 | -3.00 | -252 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.371] | 85 | 45% (35-55) | -0.85 | -2.62 | -223 |  |
| (-0.371, 0.396] | 85 | 47% (37-58) | +0.52 | -0.61 | -52 |  |
| (0.396, 5.005] | 85 | 34% (25-45) | -1.62 | -3.40 | -289 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 85 | 42% (32-53) | -0.97 | -2.35 | -200 |  |
| (0.0559, 0.126] | 85 | 45% (35-55) | +0.24 | -1.24 | -105 |  |
| (0.126, 0.924] | 85 | 39% (29-49) | -1.22 | -3.05 | -259 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 85 | 45% (35-55) | +0.18 | -0.90 | -76 |  |
| (0.212, 0.333] | 85 | 44% (33-54) | -0.82 | -2.62 | -223 |  |
| (0.333, 2.663] | 85 | 38% (28-48) | -1.31 | -3.12 | -265 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.305] | 85 | 40% (30-51) | -0.78 | -2.27 | -193 |  |
| (2.305, 3.61] | 85 | 49% (39-60) | +0.70 | -0.89 | -76 |  |
| (3.61, 18.762] | 85 | 36% (27-47) | -1.87 | -3.48 | -295 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 49% (39-60) | +0.41 | -0.35 | -30 |  |
| (0.102, 0.158] | 85 | 40% (30-51) | -1.29 | -2.43 | -207 |  |
| (0.158, 0.76] | 85 | 36% (27-47) | -1.07 | -3.86 | -328 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 43 | 42% (28-57) | -1.42 | -2.24 | -96 |  |
| (-0.938, 0.589] | 43 | 56% (41-70) | +0.15 | -0.45 | -19 |  |
| (0.589, 7.522] | 43 | 56% (41-70) | -0.27 | -1.01 | -43 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 47 | 49% (35-63) | -0.54 | -1.20 | -56 |  |
| (0.533, 0.832] | 44 | 52% (38-66) | -1.02 | -1.72 | -76 |  |
| (0.832, 3.799] | 45 | 51% (37-65) | -0.34 | -1.19 | -54 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 46 | 48% (34-62) | -1.24 | -1.82 | -84 |  |
| (0.822, 1.457] | 45 | 53% (39-67) | -0.28 | -1.00 | -45 |  |
| (1.457, 9.058] | 45 | 51% (37-65) | -0.36 | -1.26 | -57 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.369] | 46 | 46% (32-60) | -0.74 | -1.32 | -61 |  |
| (0.369, 0.594] | 45 | 60% (45-73) | -0.38 | -1.13 | -51 | ▲ |
| (0.594, 4.001] | 45 | 47% (33-61) | -0.77 | -1.64 | -74 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 111, trail_stop 106, time_stop 30, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 31% | 33% | 31% |
| (0.102, 0.158] | 85 | 51% | 45% | 2% |
| (0.158, 0.76] | 85 | 49% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
