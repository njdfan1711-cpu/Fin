# Scalp signal analysis (trail exits)

_267 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 267 | 42% (37-48) | -0.67 | -2.19 | -585 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -19 | -0.40 | 219 | -566 | -2.59 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 264 | -575 | -2.18 | +10 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 168 | -317 | -1.89 | +268 |
| skip when SPY is below its VWAP | 115 | -338 | -2.94 | 152 | -247 | -1.63 | +338 |
| skip when SPY fell over the last 15 min | 98 | -217 | -2.21 | 169 | -368 | -2.18 | +217 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 66 | -233 | -3.53 | 201 | -352 | -1.75 | +233 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 225 | -493 | -2.19 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 59 | -221 | -3.75 | 208 | -364 | -1.75 | +221 |
| skip volume spikes above 5x average | 52 | -176 | -3.39 | 215 | -409 | -1.90 | +176 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 241 | -545 | -2.26 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 37 | -63 | -1.70 | 230 | -522 | -2.27 | +63 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 143 | -170 | -1.19 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 107 | 40% (31-50) | -0.96 | -2.27 | -242 |  |
| 240-375 | 75 | 40% (30-51) | -1.57 | -3.32 | -249 |  |
| 375-390 | 48 | 46% (33-60) | +1.11 | -0.40 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 100 | 48% (38-58) | +0.24 | -1.22 | -122 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 115 | 37% (28-46) | -1.30 | -2.94 | -338 |  |
| above VWAP | 152 | 47% (39-55) | -0.20 | -1.63 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 89 | 40% (31-51) | -0.27 | -1.48 | -132 |  |
| (0.133, 0.382] | 89 | 54% (44-64) | -0.01 | -1.54 | -137 | ▲ |
| (0.382, 5.591] | 89 | 33% (24-43) | -1.74 | -3.56 | -316 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.119] | 88 | 49% (39-59) | +0.39 | -0.80 | -70 |  |
| (0.119, 0.441] | 88 | 42% (32-52) | -0.90 | -2.77 | -244 |  |
| (0.441, 4.846] | 88 | 36% (27-47) | -1.44 | -2.97 | -261 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 89 | 46% (36-56) | -0.74 | -2.46 | -219 |  |
| (-0.367, 0.41] | 89 | 48% (38-59) | +0.57 | -0.54 | -48 |  |
| (0.41, 5.005] | 89 | 33% (24-43) | -1.85 | -3.58 | -319 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 89 | 44% (34-54) | -0.85 | -2.20 | -196 |  |
| (0.0561, 0.127] | 90 | 46% (36-56) | +0.19 | -1.24 | -111 |  |
| (0.127, 0.924] | 88 | 38% (28-48) | -1.38 | -3.16 | -278 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 89 | 45% (35-55) | +0.14 | -0.93 | -82 |  |
| (0.217, 0.339] | 89 | 46% (36-56) | -0.64 | -2.39 | -213 |  |
| (0.339, 2.663] | 89 | 36% (27-46) | -1.52 | -3.26 | -290 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.354] | 89 | 42% (32-52) | -0.56 | -2.03 | -181 |  |
| (2.354, 3.61] | 89 | 48% (38-59) | +0.40 | -1.13 | -100 |  |
| (3.61, 18.762] | 89 | 37% (28-47) | -1.86 | -3.42 | -304 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 89 | 49% (39-60) | +0.45 | -0.32 | -29 |  |
| (0.103, 0.162] | 89 | 40% (31-51) | -1.31 | -2.49 | -222 |  |
| (0.162, 0.76] | 89 | 37% (28-47) | -1.15 | -3.76 | -335 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 47 | 43% (30-57) | -1.38 | -2.17 | -102 |  |
| (-0.938, 0.615] | 47 | 55% (41-69) | +0.20 | -0.40 | -19 |  |
| (0.615, 7.522] | 47 | 55% (41-69) | -0.53 | -1.26 | -59 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 50 | 52% (39-65) | -0.20 | -0.84 | -42 |  |
| (0.541, 0.837] | 51 | 53% (40-66) | -1.08 | -1.77 | -90 |  |
| (0.837, 3.799] | 47 | 47% (33-61) | -0.75 | -1.58 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.849] | 50 | 48% (35-61) | -1.30 | -1.88 | -94 |  |
| (0.849, 1.457] | 49 | 53% (39-66) | -0.27 | -0.98 | -48 |  |
| (1.457, 9.058] | 49 | 51% (37-64) | -0.44 | -1.31 | -64 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.381] | 50 | 46% (33-60) | -0.72 | -1.31 | -65 |  |
| (0.381, 0.594] | 49 | 61% (47-74) | -0.32 | -1.06 | -52 | ▲ |
| (0.594, 4.001] | 49 | 45% (32-59) | -0.98 | -1.82 | -89 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 117, trail_stop 111, time_stop 31, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 89 | 30% | 34% | 30% |
| (0.103, 0.162] | 89 | 52% | 44% | 2% |
| (0.162, 0.76] | 89 | 49% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
