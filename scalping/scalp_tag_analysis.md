# Scalp signal analysis (fixed exits)

_199 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 199 | 39% (33-46) | -0.00 | -1.80 | -358 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 29 | -3 | -0.10 | 170 | -355 | -2.09 | +3 |
| skip first 30 min | 1 | -6 | -6.31 | 198 | -352 | -1.78 | +6 |
| skip when SPY is down on the day | 80 | -120 | -1.50 | 119 | -238 | -2.00 | +120 |
| skip when SPY is below its VWAP | 83 | -183 | -2.20 | 116 | -175 | -1.51 | +183 |
| skip when SPY fell over the last 15 min | 75 | -130 | -1.73 | 124 | -228 | -1.84 | +130 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 50 | -164 | -3.28 | 149 | -194 | -1.30 | +164 |
| skip stock not beating SPY over 15 min | 33 | -26 | -0.79 | 166 | -332 | -2.00 | +26 |
| skip afternoon entries (2:00-3:45 PM) | 43 | -205 | -4.77 | 156 | -153 | -0.98 | +205 |
| skip volume spikes above 5x average | 38 | -167 | -4.39 | 161 | -191 | -1.19 | +167 |
| skip when the stop is inside normal noise (range > stop) | 11 | -28 | -2.58 | 188 | -330 | -1.75 | +28 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 20 | -32 | -1.62 | 179 | -326 | -1.82 | +32 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 106 | -291 | -2.75 | 93 | -67 | -0.72 | +291 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 59% (41-74) | +2.81 | +0.83 | +24 | ▲ |
| 60-240 | 85 | 36% (27-47) | -0.37 | -1.86 | -159 |  |
| 240-375 | 56 | 29% (18-41) | -1.86 | -3.95 | -221 |  |
| 375-390 | 29 | 48% (31-66) | +1.87 | -0.10 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 29 | 45% (28-62) | +0.81 | -0.77 | -22 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 61 | 36% (25-49) | +0.00 | -1.37 | -84 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 83 | 39% (29-49) | -0.22 | -2.20 | -183 |  |
| above VWAP | 116 | 40% (31-49) | +0.15 | -1.51 | -175 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 67 | 39% (28-51) | +0.05 | -1.34 | -90 |  |
| (0.132, 0.374] | 67 | 43% (32-55) | +0.06 | -1.74 | -117 |  |
| (0.374, 1.555] | 65 | 35% (25-48) | -0.12 | -2.33 | -151 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 66 | 41% (30-53) | +0.11 | -1.31 | -86 |  |
| (0.118, 0.404] | 66 | 44% (33-56) | +0.88 | -1.12 | -74 |  |
| (0.404, 1.281] | 66 | 33% (23-45) | -0.90 | -2.91 | -192 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.348] | 67 | 40% (29-52) | +0.13 | -1.94 | -130 |  |
| (-0.348, 0.338] | 66 | 44% (33-56) | +0.94 | -0.29 | -19 |  |
| (0.338, 2.726] | 66 | 33% (23-45) | -1.08 | -3.18 | -210 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 67 | 40% (29-52) | -0.19 | -1.75 | -117 |  |
| (0.0521, 0.122] | 66 | 45% (34-57) | +0.76 | -0.84 | -55 |  |
| (0.122, 0.678] | 66 | 32% (22-44) | -0.57 | -2.81 | -185 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.206] | 67 | 43% (32-55) | +0.07 | -1.15 | -77 |  |
| (0.206, 0.312] | 66 | 39% (29-51) | +0.28 | -1.69 | -112 |  |
| (0.312, 0.875] | 66 | 35% (24-47) | -0.36 | -2.57 | -170 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 67 | 40% (29-52) | +0.45 | -1.26 | -84 |  |
| (2.39, 3.637] | 66 | 48% (37-60) | +0.93 | -0.87 | -57 |  |
| (3.637, 18.762] | 66 | 29% (19-41) | -1.39 | -3.28 | -217 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 67 | 48% (36-60) | +0.53 | -0.22 | -15 |  |
| (0.0971, 0.145] | 66 | 38% (27-50) | +0.22 | -1.03 | -68 |  |
| (0.145, 0.392] | 66 | 32% (22-44) | -0.76 | -4.17 | -275 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.941000000000001, -0.633] | 25 | 20% (9-39) | -2.71 | -3.58 | -89 | ▼ |
| (-0.633, 0.444] | 24 | 46% (28-65) | +0.79 | +0.26 | +6 |  |
| (0.444, 5.305] | 24 | 62% (43-79) | +2.93 | +2.22 | +53 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 27 | 44% (28-63) | +0.12 | -0.55 | -15 |  |
| (0.486, 0.709] | 26 | 42% (26-61) | +0.52 | -0.16 | -4 |  |
| (0.709, 1.74] | 27 | 37% (22-56) | -0.47 | -1.32 | -36 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 27 | 52% (34-69) | +1.21 | +0.74 | +20 |  |
| (0.779, 1.206] | 26 | 35% (19-54) | -0.19 | -1.00 | -26 |  |
| (1.206, 3.566] | 27 | 37% (22-56) | -0.87 | -1.80 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.348] | 27 | 41% (25-59) | +0.07 | -0.51 | -14 |  |
| (0.348, 0.552] | 26 | 42% (26-61) | +0.08 | -0.66 | -17 |  |
| (0.552, 1.21] | 27 | 41% (25-59) | +0.00 | -0.87 | -24 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 99, target 50, time_stop 46, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 67 | 33% | 16% | 48% |
| (0.0971, 0.145] | 66 | 55% | 32% | 11% |
| (0.145, 0.392] | 66 | 62% | 27% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
