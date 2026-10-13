# Scalp signal analysis (fixed exits)

_136 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 136 | 38% (30-47) | +0.02 | -1.88 | -255 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -22 | -0.50 | 92 | -233 | -2.54 | +22 |
| skip first 30 min | 32 | -19 | -0.59 | 104 | -236 | -2.27 | +19 |
| skip when SPY is down on the day | 50 | -76 | -1.52 | 86 | -179 | -2.08 | +76 |
| skip when SPY is below its VWAP | 47 | -114 | -2.42 | 89 | -142 | -1.59 | +114 |
| skip when SPY fell over the last 15 min | 41 | -85 | -2.07 | 95 | -170 | -1.79 | +85 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 26 | -98 | -3.77 | 110 | -157 | -1.43 | +98 |
| skip stock not beating SPY over 15 min | 12 | -37 | -3.05 | 124 | -219 | -1.76 | +37 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 70 | -216 | -3.08 | 66 | -39 | -0.60 | +216 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 32 | 38% (23-55) | +0.41 | -0.59 | -19 |  |
| 15-60 | 13 | 54% (29-77) | +1.80 | -0.82 | -11 |  |
| 60-240 | 46 | 37% (25-51) | -0.15 | -1.81 | -83 |  |
| 240-375 | 33 | 30% (17-47) | -1.60 | -4.22 | -139 |  |
| 375-390 | 12 | 50% (25-75) | +2.13 | -0.25 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 38 | 42% (28-58) | +0.65 | -1.72 | -65 |  |
| 0 to 0.2 | 49 | 31% (20-45) | -0.77 | -2.06 | -101 |  |
| > 0.2 | 37 | 43% (29-59) | +0.13 | -2.11 | -78 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 47 | 38% (26-53) | -0.12 | -2.42 | -114 |  |
| above VWAP | 89 | 38% (29-49) | +0.09 | -1.59 | -142 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 35 | 37% (23-54) | -0.51 | -2.13 | -74 |  |
| (0.136, 0.374] | 34 | 47% (31-63) | +0.31 | -1.98 | -67 |  |
| (0.374, 1.555] | 35 | 31% (19-48) | -0.08 | -2.70 | -95 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.182] | 35 | 49% (33-64) | +0.88 | -0.73 | -25 |  |
| (0.182, 0.41] | 34 | 32% (19-49) | -0.61 | -3.04 | -103 |  |
| (0.41, 1.192] | 35 | 34% (21-51) | -0.59 | -3.07 | -107 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.108] | 46 | 39% (26-54) | +0.22 | -2.26 | -104 |  |
| (-0.108, 0.364] | 45 | 38% (25-52) | +0.08 | -1.15 | -52 |  |
| (0.364, 2.726] | 45 | 38% (25-52) | -0.26 | -2.21 | -99 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0558] | 46 | 46% (32-60) | +0.59 | -0.86 | -40 |  |
| (0.0558, 0.14] | 45 | 42% (29-57) | +0.45 | -1.38 | -62 |  |
| (0.14, 0.786] | 45 | 27% (16-41) | -1.00 | -3.41 | -153 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.221] | 46 | 48% (34-62) | +0.80 | -0.28 | -13 |  |
| (0.221, 0.419] | 45 | 36% (23-50) | -0.03 | -2.86 | -129 |  |
| (0.419, 3.871] | 45 | 31% (20-46) | -0.73 | -2.52 | -113 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.545] | 46 | 43% (30-58) | +0.77 | -1.34 | -62 |  |
| (2.545, 4.966] | 45 | 42% (29-57) | +0.18 | -1.72 | -77 |  |
| (4.966, 18.76] | 45 | 29% (18-43) | -0.92 | -2.58 | -116 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 46 | 50% (36-64) | +0.92 | +0.20 | +9 |  |
| (0.0946, 0.145] | 46 | 37% (25-51) | +0.25 | -0.99 | -46 |  |
| (0.145, 0.392] | 44 | 27% (16-42) | -1.17 | -4.98 | -219 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 8% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 70, target 38, time_stop 28

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 46 | 33% | 22% | 46% |
| (0.0946, 0.145] | 46 | 57% | 35% | 9% |
| (0.145, 0.392] | 44 | 66% | 27% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
