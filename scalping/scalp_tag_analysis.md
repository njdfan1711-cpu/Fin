# Scalp signal analysis (fixed exits)

_174 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 174 | 37% (31-45) | -0.14 | -1.99 | -345 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | -73 | -1.18 | 112 | -272 | -2.43 | +73 |
| skip first 30 min | 43 | -44 | -1.03 | 131 | -301 | -2.30 | +44 |
| skip when SPY is down on the day | 65 | -93 | -1.43 | 109 | -253 | -2.32 | +93 |
| skip when SPY is below its VWAP | 59 | -109 | -1.85 | 115 | -236 | -2.05 | +109 |
| skip when SPY fell over the last 15 min | 53 | -122 | -2.30 | 121 | -224 | -1.85 | +122 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 33 | -143 | -4.34 | 141 | -202 | -1.43 | +143 |
| skip stock not beating SPY over 15 min | 15 | -29 | -1.92 | 159 | -317 | -1.99 | +29 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 89 | -249 | -2.80 | 85 | -96 | -1.13 | +249 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 35% (22-50) | -0.06 | -1.03 | -44 |  |
| 15-60 | 18 | 61% (39-80) | +3.00 | +0.19 | +3 | ▲ |
| 60-240 | 55 | 36% (25-50) | -0.31 | -1.96 | -108 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 18 | 44% (25-66) | +0.78 | -1.05 | -19 |  |
| -0.2 to 0 | 47 | 43% (30-57) | +0.68 | -1.57 | -74 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 42 | 40% (27-56) | -0.36 | -2.58 | -108 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 42% (31-55) | +0.39 | -1.85 | -109 |  |
| above VWAP | 115 | 35% (27-44) | -0.41 | -2.05 | -236 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.139] | 44 | 39% (26-53) | -0.23 | -2.10 | -92 |  |
| (0.139, 0.369] | 43 | 42% (28-57) | -0.10 | -2.03 | -87 |  |
| (0.369, 1.555] | 44 | 34% (22-49) | -0.15 | -2.76 | -121 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.157] | 44 | 48% (34-62) | +0.74 | -0.93 | -41 |  |
| (0.157, 0.41] | 43 | 35% (22-50) | -0.08 | -2.54 | -109 |  |
| (0.41, 1.192] | 44 | 32% (20-47) | -1.14 | -3.44 | -151 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.104] | 58 | 41% (30-54) | +0.35 | -2.04 | -118 |  |
| (-0.104, 0.374] | 58 | 41% (30-54) | +0.58 | -0.57 | -33 |  |
| (0.374, 2.726] | 58 | 29% (19-42) | -1.33 | -3.35 | -194 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 58 | 40% (28-53) | -0.28 | -1.89 | -110 |  |
| (0.0605, 0.136] | 58 | 43% (31-56) | +0.50 | -1.24 | -72 |  |
| (0.136, 0.786] | 58 | 29% (19-42) | -0.62 | -2.82 | -164 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.229] | 58 | 43% (31-56) | +0.12 | -0.99 | -57 |  |
| (0.229, 0.419] | 58 | 34% (24-47) | -0.32 | -3.00 | -174 |  |
| (0.419, 3.871] | 58 | 34% (24-47) | -0.22 | -1.97 | -114 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.624] | 58 | 43% (31-56) | +0.71 | -1.21 | -70 |  |
| (2.624, 5.006] | 58 | 43% (31-56) | +0.36 | -1.83 | -106 |  |
| (5.006, 18.76] | 58 | 26% (16-38) | -1.48 | -2.91 | -169 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 58 | 45% (33-58) | +0.13 | -0.54 | -31 |  |
| (0.0964, 0.146] | 58 | 34% (24-47) | -0.08 | -1.41 | -82 |  |
| (0.146, 0.392] | 58 | 33% (22-46) | -0.45 | -4.00 | -232 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 93, target 48, time_stop 33

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 58 | 40% | 19% | 41% |
| (0.0964, 0.146] | 58 | 59% | 33% | 9% |
| (0.146, 0.392] | 58 | 62% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
