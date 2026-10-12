# Scalp signal analysis (trail exits)

_119 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 119 | 37% (29-46) | +0.09 | -1.78 | -212 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 41 | +65 | +1.58 | 78 | -276 | -3.54 | -65 |
| skip first 30 min | 31 | +16 | +0.52 | 88 | -228 | -2.59 | -16 |
| skip when SPY is down on the day | 36 | -63 | -1.76 | 83 | -148 | -1.79 | +63 |
| skip when SPY is below its VWAP | 37 | -91 | -2.45 | 82 | -121 | -1.48 | +91 |
| skip when SPY fell over the last 15 min | 37 | -69 | -1.87 | 82 | -142 | -1.74 | +69 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 22 | -99 | -4.50 | 97 | -113 | -1.16 | +99 |
| skip stock not beating SPY over 15 min | 11 | -43 | -3.87 | 108 | -169 | -1.57 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 60 | -164 | -2.73 | 59 | -48 | -0.81 | +164 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 31 | 42% (26-59) | +1.52 | +0.52 | +16 |  |
| 15-60 | 13 | 46% (23-71) | +0.08 | -2.54 | -33 |  |
| 60-240 | 40 | 28% (16-43) | -1.13 | -2.70 | -108 |  |
| 240-375 | 25 | 32% (17-52) | -2.64 | -5.42 | -135 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 27% (10-57) | -1.30 | -3.13 | -34 |  |
| -0.2 to 0 | 25 | 40% (23-59) | +1.15 | -1.16 | -29 |  |
| 0 to 0.2 | 47 | 32% (20-46) | -1.22 | -2.54 | -120 |  |
| > 0.2 | 36 | 44% (30-60) | +1.49 | -0.80 | -29 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 37 | 30% (17-46) | -0.28 | -2.45 | -91 |  |
| above VWAP | 82 | 40% (30-51) | +0.26 | -1.48 | -121 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 30 | 33% (19-51) | +0.89 | -0.66 | -20 |  |
| (0.136, 0.374] | 29 | 45% (28-62) | -0.94 | -3.21 | -93 |  |
| (0.374, 1.123] | 29 | 28% (15-46) | -1.24 | -3.96 | -115 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 30 | 40% (25-58) | +1.53 | -0.02 | -1 |  |
| (0.185, 0.405] | 29 | 31% (17-49) | -1.41 | -3.83 | -111 |  |
| (0.405, 1.022] | 29 | 34% (20-53) | -1.42 | -4.00 | -116 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0763] | 40 | 32% (20-48) | -0.95 | -3.40 | -136 |  |
| (-0.0763, 0.34] | 39 | 46% (32-61) | +1.78 | +0.51 | +20 |  |
| (0.34, 2.726] | 40 | 32% (20-48) | -0.52 | -2.38 | -95 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0583] | 40 | 42% (29-58) | -0.85 | -2.41 | -97 |  |
| (0.0583, 0.141] | 39 | 38% (25-54) | +0.65 | -1.14 | -44 |  |
| (0.141, 0.786] | 40 | 30% (18-45) | +0.48 | -1.77 | -71 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.151, 0.214] | 40 | 48% (33-63) | +1.28 | +0.14 | +5 |  |
| (0.214, 0.422] | 39 | 28% (17-44) | -1.40 | -4.24 | -165 |  |
| (0.422, 3.871] | 40 | 35% (22-50) | +0.35 | -1.30 | -52 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.545] | 40 | 42% (29-58) | -0.25 | -2.32 | -93 |  |
| (2.545, 5.291] | 39 | 33% (21-49) | +0.28 | -1.63 | -64 |  |
| (5.291, 18.76] | 40 | 35% (22-50) | +0.25 | -1.38 | -55 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0933] | 40 | 45% (31-60) | +1.14 | +0.48 | +19 |  |
| (0.0933, 0.145] | 40 | 40% (26-55) | -0.73 | -2.02 | -81 |  |
| (0.145, 0.392] | 39 | 26% (15-41) | -0.14 | -3.86 | -150 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.18%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 15% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 55, trail_stop 45, time_stop 19

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0933] | 40 | 30% | 35% | 35% |
| (0.0933, 0.145] | 40 | 50% | 42% | 8% |
| (0.145, 0.392] | 39 | 59% | 36% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
