# Scalp signal analysis (fixed exits)

_159 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 159 | 37% (30-45) | -0.25 | -2.32 | -369 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | -16 | -0.67 | 135 | -352 | -2.61 | +16 |
| skip first 30 min | 1 | -6 | -6.31 | 158 | -362 | -2.29 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 97 | -223 | -2.30 | +145 |
| skip when SPY is below its VWAP | 66 | -185 | -2.80 | 93 | -183 | -1.97 | +185 |
| skip when SPY fell over the last 15 min | 62 | -143 | -2.30 | 97 | -226 | -2.33 | +143 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 40 | -158 | -3.95 | 119 | -210 | -1.77 | +158 |
| skip stock not beating SPY over 15 min | 25 | -22 | -0.90 | 134 | -346 | -2.58 | +22 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -184 | -5.41 | 125 | -185 | -1.48 | +184 |
| skip volume spikes above 5x average | 28 | -134 | -4.79 | 131 | -235 | -1.79 | +134 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 153 | -358 | -2.34 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 10 | -21 | -2.12 | 149 | -347 | -2.33 | +21 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 67 | -63 | -0.94 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 59% (39-77) | +2.81 | +0.42 | +9 | ▲ |
| 60-240 | 67 | 34% (24-46) | -0.59 | -2.27 | -152 |  |
| 240-375 | 46 | 26% (16-40) | -2.17 | -4.56 | -210 |  |
| 375-390 | 24 | 46% (28-65) | +1.55 | -0.67 | -16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 46 | 37% (25-51) | +0.16 | -1.42 | -65 |  |
| > 0.2 | 51 | 35% (24-49) | -0.84 | -3.10 | -158 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 36% (26-48) | -0.47 | -2.80 | -185 |  |
| above VWAP | 93 | 38% (28-48) | -0.10 | -1.97 | -183 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 53 | 36% (24-49) | -0.24 | -1.84 | -98 |  |
| (0.129, 0.369] | 53 | 40% (28-53) | -0.41 | -2.35 | -125 |  |
| (0.369, 1.555] | 53 | 36% (24-49) | -0.11 | -2.76 | -146 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 53 | 38% (26-51) | -0.34 | -2.11 | -112 |  |
| (0.147, 0.404] | 52 | 44% (32-58) | +1.17 | -1.04 | -54 |  |
| (0.404, 1.281] | 53 | 30% (20-44) | -1.45 | -3.71 | -196 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.242] | 53 | 38% (26-51) | -0.10 | -2.52 | -134 |  |
| (-0.242, 0.41] | 53 | 43% (31-57) | +0.60 | -0.75 | -40 |  |
| (0.41, 2.726] | 53 | 30% (20-44) | -1.25 | -3.68 | -195 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 53 | 38% (26-51) | -0.60 | -2.36 | -125 |  |
| (0.052, 0.122] | 53 | 43% (31-57) | +0.56 | -1.28 | -68 |  |
| (0.122, 0.678] | 53 | 30% (20-44) | -0.72 | -3.31 | -176 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 53 | 45% (33-59) | +0.18 | -1.11 | -59 |  |
| (0.198, 0.301] | 53 | 34% (23-47) | -0.30 | -2.55 | -135 |  |
| (0.301, 0.875] | 53 | 32% (21-45) | -0.64 | -3.29 | -174 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 53 | 34% (23-47) | -0.34 | -2.28 | -121 |  |
| (2.382, 3.448] | 53 | 49% (36-62) | +1.02 | -1.06 | -56 |  |
| (3.448, 18.76] | 53 | 28% (18-42) | -1.44 | -3.62 | -192 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0968] | 53 | 43% (31-57) | -0.04 | -0.83 | -44 |  |
| (0.0968, 0.147] | 53 | 34% (23-47) | -0.41 | -1.79 | -95 |  |
| (0.147, 0.392] | 53 | 34% (23-47) | -0.31 | -4.34 | -230 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.088] | 11 | 27% (10-57) | -2.04 | -3.07 | -34 |  |
| (-1.088, 0.125] | 11 | 18% (5-48) | -2.21 | -2.70 | -30 |  |
| (0.125, 5.305] | 11 | 64% (35-85) | +2.62 | +2.12 | +23 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 14 | 21% (8-48) | -2.87 | -3.63 | -51 |  |
| (0.486, 0.6] | 13 | 38% (18-64) | -0.51 | -1.13 | -15 |  |
| (0.6, 1.74] | 13 | 46% (23-71) | +0.86 | +0.05 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 14 | 43% (21-67) | +0.28 | -0.18 | -2 |  |
| (0.775, 1.178] | 13 | 38% (18-64) | +0.51 | -0.31 | -4 |  |
| (1.178, 3.566] | 13 | 23% (8-50) | -3.55 | -4.49 | -58 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 15 | 20% (7-45) | -2.25 | -2.88 | -43 |  |
| (0.315, 0.508] | 12 | 50% (25-75) | -0.00 | -0.64 | -8 |  |
| (0.508, 1.14] | 13 | 38% (18-64) | -0.14 | -1.07 | -14 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 83, target 39, time_stop 35, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0968] | 53 | 38% | 15% | 45% |
| (0.0968, 0.147] | 53 | 58% | 28% | 11% |
| (0.147, 0.392] | 53 | 60% | 30% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
