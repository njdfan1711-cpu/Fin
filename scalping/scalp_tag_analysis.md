# Scalp signal analysis (fixed exits)

_200 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 200 | 37% (31-44) | -0.11 | -2.00 | -400 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 79 | -101 | -1.28 | 121 | -299 | -2.47 | +101 |
| skip first 30 min | 59 | -77 | -1.30 | 141 | -324 | -2.29 | +77 |
| skip when SPY is down on the day | 73 | -123 | -1.68 | 127 | -278 | -2.19 | +123 |
| skip when SPY is below its VWAP | 66 | -134 | -2.03 | 134 | -266 | -1.99 | +134 |
| skip when SPY fell over the last 15 min | 57 | -139 | -2.44 | 143 | -261 | -1.83 | +139 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 35 | -149 | -4.25 | 165 | -252 | -1.52 | +149 |
| skip stock not beating SPY over 15 min | 18 | -37 | -2.08 | 182 | -363 | -1.99 | +37 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -316 | -2.85 | 89 | -84 | -0.94 | +316 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 58 | 34% (24-47) | -0.04 | -1.21 | -70 |  |
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 61 | 36% (25-49) | -0.32 | -2.11 | -129 |  |
| 240-375 | 40 | 28% (16-43) | -2.00 | -4.42 | -177 |  |
| 375-390 | 21 | 43% (24-63) | +1.01 | -1.46 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.48 | -1.76 | -90 |  |
| 0 to 0.2 | 82 | 32% (23-42) | -0.46 | -1.92 | -157 |  |
| > 0.2 | 45 | 40% (27-55) | -0.38 | -2.68 | -120 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 66 | 41% (30-53) | +0.23 | -2.03 | -134 |  |
| above VWAP | 134 | 35% (28-43) | -0.28 | -1.99 | -266 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 48 | 38% (25-52) | -0.36 | -2.27 | -109 |  |
| (0.136, 0.374] | 48 | 44% (31-58) | +0.16 | -1.87 | -90 |  |
| (0.374, 1.555] | 46 | 33% (21-47) | -0.24 | -2.85 | -131 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 47 | 45% (31-59) | +0.32 | -1.49 | -70 |  |
| (0.153, 0.408] | 47 | 38% (26-53) | +0.46 | -1.90 | -89 |  |
| (0.408, 1.192] | 47 | 32% (20-46) | -1.09 | -3.49 | -164 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.108] | 67 | 40% (29-52) | +0.25 | -1.96 | -131 |  |
| (-0.108, 0.374] | 66 | 41% (30-53) | +0.63 | -0.74 | -49 |  |
| (0.374, 2.726] | 67 | 30% (20-42) | -1.20 | -3.28 | -220 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 67 | 39% (28-51) | -0.20 | -1.89 | -126 |  |
| (0.0605, 0.136] | 66 | 41% (30-53) | +0.21 | -1.58 | -104 |  |
| (0.136, 0.786] | 67 | 31% (22-43) | -0.35 | -2.53 | -170 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.23] | 67 | 40% (29-52) | -0.20 | -1.49 | -100 |  |
| (0.23, 0.436] | 66 | 36% (26-48) | -0.01 | -2.67 | -176 |  |
| (0.436, 4.92] | 67 | 34% (24-46) | -0.13 | -1.85 | -124 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.625] | 67 | 42% (31-54) | +0.55 | -1.38 | -92 |  |
| (2.625, 4.926] | 66 | 42% (31-54) | +0.40 | -1.88 | -124 |  |
| (4.926, 18.76] | 67 | 27% (18-39) | -1.28 | -2.74 | -184 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0987] | 67 | 42% (31-54) | -0.11 | -0.84 | -57 |  |
| (0.0987, 0.163] | 66 | 32% (22-44) | -0.51 | -1.91 | -126 |  |
| (0.163, 0.395] | 67 | 37% (27-49) | +0.27 | -3.25 | -218 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 56%
- Exit mix: stop 108, target 57, time_stop 35

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0987] | 67 | 42% | 19% | 39% |
| (0.0987, 0.163] | 66 | 61% | 29% | 11% |
| (0.163, 0.395] | 67 | 60% | 37% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
