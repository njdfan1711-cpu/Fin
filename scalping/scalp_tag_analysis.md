# Scalp signal analysis (fixed exits)

_119 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 119 | 39% (30-48) | +0.18 | -1.69 | -201 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 41 | -16 | -0.39 | 78 | -185 | -2.38 | +16 |
| skip first 30 min | 31 | -12 | -0.39 | 88 | -189 | -2.15 | +12 |
| skip when SPY is down on the day | 36 | -33 | -0.91 | 83 | -169 | -2.03 | +33 |
| skip when SPY is below its VWAP | 37 | -83 | -2.25 | 82 | -118 | -1.44 | +83 |
| skip when SPY fell over the last 15 min | 37 | -60 | -1.63 | 82 | -141 | -1.72 | +60 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 22 | -61 | -2.79 | 97 | -140 | -1.44 | +61 |
| skip stock not beating SPY over 15 min | 11 | -42 | -3.81 | 108 | -159 | -1.48 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 60 | -192 | -3.19 | 59 | -10 | -0.16 | +192 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 31 | 39% (24-56) | +0.61 | -0.39 | -12 |  |
| 15-60 | 13 | 54% (29-77) | +1.80 | -0.82 | -11 |  |
| 60-240 | 40 | 38% (24-53) | +0.11 | -1.47 | -59 |  |
| 240-375 | 25 | 28% (14-48) | -1.86 | -4.64 | -116 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 36% (15-65) | +0.01 | -1.82 | -20 |  |
| -0.2 to 0 | 25 | 48% (30-67) | +1.80 | -0.51 | -13 |  |
| 0 to 0.2 | 47 | 32% (20-46) | -0.56 | -1.88 | -89 |  |
| > 0.2 | 36 | 42% (27-58) | +0.07 | -2.23 | -80 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 37 | 38% (24-54) | -0.08 | -2.25 | -83 |  |
| above VWAP | 82 | 39% (29-50) | +0.30 | -1.44 | -118 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 30 | 37% (22-54) | -0.72 | -2.27 | -68 |  |
| (0.136, 0.374] | 29 | 45% (28-62) | +0.27 | -2.00 | -58 |  |
| (0.374, 1.123] | 29 | 34% (20-53) | +0.56 | -2.17 | -63 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 30 | 47% (30-64) | +0.64 | -0.91 | -27 |  |
| (0.185, 0.405] | 29 | 31% (17-49) | -0.51 | -2.93 | -85 |  |
| (0.405, 1.022] | 29 | 38% (23-56) | -0.07 | -2.65 | -77 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0763] | 40 | 40% (26-55) | +0.62 | -1.83 | -73 |  |
| (-0.0763, 0.34] | 39 | 38% (25-54) | +0.08 | -1.20 | -47 |  |
| (0.34, 2.726] | 40 | 38% (24-53) | -0.17 | -2.04 | -82 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0583] | 40 | 48% (33-63) | +1.16 | -0.40 | -16 |  |
| (0.0583, 0.141] | 39 | 38% (25-54) | -0.26 | -2.05 | -80 |  |
| (0.141, 0.786] | 40 | 30% (18-45) | -0.38 | -2.63 | -105 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.151, 0.214] | 40 | 48% (33-63) | +0.98 | -0.16 | -7 |  |
| (0.214, 0.422] | 39 | 36% (23-52) | +0.04 | -2.80 | -109 |  |
| (0.422, 3.871] | 40 | 32% (20-48) | -0.49 | -2.14 | -86 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.545] | 40 | 48% (33-63) | +1.37 | -0.71 | -28 |  |
| (2.545, 5.291] | 39 | 38% (25-54) | -0.12 | -2.03 | -79 |  |
| (5.291, 18.76] | 40 | 30% (18-45) | -0.72 | -2.35 | -94 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0933] | 40 | 48% (33-63) | +0.74 | +0.08 | +3 |  |
| (0.0933, 0.145] | 40 | 40% (26-55) | +0.75 | -0.53 | -21 |  |
| (0.145, 0.392] | 39 | 28% (17-44) | -0.98 | -4.70 | -183 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 9% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 59, target 34, time_stop 26

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0933] | 40 | 32% | 20% | 48% |
| (0.0933, 0.145] | 40 | 52% | 38% | 10% |
| (0.145, 0.392] | 39 | 64% | 28% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
