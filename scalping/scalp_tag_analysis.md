# Scalp signal analysis (fixed exits)

_202 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 202 | 37% (30-43) | -0.15 | -2.03 | -410 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 79 | -101 | -1.28 | 123 | -309 | -2.51 | +101 |
| skip first 30 min | 59 | -77 | -1.30 | 143 | -333 | -2.33 | +77 |
| skip when SPY is down on the day | 73 | -123 | -1.68 | 129 | -287 | -2.23 | +123 |
| skip when SPY is below its VWAP | 67 | -137 | -2.05 | 135 | -273 | -2.02 | +137 |
| skip when SPY fell over the last 15 min | 57 | -139 | -2.44 | 145 | -271 | -1.87 | +139 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 36 | -155 | -4.32 | 166 | -255 | -1.54 | +155 |
| skip stock not beating SPY over 15 min | 19 | -41 | -2.14 | 183 | -370 | -2.02 | +41 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 112 | -323 | -2.88 | 90 | -87 | -0.97 | +323 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 58 | 34% (24-47) | -0.04 | -1.21 | -70 |  |
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 62 | 35% (25-48) | -0.36 | -2.13 | -132 |  |
| 240-375 | 41 | 27% (16-42) | -2.08 | -4.47 | -183 |  |
| 375-390 | 21 | 43% (24-63) | +1.01 | -1.46 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.48 | -1.76 | -90 |  |
| 0 to 0.2 | 82 | 32% (23-42) | -0.46 | -1.92 | -157 |  |
| > 0.2 | 47 | 38% (26-53) | -0.53 | -2.77 | -130 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 67 | 40% (29-52) | +0.19 | -2.05 | -137 |  |
| above VWAP | 135 | 35% (27-43) | -0.32 | -2.02 | -273 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.135] | 48 | 38% (25-52) | -0.29 | -2.04 | -98 |  |
| (0.135, 0.371] | 48 | 40% (27-54) | -0.36 | -2.52 | -121 |  |
| (0.371, 1.555] | 48 | 35% (23-50) | +0.05 | -2.52 | -121 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.152] | 48 | 42% (29-56) | -0.07 | -1.88 | -90 |  |
| (0.152, 0.406] | 47 | 40% (28-55) | +0.81 | -1.54 | -72 |  |
| (0.406, 1.192] | 48 | 31% (20-45) | -1.19 | -3.57 | -171 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 68 | 40% (29-52) | +0.20 | -1.98 | -134 |  |
| (-0.108, 0.374] | 67 | 40% (29-52) | +0.53 | -0.85 | -57 |  |
| (0.374, 2.726] | 67 | 30% (20-42) | -1.20 | -3.27 | -219 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0572] | 68 | 37% (26-49) | -0.44 | -2.12 | -144 |  |
| (0.0572, 0.136] | 67 | 42% (31-54) | +0.34 | -1.44 | -97 |  |
| (0.136, 0.786] | 67 | 31% (22-43) | -0.35 | -2.53 | -170 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.229] | 68 | 38% (28-50) | -0.47 | -1.74 | -118 |  |
| (0.229, 0.436] | 67 | 37% (27-49) | +0.15 | -2.51 | -168 |  |
| (0.436, 4.92] | 67 | 34% (24-46) | -0.13 | -1.85 | -124 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 68 | 41% (30-53) | +0.51 | -1.38 | -94 |  |
| (2.623, 4.845] | 67 | 42% (31-54) | +0.30 | -1.98 | -133 |  |
| (4.845, 18.76] | 67 | 27% (18-39) | -1.28 | -2.74 | -184 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 68 | 40% (29-52) | -0.37 | -1.12 | -76 |  |
| (0.0985, 0.162] | 67 | 33% (23-45) | -0.35 | -1.74 | -117 |  |
| (0.162, 0.395] | 67 | 37% (27-49) | +0.27 | -3.25 | -218 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 56%
- Exit mix: stop 109, target 57, time_stop 36

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 68 | 43% | 18% | 40% |
| (0.0985, 0.162] | 67 | 60% | 30% | 10% |
| (0.162, 0.395] | 67 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
