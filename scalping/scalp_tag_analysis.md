# Scalp signal analysis (fixed exits)

_152 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 152 | 37% (30-45) | -0.19 | -2.06 | -313 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 52 | -53 | -1.01 | 100 | -261 | -2.61 | +53 |
| skip first 30 min | 38 | -45 | -1.17 | 114 | -269 | -2.36 | +45 |
| skip when SPY is down on the day | 54 | -84 | -1.55 | 98 | -230 | -2.34 | +84 |
| skip when SPY is below its VWAP | 51 | -106 | -2.08 | 101 | -207 | -2.05 | +106 |
| skip when SPY fell over the last 15 min | 47 | -97 | -2.06 | 105 | -216 | -2.06 | +97 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 29 | -120 | -4.13 | 123 | -194 | -1.57 | +120 |
| skip stock not beating SPY over 15 min | 13 | -32 | -2.43 | 139 | -282 | -2.03 | +32 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 77 | -230 | -2.98 | 75 | -83 | -1.11 | +230 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 34% (21-50) | -0.15 | -1.17 | -45 |  |
| 15-60 | 15 | 60% (36-80) | +2.60 | +0.13 | +2 |  |
| 60-240 | 48 | 35% (23-50) | -0.32 | -1.95 | -94 |  |
| 240-375 | 37 | 27% (15-43) | -2.06 | -4.57 | -169 |  |
| 375-390 | 14 | 50% (27-73) | +2.16 | -0.58 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 42 | 43% (29-58) | +0.68 | -1.74 | -73 |  |
| 0 to 0.2 | 60 | 28% (19-41) | -1.11 | -2.41 | -145 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.23 | -85 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 41% (29-55) | +0.29 | -2.08 | -106 |  |
| above VWAP | 101 | 35% (26-44) | -0.42 | -2.05 | -207 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.158] | 38 | 39% (26-55) | -0.20 | -1.94 | -74 |  |
| (0.158, 0.378] | 38 | 42% (28-58) | -0.28 | -2.47 | -94 |  |
| (0.378, 1.555] | 38 | 32% (19-47) | -0.11 | -2.66 | -101 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.184] | 38 | 50% (35-65) | +1.06 | -0.51 | -19 |  |
| (0.184, 0.422] | 38 | 34% (21-50) | -0.23 | -2.83 | -108 |  |
| (0.422, 1.192] | 38 | 29% (17-45) | -1.42 | -3.73 | -142 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0943] | 51 | 39% (27-53) | +0.31 | -2.16 | -110 |  |
| (-0.0943, 0.374] | 50 | 38% (26-52) | -0.07 | -1.24 | -62 |  |
| (0.374, 2.726] | 51 | 33% (22-47) | -0.80 | -2.77 | -141 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0563] | 51 | 43% (31-57) | +0.19 | -1.22 | -62 |  |
| (0.0563, 0.135] | 50 | 40% (28-54) | +0.20 | -1.69 | -85 |  |
| (0.135, 0.786] | 51 | 27% (17-41) | -0.94 | -3.26 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.23] | 51 | 45% (32-59) | +0.52 | -0.64 | -33 |  |
| (0.23, 0.422] | 50 | 32% (21-46) | -0.71 | -3.44 | -172 |  |
| (0.422, 3.871] | 51 | 33% (22-47) | -0.38 | -2.13 | -109 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 51 | 41% (29-55) | +0.41 | -1.59 | -81 |  |
| (2.623, 5.046] | 50 | 44% (31-58) | +0.55 | -1.49 | -74 |  |
| (5.046, 18.76] | 51 | 25% (16-39) | -1.50 | -3.09 | -158 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0945] | 51 | 45% (32-59) | +0.32 | -0.42 | -22 |  |
| (0.0945, 0.145] | 51 | 35% (24-49) | -0.03 | -1.28 | -65 |  |
| (0.145, 0.392] | 50 | 30% (19-44) | -0.86 | -4.52 | -226 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.21%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 81, target 41, time_stop 30

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0945] | 51 | 37% | 20% | 43% |
| (0.0945, 0.145] | 51 | 59% | 33% | 8% |
| (0.145, 0.392] | 50 | 64% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
