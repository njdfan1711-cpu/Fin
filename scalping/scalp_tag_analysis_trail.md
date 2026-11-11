# Scalp signal analysis (trail exits)

_258 tagged trades, 30 trading days (2026-10-01 to 2026-11-11). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 258 | 42% (36-48) | -0.64 | -2.19 | -566 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 46 | -6 | -0.13 | 212 | -560 | -2.64 | +6 |
| skip first 30 min | 2 | -3 | -1.70 | 256 | -563 | -2.20 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 159 | -298 | -1.87 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 146 | -240 | -1.64 | +326 |
| skip when SPY fell over the last 15 min | 94 | -207 | -2.20 | 164 | -359 | -2.19 | +207 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 64 | -221 | -3.46 | 194 | -345 | -1.78 | +221 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 216 | -473 | -2.19 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.80 | 201 | -349 | -1.74 | +217 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 210 | -399 | -1.90 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 232 | -525 | -2.26 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 35 | -50 | -1.44 | 223 | -516 | -2.31 | +50 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 134 | -150 | -1.12 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 103 | 39% (30-48) | -1.06 | -2.40 | -247 |  |
| 240-375 | 73 | 40% (29-51) | -1.57 | -3.35 | -245 |  |
| 375-390 | 46 | 48% (34-62) | +1.41 | -0.13 | -6 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 91 | 48% (38-58) | +0.42 | -1.13 | -103 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 146 | 47% (39-55) | -0.17 | -1.64 | -240 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 86 | 40% (30-50) | -0.20 | -1.54 | -132 |  |
| (0.136, 0.382] | 86 | 55% (44-65) | -0.04 | -1.50 | -129 | ▲ |
| (0.382, 5.591] | 86 | 33% (24-43) | -1.68 | -3.54 | -304 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.119] | 86 | 49% (39-59) | +0.43 | -0.78 | -67 |  |
| (0.119, 0.44] | 85 | 40% (30-51) | -1.06 | -2.98 | -254 |  |
| (0.44, 4.846] | 85 | 38% (28-48) | -1.28 | -2.85 | -242 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.371] | 86 | 44% (34-55) | -0.90 | -2.66 | -229 |  |
| (-0.371, 0.388] | 86 | 48% (37-58) | +0.57 | -0.57 | -49 |  |
| (0.388, 5.005] | 86 | 35% (26-45) | -1.58 | -3.35 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 86 | 43% (33-54) | -0.93 | -2.31 | -199 |  |
| (0.0559, 0.126] | 86 | 45% (35-56) | +0.28 | -1.18 | -102 |  |
| (0.126, 0.924] | 86 | 38% (29-49) | -1.27 | -3.09 | -265 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.213] | 86 | 44% (34-55) | +0.11 | -0.96 | -83 |  |
| (0.213, 0.333] | 86 | 45% (35-56) | -0.67 | -2.46 | -212 |  |
| (0.333, 2.663] | 86 | 37% (28-48) | -1.36 | -3.15 | -271 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.331] | 86 | 41% (31-51) | -0.67 | -2.16 | -185 |  |
| (2.331, 3.538] | 86 | 50% (40-60) | +0.67 | -0.91 | -79 |  |
| (3.538, 18.762] | 86 | 36% (27-47) | -1.91 | -3.51 | -302 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 87 | 48% (38-59) | +0.36 | -0.42 | -37 |  |
| (0.102, 0.16] | 85 | 42% (32-53) | -1.09 | -2.28 | -194 |  |
| (0.16, 0.76] | 86 | 36% (27-47) | -1.20 | -3.91 | -336 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.008] | 44 | 43% (30-58) | -1.30 | -2.10 | -92 |  |
| (-1.008, 0.589] | 44 | 55% (40-68) | +0.02 | -0.59 | -26 |  |
| (0.589, 7.522] | 44 | 57% (42-70) | -0.21 | -0.96 | -42 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 47 | 49% (35-63) | -0.54 | -1.20 | -56 |  |
| (0.533, 0.832] | 46 | 54% (40-68) | -0.84 | -1.54 | -71 |  |
| (0.832, 3.799] | 46 | 50% (36-64) | -0.46 | -1.30 | -60 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.828] | 47 | 49% (35-63) | -1.16 | -1.75 | -82 |  |
| (0.828, 1.467] | 46 | 54% (40-68) | -0.23 | -0.94 | -43 |  |
| (1.467, 9.058] | 46 | 50% (36-64) | -0.44 | -1.34 | -61 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.374] | 47 | 47% (33-61) | -0.67 | -1.25 | -59 |  |
| (0.374, 0.594] | 46 | 61% (46-74) | -0.23 | -0.99 | -46 | ▲ |
| (0.594, 4.001] | 46 | 46% (32-60) | -0.94 | -1.80 | -83 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 112, trail_stop 108, time_stop 30, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 87 | 31% | 33% | 30% |
| (0.102, 0.16] | 85 | 49% | 46% | 2% |
| (0.16, 0.76] | 86 | 50% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
