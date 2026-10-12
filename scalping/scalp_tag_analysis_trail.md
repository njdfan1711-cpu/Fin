# Scalp signal analysis (trail exits)

_122 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 122 | 37% (29-46) | +0.07 | -1.84 | -225 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 41 | +65 | +1.58 | 81 | -290 | -3.58 | -65 |
| skip first 30 min | 31 | +16 | +0.52 | 91 | -241 | -2.65 | -16 |
| skip when SPY is down on the day | 39 | -77 | -1.96 | 83 | -148 | -1.79 | +77 |
| skip when SPY is below its VWAP | 40 | -104 | -2.59 | 82 | -121 | -1.48 | +104 |
| skip when SPY fell over the last 15 min | 38 | -72 | -1.89 | 84 | -153 | -1.82 | +72 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 23 | -110 | -4.79 | 99 | -115 | -1.16 | +110 |
| skip stock not beating SPY over 15 min | 12 | -45 | -3.77 | 110 | -180 | -1.63 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 62 | -178 | -2.87 | 60 | -47 | -0.79 | +178 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 31 | 42% (26-59) | +1.52 | +0.52 | +16 |  |
| 15-60 | 13 | 46% (23-71) | +0.08 | -2.54 | -33 |  |
| 60-240 | 43 | 28% (17-43) | -1.11 | -2.82 | -121 |  |
| 240-375 | 25 | 32% (17-52) | -2.64 | -5.42 | -135 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 27% (10-57) | -1.30 | -3.13 | -34 |  |
| -0.2 to 0 | 28 | 39% (24-58) | +0.94 | -1.51 | -42 |  |
| 0 to 0.2 | 47 | 32% (20-46) | -1.22 | -2.54 | -120 |  |
| > 0.2 | 36 | 44% (30-60) | +1.49 | -0.80 | -29 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 40 | 30% (18-45) | -0.33 | -2.59 | -104 |  |
| above VWAP | 82 | 40% (30-51) | +0.26 | -1.48 | -121 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 31 | 32% (19-50) | +0.94 | -0.73 | -23 |  |
| (0.136, 0.374] | 30 | 47% (30-64) | -0.87 | -3.08 | -93 |  |
| (0.374, 1.123] | 30 | 27% (14-44) | -1.40 | -4.20 | -126 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 31 | 39% (24-56) | +1.56 | -0.11 | -3 |  |
| (0.185, 0.405] | 30 | 33% (19-51) | -1.33 | -3.69 | -111 |  |
| (0.405, 1.022] | 30 | 33% (19-51) | -1.58 | -4.24 | -127 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0763] | 41 | 34% (22-49) | -0.91 | -3.31 | -136 |  |
| (-0.0763, 0.356] | 40 | 48% (33-63) | +1.94 | +0.63 | +25 |  |
| (0.356, 2.726] | 41 | 29% (18-44) | -0.78 | -2.80 | -115 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0583] | 41 | 44% (30-59) | -0.80 | -2.34 | -96 |  |
| (0.0583, 0.141] | 40 | 38% (24-53) | +0.70 | -1.18 | -47 |  |
| (0.141, 0.786] | 41 | 29% (18-44) | +0.32 | -2.00 | -82 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.151, 0.217] | 41 | 49% (34-64) | +1.41 | +0.27 | +11 |  |
| (0.217, 0.42] | 40 | 28% (16-43) | -1.43 | -4.23 | -169 |  |
| (0.42, 3.871] | 41 | 34% (22-49) | +0.20 | -1.63 | -67 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.562] | 41 | 41% (28-57) | -0.38 | -2.43 | -99 |  |
| (2.562, 5.291] | 40 | 35% (22-50) | +0.29 | -1.69 | -68 |  |
| (5.291, 18.76] | 41 | 34% (22-49) | +0.30 | -1.41 | -58 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0933] | 41 | 46% (32-61) | +1.14 | +0.48 | +20 |  |
| (0.0933, 0.146] | 40 | 40% (26-55) | -0.73 | -2.02 | -81 |  |
| (0.146, 0.392] | 41 | 24% (14-39) | -0.22 | -4.01 | -164 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.17%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 15% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 56, trail_stop 47, time_stop 19

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0933] | 41 | 29% | 37% | 34% |
| (0.0933, 0.146] | 40 | 50% | 42% | 8% |
| (0.146, 0.392] | 41 | 59% | 37% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
