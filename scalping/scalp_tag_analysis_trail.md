# Scalp signal analysis (trail exits)

_164 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 164 | 35% (28-43) | -0.95 | -2.96 | -486 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | +13 | +0.52 | 140 | -498 | -3.56 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 163 | -479 | -2.94 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 102 | -232 | -2.27 | +254 |
| skip when SPY is below its VWAP | 69 | -286 | -4.14 | 95 | -200 | -2.10 | +286 |
| skip when SPY fell over the last 15 min | 64 | -175 | -2.74 | 100 | -310 | -3.10 | +175 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 41 | -193 | -4.71 | 123 | -293 | -2.38 | +193 |
| skip stock not beating SPY over 15 min | 26 | -52 | -2.02 | 138 | -433 | -3.14 | +52 |
| skip afternoon entries (2:00-3:45 PM) | 36 | -206 | -5.72 | 128 | -280 | -2.19 | +206 |
| skip volume spikes above 5x average | 30 | -146 | -4.87 | 134 | -339 | -2.53 | +146 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 158 | -477 | -3.02 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 11 | -45 | -4.06 | 153 | -441 | -2.88 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 72 | -118 | -1.63 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 57% (37-74) | +0.47 | -1.83 | -42 | ▲ |
| 60-240 | 69 | 30% (21-42) | -1.47 | -3.11 | -214 |  |
| 240-375 | 48 | 29% (18-43) | -2.73 | -5.04 | -242 |  |
| 375-390 | 24 | 42% (24-61) | +2.74 | +0.52 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 46 | 33% (21-47) | -1.30 | -2.88 | -132 |  |
| > 0.2 | 56 | 41% (29-54) | +0.31 | -1.78 | -99 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 69 | 28% (18-39) | -1.89 | -4.14 | -286 |  |
| above VWAP | 95 | 41% (32-51) | -0.26 | -2.10 | -200 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 55 | 35% (23-48) | +0.18 | -1.36 | -75 |  |
| (0.126, 0.369] | 54 | 44% (32-58) | -1.12 | -3.03 | -164 |  |
| (0.369, 1.555] | 55 | 27% (17-40) | -1.92 | -4.49 | -247 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 55 | 36% (25-50) | +0.01 | -1.70 | -94 |  |
| (0.146, 0.403] | 54 | 39% (27-52) | -0.78 | -2.92 | -157 |  |
| (0.403, 1.281] | 54 | 31% (21-45) | -2.01 | -4.23 | -228 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.237] | 55 | 31% (20-44) | -1.55 | -3.90 | -214 |  |
| (-0.237, 0.418] | 54 | 50% (37-63) | +0.95 | -0.37 | -20 | ▲ |
| (0.418, 2.726] | 55 | 25% (16-38) | -2.22 | -4.57 | -251 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0534] | 55 | 35% (23-48) | -1.65 | -3.41 | -187 |  |
| (0.0534, 0.122] | 54 | 41% (29-54) | +0.63 | -1.13 | -61 |  |
| (0.122, 0.678] | 55 | 31% (20-44) | -1.80 | -4.32 | -237 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 55 | 45% (33-58) | +0.40 | -0.88 | -48 |  |
| (0.198, 0.301] | 54 | 35% (24-49) | -1.36 | -3.54 | -191 |  |
| (0.301, 0.875] | 55 | 25% (16-38) | -1.91 | -4.47 | -246 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 55 | 35% (23-48) | -1.00 | -2.89 | -159 |  |
| (2.374, 3.475] | 54 | 44% (32-58) | -0.34 | -2.38 | -129 |  |
| (3.475, 18.762] | 55 | 27% (17-40) | -1.49 | -3.60 | -198 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 55 | 44% (31-57) | +0.27 | -0.49 | -27 |  |
| (0.0966, 0.146] | 54 | 37% (25-50) | -1.33 | -2.68 | -145 |  |
| (0.146, 0.392] | 55 | 25% (16-38) | -1.81 | -5.72 | -314 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.862] | 13 | 31% (13-58) | -3.10 | -4.03 | -52 |  |
| (-0.862, 0.297] | 12 | 25% (9-53) | -3.01 | -3.50 | -42 |  |
| (0.297, 5.305] | 13 | 77% (50-92) | +1.51 | +1.09 | +14 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.482] | 15 | 33% (15-58) | -1.98 | -2.63 | -40 |  |
| (0.482, 0.603] | 15 | 47% (25-70) | -1.56 | -2.19 | -33 |  |
| (0.603, 1.74] | 15 | 53% (30-75) | -1.54 | -2.30 | -35 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.751] | 15 | 53% (30-75) | -0.72 | -1.10 | -16 |  |
| (0.751, 1.113] | 15 | 40% (20-64) | -1.85 | -2.60 | -39 |  |
| (1.113, 3.566] | 15 | 40% (20-64) | -2.52 | -3.43 | -51 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 16 | 25% (10-49) | -2.82 | -3.41 | -55 |  |
| (0.315, 0.514] | 14 | 64% (39-84) | +0.02 | -0.55 | -8 | ▲ |
| (0.514, 1.14] | 15 | 47% (25-70) | -2.11 | -2.97 | -45 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 77, trail_stop 61, time_stop 25, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 55 | 35% | 27% | 36% |
| (0.0966, 0.146] | 54 | 52% | 43% | 6% |
| (0.146, 0.392] | 55 | 55% | 42% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
