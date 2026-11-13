# Scalp signal analysis (trail exits)

_268 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 268 | 42% (36-48) | -0.69 | -2.21 | -592 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -19 | -0.40 | 220 | -573 | -2.60 | +19 |
| skip first 30 min | 3 | -10 | -3.32 | 265 | -582 | -2.19 | +10 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 169 | -323 | -1.91 | +268 |
| skip when SPY is below its VWAP | 116 | -344 | -2.97 | 152 | -247 | -1.63 | +344 |
| skip when SPY fell over the last 15 min | 99 | -223 | -2.25 | 169 | -368 | -2.18 | +223 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 66 | -233 | -3.53 | 202 | -358 | -1.77 | +233 |
| skip stock not beating SPY over 15 min | 43 | -99 | -2.30 | 225 | -493 | -2.19 | +99 |
| skip afternoon entries (2:00-3:45 PM) | 60 | -227 | -3.79 | 208 | -364 | -1.75 | +227 |
| skip volume spikes above 5x average | 53 | -182 | -3.44 | 215 | -409 | -1.90 | +182 |
| skip when the stop is inside normal noise (range > stop) | 27 | -47 | -1.74 | 241 | -545 | -2.26 | +47 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 37 | -63 | -1.70 | 231 | -529 | -2.29 | +63 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 144 | -176 | -1.22 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 107 | 40% (31-50) | -0.96 | -2.27 | -242 |  |
| 240-375 | 76 | 39% (29-51) | -1.62 | -3.36 | -255 |  |
| 375-390 | 48 | 46% (33-60) | +1.11 | -0.40 | -19 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 116 | 36% (28-45) | -1.34 | -2.97 | -344 |  |
| above VWAP | 152 | 47% (39-55) | -0.20 | -1.63 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 90 | 40% (30-50) | -0.33 | -1.53 | -138 |  |
| (0.132, 0.382] | 89 | 54% (44-64) | -0.01 | -1.54 | -137 | ▲ |
| (0.382, 5.591] | 89 | 33% (24-43) | -1.74 | -3.56 | -316 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 89 | 48% (38-59) | +0.32 | -0.86 | -76 |  |
| (0.118, 0.44] | 88 | 42% (32-52) | -0.90 | -2.77 | -244 |  |
| (0.44, 4.846] | 88 | 36% (27-47) | -1.44 | -2.97 | -261 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 90 | 46% (36-56) | -0.80 | -2.50 | -225 |  |
| (-0.367, 0.426] | 89 | 48% (38-59) | +0.58 | -0.54 | -48 |  |
| (0.426, 9.926] | 89 | 33% (24-43) | -1.86 | -3.58 | -319 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 90 | 43% (34-54) | -0.90 | -2.24 | -202 |  |
| (0.056, 0.127] | 90 | 46% (36-56) | +0.19 | -1.24 | -111 |  |
| (0.127, 0.924] | 88 | 38% (28-48) | -1.38 | -3.16 | -278 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 90 | 46% (36-56) | +0.21 | -0.86 | -77 |  |
| (0.217, 0.34] | 89 | 46% (36-56) | -0.67 | -2.43 | -216 |  |
| (0.34, 2.663] | 89 | 35% (26-45) | -1.62 | -3.36 | -299 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.356] | 90 | 42% (33-53) | -0.54 | -2.00 | -180 |  |
| (2.356, 3.611] | 89 | 48% (38-59) | +0.40 | -1.12 | -100 |  |
| (3.611, 19.488] | 89 | 36% (27-46) | -1.94 | -3.50 | -311 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 90 | 49% (39-59) | +0.38 | -0.39 | -35 |  |
| (0.104, 0.164] | 89 | 40% (31-51) | -1.31 | -2.54 | -226 |  |
| (0.164, 0.76] | 89 | 37% (28-47) | -1.15 | -3.70 | -330 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 48 | 42% (29-56) | -1.47 | -2.25 | -108 |  |
| (-0.974, 0.613] | 47 | 55% (41-69) | +0.20 | -0.40 | -19 |  |
| (0.613, 7.522] | 47 | 55% (41-69) | -0.53 | -1.26 | -59 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.542] | 50 | 52% (39-65) | -0.20 | -0.84 | -42 |  |
| (0.542, 0.837] | 51 | 53% (40-66) | -1.08 | -1.77 | -90 |  |
| (0.837, 3.799] | 48 | 46% (33-60) | -0.86 | -1.68 | -81 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.852] | 50 | 48% (35-61) | -1.30 | -1.88 | -94 |  |
| (0.852, 1.463] | 49 | 53% (39-66) | -0.27 | -0.98 | -48 |  |
| (1.463, 9.058] | 50 | 50% (37-63) | -0.55 | -1.41 | -70 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.382] | 50 | 46% (33-60) | -0.72 | -1.31 | -65 |  |
| (0.382, 0.594] | 49 | 61% (47-74) | -0.32 | -1.06 | -52 | ▲ |
| (0.594, 4.001] | 50 | 44% (31-58) | -1.07 | -1.91 | -95 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 118, trail_stop 111, time_stop 31, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 90 | 31% | 33% | 30% |
| (0.104, 0.164] | 89 | 52% | 44% | 2% |
| (0.164, 0.76] | 89 | 49% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
