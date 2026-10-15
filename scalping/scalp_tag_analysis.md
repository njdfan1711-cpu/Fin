# Scalp signal analysis (fixed exits)

_167 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 167 | 37% (30-45) | -0.17 | -2.01 | -336 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -76 | -1.27 | 107 | -260 | -2.43 | +76 |
| skip first 30 min | 41 | -47 | -1.15 | 126 | -289 | -2.30 | +47 |
| skip when SPY is down on the day | 59 | -90 | -1.52 | 108 | -247 | -2.28 | +90 |
| skip when SPY is below its VWAP | 56 | -112 | -1.99 | 111 | -225 | -2.02 | +112 |
| skip when SPY fell over the last 15 min | 51 | -101 | -1.99 | 116 | -235 | -2.03 | +101 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 32 | -129 | -4.02 | 135 | -208 | -1.54 | +129 |
| skip stock not beating SPY over 15 min | 14 | -23 | -1.63 | 153 | -314 | -2.05 | +23 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 86 | -235 | -2.73 | 81 | -102 | -1.26 | +235 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 34% (22-49) | -0.16 | -1.15 | -47 |  |
| 15-60 | 17 | 65% (41-83) | +3.53 | +1.06 | +18 | ▲ |
| 60-240 | 51 | 35% (24-49) | -0.48 | -2.16 | -110 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 40% (20-64) | +0.07 | -1.43 | -21 |  |
| -0.2 to 0 | 44 | 43% (30-58) | +0.77 | -1.55 | -68 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 41 | 41% (28-57) | -0.24 | -2.50 | -102 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 41% (29-54) | +0.18 | -1.99 | -112 |  |
| above VWAP | 111 | 35% (27-44) | -0.35 | -2.02 | -225 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 42 | 40% (27-56) | +0.02 | -1.92 | -80 |  |
| (0.136, 0.371] | 42 | 38% (25-53) | -0.69 | -2.70 | -113 |  |
| (0.371, 1.555] | 42 | 36% (23-51) | +0.13 | -2.28 | -96 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 42 | 48% (33-62) | +0.66 | -1.02 | -43 |  |
| (0.153, 0.408] | 42 | 36% (23-51) | +0.08 | -2.41 | -101 |  |
| (0.408, 1.192] | 42 | 31% (19-46) | -1.27 | -3.46 | -145 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.101] | 56 | 41% (29-54) | +0.31 | -2.00 | -112 |  |
| (-0.101, 0.374] | 55 | 40% (28-53) | +0.35 | -0.82 | -45 |  |
| (0.374, 2.726] | 56 | 30% (20-43) | -1.18 | -3.21 | -180 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 56 | 41% (29-54) | -0.09 | -1.60 | -89 |  |
| (0.0605, 0.136] | 55 | 42% (30-55) | +0.28 | -1.50 | -82 |  |
| (0.136, 0.786] | 56 | 29% (18-41) | -0.71 | -2.94 | -165 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.224] | 56 | 45% (32-58) | +0.28 | -0.86 | -48 |  |
| (0.224, 0.417] | 55 | 33% (22-46) | -0.52 | -3.13 | -172 |  |
| (0.417, 3.871] | 56 | 34% (23-47) | -0.28 | -2.08 | -116 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 56 | 43% (31-56) | +0.66 | -1.30 | -73 |  |
| (2.623, 4.926] | 55 | 45% (33-58) | +0.71 | -1.31 | -72 |  |
| (4.926, 18.76] | 56 | 23% (14-36) | -1.88 | -3.43 | -192 | ▼ |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0956] | 56 | 46% (34-59) | +0.34 | -0.32 | -18 |  |
| (0.0956, 0.145] | 56 | 34% (23-47) | -0.16 | -1.49 | -84 |  |
| (0.145, 0.392] | 55 | 31% (20-44) | -0.72 | -4.26 | -235 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 89, target 45, time_stop 33

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0956] | 56 | 38% | 20% | 43% |
| (0.0956, 0.145] | 56 | 59% | 32% | 9% |
| (0.145, 0.392] | 55 | 64% | 29% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
