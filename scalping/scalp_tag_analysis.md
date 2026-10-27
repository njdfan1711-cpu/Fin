# Scalp signal analysis (fixed exits)

_166 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 166 | 38% (31-46) | -0.20 | -2.20 | -365 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 141 | -348 | -2.47 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 165 | -359 | -2.18 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 104 | -220 | -2.12 | +145 |
| skip when SPY is below its VWAP | 70 | -196 | -2.80 | 96 | -170 | -1.77 | +196 |
| skip when SPY fell over the last 15 min | 65 | -140 | -2.16 | 101 | -225 | -2.23 | +140 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 41 | -174 | -4.25 | 125 | -191 | -1.53 | +174 |
| skip stock not beating SPY over 15 min | 27 | -10 | -0.39 | 139 | -355 | -2.55 | +10 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -195 | -5.26 | 129 | -171 | -1.32 | +195 |
| skip volume spikes above 5x average | 30 | -137 | -4.58 | 136 | -228 | -1.68 | +137 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 160 | -355 | -2.22 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 12 | -34 | -2.83 | 154 | -331 | -2.15 | +34 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 93 | -303 | -3.26 | 73 | -62 | -0.85 | +303 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 61% (41-78) | +3.12 | +0.83 | +19 | ▲ |
| 60-240 | 69 | 36% (26-48) | -0.49 | -2.13 | -147 |  |
| 240-375 | 49 | 27% (16-40) | -2.21 | -4.50 | -220 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 46 | 37% (25-51) | +0.16 | -1.42 | -65 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 70 | 36% (26-47) | -0.57 | -2.80 | -196 |  |
| above VWAP | 96 | 40% (30-50) | +0.07 | -1.77 | -170 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 56 | 39% (28-52) | +0.07 | -1.47 | -82 |  |
| (0.122, 0.37] | 55 | 40% (28-53) | -0.46 | -2.44 | -134 |  |
| (0.37, 1.555] | 55 | 35% (23-48) | -0.22 | -2.71 | -149 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.145] | 55 | 42% (30-55) | +0.07 | -1.63 | -90 |  |
| (0.145, 0.404] | 55 | 44% (31-57) | +0.93 | -1.19 | -66 |  |
| (0.404, 1.281] | 55 | 29% (19-42) | -1.52 | -3.70 | -204 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.25] | 56 | 38% (26-51) | -0.15 | -2.48 | -139 |  |
| (-0.25, 0.401] | 55 | 44% (31-57) | +0.64 | -0.66 | -37 |  |
| (0.401, 2.726] | 55 | 33% (22-46) | -1.11 | -3.46 | -190 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 56 | 38% (26-51) | -0.62 | -2.34 | -131 |  |
| (0.0521, 0.121] | 55 | 47% (35-60) | +0.93 | -0.84 | -46 |  |
| (0.121, 0.678] | 55 | 29% (19-42) | -0.91 | -3.42 | -188 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 56 | 45% (32-58) | +0.02 | -1.28 | -72 |  |
| (0.198, 0.301] | 55 | 38% (27-51) | +0.20 | -1.94 | -107 |  |
| (0.301, 0.875] | 55 | 31% (20-44) | -0.84 | -3.40 | -187 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.367] | 56 | 36% (24-49) | -0.33 | -2.20 | -123 |  |
| (2.367, 3.421] | 55 | 49% (36-62) | +1.15 | -0.86 | -47 |  |
| (3.421, 18.762] | 55 | 29% (19-42) | -1.44 | -3.54 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 56 | 46% (34-59) | +0.11 | -0.65 | -37 |  |
| (0.0966, 0.145] | 55 | 35% (23-48) | -0.22 | -1.56 | -86 |  |
| (0.145, 0.392] | 55 | 33% (22-46) | -0.51 | -4.42 | -243 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.913] | 14 | 29% (12-55) | -1.79 | -2.75 | -38 |  |
| (-0.913, 0.134] | 13 | 15% (4-42) | -2.79 | -3.28 | -43 |  |
| (0.134, 5.305] | 13 | 77% (50-92) | +3.81 | +3.40 | +44 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.484] | 16 | 38% (18-61) | -1.61 | -2.29 | -37 |  |
| (0.484, 0.597] | 15 | 33% (15-58) | -0.89 | -1.46 | -22 |  |
| (0.597, 1.74] | 16 | 44% (23-67) | +0.59 | -0.19 | -3 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.763] | 16 | 50% (28-72) | +1.03 | +0.65 | +10 |  |
| (0.763, 1.164] | 15 | 33% (15-58) | -0.87 | -1.64 | -25 |  |
| (1.164, 3.566] | 16 | 31% (14-56) | -2.07 | -2.96 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 17 | 29% (13-53) | -1.60 | -2.23 | -38 |  |
| (0.315, 0.495] | 14 | 57% (33-79) | +1.20 | +0.70 | +10 |  |
| (0.495, 1.14] | 16 | 31% (14-56) | -1.19 | -2.09 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 85, target 40, time_stop 38, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 56 | 36% | 14% | 48% |
| (0.0966, 0.145] | 55 | 56% | 29% | 11% |
| (0.145, 0.392] | 55 | 62% | 29% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
