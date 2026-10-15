# Scalp signal analysis (fixed exits)

_168 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 168 | 37% (30-44) | -0.21 | -2.04 | -342 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -76 | -1.27 | 108 | -266 | -2.46 | +76 |
| skip first 30 min | 41 | -47 | -1.15 | 127 | -295 | -2.33 | +47 |
| skip when SPY is down on the day | 59 | -90 | -1.52 | 109 | -253 | -2.32 | +90 |
| skip when SPY is below its VWAP | 56 | -112 | -1.99 | 112 | -231 | -2.06 | +112 |
| skip when SPY fell over the last 15 min | 52 | -107 | -2.06 | 116 | -235 | -2.03 | +107 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 32 | -129 | -4.02 | 136 | -214 | -1.57 | +129 |
| skip stock not beating SPY over 15 min | 15 | -29 | -1.92 | 153 | -314 | -2.05 | +29 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 86 | -235 | -2.73 | 82 | -108 | -1.31 | +235 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 34% (22-49) | -0.16 | -1.15 | -47 |  |
| 15-60 | 17 | 65% (41-83) | +3.53 | +1.06 | +18 | ▲ |
| 60-240 | 52 | 35% (23-48) | -0.58 | -2.23 | -116 |  |
| 240-375 | 39 | 28% (17-44) | -1.91 | -4.30 | -168 |  |
| 375-390 | 19 | 42% (23-64) | +0.87 | -1.54 | -29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 40% (20-64) | +0.07 | -1.43 | -21 |  |
| -0.2 to 0 | 44 | 43% (30-58) | +0.77 | -1.55 | -68 |  |
| 0 to 0.2 | 67 | 30% (20-42) | -0.81 | -2.15 | -144 |  |
| > 0.2 | 42 | 40% (27-56) | -0.36 | -2.58 | -108 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 41% (29-54) | +0.18 | -1.99 | -112 |  |
| above VWAP | 112 | 35% (27-44) | -0.40 | -2.06 | -231 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 43 | 40% (26-54) | -0.11 | -2.01 | -86 |  |
| (0.136, 0.37] | 42 | 38% (25-53) | -0.69 | -2.70 | -113 |  |
| (0.37, 1.555] | 42 | 36% (23-51) | +0.13 | -2.28 | -96 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 43 | 47% (33-61) | +0.52 | -1.13 | -49 |  |
| (0.153, 0.406] | 42 | 36% (23-51) | +0.08 | -2.41 | -101 |  |
| (0.406, 1.192] | 42 | 31% (19-46) | -1.27 | -3.46 | -145 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.1] | 56 | 41% (29-54) | +0.31 | -2.00 | -112 |  |
| (-0.1, 0.377] | 56 | 39% (28-52) | +0.23 | -0.94 | -53 |  |
| (0.377, 2.726] | 56 | 30% (20-43) | -1.17 | -3.17 | -178 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0593] | 56 | 39% (28-52) | -0.34 | -1.84 | -103 |  |
| (0.0593, 0.136] | 56 | 43% (31-56) | +0.43 | -1.33 | -75 |  |
| (0.136, 0.786] | 56 | 29% (18-41) | -0.71 | -2.94 | -165 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.22] | 56 | 45% (32-58) | +0.28 | -0.84 | -47 |  |
| (0.22, 0.416] | 56 | 32% (21-45) | -0.62 | -3.19 | -179 |  |
| (0.416, 3.871] | 56 | 34% (23-47) | -0.28 | -2.08 | -116 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.624] | 56 | 43% (31-56) | +0.66 | -1.30 | -73 |  |
| (2.624, 5.006] | 56 | 45% (32-58) | +0.59 | -1.49 | -83 |  |
| (5.006, 18.76] | 56 | 23% (14-36) | -1.87 | -3.33 | -187 | ▼ |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0958] | 56 | 46% (34-59) | +0.34 | -0.32 | -18 |  |
| (0.0958, 0.145] | 57 | 33% (22-46) | -0.25 | -1.57 | -90 |  |
| (0.145, 0.392] | 55 | 31% (20-44) | -0.72 | -4.26 | -235 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.21%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 90, target 45, time_stop 33

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0958] | 56 | 38% | 20% | 43% |
| (0.0958, 0.145] | 57 | 60% | 32% | 9% |
| (0.145, 0.392] | 55 | 64% | 29% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
