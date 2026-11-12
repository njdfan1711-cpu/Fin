# Scalp signal analysis (trail exits)

_265 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 265 | 43% (37-49) | -0.63 | -2.16 | -573 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -12 | -0.26 | 218 | -560 | -2.57 | +12 |
| skip first 30 min | 3 | -10 | -3.32 | 262 | -563 | -2.15 | +10 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 166 | -304 | -1.83 | +268 |
| skip when SPY is below its VWAP | 113 | -326 | -2.88 | 152 | -247 | -1.63 | +326 |
| skip when SPY fell over the last 15 min | 96 | -204 | -2.13 | 169 | -368 | -2.18 | +204 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 66 | -227 | -3.45 | 199 | -345 | -1.74 | +227 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 223 | -480 | -2.15 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 207 | -358 | -1.73 | +215 |
| skip volume spikes above 5x average | 51 | -170 | -3.33 | 214 | -403 | -1.88 | +170 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 239 | -532 | -2.23 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 37 | -57 | -1.55 | 228 | -515 | -2.26 | +57 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 141 | -157 | -1.12 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 107 | 40% (31-50) | -0.96 | -2.27 | -242 |  |
| 240-375 | 74 | 41% (30-52) | -1.51 | -3.28 | -243 |  |
| 375-390 | 47 | 47% (33-61) | +1.25 | -0.26 | -12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 98 | 49% (39-59) | +0.36 | -1.12 | -110 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 113 | 37% (29-46) | -1.23 | -2.88 | -326 |  |
| above VWAP | 152 | 47% (39-55) | -0.20 | -1.63 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 89 | 40% (31-51) | -0.27 | -1.48 | -132 |  |
| (0.132, 0.377] | 88 | 53% (43-63) | -0.09 | -1.63 | -143 | ▲ |
| (0.377, 5.591] | 88 | 34% (25-44) | -1.55 | -3.38 | -298 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 88 | 49% (39-59) | +0.39 | -0.80 | -70 |  |
| (0.118, 0.44] | 87 | 43% (33-53) | -0.84 | -2.63 | -229 |  |
| (0.44, 4.846] | 87 | 37% (27-47) | -1.39 | -3.03 | -263 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 89 | 46% (36-56) | -0.74 | -2.46 | -219 |  |
| (-0.367, 0.4] | 88 | 48% (38-58) | +0.57 | -0.55 | -49 |  |
| (0.4, 5.005] | 88 | 34% (25-44) | -1.73 | -3.47 | -306 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 89 | 44% (34-54) | -0.85 | -2.20 | -196 |  |
| (0.056, 0.126] | 88 | 44% (34-55) | +0.15 | -1.30 | -114 |  |
| (0.126, 0.924] | 88 | 40% (30-50) | -1.20 | -2.99 | -263 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.216] | 89 | 45% (35-55) | +0.14 | -0.93 | -82 |  |
| (0.216, 0.335] | 88 | 45% (35-56) | -0.66 | -2.42 | -213 |  |
| (0.335, 2.663] | 88 | 38% (28-48) | -1.40 | -3.15 | -277 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.351] | 89 | 42% (32-52) | -0.56 | -2.03 | -181 |  |
| (2.351, 3.61] | 88 | 49% (39-59) | +0.47 | -1.07 | -94 |  |
| (3.61, 18.762] | 88 | 38% (28-48) | -1.82 | -3.39 | -298 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 89 | 49% (39-60) | +0.45 | -0.32 | -29 |  |
| (0.102, 0.161] | 88 | 41% (31-51) | -1.26 | -2.43 | -214 |  |
| (0.161, 0.76] | 88 | 38% (28-48) | -1.10 | -3.76 | -331 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.92] | 47 | 45% (31-59) | -1.15 | -1.95 | -92 |  |
| (-0.92, 0.613] | 46 | 54% (40-68) | +0.09 | -0.50 | -23 |  |
| (0.613, 7.522] | 46 | 57% (42-70) | -0.41 | -1.15 | -53 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.536] | 49 | 51% (37-64) | -0.35 | -0.99 | -49 |  |
| (0.536, 0.832] | 49 | 53% (39-66) | -0.96 | -1.65 | -81 |  |
| (0.832, 3.799] | 48 | 50% (36-64) | -0.51 | -1.34 | -64 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.844] | 49 | 49% (36-63) | -1.21 | -1.80 | -88 |  |
| (0.844, 1.463] | 48 | 54% (40-67) | -0.17 | -0.87 | -42 |  |
| (1.463, 9.058] | 49 | 51% (37-64) | -0.44 | -1.31 | -64 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.379] | 49 | 47% (34-61) | -0.62 | -1.20 | -59 |  |
| (0.379, 0.581] | 48 | 58% (44-71) | -0.55 | -1.29 | -62 | ▲ |
| (0.581, 4.001] | 49 | 49% (36-63) | -0.65 | -1.49 | -73 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 115, trail_stop 111, time_stop 31, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 89 | 30% | 34% | 30% |
| (0.102, 0.161] | 88 | 51% | 44% | 2% |
| (0.161, 0.76] | 88 | 49% | 48% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
