# Scalp signal analysis (trail exits)

_168 tagged trades, 19 trading days (2026-10-01 to 2026-10-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 168 | 36% (29-43) | -0.87 | -2.86 | -480 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 143 | -492 | -3.44 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 167 | -474 | -2.84 | +6 |
| skip when SPY is down on the day | 63 | -254 | -4.03 | 105 | -226 | -2.15 | +254 |
| skip when SPY is below its VWAP | 71 | -287 | -4.04 | 97 | -193 | -1.99 | +287 |
| skip when SPY fell over the last 15 min | 65 | -176 | -2.71 | 103 | -304 | -2.95 | +176 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 42 | -185 | -4.40 | 126 | -295 | -2.34 | +185 |
| skip stock not beating SPY over 15 min | 27 | -48 | -1.79 | 141 | -432 | -3.06 | +48 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 131 | -279 | -2.13 | +202 |
| skip volume spikes above 5x average | 30 | -146 | -4.87 | 138 | -334 | -2.42 | +146 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 161 | -471 | -2.93 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.57%) | 12 | -43 | -3.57 | 156 | -437 | -2.80 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -362 | -3.81 | 73 | -119 | -1.62 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 24 | 54% (35-72) | +0.49 | -1.76 | -42 |  |
| 60-240 | 70 | 31% (22-43) | -1.40 | -3.03 | -212 |  |
| 240-375 | 49 | 31% (20-45) | -2.56 | -4.85 | -237 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 39 | 31% (19-46) | -2.10 | -4.66 | -182 |  |
| 0 to 0.2 | 47 | 34% (22-48) | -1.20 | -2.77 | -130 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 71 | 27% (18-38) | -1.83 | -4.04 | -287 |  |
| above VWAP | 97 | 42% (33-52) | -0.17 | -1.99 | -193 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 56 | 36% (24-49) | +0.28 | -1.26 | -71 |  |
| (0.129, 0.369] | 56 | 45% (32-58) | -1.00 | -2.88 | -161 |  |
| (0.369, 1.555] | 56 | 27% (17-40) | -1.90 | -4.43 | -248 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 56 | 38% (26-51) | +0.11 | -1.59 | -89 |  |
| (0.147, 0.406] | 55 | 40% (28-53) | -0.69 | -2.81 | -155 |  |
| (0.406, 1.281] | 56 | 30% (20-43) | -1.94 | -4.11 | -230 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.242] | 56 | 32% (21-45) | -1.38 | -3.71 | -208 |  |
| (-0.242, 0.397] | 56 | 48% (36-61) | +0.93 | -0.38 | -21 |  |
| (0.397, 2.726] | 56 | 27% (17-40) | -2.16 | -4.48 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 56 | 36% (24-49) | -1.38 | -3.11 | -174 |  |
| (0.052, 0.12] | 56 | 39% (28-52) | +0.42 | -1.33 | -75 |  |
| (0.12, 0.678] | 56 | 32% (21-45) | -1.65 | -4.14 | -232 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.199] | 56 | 45% (32-58) | +0.29 | -1.01 | -56 |  |
| (0.199, 0.301] | 56 | 38% (26-51) | -1.05 | -3.17 | -178 |  |
| (0.301, 0.875] | 56 | 25% (16-38) | -1.86 | -4.40 | -246 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.363] | 56 | 36% (24-49) | -0.78 | -2.65 | -149 |  |
| (2.363, 3.448] | 56 | 43% (31-56) | -0.43 | -2.42 | -136 |  |
| (3.448, 18.762] | 56 | 29% (18-41) | -1.40 | -3.50 | -196 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0969] | 56 | 45% (32-58) | +0.37 | -0.40 | -23 |  |
| (0.0969, 0.147] | 56 | 36% (24-49) | -1.39 | -2.72 | -152 |  |
| (0.147, 0.392] | 56 | 27% (17-40) | -1.59 | -5.46 | -306 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.912] | 14 | 36% (16-61) | -2.09 | -3.05 | -43 |  |
| (-0.912, 0.215] | 14 | 29% (12-55) | -2.75 | -3.29 | -46 |  |
| (0.215, 5.305] | 14 | 71% (45-88) | +1.47 | +1.00 | +14 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 17 | 35% (17-59) | -1.78 | -2.49 | -42 |  |
| (0.486, 0.61] | 16 | 44% (23-67) | -1.50 | -2.07 | -33 |  |
| (0.61, 1.74] | 16 | 56% (33-77) | -0.79 | -1.62 | -26 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 17 | 53% (31-74) | -0.65 | -1.05 | -18 |  |
| (0.775, 1.178] | 16 | 38% (18-61) | -1.81 | -2.61 | -42 |  |
| (1.178, 3.566] | 16 | 44% (23-67) | -1.67 | -2.61 | -42 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 17 | 29% (13-53) | -2.33 | -2.96 | -50 |  |
| (0.315, 0.527] | 16 | 62% (39-82) | +0.19 | -0.37 | -6 | ▲ |
| (0.527, 1.14] | 16 | 44% (23-67) | -1.89 | -2.82 | -45 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 77, trail_stop 64, time_stop 25, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0969] | 56 | 34% | 29% | 36% |
| (0.0969, 0.147] | 56 | 52% | 41% | 5% |
| (0.147, 0.392] | 56 | 52% | 45% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
