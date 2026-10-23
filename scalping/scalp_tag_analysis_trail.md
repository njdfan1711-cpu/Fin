# Scalp signal analysis (trail exits)

_156 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 156 | 35% (28-42) | -0.94 | -3.04 | -474 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | +10 | +0.43 | 133 | -484 | -3.64 | -10 |
| skip first 30 min | 1 | -6 | -6.31 | 155 | -468 | -3.02 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 94 | -221 | -2.35 | +254 |
| skip when SPY is below its VWAP | 64 | -272 | -4.26 | 92 | -202 | -2.20 | +272 |
| skip when SPY fell over the last 15 min | 61 | -178 | -2.92 | 95 | -296 | -3.12 | +178 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 39 | -186 | -4.78 | 117 | -288 | -2.46 | +186 |
| skip stock not beating SPY over 15 min | 24 | -53 | -2.21 | 132 | -421 | -3.19 | +53 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -193 | -5.68 | 122 | -281 | -2.31 | +193 |
| skip volume spikes above 5x average | 27 | -137 | -5.06 | 129 | -338 | -2.62 | +137 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 150 | -466 | -3.11 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 9 | -32 | -3.54 | 147 | -443 | -3.01 | +32 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 64 | -106 | -1.66 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 55% (35-73) | +0.18 | -2.22 | -49 | ▲ |
| 60-240 | 66 | 29% (19-41) | -1.53 | -3.23 | -213 |  |
| 240-375 | 45 | 31% (20-46) | -2.51 | -4.94 | -222 |  |
| 375-390 | 23 | 39% (22-59) | +2.72 | +0.43 | +10 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 44 | 32% (20-47) | -1.30 | -2.92 | -129 |  |
| > 0.2 | 50 | 40% (28-54) | +0.46 | -1.84 | -92 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 27% (17-38) | -1.86 | -4.26 | -272 |  |
| above VWAP | 92 | 40% (31-50) | -0.30 | -2.20 | -202 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 52 | 33% (22-46) | +0.12 | -1.51 | -79 |  |
| (0.129, 0.369] | 52 | 44% (32-58) | -1.09 | -3.06 | -159 |  |
| (0.369, 1.555] | 52 | 27% (17-40) | -1.86 | -4.56 | -237 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 52 | 35% (23-48) | -0.07 | -1.87 | -97 |  |
| (0.147, 0.404] | 51 | 37% (25-51) | -0.81 | -3.05 | -156 |  |
| (0.404, 1.281] | 52 | 33% (22-46) | -1.86 | -4.14 | -215 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.252] | 52 | 31% (20-44) | -1.55 | -4.00 | -208 |  |
| (-0.252, 0.387] | 52 | 48% (35-61) | +0.96 | -0.42 | -22 | ▲ |
| (0.387, 2.726] | 52 | 25% (15-38) | -2.24 | -4.70 | -245 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 52 | 35% (23-48) | -1.54 | -3.33 | -173 |  |
| (0.052, 0.122] | 52 | 38% (26-52) | +0.45 | -1.42 | -74 |  |
| (0.122, 0.678] | 52 | 31% (20-44) | -1.74 | -4.37 | -227 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 52 | 44% (32-58) | +0.23 | -1.09 | -57 |  |
| (0.197, 0.303] | 52 | 33% (22-46) | -1.30 | -3.59 | -187 |  |
| (0.303, 0.875] | 52 | 27% (17-40) | -1.76 | -4.45 | -231 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 52 | 35% (23-48) | -0.91 | -2.88 | -150 |  |
| (2.39, 3.448] | 52 | 42% (30-56) | -0.51 | -2.61 | -136 |  |
| (3.448, 18.76] | 52 | 27% (17-40) | -1.41 | -3.63 | -189 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0962] | 52 | 42% (30-56) | +0.30 | -0.46 | -24 |  |
| (0.0962, 0.148] | 52 | 35% (23-48) | -1.57 | -3.00 | -156 |  |
| (0.148, 0.392] | 52 | 27% (17-40) | -1.57 | -5.67 | -295 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.779] | 10 | 40% (17-69) | -2.33 | -3.32 | -33 |  |
| (-1.779, 0.0478] | 10 | 30% (11-60) | -2.37 | -2.98 | -30 |  |
| (0.0478, 5.305] | 10 | 60% (31-83) | -0.12 | -0.60 | -6 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.473] | 13 | 23% (8-50) | -2.69 | -3.42 | -44 |  |
| (0.473, 0.736] | 12 | 42% (19-68) | -2.29 | -2.98 | -36 |  |
| (0.736, 1.74] | 12 | 67% (39-86) | -0.44 | -1.28 | -15 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 13 | 46% (23-71) | -1.31 | -1.79 | -23 |  |
| (0.775, 1.178] | 12 | 50% (25-75) | -1.01 | -1.85 | -22 |  |
| (1.178, 3.566] | 12 | 33% (14-61) | -3.21 | -4.18 | -50 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.312] | 13 | 15% (4-42) | -3.38 | -4.03 | -52 |  |
| (0.312, 0.508] | 12 | 67% (39-86) | -0.08 | -0.73 | -9 | ▲ |
| (0.508, 1.14] | 12 | 50% (25-75) | -1.90 | -2.87 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 73, trail_stop 59, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0962] | 52 | 35% | 29% | 35% |
| (0.0962, 0.148] | 52 | 54% | 40% | 6% |
| (0.148, 0.392] | 52 | 52% | 44% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
