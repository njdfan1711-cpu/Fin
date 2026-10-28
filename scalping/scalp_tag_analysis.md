# Scalp signal analysis (fixed exits)

_180 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 180 | 39% (32-46) | -0.03 | -1.94 | -349 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 155 | -332 | -2.14 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 179 | -343 | -1.91 | +6 |
| skip when SPY is down on the day | 69 | -113 | -1.63 | 111 | -236 | -2.13 | +113 |
| skip when SPY is below its VWAP | 74 | -189 | -2.56 | 106 | -160 | -1.51 | +189 |
| skip when SPY fell over the last 15 min | 68 | -141 | -2.07 | 112 | -208 | -1.86 | +141 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 45 | -162 | -3.60 | 135 | -187 | -1.38 | +162 |
| skip stock not beating SPY over 15 min | 30 | -23 | -0.77 | 150 | -326 | -2.17 | +23 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -195 | -5.26 | 143 | -154 | -1.08 | +195 |
| skip volume spikes above 5x average | 33 | -150 | -4.53 | 147 | -199 | -1.36 | +150 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 173 | -348 | -2.01 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.57%) | 15 | -47 | -3.16 | 165 | -302 | -1.83 | +47 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 100 | -282 | -2.82 | 80 | -67 | -0.84 | +282 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 64% (45-80) | +3.57 | +1.39 | +35 | ▲ |
| 60-240 | 81 | 37% (27-48) | -0.28 | -1.81 | -146 |  |
| 240-375 | 49 | 27% (16-40) | -2.21 | -4.50 | -220 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 45 | 42% (29-57) | +0.51 | -1.84 | -83 |  |
| 0 to 0.2 | 53 | 36% (24-49) | -0.06 | -1.53 | -81 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 74 | 36% (26-48) | -0.42 | -2.56 | -189 |  |
| above VWAP | 106 | 41% (32-50) | +0.24 | -1.51 | -160 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 60 | 38% (27-51) | +0.05 | -1.42 | -85 |  |
| (0.129, 0.367] | 60 | 43% (32-56) | +0.16 | -1.67 | -100 |  |
| (0.367, 1.555] | 60 | 35% (24-48) | -0.30 | -2.73 | -164 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.149] | 60 | 43% (32-56) | +0.34 | -1.33 | -80 |  |
| (0.149, 0.41] | 59 | 41% (29-53) | +0.63 | -1.37 | -81 |  |
| (0.41, 1.281] | 60 | 33% (23-46) | -0.94 | -3.03 | -182 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.286] | 60 | 38% (27-51) | +0.02 | -2.23 | -134 |  |
| (-0.286, 0.371] | 60 | 45% (33-58) | +1.01 | -0.27 | -16 |  |
| (0.371, 2.726] | 60 | 33% (23-46) | -1.11 | -3.32 | -199 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 60 | 40% (29-53) | -0.25 | -1.92 | -115 |  |
| (0.052, 0.119] | 60 | 47% (35-59) | +1.00 | -0.55 | -33 |  |
| (0.119, 0.678] | 60 | 30% (20-43) | -0.84 | -3.35 | -201 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.201] | 60 | 45% (33-58) | +0.26 | -1.00 | -60 |  |
| (0.201, 0.303] | 60 | 38% (27-51) | +0.24 | -1.79 | -108 |  |
| (0.303, 0.875] | 60 | 33% (23-46) | -0.58 | -3.02 | -181 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 60 | 38% (27-51) | +0.11 | -1.71 | -103 |  |
| (2.382, 3.545] | 60 | 50% (38-62) | +1.35 | -0.55 | -33 |  |
| (3.545, 18.762] | 60 | 28% (19-41) | -1.55 | -3.55 | -213 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0962] | 60 | 47% (35-59) | +0.49 | -0.24 | -14 |  |
| (0.0962, 0.145] | 60 | 35% (24-48) | -0.28 | -1.57 | -94 |  |
| (0.145, 0.392] | 60 | 35% (24-48) | -0.29 | -4.01 | -240 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.564] | 18 | 22% (9-45) | -2.54 | -3.41 | -61 |  |
| (-0.564, 0.454] | 18 | 39% (20-61) | -0.11 | -0.66 | -12 |  |
| (0.454, 5.305] | 18 | 67% (44-84) | +3.59 | +2.92 | +53 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.473] | 21 | 38% (21-59) | -0.42 | -1.07 | -22 |  |
| (0.473, 0.619] | 20 | 35% (18-57) | -0.85 | -1.48 | -30 |  |
| (0.619, 1.74] | 20 | 50% (30-70) | +1.26 | +0.34 | +7 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 21 | 52% (32-72) | +1.33 | +0.92 | +19 |  |
| (0.789, 1.188] | 20 | 35% (18-57) | +0.24 | -0.60 | -12 |  |
| (1.188, 3.566] | 20 | 35% (18-57) | -1.67 | -2.62 | -52 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.316] | 21 | 33% (17-55) | -0.59 | -1.16 | -24 |  |
| (0.316, 0.527] | 20 | 55% (34-74) | +1.34 | +0.65 | +13 |  |
| (0.527, 1.14] | 20 | 35% (18-57) | -0.75 | -1.70 | -34 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 89, target 45, time_stop 43, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0962] | 60 | 32% | 17% | 50% |
| (0.0962, 0.145] | 60 | 57% | 28% | 12% |
| (0.145, 0.392] | 60 | 60% | 30% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
