# Scalp signal analysis (fixed exits)

_255 tagged trades, 29 trading days (2026-10-01 to 2026-11-10). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 255 | 41% (35-47) | +0.21 | -1.35 | -345 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -2 | -0.05 | 211 | -342 | -1.62 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 253 | -337 | -1.33 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 156 | -245 | -1.57 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 143 | -167 | -1.16 | +178 |
| skip when SPY fell over the last 15 min | 93 | -134 | -1.44 | 162 | -211 | -1.30 | +134 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 63 | -168 | -2.66 | 192 | -177 | -0.92 | +168 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 213 | -305 | -1.43 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.81 | 198 | -127 | -0.64 | +217 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 207 | -227 | -1.10 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 229 | -338 | -1.48 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 34 | -19 | -0.55 | 221 | -326 | -1.48 | +19 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 123 | -319 | -2.60 | 132 | -25 | -0.19 | +319 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 102 | 39% (30-49) | +0.05 | -1.29 | -131 |  |
| 240-375 | 73 | 32% (22-43) | -1.29 | -3.08 | -225 |  |
| 375-390 | 44 | 50% (36-64) | +1.54 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 67 | 33% (23-45) | -0.43 | -1.75 | -118 |  |
| > 0.2 | 89 | 43% (33-53) | +0.14 | -1.44 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 143 | 41% (33-49) | +0.32 | -1.16 | -167 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 85 | 41% (31-52) | +0.30 | -0.96 | -82 |  |
| (0.135, 0.382] | 85 | 46% (36-56) | +0.60 | -0.96 | -82 |  |
| (0.382, 5.591] | 85 | 35% (26-46) | -0.25 | -2.13 | -181 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.116] | 85 | 46% (36-56) | +0.73 | -0.48 | -41 |  |
| (0.116, 0.439] | 84 | 40% (31-51) | +0.46 | -1.37 | -115 |  |
| (0.439, 4.846] | 84 | 37% (27-48) | -0.46 | -2.15 | -180 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.371] | 85 | 45% (35-55) | +0.65 | -1.12 | -95 |  |
| (-0.371, 0.396] | 85 | 46% (36-56) | +1.06 | -0.07 | -6 |  |
| (0.396, 5.005] | 85 | 32% (23-42) | -1.07 | -2.86 | -243 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 85 | 41% (31-52) | -0.03 | -1.42 | -120 |  |
| (0.0559, 0.126] | 85 | 47% (37-58) | +0.82 | -0.66 | -56 |  |
| (0.126, 0.924] | 85 | 34% (25-45) | -0.15 | -1.98 | -168 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 85 | 44% (33-54) | +0.35 | -0.73 | -62 |  |
| (0.212, 0.333] | 85 | 42% (32-53) | +0.41 | -1.39 | -118 |  |
| (0.333, 2.663] | 85 | 36% (27-47) | -0.12 | -1.93 | -164 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.305] | 85 | 35% (26-46) | -0.27 | -1.76 | -149 |  |
| (2.305, 3.61] | 85 | 51% (40-61) | +1.28 | -0.31 | -26 |  |
| (3.61, 18.762] | 85 | 36% (27-47) | -0.38 | -1.99 | -169 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 48% (38-59) | +0.70 | -0.07 | -6 |  |
| (0.102, 0.158] | 85 | 35% (26-46) | -0.42 | -1.56 | -133 |  |
| (0.158, 0.76] | 85 | 39% (29-49) | +0.36 | -2.43 | -206 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 43 | 35% (22-50) | -0.62 | -1.44 | -62 |  |
| (-0.938, 0.589] | 43 | 51% (37-65) | +1.31 | +0.71 | +30 |  |
| (0.589, 7.522] | 43 | 47% (33-61) | +1.09 | +0.35 | +15 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 47 | 45% (31-59) | +0.20 | -0.46 | -22 |  |
| (0.533, 0.832] | 44 | 43% (30-58) | +0.38 | -0.32 | -14 |  |
| (0.832, 3.799] | 45 | 42% (29-57) | +0.73 | -0.12 | -5 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.822] | 46 | 43% (30-58) | +0.23 | -0.35 | -16 |  |
| (0.822, 1.457] | 45 | 44% (31-59) | +0.85 | +0.12 | +5 |  |
| (1.457, 9.058] | 45 | 42% (29-57) | +0.23 | -0.68 | -30 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.369] | 46 | 41% (28-56) | +0.10 | -0.48 | -22 |  |
| (0.369, 0.594] | 45 | 47% (33-61) | +0.72 | -0.03 | -1 |  |
| (0.594, 4.001] | 45 | 42% (29-57) | +0.48 | -0.39 | -18 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 123, target 67, time_stop 52, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 33% | 18% | 42% |
| (0.102, 0.158] | 85 | 56% | 26% | 12% |
| (0.158, 0.76] | 85 | 55% | 35% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
