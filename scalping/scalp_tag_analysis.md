# Scalp signal analysis (fixed exits)

_175 tagged trades, 12 trading days (2026-10-01 to 2026-10-16). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 175 | 37% (30-45) | -0.17 | -2.01 | -351 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | -73 | -1.18 | 113 | -278 | -2.46 | +73 |
| skip first 30 min | 43 | -44 | -1.03 | 132 | -307 | -2.33 | +44 |
| skip when SPY is down on the day | 66 | -99 | -1.50 | 109 | -253 | -2.32 | +99 |
| skip when SPY is below its VWAP | 60 | -115 | -1.92 | 115 | -236 | -2.05 | +115 |
| skip when SPY fell over the last 15 min | 54 | -128 | -2.37 | 121 | -224 | -1.85 | +128 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 33 | -143 | -4.34 | 142 | -208 | -1.47 | +143 |
| skip stock not beating SPY over 15 min | 16 | -35 | -2.18 | 159 | -317 | -1.99 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 89 | -249 | -2.80 | 86 | -102 | -1.19 | +249 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 43 | 35% (22-50) | -0.06 | -1.03 | -44 |  |
| 15-60 | 18 | 61% (39-80) | +3.00 | +0.19 | +3 | ▲ |
| 60-240 | 56 | 36% (24-49) | -0.40 | -2.03 | -114 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 19 | 42% (23-64) | +0.45 | -1.31 | -25 |  |
| -0.2 to 0 | 47 | 43% (30-57) | +0.68 | -1.57 | -74 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 42 | 40% (27-56) | -0.36 | -2.58 | -108 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 60 | 42% (30-54) | +0.29 | -1.92 | -115 |  |
| above VWAP | 115 | 35% (27-44) | -0.41 | -2.05 | -236 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 44 | 39% (26-53) | -0.23 | -2.10 | -92 |  |
| (0.136, 0.369] | 44 | 41% (28-56) | -0.22 | -2.12 | -93 |  |
| (0.369, 1.555] | 44 | 34% (22-49) | -0.15 | -2.76 | -121 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 44 | 45% (32-60) | +0.38 | -1.25 | -55 |  |
| (0.153, 0.408] | 44 | 36% (24-51) | +0.15 | -2.30 | -101 |  |
| (0.408, 1.192] | 44 | 32% (20-47) | -1.14 | -3.44 | -151 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.108] | 59 | 41% (29-53) | +0.25 | -2.11 | -124 |  |
| (-0.108, 0.374] | 58 | 41% (30-54) | +0.58 | -0.57 | -33 |  |
| (0.374, 2.726] | 58 | 29% (19-42) | -1.33 | -3.35 | -194 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0604] | 59 | 39% (28-52) | -0.37 | -1.96 | -116 |  |
| (0.0604, 0.136] | 58 | 43% (31-56) | +0.50 | -1.24 | -72 |  |
| (0.136, 0.786] | 58 | 29% (19-42) | -0.62 | -2.82 | -164 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.228] | 59 | 42% (31-55) | +0.03 | -1.07 | -63 |  |
| (0.228, 0.419] | 58 | 34% (24-47) | -0.32 | -3.00 | -174 |  |
| (0.419, 3.871] | 58 | 34% (24-47) | -0.22 | -1.97 | -114 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 59 | 42% (31-55) | +0.60 | -1.29 | -76 |  |
| (2.623, 4.966] | 58 | 43% (31-56) | +0.36 | -1.83 | -106 |  |
| (4.966, 18.76] | 58 | 26% (16-38) | -1.48 | -2.91 | -169 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0967] | 59 | 44% (32-57) | +0.03 | -0.63 | -37 |  |
| (0.0967, 0.145] | 58 | 34% (24-47) | -0.09 | -1.42 | -82 |  |
| (0.145, 0.392] | 58 | 33% (22-46) | -0.45 | -4.00 | -232 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 94, target 48, time_stop 33

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0967] | 59 | 41% | 19% | 41% |
| (0.0967, 0.145] | 58 | 59% | 33% | 9% |
| (0.145, 0.392] | 58 | 62% | 31% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
