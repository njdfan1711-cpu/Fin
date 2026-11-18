# Scalp signal analysis (trail exits)

_299 tagged trades, 35 trading days (2026-10-01 to 2026-11-18). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 299 | 42% (36-47) | -0.68 | -2.11 | -632 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 57 | +23 | +0.41 | 242 | -655 | -2.71 | -23 |
| skip first 30 min | 4 | -17 | -4.16 | 295 | -616 | -2.09 | +17 |
| skip when SPY is down on the day | 129 | -302 | -2.34 | 170 | -330 | -1.94 | +302 |
| skip when SPY is below its VWAP | 133 | -341 | -2.56 | 166 | -291 | -1.75 | +341 |
| skip when SPY fell over the last 15 min | 103 | -215 | -2.09 | 196 | -418 | -2.13 | +215 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 74 | -225 | -3.04 | 225 | -407 | -1.81 | +225 |
| skip stock not beating SPY over 15 min | 47 | -108 | -2.29 | 252 | -525 | -2.08 | +108 |
| skip afternoon entries (2:00-3:45 PM) | 66 | -245 | -3.71 | 233 | -387 | -1.66 | +245 |
| skip volume spikes above 5x average | 61 | -225 | -3.69 | 238 | -407 | -1.71 | +225 |
| skip when the stop is inside normal noise (range > stop) | 38 | -68 | -1.79 | 261 | -564 | -2.16 | +68 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 45 | -85 | -1.88 | 254 | -548 | -2.16 | +85 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 136 | -419 | -3.08 | 163 | -213 | -1.31 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 121 | 38% (30-47) | -1.26 | -2.48 | -300 |  |
| 240-375 | 83 | 39% (29-49) | -1.62 | -3.30 | -274 |  |
| 375-390 | 57 | 51% (38-63) | +1.81 | +0.41 | +23 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 78 | 44% (33-55) | -0.45 | -1.52 | -119 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 133 | 38% (31-47) | -1.05 | -2.56 | -341 |  |
| above VWAP | 166 | 45% (37-52) | -0.38 | -1.75 | -291 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 100 | 41% (32-51) | -0.24 | -1.38 | -138 |  |
| (0.133, 0.376] | 99 | 48% (39-58) | -0.46 | -1.93 | -191 |  |
| (0.376, 5.591] | 100 | 36% (27-46) | -1.33 | -3.03 | -303 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 99 | 49% (40-59) | +0.33 | -0.80 | -79 |  |
| (0.133, 0.451] | 98 | 41% (32-51) | -0.87 | -2.64 | -258 |  |
| (0.451, 4.846] | 98 | 36% (27-46) | -1.38 | -2.84 | -278 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.557] | 100 | 44% (35-54) | -0.63 | -2.13 | -213 |  |
| (-0.557, 0.356] | 99 | 45% (36-55) | +0.15 | -1.06 | -105 |  |
| (0.356, 9.926] | 100 | 36% (27-46) | -1.54 | -3.15 | -315 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 100 | 43% (34-53) | -0.94 | -2.23 | -223 |  |
| (0.0559, 0.133] | 99 | 45% (36-55) | +0.14 | -1.22 | -120 |  |
| (0.133, 0.924] | 100 | 37% (28-47) | -1.22 | -2.89 | -289 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 100 | 46% (37-56) | +0.28 | -0.74 | -74 |  |
| (0.217, 0.346] | 99 | 45% (36-55) | -0.69 | -2.34 | -232 |  |
| (0.346, 2.663] | 100 | 34% (25-44) | -1.62 | -3.26 | -326 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.378] | 100 | 41% (32-51) | -0.58 | -1.98 | -198 |  |
| (2.378, 3.611] | 99 | 49% (40-59) | +0.64 | -0.82 | -82 |  |
| (3.611, 19.488] | 100 | 35% (26-45) | -2.08 | -3.53 | -353 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.105] | 100 | 47% (38-57) | +0.16 | -0.61 | -61 |  |
| (0.105, 0.166] | 100 | 44% (35-54) | -0.94 | -2.09 | -209 |  |
| (0.166, 0.76] | 99 | 34% (26-44) | -1.25 | -3.66 | -362 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.793] | 59 | 41% (29-53) | -1.40 | -2.22 | -131 |  |
| (-0.793, 0.622] | 56 | 52% (39-64) | +0.06 | -0.50 | -28 |  |
| (0.622, 7.522] | 58 | 53% (41-66) | -0.41 | -1.17 | -68 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.563] | 60 | 48% (36-61) | -0.55 | -1.19 | -71 |  |
| (0.563, 0.855] | 60 | 53% (41-65) | -0.68 | -1.40 | -84 |  |
| (0.855, 3.799] | 60 | 43% (32-56) | -0.81 | -1.64 | -98 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 60 | 47% (35-59) | -1.35 | -1.95 | -117 |  |
| (0.909, 1.652] | 60 | 52% (39-64) | -0.28 | -1.00 | -60 |  |
| (1.652, 9.058] | 60 | 47% (35-59) | -0.42 | -1.28 | -77 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 60 | 45% (33-58) | -0.70 | -1.29 | -77 |  |
| (0.409, 0.62] | 60 | 62% (49-73) | -0.00 | -0.73 | -44 | ▲ |
| (0.62, 4.001] | 60 | 38% (27-51) | -1.35 | -2.20 | -132 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 132, trail_stop 122, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.105] | 100 | 33% | 32% | 30% |
| (0.105, 0.166] | 100 | 47% | 46% | 3% |
| (0.166, 0.76] | 99 | 53% | 44% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
