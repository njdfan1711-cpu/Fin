# Scalp signal analysis (trail exits)

_161 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 161 | 35% (28-43) | -0.91 | -2.96 | -476 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | +13 | +0.52 | 137 | -489 | -3.57 | -13 |
| skip first 30 min | 1 | -6 | -6.31 | 160 | -470 | -2.94 | +6 |
| skip when SPY is down on the day | 62 | -254 | -4.09 | 99 | -222 | -2.24 | +254 |
| skip when SPY is below its VWAP | 66 | -276 | -4.18 | 95 | -200 | -2.10 | +276 |
| skip when SPY fell over the last 15 min | 63 | -169 | -2.68 | 98 | -307 | -3.13 | +169 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 40 | -187 | -4.66 | 121 | -289 | -2.39 | +187 |
| skip stock not beating SPY over 15 min | 26 | -52 | -2.02 | 135 | -423 | -3.14 | +52 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -193 | -5.68 | 127 | -283 | -2.23 | +193 |
| skip volume spikes above 5x average | 28 | -143 | -5.10 | 133 | -333 | -2.50 | +143 |
| skip when the stop is inside normal noise (range > stop) | 6 | -9 | -1.42 | 155 | -467 | -3.02 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 11 | -28 | -2.55 | 150 | -448 | -2.99 | +28 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -368 | -4.00 | 69 | -108 | -1.56 | +368 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 57% (37-74) | +0.47 | -1.83 | -42 | ▲ |
| 60-240 | 68 | 29% (20-41) | -1.54 | -3.20 | -218 |  |
| 240-375 | 46 | 30% (19-45) | -2.59 | -4.98 | -229 |  |
| 375-390 | 24 | 42% (24-61) | +2.74 | +0.52 | +13 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 38 | 32% (19-47) | -2.18 | -4.78 | -182 |  |
| 0 to 0.2 | 46 | 33% (21-47) | -1.30 | -2.88 | -132 |  |
| > 0.2 | 53 | 42% (29-55) | +0.49 | -1.69 | -90 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 27% (18-39) | -1.85 | -4.18 | -276 |  |
| above VWAP | 95 | 41% (32-51) | -0.26 | -2.10 | -200 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 54 | 33% (22-47) | +0.13 | -1.45 | -78 |  |
| (0.126, 0.368] | 53 | 43% (31-57) | -1.16 | -3.10 | -164 |  |
| (0.368, 1.555] | 54 | 30% (19-43) | -1.72 | -4.33 | -234 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 54 | 35% (24-49) | -0.05 | -1.79 | -97 |  |
| (0.146, 0.403] | 53 | 40% (28-53) | -0.68 | -2.85 | -151 |  |
| (0.403, 1.281] | 53 | 32% (21-45) | -1.94 | -4.19 | -222 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.237] | 54 | 31% (21-45) | -1.46 | -3.85 | -208 |  |
| (-0.237, 0.418] | 53 | 51% (38-64) | +1.08 | -0.26 | -14 | ▲ |
| (0.418, 2.726] | 54 | 24% (15-37) | -2.32 | -4.71 | -254 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 54 | 35% (24-49) | -1.57 | -3.32 | -179 |  |
| (0.0521, 0.122] | 53 | 40% (28-53) | +0.58 | -1.24 | -66 |  |
| (0.122, 0.678] | 54 | 31% (21-45) | -1.73 | -4.28 | -231 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 54 | 44% (32-58) | +0.35 | -0.95 | -52 |  |
| (0.198, 0.3] | 53 | 34% (23-47) | -1.40 | -3.62 | -192 |  |
| (0.3, 0.875] | 54 | 28% (18-41) | -1.70 | -4.30 | -232 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 54 | 35% (24-49) | -0.91 | -2.82 | -153 |  |
| (2.374, 3.392] | 53 | 45% (33-59) | -0.30 | -2.36 | -125 |  |
| (3.392, 18.76] | 54 | 26% (16-39) | -1.52 | -3.67 | -198 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 54 | 43% (30-56) | +0.22 | -0.55 | -30 |  |
| (0.0966, 0.146] | 53 | 38% (26-51) | -1.24 | -2.61 | -138 |  |
| (0.146, 0.392] | 54 | 26% (16-39) | -1.73 | -5.70 | -308 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.912] | 12 | 33% (14-61) | -2.86 | -3.83 | -46 |  |
| (-0.912, 0.297] | 11 | 27% (10-57) | -2.74 | -3.23 | -36 |  |
| (0.297, 5.305] | 12 | 75% (47-91) | +1.37 | +0.92 | +11 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.482] | 14 | 29% (12-55) | -2.35 | -3.04 | -43 |  |
| (0.482, 0.595] | 14 | 43% (21-67) | -1.81 | -2.39 | -34 |  |
| (0.595, 1.74] | 14 | 64% (39-84) | -0.66 | -1.50 | -21 | ▲ |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.751] | 14 | 50% (27-73) | -1.00 | -1.40 | -20 |  |
| (0.751, 1.15] | 14 | 43% (21-67) | -1.54 | -2.33 | -33 |  |
| (1.15, 3.566] | 14 | 43% (21-67) | -2.30 | -3.20 | -45 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 15 | 20% (7-45) | -3.22 | -3.85 | -58 |  |
| (0.315, 0.483] | 13 | 62% (36-82) | -0.12 | -0.63 | -8 | ▲ |
| (0.483, 1.14] | 14 | 57% (33-79) | -1.27 | -2.23 | -31 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 75, trail_stop 61, time_stop 24, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 54 | 35% | 28% | 35% |
| (0.0966, 0.146] | 53 | 51% | 43% | 6% |
| (0.146, 0.392] | 54 | 54% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
