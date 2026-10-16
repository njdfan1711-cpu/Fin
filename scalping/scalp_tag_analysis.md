# Scalp signal analysis (fixed exits)

_171 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 171 | 37% (30-44) | -0.21 | -2.07 | -354 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | -73 | -1.18 | 109 | -281 | -2.57 | +73 |
| skip first 30 min | 43 | -44 | -1.03 | 128 | -310 | -2.42 | +44 |
| skip when SPY is down on the day | 62 | -101 | -1.64 | 109 | -253 | -2.32 | +101 |
| skip when SPY is below its VWAP | 57 | -126 | -2.21 | 114 | -228 | -2.00 | +126 |
| skip when SPY fell over the last 15 min | 53 | -122 | -2.30 | 118 | -232 | -1.97 | +122 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 32 | -137 | -4.27 | 139 | -217 | -1.56 | +137 |
| skip stock not beating SPY over 15 min | 15 | -29 | -1.92 | 156 | -325 | -2.08 | +29 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 87 | -249 | -2.86 | 84 | -105 | -1.25 | +249 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 35% (22-50) | -0.06 | -1.03 | -44 |  |
| 15-60 | 18 | 61% (39-80) | +3.00 | +0.19 | +3 | ▲ |
| 60-240 | 52 | 35% (23-48) | -0.58 | -2.23 | -116 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 16 | 38% (18-61) | -0.31 | -2.25 | -36 |  |
| -0.2 to 0 | 46 | 43% (30-58) | +0.82 | -1.42 | -66 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 42 | 40% (27-56) | -0.36 | -2.58 | -108 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 57 | 40% (29-53) | +0.07 | -2.21 | -126 |  |
| above VWAP | 114 | 35% (27-44) | -0.36 | -2.00 | -228 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 43 | 40% (26-54) | -0.11 | -2.01 | -86 |  |
| (0.136, 0.372] | 42 | 38% (25-53) | -0.69 | -2.70 | -113 |  |
| (0.372, 1.555] | 43 | 35% (22-50) | -0.01 | -2.56 | -110 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 43 | 47% (33-61) | +0.52 | -1.13 | -49 |  |
| (0.153, 0.41] | 42 | 36% (23-51) | +0.08 | -2.41 | -101 |  |
| (0.41, 1.192] | 43 | 30% (19-45) | -1.38 | -3.72 | -160 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 57 | 40% (29-53) | +0.20 | -2.22 | -126 |  |
| (-0.1, 0.374] | 57 | 40% (29-53) | +0.41 | -0.74 | -42 |  |
| (0.374, 2.726] | 57 | 30% (20-43) | -1.25 | -3.26 | -186 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0593] | 57 | 39% (27-52) | -0.44 | -2.06 | -118 |  |
| (0.0593, 0.136] | 57 | 42% (30-55) | +0.33 | -1.42 | -81 |  |
| (0.136, 0.786] | 57 | 30% (20-43) | -0.53 | -2.73 | -155 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.226] | 57 | 44% (32-57) | +0.17 | -0.95 | -54 |  |
| (0.226, 0.419] | 57 | 33% (22-46) | -0.43 | -3.11 | -177 |  |
| (0.419, 3.871] | 57 | 33% (22-46) | -0.39 | -2.15 | -123 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.624] | 57 | 42% (30-55) | +0.55 | -1.39 | -79 |  |
| (2.624, 5.006] | 57 | 44% (32-57) | +0.47 | -1.71 | -98 |  |
| (5.006, 18.76] | 57 | 25% (15-37) | -1.67 | -3.11 | -177 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0958] | 57 | 46% (33-58) | +0.23 | -0.43 | -25 |  |
| (0.0958, 0.145] | 58 | 34% (24-47) | -0.08 | -1.38 | -80 |  |
| (0.145, 0.392] | 56 | 30% (20-43) | -0.81 | -4.45 | -249 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 92, target 46, time_stop 33

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0958] | 57 | 39% | 19% | 42% |
| (0.0958, 0.145] | 58 | 59% | 33% | 9% |
| (0.145, 0.392] | 56 | 64% | 29% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
