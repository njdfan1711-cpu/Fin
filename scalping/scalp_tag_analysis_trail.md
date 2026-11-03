# Scalp signal analysis (trail exits)

_215 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 215 | 37% (31-44) | -0.98 | -2.70 | -581 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 180 | -573 | -3.18 | +8 |
| skip first 30 min | 2 | -3 | -1.70 | 213 | -578 | -2.71 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 126 | -300 | -2.38 | +281 |
| skip when SPY is below its VWAP | 94 | -328 | -3.49 | 121 | -253 | -2.09 | +328 |
| skip when SPY fell over the last 15 min | 79 | -192 | -2.43 | 136 | -389 | -2.86 | +192 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 53 | -229 | -4.31 | 162 | -352 | -2.18 | +229 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 178 | -500 | -2.81 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -217 | -4.83 | 170 | -364 | -2.14 | +217 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 175 | -392 | -2.24 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 201 | -535 | -2.66 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 24 | -81 | -3.36 | 191 | -501 | -2.62 | +81 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 110 | -393 | -3.57 | 105 | -188 | -1.79 | +393 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 48% (33-65) | -0.32 | -2.12 | -70 |  |
| 60-240 | 88 | 33% (24-43) | -1.47 | -2.94 | -259 |  |
| 240-375 | 59 | 34% (23-47) | -2.12 | -4.13 | -244 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 65 | 35% (25-48) | -1.50 | -2.82 | -183 |  |
| > 0.2 | 61 | 39% (28-52) | +0.07 | -1.91 | -116 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 31% (22-41) | -1.65 | -3.49 | -328 |  |
| above VWAP | 121 | 42% (34-51) | -0.47 | -2.09 | -253 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 72 | 35% (25-46) | -0.37 | -1.70 | -123 |  |
| (0.126, 0.374] | 71 | 48% (37-59) | -0.55 | -2.29 | -163 |  |
| (0.374, 1.555] | 72 | 29% (20-41) | -2.03 | -4.11 | -296 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.122] | 71 | 42% (31-54) | +0.09 | -1.26 | -90 |  |
| (0.122, 0.415] | 71 | 39% (29-51) | -1.06 | -3.05 | -216 |  |
| (0.415, 2.453] | 71 | 30% (20-41) | -1.97 | -3.83 | -272 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.351] | 72 | 38% (27-49) | -1.36 | -3.33 | -240 |  |
| (-0.351, 0.356] | 71 | 45% (34-57) | +0.57 | -0.64 | -45 |  |
| (0.356, 2.726] | 72 | 29% (20-41) | -2.14 | -4.11 | -296 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 72 | 39% (28-50) | -1.21 | -2.73 | -197 |  |
| (0.0521, 0.122] | 71 | 39% (29-51) | +0.06 | -1.46 | -103 |  |
| (0.122, 0.678] | 72 | 33% (24-45) | -1.79 | -3.91 | -281 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.209] | 72 | 42% (31-53) | -0.01 | -1.19 | -85 |  |
| (0.209, 0.314] | 71 | 37% (26-48) | -1.23 | -3.12 | -222 |  |
| (0.314, 0.979] | 72 | 33% (24-45) | -1.71 | -3.81 | -274 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.35] | 72 | 38% (27-49) | -0.71 | -2.34 | -169 |  |
| (2.35, 3.574] | 71 | 46% (35-58) | +0.49 | -1.24 | -88 |  |
| (3.574, 18.762] | 72 | 28% (19-39) | -2.70 | -4.50 | -324 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 44% (33-55) | +0.20 | -0.57 | -41 |  |
| (0.0985, 0.149] | 70 | 41% (31-53) | -1.20 | -2.41 | -169 |  |
| (0.149, 0.392] | 72 | 26% (18-38) | -1.96 | -5.15 | -371 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.899] | 30 | 27% (14-44) | -2.88 | -3.75 | -112 |  |
| (-0.899, 0.444] | 30 | 50% (33-67) | -0.48 | -1.01 | -30 |  |
| (0.444, 5.305] | 29 | 55% (38-72) | -0.39 | -1.13 | -33 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.511] | 32 | 47% (31-64) | -0.52 | -1.15 | -37 |  |
| (0.511, 0.74] | 32 | 44% (28-61) | -1.56 | -2.32 | -74 |  |
| (0.74, 1.74] | 32 | 41% (26-58) | -2.04 | -2.85 | -91 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 32 | 44% (28-61) | -1.45 | -1.96 | -63 |  |
| (0.769, 1.194] | 32 | 44% (28-61) | -1.15 | -1.89 | -60 |  |
| (1.194, 5.866] | 32 | 44% (28-61) | -1.52 | -2.47 | -79 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.346] | 32 | 38% (23-55) | -1.28 | -1.87 | -60 |  |
| (0.346, 0.554] | 32 | 53% (36-69) | -0.74 | -1.50 | -48 |  |
| (0.554, 1.659] | 32 | 41% (26-58) | -2.09 | -2.95 | -95 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 100, trail_stop 82, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 34% | 29% | 33% |
| (0.0985, 0.149] | 70 | 50% | 44% | 4% |
| (0.149, 0.392] | 72 | 56% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
