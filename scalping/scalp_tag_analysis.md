# Scalp signal analysis (fixed exits)

_122 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 122 | 39% (31-48) | +0.22 | -1.69 | -206 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 41 | -16 | -0.39 | 81 | -190 | -2.34 | +16 |
| skip first 30 min | 31 | -12 | -0.39 | 91 | -194 | -2.13 | +12 |
| skip when SPY is down on the day | 39 | -37 | -0.96 | 83 | -169 | -2.03 | +37 |
| skip when SPY is below its VWAP | 40 | -88 | -2.19 | 82 | -118 | -1.44 | +88 |
| skip when SPY fell over the last 15 min | 38 | -55 | -1.45 | 84 | -151 | -1.80 | +55 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 23 | -73 | -3.16 | 99 | -133 | -1.35 | +73 |
| skip stock not beating SPY over 15 min | 12 | -37 | -3.05 | 110 | -169 | -1.54 | +37 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 62 | -198 | -3.19 | 60 | -8 | -0.14 | +198 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 31 | 39% (24-56) | +0.61 | -0.39 | -12 |  |
| 15-60 | 13 | 54% (29-77) | +1.80 | -0.82 | -11 |  |
| 60-240 | 43 | 40% (26-54) | +0.24 | -1.47 | -63 |  |
| 240-375 | 25 | 28% (14-48) | -1.86 | -4.64 | -116 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 36% (15-65) | +0.01 | -1.82 | -20 |  |
| -0.2 to 0 | 28 | 50% (33-67) | +1.83 | -0.62 | -17 |  |
| 0 to 0.2 | 47 | 32% (20-46) | -0.56 | -1.88 | -89 |  |
| > 0.2 | 36 | 42% (27-58) | +0.07 | -2.23 | -80 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 40 | 40% (26-55) | +0.08 | -2.19 | -88 |  |
| above VWAP | 82 | 39% (29-50) | +0.30 | -1.44 | -118 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 31 | 39% (24-56) | -0.36 | -2.03 | -63 |  |
| (0.136, 0.374] | 30 | 47% (30-64) | +0.31 | -1.90 | -57 |  |
| (0.374, 1.123] | 30 | 33% (19-51) | +0.34 | -2.47 | -74 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 31 | 48% (32-65) | +0.96 | -0.71 | -22 |  |
| (0.185, 0.405] | 30 | 33% (19-51) | -0.44 | -2.80 | -84 |  |
| (0.405, 1.022] | 30 | 37% (22-54) | -0.27 | -2.93 | -88 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0763] | 41 | 41% (28-57) | +0.65 | -1.75 | -72 |  |
| (-0.0763, 0.356] | 40 | 40% (26-55) | +0.34 | -0.96 | -38 |  |
| (0.356, 2.726] | 41 | 37% (24-52) | -0.32 | -2.33 | -96 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0583] | 41 | 49% (34-64) | +1.18 | -0.36 | -15 |  |
| (0.0583, 0.141] | 40 | 40% (26-55) | +0.01 | -1.86 | -75 |  |
| (0.141, 0.786] | 41 | 29% (18-44) | -0.52 | -2.84 | -116 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.151, 0.217] | 41 | 49% (34-64) | +1.21 | +0.08 | +3 |  |
| (0.217, 0.42] | 40 | 38% (24-53) | +0.08 | -2.72 | -109 |  |
| (0.42, 3.871] | 41 | 32% (20-47) | -0.63 | -2.45 | -101 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.562] | 41 | 46% (32-61) | +1.19 | -0.85 | -35 |  |
| (2.562, 5.291] | 40 | 40% (26-55) | -0.08 | -2.06 | -83 |  |
| (5.291, 18.76] | 41 | 32% (20-47) | -0.44 | -2.16 | -89 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0933] | 41 | 49% (34-64) | +0.76 | +0.11 | +4 |  |
| (0.0933, 0.146] | 40 | 40% (26-55) | +0.75 | -0.53 | -21 |  |
| (0.146, 0.392] | 41 | 29% (18-44) | -0.83 | -4.61 | -189 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 9% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 60, target 35, time_stop 27

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0933] | 41 | 32% | 20% | 49% |
| (0.0933, 0.146] | 40 | 52% | 38% | 10% |
| (0.146, 0.392] | 41 | 63% | 29% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
