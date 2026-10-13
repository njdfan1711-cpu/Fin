# Scalp signal analysis (trail exits)

_136 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 136 | 37% (29-45) | -0.19 | -2.09 | -284 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | +50 | +1.15 | 92 | -334 | -3.63 | -50 |
| skip first 30 min | 32 | +9 | +0.29 | 104 | -293 | -2.82 | -9 |
| skip when SPY is down on the day | 50 | -125 | -2.50 | 86 | -159 | -1.85 | +125 |
| skip when SPY is below its VWAP | 47 | -138 | -2.94 | 89 | -146 | -1.64 | +138 |
| skip when SPY fell over the last 15 min | 41 | -102 | -2.48 | 95 | -182 | -1.92 | +102 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 26 | -124 | -4.78 | 110 | -160 | -1.45 | +124 |
| skip stock not beating SPY over 15 min | 12 | -45 | -3.77 | 124 | -239 | -1.92 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 70 | -213 | -3.04 | 66 | -71 | -1.08 | +213 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 32 | 41% (26-58) | +1.29 | +0.29 | +9 |  |
| 15-60 | 13 | 46% (23-71) | +0.08 | -2.54 | -33 |  |
| 60-240 | 46 | 26% (16-40) | -1.41 | -3.07 | -141 |  |
| 240-375 | 33 | 36% (22-53) | -2.22 | -4.85 | -160 |  |
| 375-390 | 12 | 58% (32-81) | +5.80 | +3.42 | +41 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.38 | -29 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.17 | -2.54 | -96 |  |
| 0 to 0.2 | 49 | 31% (20-45) | -1.40 | -2.70 | -132 |  |
| > 0.2 | 37 | 46% (31-62) | +1.52 | -0.73 | -27 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 47 | 30% (19-44) | -0.64 | -2.94 | -138 |  |
| above VWAP | 89 | 40% (31-51) | +0.04 | -1.64 | -146 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 35 | 31% (19-48) | +0.40 | -1.21 | -42 |  |
| (0.136, 0.374] | 34 | 47% (31-63) | -0.84 | -3.13 | -106 |  |
| (0.374, 1.555] | 35 | 29% (16-45) | -1.51 | -4.13 | -144 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.182] | 35 | 40% (26-56) | +0.91 | -0.70 | -25 |  |
| (0.182, 0.41] | 34 | 35% (21-52) | -0.99 | -3.42 | -116 |  |
| (0.41, 1.192] | 35 | 31% (19-48) | -1.87 | -4.35 | -152 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.108] | 46 | 35% (23-49) | -1.09 | -3.58 | -165 |  |
| (-0.108, 0.364] | 45 | 44% (31-59) | +1.40 | +0.17 | +7 |  |
| (0.364, 2.726] | 45 | 31% (20-46) | -0.87 | -2.82 | -127 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0558] | 46 | 43% (30-58) | -1.01 | -2.47 | -114 |  |
| (0.0558, 0.14] | 45 | 40% (27-55) | +0.68 | -1.14 | -51 |  |
| (0.14, 0.786] | 45 | 27% (16-41) | -0.23 | -2.64 | -119 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.221] | 46 | 48% (34-62) | +0.95 | -0.13 | -6 |  |
| (0.221, 0.419] | 45 | 29% (18-43) | -1.39 | -4.22 | -190 |  |
| (0.419, 3.871] | 45 | 33% (21-48) | -0.17 | -1.96 | -88 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.545] | 46 | 39% (26-54) | -0.71 | -2.82 | -130 |  |
| (2.545, 4.966] | 45 | 40% (27-55) | +0.38 | -1.52 | -69 |  |
| (4.966, 18.76] | 45 | 31% (20-46) | -0.24 | -1.90 | -85 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 46 | 48% (34-62) | +0.96 | +0.24 | +11 |  |
| (0.0946, 0.145] | 46 | 39% (26-54) | -0.95 | -2.19 | -101 |  |
| (0.145, 0.392] | 44 | 23% (13-37) | -0.61 | -4.42 | -194 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 14% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 65, trail_stop 51, time_stop 20

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 46 | 30% | 37% | 33% |
| (0.0946, 0.145] | 46 | 52% | 41% | 7% |
| (0.145, 0.392] | 44 | 61% | 34% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
