# Scalp signal analysis (trail exits)

_129 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 129 | 36% (29-45) | -0.09 | -1.95 | -251 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 42 | +58 | +1.38 | 87 | -309 | -3.55 | -58 |
| skip first 30 min | 32 | +9 | +0.29 | 97 | -260 | -2.68 | -9 |
| skip when SPY is down on the day | 43 | -92 | -2.14 | 86 | -159 | -1.85 | +92 |
| skip when SPY is below its VWAP | 44 | -119 | -2.71 | 85 | -132 | -1.55 | +119 |
| skip when SPY fell over the last 15 min | 39 | -79 | -2.04 | 90 | -172 | -1.91 | +79 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 24 | -126 | -5.26 | 105 | -125 | -1.19 | +126 |
| skip stock not beating SPY over 15 min | 12 | -45 | -3.77 | 117 | -206 | -1.76 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 65 | -186 | -2.87 | 64 | -65 | -1.01 | +186 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 32 | 41% (26-58) | +1.29 | +0.29 | +9 |  |
| 15-60 | 13 | 46% (23-71) | +0.08 | -2.54 | -33 |  |
| 60-240 | 46 | 26% (16-40) | -1.41 | -3.07 | -141 |  |
| 240-375 | 28 | 36% (21-54) | -2.23 | -4.81 | -135 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.38 | -29 |  |
| -0.2 to 0 | 31 | 35% (21-53) | +0.28 | -2.05 | -63 |  |
| 0 to 0.2 | 49 | 31% (20-45) | -1.40 | -2.70 | -132 |  |
| > 0.2 | 37 | 46% (31-62) | +1.52 | -0.73 | -27 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 44 | 30% (18-44) | -0.54 | -2.71 | -119 |  |
| above VWAP | 85 | 40% (30-51) | +0.15 | -1.55 | -132 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 33 | 30% (17-47) | +0.54 | -1.09 | -36 |  |
| (0.136, 0.374] | 32 | 50% (34-66) | -0.52 | -2.65 | -85 |  |
| (0.374, 1.123] | 32 | 25% (13-42) | -1.68 | -4.37 | -140 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 33 | 39% (25-56) | +1.36 | -0.27 | -9 |  |
| (0.185, 0.406] | 32 | 38% (23-55) | -0.96 | -3.24 | -104 |  |
| (0.406, 1.022] | 32 | 28% (16-45) | -2.08 | -4.62 | -148 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0885] | 43 | 35% (22-50) | -0.85 | -3.21 | -138 |  |
| (-0.0885, 0.364] | 43 | 44% (30-59) | +1.41 | +0.15 | +6 |  |
| (0.364, 2.726] | 43 | 30% (19-45) | -0.82 | -2.77 | -119 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0546] | 43 | 42% (28-57) | -1.11 | -2.62 | -113 |  |
| (0.0546, 0.14] | 43 | 40% (26-54) | +0.81 | -1.00 | -43 |  |
| (0.14, 0.786] | 43 | 28% (17-43) | +0.03 | -2.22 | -95 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.218] | 43 | 49% (35-63) | +1.27 | +0.17 | +7 |  |
| (0.218, 0.419] | 43 | 28% (17-43) | -1.45 | -4.13 | -178 |  |
| (0.419, 3.871] | 43 | 33% (20-47) | -0.09 | -1.87 | -80 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.546] | 43 | 42% (28-57) | -0.34 | -2.34 | -101 |  |
| (2.546, 5.131] | 43 | 35% (22-50) | +0.06 | -1.84 | -79 |  |
| (5.131, 18.76] | 43 | 33% (20-47) | +0.01 | -1.66 | -71 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0951] | 43 | 49% (35-63) | +1.17 | +0.51 | +22 |  |
| (0.0951, 0.145] | 44 | 36% (24-51) | -1.06 | -2.32 | -102 |  |
| (0.145, 0.392] | 42 | 24% (13-39) | -0.36 | -4.07 | -171 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.18%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 15% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 61, trail_stop 48, time_stop 20

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0951] | 43 | 28% | 37% | 35% |
| (0.0951, 0.145] | 44 | 55% | 39% | 7% |
| (0.145, 0.392] | 42 | 60% | 36% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
