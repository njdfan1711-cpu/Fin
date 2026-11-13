# Scalp signal analysis (trail exits)

_270 tagged trades, 32 trading days (2026-10-01 to 2026-11-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 270 | 42% (36-48) | -0.72 | -2.23 | -602 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -19 | -0.40 | 222 | -584 | -2.63 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 267 | -593 | -2.22 | +10 |
| skip when SPY is down on the day | 101 | -279 | -2.77 | 169 | -323 | -1.91 | +279 |
| skip when SPY is below its VWAP | 117 | -351 | -3.00 | 153 | -252 | -1.64 | +351 |
| skip when SPY fell over the last 15 min | 100 | -230 | -2.30 | 170 | -373 | -2.19 | +230 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 67 | -240 | -3.59 | 203 | -362 | -1.78 | +240 |
| skip stock not beating SPY over 15 min | 44 | -103 | -2.34 | 226 | -499 | -2.21 | +103 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -227 | -3.79 | 210 | -375 | -1.79 | +227 |
| skip volume spikes above 5x average | 54 | -189 | -3.50 | 216 | -414 | -1.92 | +189 |
| skip when the stop is inside normal noise (range > stop) | 27 | -47 | -1.74 | 243 | -555 | -2.29 | +47 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 38 | -70 | -1.84 | 232 | -533 | -2.30 | +70 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 146 | -187 | -1.28 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 109 | 39% (31-49) | -1.03 | -2.32 | -253 |  |
| 240-375 | 76 | 39% (29-51) | -1.62 | -3.36 | -255 |  |
| 375-390 | 48 | 46% (33-60) | +1.11 | -0.40 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 50 | 44% (31-58) | -0.68 | -1.91 | -95 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 117 | 36% (28-45) | -1.38 | -3.00 | -351 |  |
| above VWAP | 153 | 46% (39-54) | -0.22 | -1.64 | -252 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 90 | 39% (29-49) | -0.39 | -1.59 | -143 |  |
| (0.129, 0.379] | 90 | 53% (43-63) | -0.13 | -1.66 | -149 | ▲ |
| (0.379, 5.591] | 90 | 33% (24-44) | -1.64 | -3.45 | -310 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.119] | 89 | 48% (38-59) | +0.32 | -0.86 | -76 |  |
| (0.119, 0.441] | 89 | 42% (32-52) | -0.93 | -2.79 | -248 |  |
| (0.441, 4.846] | 89 | 36% (27-46) | -1.49 | -3.01 | -268 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 90 | 46% (36-56) | -0.80 | -2.50 | -225 |  |
| (-0.367, 0.421] | 90 | 48% (38-58) | +0.52 | -0.59 | -53 |  |
| (0.421, 9.926] | 90 | 32% (23-42) | -1.90 | -3.61 | -325 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 90 | 42% (33-53) | -1.00 | -2.34 | -211 |  |
| (0.0559, 0.126] | 90 | 44% (35-55) | +0.13 | -1.29 | -116 |  |
| (0.126, 0.924] | 90 | 39% (29-49) | -1.30 | -3.06 | -276 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.215] | 90 | 43% (34-54) | -0.03 | -1.08 | -98 |  |
| (0.215, 0.339] | 90 | 47% (37-57) | -0.57 | -2.32 | -208 |  |
| (0.339, 2.663] | 90 | 36% (26-46) | -1.57 | -3.29 | -296 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.354] | 90 | 41% (32-51) | -0.60 | -2.05 | -185 |  |
| (2.354, 3.618] | 90 | 49% (39-59) | +0.41 | -1.11 | -100 |  |
| (3.618, 19.488] | 90 | 36% (26-46) | -1.98 | -3.53 | -318 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 90 | 49% (39-59) | +0.40 | -0.37 | -33 |  |
| (0.103, 0.162] | 90 | 40% (30-50) | -1.36 | -2.54 | -228 |  |
| (0.162, 0.76] | 90 | 37% (27-47) | -1.20 | -3.79 | -341 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 48 | 42% (29-56) | -1.47 | -2.25 | -108 |  |
| (-0.938, 0.615] | 48 | 54% (40-67) | +0.11 | -0.48 | -23 |  |
| (0.615, 7.522] | 48 | 54% (40-67) | -0.64 | -1.37 | -66 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 51 | 49% (36-62) | -0.53 | -1.17 | -59 |  |
| (0.533, 0.837] | 52 | 54% (41-67) | -0.92 | -1.61 | -84 |  |
| (0.837, 3.799] | 48 | 46% (33-60) | -0.86 | -1.68 | -81 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.849] | 51 | 47% (34-60) | -1.39 | -1.98 | -101 |  |
| (0.849, 1.457] | 50 | 52% (39-65) | -0.35 | -1.05 | -52 |  |
| (1.457, 9.058] | 50 | 50% (37-63) | -0.55 | -1.41 | -70 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.377] | 51 | 45% (32-59) | -0.79 | -1.37 | -70 |  |
| (0.377, 0.594] | 50 | 60% (46-72) | -0.44 | -1.17 | -59 | ▲ |
| (0.594, 4.001] | 50 | 44% (31-58) | -1.07 | -1.91 | -95 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 119, trail_stop 111, time_stop 32, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 90 | 30% | 33% | 31% |
| (0.103, 0.162] | 90 | 52% | 43% | 2% |
| (0.162, 0.76] | 90 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
