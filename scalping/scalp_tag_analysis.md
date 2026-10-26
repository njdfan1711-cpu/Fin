# Scalp signal analysis (fixed exits)

_161 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 161 | 38% (31-46) | -0.17 | -2.22 | -357 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | -16 | -0.67 | 137 | -341 | -2.49 | +16 |
| skip first 30 min | 1 | -6 | -6.31 | 160 | -351 | -2.19 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 99 | -212 | -2.14 | +145 |
| skip when SPY is below its VWAP | 66 | -185 | -2.80 | 95 | -172 | -1.81 | +185 |
| skip when SPY fell over the last 15 min | 63 | -133 | -2.11 | 98 | -224 | -2.28 | +133 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 40 | -158 | -3.95 | 121 | -199 | -1.64 | +158 |
| skip stock not beating SPY over 15 min | 26 | -13 | -0.49 | 135 | -344 | -2.55 | +13 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -184 | -5.41 | 127 | -173 | -1.36 | +184 |
| skip volume spikes above 5x average | 28 | -134 | -4.79 | 133 | -223 | -1.68 | +134 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 155 | -346 | -2.23 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 11 | -13 | -1.15 | 150 | -344 | -2.29 | +13 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 69 | -52 | -0.75 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 61% (41-78) | +3.12 | +0.83 | +19 | ▲ |
| 60-240 | 68 | 35% (25-47) | -0.55 | -2.21 | -150 |  |
| 240-375 | 46 | 26% (16-40) | -2.17 | -4.56 | -210 |  |
| 375-390 | 24 | 46% (28-65) | +1.55 | -0.67 | -16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 46 | 37% (25-51) | +0.16 | -1.42 | -65 |  |
| > 0.2 | 53 | 38% (26-51) | -0.58 | -2.76 | -146 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 36% (26-48) | -0.47 | -2.80 | -185 |  |
| above VWAP | 95 | 39% (30-49) | +0.03 | -1.81 | -172 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 54 | 37% (25-50) | -0.05 | -1.63 | -88 |  |
| (0.126, 0.368] | 53 | 40% (28-53) | -0.40 | -2.34 | -124 |  |
| (0.368, 1.555] | 54 | 37% (25-50) | -0.08 | -2.69 | -145 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 54 | 39% (27-52) | -0.15 | -1.89 | -102 |  |
| (0.146, 0.403] | 53 | 45% (33-59) | +1.18 | -0.99 | -52 |  |
| (0.403, 1.281] | 53 | 30% (20-44) | -1.45 | -3.71 | -196 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.237] | 54 | 37% (25-50) | -0.14 | -2.53 | -137 |  |
| (-0.237, 0.418] | 53 | 45% (33-59) | +0.83 | -0.51 | -27 |  |
| (0.418, 2.726] | 54 | 31% (21-45) | -1.19 | -3.58 | -193 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 54 | 37% (25-50) | -0.70 | -2.45 | -132 |  |
| (0.0521, 0.122] | 53 | 47% (34-60) | +1.01 | -0.81 | -43 |  |
| (0.122, 0.678] | 54 | 30% (19-43) | -0.82 | -3.37 | -182 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 54 | 44% (32-58) | +0.07 | -1.24 | -67 |  |
| (0.198, 0.3] | 53 | 36% (24-49) | -0.14 | -2.37 | -125 |  |
| (0.3, 0.875] | 54 | 33% (22-47) | -0.45 | -3.05 | -165 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 54 | 35% (24-49) | -0.29 | -2.20 | -119 |  |
| (2.374, 3.392] | 53 | 51% (38-64) | +1.26 | -0.81 | -43 |  |
| (3.392, 18.76] | 54 | 28% (18-41) | -1.46 | -3.61 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 54 | 44% (32-58) | -0.00 | -0.78 | -42 |  |
| (0.0966, 0.146] | 53 | 36% (24-49) | -0.11 | -1.48 | -78 |  |
| (0.146, 0.392] | 54 | 33% (22-47) | -0.41 | -4.38 | -237 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.912] | 12 | 25% (9-53) | -2.33 | -3.31 | -40 |  |
| (-0.912, 0.297] | 11 | 18% (5-48) | -2.21 | -2.71 | -30 |  |
| (0.297, 5.305] | 12 | 75% (47-91) | +3.86 | +3.42 | +41 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.482] | 14 | 29% (12-55) | -2.30 | -2.99 | -42 |  |
| (0.482, 0.595] | 14 | 36% (16-61) | -0.92 | -1.50 | -21 |  |
| (0.595, 1.74] | 14 | 50% (27-73) | +1.53 | +0.70 | +10 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.751] | 14 | 50% (27-73) | +1.16 | +0.75 | +11 |  |
| (0.751, 1.15] | 14 | 36% (16-61) | -0.27 | -1.07 | -15 |  |
| (1.15, 3.566] | 14 | 29% (12-55) | -2.57 | -3.47 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 15 | 20% (7-45) | -2.25 | -2.88 | -43 |  |
| (0.315, 0.483] | 13 | 62% (36-82) | +1.33 | +0.83 | +11 |  |
| (0.483, 1.14] | 14 | 36% (16-61) | -0.51 | -1.48 | -21 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 83, target 40, time_stop 36, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 54 | 37% | 15% | 46% |
| (0.0966, 0.146] | 53 | 57% | 30% | 11% |
| (0.146, 0.392] | 54 | 61% | 30% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
