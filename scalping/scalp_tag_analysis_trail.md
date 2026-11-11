# Scalp signal analysis (trail exits)

_259 tagged trades, 30 trading days (2026-10-01 to 2026-11-11). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 259 | 42% (37-49) | -0.63 | -2.18 | -564 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 46 | -6 | -0.13 | 213 | -558 | -2.62 | +6 |
| skip first 30 min | 2 | -3 | -1.70 | 257 | -561 | -2.18 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 160 | -296 | -1.85 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 147 | -238 | -1.62 | +326 |
| skip when SPY fell over the last 15 min | 95 | -205 | -2.16 | 164 | -359 | -2.19 | +205 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 64 | -221 | -3.46 | 195 | -343 | -1.76 | +221 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 217 | -472 | -2.17 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 201 | -349 | -1.74 | +215 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 211 | -397 | -1.88 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 233 | -523 | -2.25 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 35 | -50 | -1.44 | 224 | -514 | -2.29 | +50 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 135 | -149 | -1.10 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 50% (34-66) | -0.17 | -1.90 | -68 |  |
| 60-240 | 103 | 39% (30-48) | -1.06 | -2.40 | -247 |  |
| 240-375 | 74 | 41% (30-52) | -1.51 | -3.28 | -243 |  |
| 375-390 | 46 | 48% (34-62) | +1.41 | -0.13 | -6 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 92 | 49% (39-59) | +0.44 | -1.10 | -101 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 147 | 47% (39-55) | -0.16 | -1.62 | -238 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 87 | 40% (31-51) | -0.17 | -1.50 | -131 |  |
| (0.136, 0.382] | 86 | 55% (44-65) | -0.04 | -1.50 | -129 | ▲ |
| (0.382, 5.591] | 86 | 33% (24-43) | -1.68 | -3.54 | -304 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.117] | 86 | 49% (39-59) | +0.43 | -0.78 | -67 |  |
| (0.117, 0.44] | 85 | 41% (31-52) | -0.96 | -2.79 | -237 |  |
| (0.44, 4.846] | 86 | 37% (28-48) | -1.34 | -2.99 | -257 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 87 | 45% (35-55) | -0.86 | -2.60 | -226 |  |
| (-0.367, 0.394] | 86 | 48% (37-58) | +0.55 | -0.59 | -50 |  |
| (0.394, 5.005] | 86 | 35% (26-45) | -1.57 | -3.34 | -288 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 87 | 44% (34-54) | -0.88 | -2.26 | -196 |  |
| (0.056, 0.127] | 87 | 46% (36-56) | +0.29 | -1.17 | -101 |  |
| (0.127, 0.924] | 85 | 38% (28-48) | -1.31 | -3.13 | -266 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.214] | 87 | 45% (35-55) | +0.15 | -0.92 | -80 |  |
| (0.214, 0.335] | 86 | 45% (35-56) | -0.67 | -2.47 | -212 |  |
| (0.335, 2.663] | 86 | 37% (28-48) | -1.37 | -3.16 | -271 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.337] | 87 | 41% (32-52) | -0.64 | -2.11 | -183 |  |
| (2.337, 3.502] | 86 | 50% (40-60) | +0.67 | -0.91 | -79 |  |
| (3.502, 18.762] | 86 | 36% (27-47) | -1.91 | -3.51 | -302 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 87 | 48% (38-59) | +0.36 | -0.42 | -37 |  |
| (0.102, 0.161] | 86 | 42% (32-52) | -1.15 | -2.33 | -201 |  |
| (0.161, 0.76] | 86 | 37% (28-48) | -1.10 | -3.80 | -327 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 45 | 42% (29-57) | -1.40 | -2.20 | -99 |  |
| (-0.974, 0.613] | 44 | 55% (40-68) | +0.15 | -0.45 | -20 |  |
| (0.613, 7.522] | 44 | 59% (44-72) | -0.16 | -0.91 | -40 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.536] | 47 | 49% (35-63) | -0.54 | -1.20 | -56 |  |
| (0.536, 0.835] | 46 | 54% (40-68) | -0.84 | -1.54 | -71 |  |
| (0.835, 3.799] | 47 | 51% (37-65) | -0.40 | -1.23 | -58 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.832] | 47 | 49% (35-63) | -1.16 | -1.75 | -82 |  |
| (0.832, 1.484] | 46 | 54% (40-68) | -0.23 | -0.94 | -43 |  |
| (1.484, 9.058] | 47 | 51% (37-65) | -0.38 | -1.27 | -60 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.375] | 47 | 47% (33-61) | -0.67 | -1.25 | -59 |  |
| (0.375, 0.594] | 46 | 61% (46-74) | -0.33 | -1.08 | -50 | ▲ |
| (0.594, 4.001] | 47 | 47% (33-61) | -0.78 | -1.63 | -77 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 112, trail_stop 109, time_stop 30, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 87 | 31% | 33% | 30% |
| (0.102, 0.161] | 86 | 50% | 45% | 2% |
| (0.161, 0.76] | 86 | 49% | 48% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
