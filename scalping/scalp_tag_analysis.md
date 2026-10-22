# Scalp signal analysis (fixed exits)

_151 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 151 | 37% (30-45) | -0.24 | -2.38 | -360 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | -31 | -1.41 | 129 | -329 | -2.55 | +31 |
| skip first 30 min | 1 | -6 | -6.31 | 150 | -353 | -2.36 | +6 |
| skip when SPY is down on the day | 58 | -151 | -2.61 | 93 | -208 | -2.24 | +151 |
| skip when SPY is below its VWAP | 60 | -190 | -3.17 | 91 | -170 | -1.87 | +190 |
| skip when SPY fell over the last 15 min | 59 | -151 | -2.56 | 92 | -209 | -2.27 | +151 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 38 | -144 | -3.79 | 113 | -216 | -1.91 | +144 |
| skip stock not beating SPY over 15 min | 22 | -36 | -1.63 | 129 | -324 | -2.51 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 33 | -177 | -5.37 | 118 | -183 | -1.55 | +177 |
| skip volume spikes above 5x average | 27 | -128 | -4.73 | 124 | -232 | -1.87 | +128 |
| skip when the stop is inside normal noise (range > stop) | 4 | +4 | +0.89 | 147 | -363 | -2.47 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 8 | -7 | -0.88 | 143 | -353 | -2.47 | +7 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 91 | -298 | -3.27 | 60 | -62 | -1.03 | +298 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 65 | 35% (25-48) | -0.42 | -2.13 | -138 |  |
| 240-375 | 44 | 27% (16-42) | -2.00 | -4.47 | -197 |  |
| 375-390 | 22 | 41% (23-61) | +0.97 | -1.41 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 36 | 36% (22-52) | -0.57 | -3.28 | -118 |  |
| 0 to 0.2 | 43 | 37% (24-52) | +0.31 | -1.31 | -57 |  |
| > 0.2 | 50 | 36% (24-50) | -0.73 | -3.04 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 60 | 35% (24-48) | -0.65 | -3.17 | -190 |  |
| above VWAP | 91 | 38% (29-49) | +0.03 | -1.87 | -170 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 51 | 35% (24-49) | -0.33 | -2.00 | -102 |  |
| (0.132, 0.37] | 50 | 40% (28-54) | -0.40 | -2.50 | -125 |  |
| (0.37, 1.555] | 50 | 36% (24-50) | +0.01 | -2.66 | -133 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 50 | 36% (24-50) | -0.64 | -2.50 | -125 |  |
| (0.147, 0.404] | 50 | 44% (31-58) | +1.22 | -1.05 | -53 |  |
| (0.404, 1.192] | 50 | 32% (21-46) | -1.18 | -3.52 | -176 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.257] | 51 | 37% (25-51) | -0.11 | -2.59 | -132 |  |
| (-0.257, 0.364] | 50 | 44% (31-58) | +0.74 | -0.64 | -32 |  |
| (0.364, 2.726] | 50 | 30% (19-44) | -1.36 | -3.91 | -195 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 51 | 37% (25-51) | -0.71 | -2.53 | -129 |  |
| (0.0521, 0.122] | 50 | 44% (31-58) | +0.64 | -1.29 | -64 |  |
| (0.122, 0.678] | 50 | 30% (19-44) | -0.64 | -3.33 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 51 | 45% (32-59) | +0.11 | -1.22 | -62 |  |
| (0.197, 0.307] | 50 | 32% (21-46) | -0.42 | -2.83 | -141 |  |
| (0.307, 0.875] | 50 | 34% (22-48) | -0.42 | -3.12 | -156 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.408] | 51 | 37% (25-51) | +0.13 | -2.01 | -102 |  |
| (2.408, 3.502] | 50 | 48% (35-61) | +0.93 | -1.09 | -55 |  |
| (3.502, 18.76] | 50 | 26% (16-40) | -1.78 | -4.05 | -203 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 51 | 45% (32-59) | +0.19 | -0.57 | -29 |  |
| (0.0946, 0.147] | 50 | 30% (19-44) | -0.95 | -2.42 | -121 |  |
| (0.147, 0.392] | 50 | 36% (24-50) | +0.03 | -4.19 | -210 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.439] | 9 | 33% (12-65) | -1.18 | -2.21 | -20 | few trades |
| (-1.439, 0.134] | 8 | 0% (0-32) | -4.78 | -5.29 | -42 | few trades |
| (0.134, 5.305] | 8 | 75% (41-93) | +4.33 | +3.85 | +31 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.457] | 11 | 27% (10-57) | -2.59 | -3.31 | -36 |  |
| (0.457, 0.691] | 10 | 20% (6-51) | -2.63 | -3.45 | -35 |  |
| (0.691, 1.74] | 11 | 55% (28-79) | +2.10 | +1.35 | +15 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.763] | 11 | 36% (15-65) | -0.23 | -0.72 | -8 |  |
| (0.763, 1.164] | 10 | 40% (17-69) | +0.05 | -0.83 | -8 |  |
| (1.164, 3.566] | 11 | 27% (10-57) | -2.70 | -3.62 | -40 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.302] | 11 | 9% (2-38) | -3.51 | -4.18 | -46 |  |
| (0.302, 0.495] | 10 | 60% (31-83) | +0.77 | +0.14 | +1 |  |
| (0.495, 0.815] | 11 | 36% (15-65) | -0.08 | -1.05 | -12 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 78, target 37, time_stop 35, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 51 | 35% | 16% | 47% |
| (0.0946, 0.147] | 50 | 62% | 26% | 12% |
| (0.147, 0.392] | 50 | 58% | 32% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
