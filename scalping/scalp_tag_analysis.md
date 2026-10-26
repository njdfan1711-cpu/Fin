# Scalp signal analysis (fixed exits)

_160 tagged trades, 18 trading days (2026-10-01 to 2026-10-26). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 160 | 38% (30-45) | -0.19 | -2.24 | -359 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 24 | -16 | -0.67 | 136 | -343 | -2.52 | +16 |
| skip first 30 min | 1 | -6 | -6.31 | 159 | -352 | -2.22 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 98 | -213 | -2.18 | +145 |
| skip when SPY is below its VWAP | 66 | -185 | -2.80 | 94 | -174 | -1.85 | +185 |
| skip when SPY fell over the last 15 min | 63 | -133 | -2.11 | 97 | -226 | -2.33 | +133 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 40 | -158 | -3.95 | 120 | -201 | -1.67 | +158 |
| skip stock not beating SPY over 15 min | 26 | -13 | -0.49 | 134 | -346 | -2.58 | +13 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -184 | -5.41 | 126 | -175 | -1.39 | +184 |
| skip volume spikes above 5x average | 28 | -134 | -4.79 | 132 | -225 | -1.70 | +134 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 154 | -348 | -2.26 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 10 | -21 | -2.12 | 150 | -338 | -2.25 | +21 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 68 | -53 | -0.78 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 23 | 61% (41-78) | +3.12 | +0.83 | +19 | ▲ |
| 60-240 | 67 | 34% (24-46) | -0.59 | -2.27 | -152 |  |
| 240-375 | 46 | 26% (16-40) | -2.17 | -4.56 | -210 |  |
| 375-390 | 24 | 46% (28-65) | +1.55 | -0.67 | -16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 46 | 37% (25-51) | +0.16 | -1.42 | -65 |  |
| > 0.2 | 52 | 37% (25-50) | -0.63 | -2.85 | -148 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 36% (26-48) | -0.47 | -2.80 | -185 |  |
| above VWAP | 94 | 38% (29-48) | +0.01 | -1.85 | -174 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 54 | 37% (25-50) | -0.05 | -1.63 | -88 |  |
| (0.122, 0.368] | 53 | 40% (28-53) | -0.41 | -2.35 | -125 |  |
| (0.368, 1.555] | 53 | 36% (24-49) | -0.11 | -2.76 | -146 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.145] | 53 | 40% (28-53) | -0.05 | -1.79 | -95 |  |
| (0.145, 0.404] | 53 | 43% (31-57) | +1.04 | -1.15 | -61 |  |
| (0.404, 1.281] | 53 | 30% (20-44) | -1.45 | -3.71 | -196 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.239] | 54 | 37% (25-50) | -0.14 | -2.53 | -137 |  |
| (-0.239, 0.401] | 53 | 45% (33-59) | +0.83 | -0.51 | -27 |  |
| (0.401, 2.726] | 53 | 30% (20-44) | -1.25 | -3.68 | -195 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 54 | 37% (25-50) | -0.70 | -2.45 | -132 |  |
| (0.0521, 0.122] | 53 | 45% (33-59) | +0.86 | -0.96 | -51 |  |
| (0.122, 0.678] | 53 | 30% (20-44) | -0.72 | -3.31 | -176 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 54 | 44% (32-58) | +0.07 | -1.24 | -67 |  |
| (0.198, 0.301] | 53 | 36% (24-49) | +0.00 | -2.22 | -118 |  |
| (0.301, 0.875] | 53 | 32% (21-45) | -0.64 | -3.29 | -174 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 54 | 35% (24-49) | -0.14 | -2.06 | -111 |  |
| (2.389, 3.421] | 53 | 49% (36-62) | +1.01 | -1.05 | -56 |  |
| (3.421, 18.76] | 53 | 28% (18-42) | -1.44 | -3.62 | -192 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 54 | 43% (30-56) | -0.15 | -0.94 | -51 |  |
| (0.0971, 0.147] | 53 | 36% (24-49) | -0.11 | -1.47 | -78 |  |
| (0.147, 0.392] | 53 | 34% (23-47) | -0.31 | -4.34 | -230 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.913] | 12 | 25% (9-53) | -2.33 | -3.31 | -40 |  |
| (-0.913, 0.134] | 11 | 18% (5-48) | -2.21 | -2.71 | -30 |  |
| (0.134, 5.305] | 11 | 73% (43-90) | +4.03 | +3.56 | +39 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.488] | 14 | 21% (8-48) | -2.87 | -3.63 | -51 |  |
| (0.488, 0.597] | 13 | 38% (18-64) | -0.54 | -1.07 | -14 |  |
| (0.597, 1.74] | 14 | 50% (27-73) | +1.53 | +0.70 | +10 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.763] | 14 | 43% (21-67) | +0.81 | +0.39 | +5 |  |
| (0.763, 1.164] | 13 | 38% (18-64) | -0.08 | -0.91 | -12 |  |
| (1.164, 3.566] | 14 | 29% (12-55) | -2.57 | -3.47 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.315] | 15 | 20% (7-45) | -2.25 | -2.88 | -43 |  |
| (0.315, 0.495] | 12 | 58% (32-81) | +1.27 | +0.74 | +9 |  |
| (0.495, 1.14] | 14 | 36% (16-61) | -0.51 | -1.48 | -21 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 83, target 40, time_stop 35, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 54 | 39% | 15% | 44% |
| (0.0971, 0.147] | 53 | 57% | 30% | 11% |
| (0.147, 0.392] | 53 | 60% | 30% | 9% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
