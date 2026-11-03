# Scalp signal analysis (trail exits)

_213 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 213 | 38% (31-44) | -0.94 | -2.66 | -567 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 178 | -559 | -3.14 | +8 |
| skip first 30 min | 2 | -3 | -1.70 | 211 | -564 | -2.67 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 124 | -286 | -2.31 | +281 |
| skip when SPY is below its VWAP | 94 | -328 | -3.49 | 119 | -239 | -2.01 | +328 |
| skip when SPY fell over the last 15 min | 79 | -192 | -2.43 | 134 | -375 | -2.80 | +192 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 53 | -222 | -4.20 | 160 | -345 | -2.16 | +222 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 176 | -486 | -2.76 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -217 | -4.83 | 168 | -350 | -2.08 | +217 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 173 | -378 | -2.18 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 199 | -522 | -2.62 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 24 | -81 | -3.36 | 189 | -487 | -2.58 | +81 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -386 | -3.54 | 104 | -182 | -1.75 | +386 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 32 | 50% (34-66) | -0.15 | -1.99 | -64 |  |
| 60-240 | 87 | 33% (24-44) | -1.42 | -2.89 | -252 |  |
| 240-375 | 59 | 34% (23-47) | -2.12 | -4.13 | -244 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 65 | 35% (25-48) | -1.50 | -2.82 | -183 |  |
| > 0.2 | 59 | 41% (29-53) | +0.27 | -1.74 | -103 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 31% (22-41) | -1.65 | -3.49 | -328 |  |
| above VWAP | 119 | 43% (34-52) | -0.38 | -2.01 | -239 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 71 | 35% (25-47) | -0.49 | -1.72 | -122 |  |
| (0.122, 0.374] | 71 | 46% (35-58) | -0.48 | -2.33 | -166 |  |
| (0.374, 1.555] | 71 | 31% (21-42) | -1.85 | -3.94 | -279 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.119] | 71 | 42% (31-54) | +0.09 | -1.26 | -90 |  |
| (0.119, 0.412] | 70 | 40% (29-52) | -0.99 | -3.00 | -210 |  |
| (0.412, 2.453] | 70 | 30% (21-42) | -1.92 | -3.78 | -265 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.357] | 71 | 38% (28-50) | -1.40 | -3.38 | -240 |  |
| (-0.357, 0.339] | 71 | 44% (33-55) | +0.47 | -0.72 | -51 |  |
| (0.339, 2.726] | 71 | 31% (21-42) | -1.89 | -3.89 | -276 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.054] | 71 | 39% (29-51) | -1.15 | -2.69 | -191 |  |
| (0.054, 0.123] | 71 | 39% (29-51) | +0.06 | -1.55 | -110 |  |
| (0.123, 0.678] | 71 | 34% (24-45) | -1.73 | -3.75 | -266 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.21] | 71 | 42% (31-54) | +0.07 | -1.11 | -79 |  |
| (0.21, 0.314] | 71 | 37% (26-48) | -1.23 | -3.12 | -222 |  |
| (0.314, 0.979] | 71 | 34% (24-45) | -1.65 | -3.76 | -267 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.353] | 71 | 38% (28-50) | -0.64 | -2.27 | -161 |  |
| (2.353, 3.617] | 71 | 46% (35-58) | +0.48 | -1.24 | -88 |  |
| (3.617, 18.762] | 71 | 28% (19-40) | -2.66 | -4.48 | -318 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 71 | 45% (34-57) | +0.37 | -0.38 | -27 |  |
| (0.0985, 0.15] | 71 | 41% (30-52) | -1.27 | -2.49 | -176 |  |
| (0.15, 0.392] | 71 | 27% (18-38) | -1.91 | -5.13 | -364 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.887] | 29 | 28% (15-46) | -2.78 | -3.65 | -106 |  |
| (-0.887, 0.444] | 30 | 50% (33-67) | -0.48 | -1.01 | -30 |  |
| (0.444, 5.305] | 28 | 57% (39-73) | -0.19 | -0.92 | -26 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.507] | 32 | 47% (31-64) | -0.52 | -1.15 | -37 |  |
| (0.507, 0.747] | 31 | 45% (29-62) | -1.42 | -2.16 | -67 |  |
| (0.747, 1.74] | 31 | 42% (26-59) | -1.92 | -2.73 | -85 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 32 | 47% (31-64) | -1.18 | -1.68 | -54 |  |
| (0.775, 1.2] | 31 | 42% (26-59) | -1.26 | -2.02 | -63 |  |
| (1.2, 5.866] | 31 | 45% (29-62) | -1.40 | -2.33 | -72 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.347] | 32 | 38% (23-55) | -1.27 | -1.85 | -59 |  |
| (0.347, 0.559] | 31 | 58% (41-74) | -0.33 | -1.10 | -34 | ▲ |
| (0.559, 1.659] | 31 | 39% (24-56) | -2.22 | -3.07 | -95 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 98, trail_stop 82, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 71 | 32% | 30% | 34% |
| (0.0985, 0.15] | 71 | 51% | 44% | 4% |
| (0.15, 0.392] | 71 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
