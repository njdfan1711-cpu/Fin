# Scalp signal analysis (fixed exits)

_153 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 153 | 37% (30-45) | -0.12 | -1.95 | -298 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 53 | -43 | -0.81 | 100 | -255 | -2.55 | +43 |
| skip first 30 min | 38 | -43 | -1.13 | 115 | -255 | -2.22 | +43 |
| skip when SPY is down on the day | 54 | -81 | -1.50 | 99 | -217 | -2.19 | +81 |
| skip when SPY is below its VWAP | 51 | -103 | -2.02 | 102 | -195 | -1.91 | +103 |
| skip when SPY fell over the last 15 min | 48 | -87 | -1.81 | 105 | -211 | -2.01 | +87 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 29 | -117 | -4.04 | 124 | -181 | -1.46 | +117 |
| skip stock not beating SPY over 15 min | 13 | -31 | -2.37 | 140 | -267 | -1.91 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 78 | -218 | -2.79 | 75 | -80 | -1.07 | +218 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 34% (21-50) | -0.15 | -1.13 | -43 |  |
| 15-60 | 15 | 60% (36-80) | +2.60 | +0.14 | +2 |  |
| 60-240 | 48 | 35% (23-50) | -0.32 | -1.89 | -91 |  |
| 240-375 | 37 | 27% (15-43) | -2.06 | -4.50 | -166 |  |
| 375-390 | 15 | 53% (30-75) | +2.69 | -0.00 | -0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 42 | 43% (29-58) | +0.68 | -1.68 | -71 |  |
| 0 to 0.2 | 61 | 30% (20-42) | -0.93 | -2.20 | -134 |  |
| > 0.2 | 38 | 42% (28-58) | -0.02 | -2.18 | -83 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 41% (29-55) | +0.29 | -2.02 | -103 |  |
| above VWAP | 102 | 35% (27-45) | -0.32 | -1.91 | -195 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.17] | 39 | 38% (25-54) | -0.25 | -1.95 | -76 |  |
| (0.17, 0.374] | 38 | 45% (30-60) | +0.05 | -2.09 | -80 |  |
| (0.374, 1.555] | 38 | 32% (19-47) | -0.11 | -2.63 | -100 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.181] | 39 | 51% (36-66) | +1.30 | -0.27 | -11 |  |
| (0.181, 0.421] | 38 | 34% (21-50) | -0.23 | -2.79 | -106 |  |
| (0.421, 1.192] | 38 | 29% (17-45) | -1.42 | -3.65 | -139 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0885] | 51 | 39% (27-53) | +0.31 | -2.12 | -108 |  |
| (-0.0885, 0.374] | 51 | 39% (27-53) | +0.14 | -1.01 | -51 |  |
| (0.374, 2.726] | 51 | 33% (22-47) | -0.81 | -2.72 | -139 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0567] | 51 | 43% (31-57) | +0.19 | -1.19 | -61 |  |
| (0.0567, 0.137] | 51 | 41% (29-55) | +0.40 | -1.43 | -73 |  |
| (0.137, 0.786] | 51 | 27% (17-41) | -0.94 | -3.23 | -165 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.23] | 51 | 45% (32-59) | +0.52 | -0.60 | -31 |  |
| (0.23, 0.422] | 51 | 33% (22-47) | -0.50 | -3.15 | -161 |  |
| (0.422, 3.871] | 51 | 33% (22-47) | -0.38 | -2.10 | -107 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.613] | 51 | 43% (31-57) | +0.73 | -1.27 | -65 |  |
| (2.613, 5.006] | 51 | 43% (31-57) | +0.42 | -1.54 | -78 |  |
| (5.006, 18.76] | 51 | 25% (16-39) | -1.50 | -3.05 | -155 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0945] | 51 | 45% (32-59) | +0.32 | -0.35 | -18 |  |
| (0.0945, 0.145] | 52 | 37% (25-50) | +0.16 | -1.10 | -57 |  |
| (0.145, 0.392] | 50 | 30% (19-44) | -0.86 | -4.46 | -223 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.21%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 27% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 54%
- Exit mix: stop 81, target 42, time_stop 30

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0945] | 51 | 37% | 20% | 43% |
| (0.0945, 0.145] | 52 | 58% | 35% | 8% |
| (0.145, 0.392] | 50 | 64% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
