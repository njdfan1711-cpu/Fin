# Scalp signal analysis (trail exits)

_238 tagged trades, 26 trading days (2026-10-01 to 2026-11-05). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 238 | 41% (35-48) | -0.63 | -2.25 | -536 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 42 | -2 | -0.05 | 196 | -534 | -2.73 | +2 |
| skip first 30 min | 2 | -3 | -1.70 | 236 | -533 | -2.26 | +3 |
| skip when SPY is down on the day | 95 | -267 | -2.81 | 143 | -270 | -1.89 | +267 |
| skip when SPY is below its VWAP | 105 | -315 | -3.00 | 133 | -221 | -1.66 | +315 |
| skip when SPY fell over the last 15 min | 87 | -187 | -2.15 | 151 | -349 | -2.31 | +187 |
| skip over-extended (30-min run in top quarter, > 0.50%) | 59 | -221 | -3.75 | 179 | -315 | -1.76 | +221 |
| skip stock not beating SPY over 15 min | 38 | -76 | -1.99 | 200 | -461 | -2.30 | +76 |
| skip afternoon entries (2:00-3:45 PM) | 50 | -216 | -4.32 | 188 | -320 | -1.70 | +216 |
| skip volume spikes above 5x average | 45 | -166 | -3.68 | 193 | -371 | -1.92 | +166 |
| skip when the stop is inside normal noise (range > stop) | 22 | -22 | -0.99 | 216 | -515 | -2.38 | +22 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 30 | -46 | -1.54 | 208 | -490 | -2.36 | +46 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 117 | -404 | -3.45 | 121 | -133 | -1.10 | +404 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 96 | 39% (29-49) | -0.97 | -2.36 | -226 |  |
| 240-375 | 66 | 36% (26-48) | -1.80 | -3.70 | -244 |  |
| 375-390 | 42 | 48% (33-62) | +1.58 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 44 | 43% (30-58) | -0.57 | -1.88 | -83 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 77 | 48% (37-59) | +0.68 | -1.03 | -79 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 105 | 35% (27-45) | -1.27 | -3.00 | -315 |  |
| above VWAP | 133 | 46% (38-54) | -0.12 | -1.66 | -221 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 80 | 39% (29-50) | -0.10 | -1.47 | -118 |  |
| (0.136, 0.382] | 79 | 53% (42-64) | -0.11 | -1.65 | -130 | ▲ |
| (0.382, 5.591] | 79 | 32% (22-43) | -1.69 | -3.65 | -288 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.112] | 79 | 48% (37-59) | +0.56 | -0.68 | -54 |  |
| (0.112, 0.433] | 78 | 41% (31-52) | -0.89 | -2.83 | -220 |  |
| (0.433, 4.846] | 79 | 34% (25-45) | -1.55 | -3.27 | -259 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.039000000000001, -0.367] | 80 | 45% (35-56) | -0.73 | -2.57 | -206 |  |
| (-0.367, 0.394] | 79 | 46% (35-57) | +0.51 | -0.65 | -51 |  |
| (0.394, 4.204] | 79 | 33% (24-44) | -1.67 | -3.54 | -280 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 80 | 41% (31-52) | -1.01 | -2.43 | -195 |  |
| (0.056, 0.127] | 80 | 45% (35-56) | +0.34 | -1.18 | -95 |  |
| (0.127, 0.924] | 78 | 37% (27-48) | -1.24 | -3.17 | -247 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 80 | 45% (35-56) | +0.34 | -0.78 | -62 |  |
| (0.212, 0.331] | 79 | 43% (33-54) | -0.91 | -2.70 | -213 |  |
| (0.331, 2.663] | 79 | 35% (26-46) | -1.33 | -3.31 | -261 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.318] | 80 | 41% (31-52) | -0.51 | -2.03 | -163 |  |
| (2.318, 3.637] | 79 | 48% (37-59) | +0.59 | -1.07 | -84 |  |
| (3.637, 18.762] | 79 | 34% (25-45) | -1.97 | -3.67 | -290 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0997] | 81 | 48% (38-59) | +0.38 | -0.40 | -32 |  |
| (0.0997, 0.154] | 78 | 41% (31-52) | -1.24 | -2.39 | -186 |  |
| (0.154, 0.76] | 79 | 34% (25-45) | -1.07 | -4.03 | -318 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.078] | 38 | 42% (28-58) | -1.36 | -2.17 | -83 |  |
| (-1.078, 0.444] | 37 | 51% (36-67) | -0.32 | -0.90 | -33 |  |
| (0.444, 5.599] | 37 | 59% (43-74) | +0.35 | -0.40 | -15 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.523] | 40 | 50% (35-65) | -0.34 | -0.95 | -38 |  |
| (0.523, 0.775] | 39 | 49% (34-64) | -1.28 | -2.06 | -80 |  |
| (0.775, 3.799] | 40 | 52% (37-67) | -0.17 | -0.99 | -39 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.824] | 40 | 45% (31-60) | -1.50 | -2.05 | -82 |  |
| (0.824, 1.432] | 39 | 54% (39-68) | -0.14 | -0.89 | -35 |  |
| (1.432, 7.752] | 40 | 52% (37-67) | -0.11 | -1.02 | -41 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.362] | 40 | 48% (33-63) | -0.40 | -0.96 | -38 |  |
| (0.362, 0.594] | 39 | 59% (43-73) | -0.51 | -1.29 | -50 | ▲ |
| (0.594, 4.001] | 40 | 45% (31-60) | -0.85 | -1.72 | -69 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 104, trail_stop 98, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0997] | 81 | 31% | 32% | 31% |
| (0.0997, 0.154] | 78 | 51% | 45% | 3% |
| (0.154, 0.76] | 79 | 49% | 47% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
