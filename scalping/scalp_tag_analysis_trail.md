# Scalp signal analysis (trail exits)

_121 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 121 | 37% (29-46) | +0.05 | -1.84 | -222 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 41 | +65 | +1.58 | 80 | -287 | -3.59 | -65 |
| skip first 30 min | 31 | +16 | +0.52 | 90 | -238 | -2.65 | -16 |
| skip when SPY is down on the day | 38 | -74 | -1.95 | 83 | -148 | -1.79 | +74 |
| skip when SPY is below its VWAP | 39 | -101 | -2.59 | 82 | -121 | -1.48 | +101 |
| skip when SPY fell over the last 15 min | 37 | -69 | -1.87 | 84 | -153 | -1.82 | +69 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 23 | -110 | -4.79 | 98 | -112 | -1.15 | +110 |
| skip stock not beating SPY over 15 min | 11 | -43 | -3.87 | 110 | -180 | -1.63 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 61 | -175 | -2.87 | 60 | -47 | -0.79 | +175 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 31 | 42% (26-59) | +1.52 | +0.52 | +16 |  |
| 15-60 | 13 | 46% (23-71) | +0.08 | -2.54 | -33 |  |
| 60-240 | 42 | 29% (17-44) | -1.19 | -2.82 | -119 |  |
| 240-375 | 25 | 32% (17-52) | -2.64 | -5.42 | -135 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 27% (10-57) | -1.30 | -3.13 | -34 |  |
| -0.2 to 0 | 27 | 41% (25-59) | +0.88 | -1.47 | -40 |  |
| 0 to 0.2 | 47 | 32% (20-46) | -1.22 | -2.54 | -120 |  |
| > 0.2 | 36 | 44% (30-60) | +1.49 | -0.80 | -29 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 39 | 31% (19-46) | -0.40 | -2.59 | -101 |  |
| above VWAP | 82 | 40% (30-51) | +0.26 | -1.48 | -121 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 30 | 33% (19-51) | +0.89 | -0.66 | -20 |  |
| (0.136, 0.374] | 30 | 47% (30-64) | -0.87 | -3.08 | -93 |  |
| (0.374, 1.123] | 30 | 27% (14-44) | -1.40 | -4.20 | -126 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.193] | 30 | 40% (25-58) | +1.53 | -0.02 | -1 |  |
| (0.193, 0.405] | 30 | 33% (19-51) | -1.33 | -3.69 | -111 |  |
| (0.405, 1.022] | 30 | 33% (19-51) | -1.58 | -4.24 | -127 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0828] | 41 | 34% (22-49) | -0.91 | -3.31 | -136 |  |
| (-0.0828, 0.34] | 40 | 48% (33-63) | +1.94 | +0.63 | +25 |  |
| (0.34, 2.726] | 40 | 30% (18-45) | -0.86 | -2.80 | -112 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0572] | 41 | 44% (30-59) | -0.80 | -2.34 | -96 |  |
| (0.0572, 0.141] | 40 | 38% (24-53) | +0.51 | -1.26 | -51 |  |
| (0.141, 0.786] | 40 | 30% (18-45) | +0.45 | -1.90 | -76 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.151, 0.217] | 41 | 49% (34-64) | +1.41 | +0.27 | +11 |  |
| (0.217, 0.421] | 40 | 28% (16-43) | -1.65 | -4.54 | -182 |  |
| (0.421, 3.871] | 40 | 35% (22-50) | +0.35 | -1.30 | -52 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.546] | 41 | 41% (28-57) | -0.38 | -2.43 | -99 |  |
| (2.546, 5.135] | 40 | 35% (22-50) | +0.29 | -1.69 | -68 |  |
| (5.135, 18.76] | 40 | 35% (22-50) | +0.25 | -1.38 | -55 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0927] | 41 | 46% (32-61) | +1.14 | +0.48 | +20 |  |
| (0.0927, 0.145] | 40 | 40% (26-55) | -0.73 | -2.02 | -81 |  |
| (0.145, 0.392] | 40 | 25% (14-40) | -0.29 | -4.04 | -162 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.18%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 15% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 56, trail_stop 46, time_stop 19

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0927] | 41 | 29% | 37% | 34% |
| (0.0927, 0.145] | 40 | 50% | 42% | 8% |
| (0.145, 0.392] | 40 | 60% | 35% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
