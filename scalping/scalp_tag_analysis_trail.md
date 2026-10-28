# Scalp signal analysis (trail exits)

_170 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 170 | 36% (30-44) | -0.81 | -2.78 | -473 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 145 | -485 | -3.34 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 169 | -467 | -2.76 | +6 |
| skip when SPY is down on the day | 64 | -248 | -3.87 | 106 | -226 | -2.13 | +248 |
| skip when SPY is below its VWAP | 72 | -280 | -3.90 | 98 | -193 | -1.97 | +280 |
| skip when SPY fell over the last 15 min | 65 | -176 | -2.71 | 105 | -297 | -2.83 | +176 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 42 | -185 | -4.40 | 128 | -288 | -2.25 | +185 |
| skip stock not beating SPY over 15 min | 28 | -48 | -1.70 | 142 | -425 | -3.00 | +48 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 133 | -271 | -2.04 | +202 |
| skip volume spikes above 5x average | 31 | -146 | -4.70 | 139 | -327 | -2.36 | +146 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 163 | -464 | -2.85 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 13 | -43 | -3.27 | 157 | -431 | -2.74 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -362 | -3.81 | 75 | -112 | -1.49 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 56% (37-73) | +0.76 | -1.43 | -36 | ▲ |
| 60-240 | 71 | 32% (23-44) | -1.36 | -2.98 | -212 |  |
| 240-375 | 49 | 31% (20-45) | -2.56 | -4.85 | -237 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 40 | 32% (20-48) | -1.87 | -4.38 | -175 |  |
| 0 to 0.2 | 48 | 35% (23-50) | -1.15 | -2.70 | -130 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 72 | 28% (19-39) | -1.71 | -3.90 | -280 |  |
| above VWAP | 98 | 43% (34-53) | -0.15 | -1.97 | -193 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 57 | 37% (26-50) | +0.29 | -1.23 | -70 |  |
| (0.126, 0.368] | 56 | 45% (32-58) | -0.88 | -2.78 | -155 |  |
| (0.368, 1.555] | 57 | 28% (18-41) | -1.85 | -4.34 | -247 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 57 | 39% (27-52) | +0.23 | -1.45 | -83 |  |
| (0.146, 0.405] | 56 | 41% (29-54) | -0.66 | -2.75 | -154 |  |
| (0.405, 1.281] | 56 | 30% (20-43) | -1.94 | -4.11 | -230 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.246] | 57 | 33% (22-46) | -1.34 | -3.64 | -207 |  |
| (-0.246, 0.39] | 56 | 48% (36-61) | +1.04 | -0.29 | -16 |  |
| (0.39, 2.726] | 57 | 28% (18-41) | -2.10 | -4.38 | -250 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 57 | 37% (26-50) | -1.34 | -3.04 | -173 |  |
| (0.0519, 0.12] | 56 | 39% (28-52) | +0.42 | -1.33 | -75 |  |
| (0.12, 0.678] | 57 | 33% (22-46) | -1.49 | -3.95 | -225 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.2] | 57 | 44% (32-57) | +0.28 | -1.00 | -57 |  |
| (0.2, 0.301] | 56 | 39% (28-52) | -1.02 | -3.15 | -176 |  |
| (0.301, 0.875] | 57 | 26% (17-39) | -1.70 | -4.20 | -240 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 57 | 35% (24-48) | -0.86 | -2.72 | -155 |  |
| (2.374, 3.475] | 56 | 45% (32-58) | -0.21 | -2.20 | -123 |  |
| (3.475, 18.762] | 57 | 30% (20-43) | -1.36 | -3.43 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 57 | 46% (33-58) | +0.41 | -0.35 | -20 |  |
| (0.0964, 0.146] | 56 | 38% (26-51) | -1.19 | -2.52 | -141 |  |
| (0.146, 0.392] | 57 | 26% (17-39) | -1.66 | -5.48 | -312 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.862] | 15 | 33% (15-58) | -2.35 | -3.27 | -49 |  |
| (-0.862, 0.379] | 15 | 40% (20-64) | -1.51 | -1.99 | -30 |  |
| (0.379, 5.305] | 14 | 71% (45-88) | +1.35 | +0.80 | +11 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.48] | 17 | 41% (22-64) | -1.26 | -1.91 | -32 |  |
| (0.48, 0.603] | 17 | 47% (26-69) | -1.09 | -1.73 | -29 |  |
| (0.603, 1.74] | 17 | 53% (31-74) | -1.10 | -1.91 | -32 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 17 | 53% (31-74) | -0.37 | -0.78 | -13 |  |
| (0.769, 1.15] | 17 | 41% (22-64) | -1.68 | -2.47 | -42 |  |
| (1.15, 3.566] | 17 | 47% (26-69) | -1.39 | -2.30 | -39 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.316] | 17 | 29% (13-53) | -2.33 | -2.96 | -50 |  |
| (0.316, 0.514] | 17 | 65% (41-83) | +0.48 | -0.09 | -2 | ▲ |
| (0.514, 1.14] | 17 | 47% (26-69) | -1.59 | -2.50 | -42 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 77, trail_stop 65, time_stop 26, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 57 | 33% | 28% | 37% |
| (0.0964, 0.146] | 56 | 50% | 43% | 5% |
| (0.146, 0.392] | 57 | 53% | 44% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
