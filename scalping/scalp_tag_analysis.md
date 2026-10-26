# Scalp signal analysis (fixed exits)

_164 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 164 | 38% (31-45) | -0.22 | -2.24 | -367 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | -16 | -0.67 | 140 | -350 | -2.50 | +16 |
| skip first 30 min | 1 | -6 | -6.31 | 163 | -360 | -2.21 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 102 | -221 | -2.17 | +145 |
| skip when SPY is below its VWAP | 69 | -195 | -2.82 | 95 | -172 | -1.81 | +195 |
| skip when SPY fell over the last 15 min | 64 | -139 | -2.18 | 100 | -227 | -2.27 | +139 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 41 | -164 | -4.01 | 123 | -202 | -1.64 | +164 |
| skip stock not beating SPY over 15 min | 26 | -13 | -0.49 | 138 | -354 | -2.56 | +13 |
| skip afternoon entries (2:00-3:45 PM) | 36 | -197 | -5.46 | 128 | -170 | -1.33 | +197 |
| skip volume spikes above 5x average | 30 | -137 | -4.58 | 134 | -229 | -1.71 | +137 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 158 | -356 | -2.25 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 11 | -43 | -3.92 | 153 | -323 | -2.11 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 72 | -61 | -0.85 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 61% (41-78) | +3.12 | +0.83 | +19 | ▲ |
| 60-240 | 69 | 36% (26-48) | -0.49 | -2.13 | -147 |  |
| 240-375 | 48 | 25% (15-39) | -2.33 | -4.63 | -222 |  |
| 375-390 | 24 | 46% (28-65) | +1.55 | -0.67 | -16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 46 | 37% (25-51) | +0.16 | -1.42 | -65 |  |
| > 0.2 | 56 | 38% (26-51) | -0.70 | -2.79 | -156 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 69 | 36% (26-48) | -0.58 | -2.82 | -195 |  |
| above VWAP | 95 | 39% (30-49) | +0.03 | -1.81 | -172 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 55 | 38% (27-51) | +0.01 | -1.54 | -85 |  |
| (0.126, 0.369] | 54 | 41% (29-54) | -0.36 | -2.27 | -123 |  |
| (0.369, 1.555] | 55 | 35% (23-48) | -0.32 | -2.89 | -159 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 55 | 40% (28-53) | -0.08 | -1.80 | -99 |  |
| (0.146, 0.403] | 54 | 44% (32-58) | +1.05 | -1.09 | -59 |  |
| (0.403, 1.281] | 54 | 30% (19-43) | -1.54 | -3.76 | -203 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.237] | 55 | 36% (25-50) | -0.25 | -2.60 | -143 |  |
| (-0.237, 0.418] | 54 | 44% (32-58) | +0.71 | -0.62 | -33 |  |
| (0.418, 2.726] | 55 | 33% (22-46) | -1.11 | -3.46 | -190 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0534] | 55 | 36% (25-50) | -0.79 | -2.55 | -140 |  |
| (0.0534, 0.122] | 54 | 48% (35-61) | +1.05 | -0.71 | -38 |  |
| (0.122, 0.678] | 55 | 29% (19-42) | -0.91 | -3.42 | -188 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 55 | 45% (33-58) | +0.12 | -1.16 | -64 |  |
| (0.198, 0.301] | 54 | 37% (25-50) | +0.04 | -2.14 | -116 |  |
| (0.301, 0.875] | 55 | 31% (20-44) | -0.84 | -3.40 | -187 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 55 | 35% (23-48) | -0.39 | -2.28 | -125 |  |
| (2.374, 3.475] | 54 | 50% (37-63) | +1.18 | -0.86 | -46 |  |
| (3.475, 18.762] | 55 | 29% (19-42) | -1.44 | -3.54 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 55 | 45% (33-58) | +0.05 | -0.71 | -39 |  |
| (0.0966, 0.146] | 54 | 35% (24-49) | -0.22 | -1.57 | -85 |  |
| (0.146, 0.392] | 55 | 33% (22-46) | -0.51 | -4.42 | -243 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.862] | 13 | 23% (8-50) | -2.61 | -3.55 | -46 |  |
| (-0.862, 0.297] | 12 | 17% (5-45) | -2.53 | -3.02 | -36 |  |
| (0.297, 5.305] | 13 | 77% (50-92) | +3.81 | +3.40 | +44 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.482] | 15 | 33% (15-58) | -1.94 | -2.59 | -39 |  |
| (0.482, 0.603] | 15 | 40% (20-64) | -0.17 | -0.79 | -12 |  |
| (0.603, 1.74] | 15 | 40% (20-64) | -0.05 | -0.81 | -12 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.751] | 15 | 53% (30-75) | +1.29 | +0.91 | +14 |  |
| (0.751, 1.113] | 15 | 33% (15-58) | -0.68 | -1.42 | -21 |  |
| (1.113, 3.566] | 15 | 27% (11-52) | -2.77 | -3.68 | -55 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 16 | 25% (10-49) | -1.91 | -2.51 | -40 |  |
| (0.315, 0.514] | 14 | 57% (33-79) | +0.85 | +0.28 | +4 |  |
| (0.514, 1.14] | 15 | 33% (15-58) | -0.91 | -1.78 | -27 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 85, target 40, time_stop 37, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 55 | 36% | 15% | 47% |
| (0.0966, 0.146] | 54 | 57% | 30% | 11% |
| (0.146, 0.392] | 55 | 62% | 29% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
