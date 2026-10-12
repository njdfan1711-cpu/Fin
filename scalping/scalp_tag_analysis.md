# Scalp signal analysis (fixed exits)

_121 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 121 | 39% (31-48) | +0.14 | -1.75 | -211 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 41 | -16 | -0.39 | 80 | -195 | -2.44 | +16 |
| skip first 30 min | 31 | -12 | -0.39 | 90 | -199 | -2.21 | +12 |
| skip when SPY is down on the day | 38 | -43 | -1.12 | 83 | -169 | -2.03 | +43 |
| skip when SPY is below its VWAP | 39 | -93 | -2.39 | 82 | -118 | -1.44 | +93 |
| skip when SPY fell over the last 15 min | 37 | -60 | -1.63 | 84 | -151 | -1.80 | +60 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 23 | -73 | -3.16 | 98 | -139 | -1.42 | +73 |
| skip stock not beating SPY over 15 min | 11 | -42 | -3.81 | 110 | -169 | -1.54 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 61 | -203 | -3.33 | 60 | -8 | -0.14 | +203 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 31 | 39% (24-56) | +0.61 | -0.39 | -12 |  |
| 15-60 | 13 | 54% (29-77) | +1.80 | -0.82 | -11 |  |
| 60-240 | 42 | 38% (25-53) | -0.00 | -1.63 | -69 |  |
| 240-375 | 25 | 28% (14-48) | -1.86 | -4.64 | -116 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 36% (15-65) | +0.01 | -1.82 | -20 |  |
| -0.2 to 0 | 27 | 48% (31-66) | +1.51 | -0.84 | -23 |  |
| 0 to 0.2 | 47 | 32% (20-46) | -0.56 | -1.88 | -89 |  |
| > 0.2 | 36 | 42% (27-58) | +0.07 | -2.23 | -80 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 39 | 38% (25-54) | -0.19 | -2.39 | -93 |  |
| above VWAP | 82 | 39% (29-50) | +0.30 | -1.44 | -118 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 30 | 37% (22-54) | -0.72 | -2.27 | -68 |  |
| (0.136, 0.374] | 30 | 47% (30-64) | +0.31 | -1.90 | -57 |  |
| (0.374, 1.123] | 30 | 33% (19-51) | +0.34 | -2.47 | -74 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.193] | 30 | 47% (30-64) | +0.64 | -0.91 | -27 |  |
| (0.193, 0.405] | 30 | 33% (19-51) | -0.44 | -2.80 | -84 |  |
| (0.405, 1.022] | 30 | 37% (22-54) | -0.27 | -2.93 | -88 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0828] | 41 | 41% (28-57) | +0.65 | -1.75 | -72 |  |
| (-0.0828, 0.34] | 40 | 40% (26-55) | +0.34 | -0.96 | -38 |  |
| (0.34, 2.726] | 40 | 35% (22-50) | -0.59 | -2.52 | -101 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0572] | 41 | 49% (34-64) | +1.18 | -0.36 | -15 |  |
| (0.0572, 0.141] | 40 | 38% (24-53) | -0.37 | -2.15 | -86 |  |
| (0.141, 0.786] | 40 | 30% (18-45) | -0.41 | -2.76 | -110 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.151, 0.217] | 41 | 49% (34-64) | +1.21 | +0.08 | +3 |  |
| (0.217, 0.421] | 40 | 35% (22-50) | -0.33 | -3.22 | -129 |  |
| (0.421, 3.871] | 40 | 32% (20-48) | -0.49 | -2.14 | -86 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.546] | 41 | 46% (32-61) | +1.19 | -0.85 | -35 |  |
| (2.546, 5.135] | 40 | 40% (26-55) | -0.08 | -2.06 | -83 |  |
| (5.135, 18.76] | 40 | 30% (18-45) | -0.72 | -2.35 | -94 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0927] | 41 | 49% (34-64) | +0.76 | +0.11 | +4 |  |
| (0.0927, 0.145] | 40 | 40% (26-55) | +0.75 | -0.53 | -21 |  |
| (0.145, 0.392] | 40 | 28% (16-43) | -1.11 | -4.86 | -194 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 9% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 60, target 34, time_stop 27

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0927] | 41 | 32% | 20% | 49% |
| (0.0927, 0.145] | 40 | 52% | 38% | 10% |
| (0.145, 0.392] | 40 | 65% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
