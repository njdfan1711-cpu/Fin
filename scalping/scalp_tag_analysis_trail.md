# Scalp signal analysis (trail exits)

_148 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 148 | 35% (28-43) | -0.36 | -2.24 | -332 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 52 | +11 | +0.22 | 96 | -343 | -3.58 | -11 |
| skip first 30 min | 38 | -23 | -0.59 | 110 | -309 | -2.81 | +23 |
| skip when SPY is down on the day | 53 | -130 | -2.45 | 95 | -202 | -2.13 | +130 |
| skip when SPY is below its VWAP | 51 | -144 | -2.82 | 97 | -188 | -1.94 | +144 |
| skip when SPY fell over the last 15 min | 46 | -117 | -2.55 | 102 | -214 | -2.10 | +117 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 28 | -138 | -4.91 | 120 | -194 | -1.62 | +138 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.34 | 135 | -288 | -2.14 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 74 | -220 | -2.98 | 74 | -112 | -1.51 | +220 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 37% (23-53) | +0.43 | -0.59 | -23 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.13 | -32 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.16 | -151 |  |
| 240-375 | 33 | 36% (22-53) | -2.22 | -4.85 | -160 |  |
| 375-390 | 14 | 50% (27-73) | +5.16 | +2.43 | +34 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.38 | -29 |  |
| -0.2 to 0 | 41 | 37% (24-52) | -0.04 | -2.47 | -101 |  |
| 0 to 0.2 | 57 | 28% (18-41) | -1.66 | -2.96 | -168 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.88 | -34 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 29% (19-43) | -0.46 | -2.82 | -144 |  |
| above VWAP | 97 | 38% (29-48) | -0.31 | -1.94 | -188 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 37 | 32% (20-49) | +0.67 | -1.11 | -41 |  |
| (0.136, 0.374] | 37 | 43% (29-59) | -1.17 | -3.33 | -123 |  |
| (0.374, 1.555] | 36 | 28% (16-44) | -1.41 | -4.03 | -145 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.171] | 37 | 41% (26-57) | +0.88 | -0.72 | -27 |  |
| (0.171, 0.406] | 36 | 31% (18-47) | -0.91 | -3.46 | -124 |  |
| (0.406, 1.192] | 37 | 32% (20-49) | -1.87 | -4.27 | -158 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.102] | 50 | 34% (22-48) | -0.95 | -3.47 | -174 |  |
| (-0.102, 0.364] | 49 | 43% (30-57) | +1.02 | -0.14 | -7 |  |
| (0.364, 2.726] | 49 | 29% (18-42) | -1.13 | -3.09 | -151 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0572] | 50 | 42% (29-56) | -1.24 | -2.64 | -132 |  |
| (0.0572, 0.136] | 49 | 39% (26-53) | +0.71 | -1.22 | -60 |  |
| (0.136, 0.786] | 49 | 24% (15-38) | -0.53 | -2.85 | -140 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.229] | 50 | 46% (33-60) | +0.75 | -0.39 | -20 |  |
| (0.229, 0.421] | 49 | 27% (16-40) | -1.88 | -4.63 | -227 |  |
| (0.421, 3.871] | 49 | 33% (21-47) | +0.03 | -1.74 | -85 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.593] | 50 | 38% (26-52) | -0.89 | -2.92 | -146 |  |
| (2.593, 5.086] | 49 | 39% (26-53) | +0.53 | -1.48 | -73 |  |
| (5.086, 18.76] | 49 | 29% (18-42) | -0.71 | -2.31 | -113 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 50 | 44% (31-58) | +0.48 | -0.23 | -12 |  |
| (0.0946, 0.145] | 49 | 39% (26-53) | -1.05 | -2.29 | -112 |  |
| (0.145, 0.392] | 49 | 22% (13-36) | -0.53 | -4.25 | -208 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 14% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 72, trail_stop 55, time_stop 21

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 50 | 34% | 34% | 32% |
| (0.0946, 0.145] | 49 | 53% | 41% | 6% |
| (0.145, 0.392] | 49 | 59% | 37% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
