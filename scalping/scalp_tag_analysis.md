# Scalp signal analysis (fixed exits)

_169 tagged trades, 19 trading days (2026-10-01 to 2026-10-27). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 169 | 38% (31-46) | -0.14 | -2.12 | -359 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 144 | -342 | -2.37 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 168 | -352 | -2.10 | +6 |
| skip when SPY is down on the day | 63 | -136 | -2.16 | 106 | -223 | -2.10 | +136 |
| skip when SPY is below its VWAP | 71 | -187 | -2.63 | 98 | -172 | -1.76 | +187 |
| skip when SPY fell over the last 15 min | 65 | -140 | -2.16 | 104 | -218 | -2.10 | +140 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 42 | -158 | -3.76 | 127 | -201 | -1.58 | +158 |
| skip stock not beating SPY over 15 min | 28 | -13 | -0.48 | 141 | -345 | -2.45 | +13 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -195 | -5.26 | 132 | -164 | -1.24 | +195 |
| skip volume spikes above 5x average | 31 | -140 | -4.52 | 138 | -218 | -1.58 | +140 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 162 | -357 | -2.21 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 13 | -34 | -2.58 | 156 | -325 | -2.08 | +34 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 95 | -294 | -3.09 | 74 | -65 | -0.88 | +294 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 24 | 62% (43-79) | +3.42 | +1.17 | +28 | ▲ |
| 60-240 | 71 | 37% (26-48) | -0.49 | -2.11 | -150 |  |
| 240-375 | 49 | 27% (16-40) | -2.21 | -4.50 | -220 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 39 | 38% (25-54) | -0.16 | -2.72 | -106 |  |
| 0 to 0.2 | 48 | 38% (25-52) | +0.13 | -1.41 | -68 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 71 | 37% (26-48) | -0.42 | -2.63 | -187 |  |
| above VWAP | 98 | 40% (31-50) | +0.06 | -1.76 | -172 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 57 | 39% (27-52) | +0.02 | -1.50 | -85 |  |
| (0.122, 0.368] | 56 | 43% (31-56) | -0.13 | -2.02 | -113 |  |
| (0.368, 1.555] | 56 | 34% (23-47) | -0.33 | -2.86 | -160 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 56 | 41% (29-54) | -0.02 | -1.72 | -97 |  |
| (0.147, 0.405] | 56 | 43% (31-56) | +0.86 | -1.23 | -69 |  |
| (0.405, 1.281] | 56 | 32% (21-45) | -1.17 | -3.34 | -187 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.25] | 57 | 37% (26-50) | -0.19 | -2.49 | -142 |  |
| (-0.25, 0.394] | 56 | 46% (34-59) | +0.95 | -0.36 | -20 |  |
| (0.394, 2.726] | 56 | 32% (21-45) | -1.20 | -3.52 | -197 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 57 | 39% (27-52) | -0.52 | -2.22 | -127 |  |
| (0.0518, 0.12] | 56 | 46% (34-59) | +0.80 | -0.95 | -53 |  |
| (0.12, 0.678] | 56 | 30% (20-43) | -0.71 | -3.20 | -179 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.2] | 57 | 44% (32-57) | +0.01 | -1.28 | -73 |  |
| (0.2, 0.301] | 56 | 39% (28-52) | +0.19 | -1.93 | -108 |  |
| (0.301, 0.875] | 56 | 32% (21-45) | -0.64 | -3.18 | -178 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.367] | 57 | 37% (26-50) | -0.14 | -2.00 | -114 |  |
| (2.367, 3.502] | 56 | 50% (37-63) | +1.29 | -0.71 | -40 |  |
| (3.502, 18.762] | 56 | 29% (18-41) | -1.58 | -3.66 | -205 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0966] | 57 | 46% (33-58) | +0.07 | -0.69 | -40 |  |
| (0.0966, 0.147] | 56 | 34% (23-47) | -0.32 | -1.65 | -92 |  |
| (0.147, 0.392] | 56 | 36% (24-49) | -0.18 | -4.05 | -227 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.911] | 15 | 27% (11-52) | -2.07 | -2.99 | -45 |  |
| (-0.911, 0.379] | 15 | 33% (15-58) | -1.04 | -1.53 | -23 |  |
| (0.379, 5.305] | 13 | 69% (42-87) | +3.42 | +2.88 | +37 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.484] | 17 | 35% (17-59) | -1.65 | -2.33 | -40 |  |
| (0.484, 0.607] | 16 | 38% (18-61) | -0.19 | -0.80 | -13 |  |
| (0.607, 1.74] | 17 | 47% (26-69) | +0.66 | -0.15 | -3 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 17 | 53% (31-74) | +1.13 | +0.72 | +12 |  |
| (0.779, 1.164] | 16 | 31% (14-56) | -0.47 | -1.27 | -20 |  |
| (1.164, 3.566] | 17 | 35% (17-59) | -1.85 | -2.77 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 17 | 29% (13-53) | -1.60 | -2.23 | -38 |  |
| (0.315, 0.521] | 16 | 50% (28-72) | +0.57 | +0.00 | +0 |  |
| (0.521, 1.14] | 17 | 41% (22-64) | -0.10 | -1.01 | -17 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 85, target 41, time_stop 40, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0966] | 57 | 35% | 14% | 49% |
| (0.0966, 0.147] | 56 | 57% | 29% | 11% |
| (0.147, 0.392] | 56 | 59% | 30% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
