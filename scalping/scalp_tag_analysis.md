# Scalp signal analysis (fixed exits)

_176 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 176 | 37% (30-44) | -0.20 | -2.03 | -358 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 63 | -80 | -1.27 | 113 | -278 | -2.46 | +80 |
| skip first 30 min | 43 | -44 | -1.03 | 133 | -314 | -2.36 | +44 |
| skip when SPY is down on the day | 67 | -105 | -1.57 | 109 | -253 | -2.32 | +105 |
| skip when SPY is below its VWAP | 61 | -122 | -1.99 | 115 | -236 | -2.05 | +122 |
| skip when SPY fell over the last 15 min | 54 | -128 | -2.37 | 122 | -230 | -1.88 | +128 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 33 | -143 | -4.33 | 143 | -215 | -1.50 | +143 |
| skip stock not beating SPY over 15 min | 16 | -35 | -2.18 | 160 | -323 | -2.02 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 89 | -249 | -2.80 | 87 | -108 | -1.25 | +249 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 35% (22-50) | -0.06 | -1.03 | -44 |  |
| 15-60 | 18 | 61% (39-80) | +3.00 | +0.19 | +3 | ▲ |
| 60-240 | 56 | 36% (24-49) | -0.40 | -2.03 | -114 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 20 | 40% (22-61) | +0.53 | -1.78 | -36 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 20 | 40% (22-61) | +0.13 | -1.57 | -31 |  |
| -0.2 to 0 | 47 | 43% (30-57) | +0.68 | -1.57 | -74 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 42 | 40% (27-56) | -0.36 | -2.58 | -108 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 61 | 41% (30-54) | +0.19 | -1.99 | -122 |  |
| above VWAP | 115 | 35% (27-44) | -0.41 | -2.05 | -236 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 45 | 38% (25-52) | -0.35 | -2.19 | -98 |  |
| (0.136, 0.37] | 44 | 41% (28-56) | -0.23 | -2.24 | -99 |  |
| (0.37, 1.555] | 44 | 34% (22-49) | -0.15 | -2.65 | -116 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.154] | 45 | 47% (33-61) | +0.60 | -1.04 | -47 |  |
| (0.154, 0.412] | 44 | 34% (22-49) | -0.22 | -2.74 | -120 |  |
| (0.412, 1.192] | 44 | 32% (20-47) | -1.13 | -3.33 | -146 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.106] | 59 | 41% (29-53) | +0.25 | -2.11 | -124 |  |
| (-0.106, 0.374] | 58 | 41% (30-54) | +0.58 | -0.57 | -33 |  |
| (0.374, 2.726] | 59 | 29% (19-41) | -1.41 | -3.40 | -200 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 59 | 39% (28-52) | -0.37 | -1.96 | -116 |  |
| (0.0605, 0.135] | 58 | 41% (30-54) | +0.21 | -1.49 | -86 |  |
| (0.135, 0.786] | 59 | 31% (20-43) | -0.43 | -2.64 | -156 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.224] | 59 | 42% (31-55) | -0.03 | -1.12 | -66 |  |
| (0.224, 0.417] | 58 | 33% (22-46) | -0.54 | -3.21 | -186 |  |
| (0.417, 3.871] | 59 | 36% (25-48) | -0.04 | -1.78 | -105 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 59 | 42% (31-55) | +0.60 | -1.29 | -76 |  |
| (2.623, 4.926] | 58 | 43% (31-56) | +0.36 | -1.75 | -101 |  |
| (4.926, 18.76] | 59 | 25% (16-38) | -1.55 | -3.05 | -180 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0968] | 59 | 44% (32-57) | +0.03 | -0.63 | -37 |  |
| (0.0968, 0.145] | 59 | 34% (23-47) | -0.18 | -1.50 | -88 |  |
| (0.145, 0.392] | 58 | 33% (22-46) | -0.45 | -4.00 | -232 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 55%
- Exit mix: stop 95, target 48, time_stop 33

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0968] | 59 | 41% | 19% | 41% |
| (0.0968, 0.145] | 59 | 59% | 32% | 8% |
| (0.145, 0.392] | 58 | 62% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
