# Scalp signal analysis (trail exits)

_112 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 112 | 38% (30-48) | +0.38 | -1.50 | -168 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | +81 | +2.19 | 75 | -249 | -3.32 | -81 |
| skip first 30 min | 27 | +32 | +1.20 | 85 | -200 | -2.36 | -32 |
| skip when SPY is down on the day | 35 | -57 | -1.62 | 77 | -111 | -1.44 | +57 |
| skip when SPY is below its VWAP | 36 | -84 | -2.33 | 76 | -84 | -1.11 | +84 |
| skip when SPY fell over the last 15 min | 34 | -42 | -1.23 | 78 | -126 | -1.62 | +42 |
| skip over-extended (30-min run in top quarter, > 0.44%) | 21 | -84 | -4.00 | 91 | -84 | -0.92 | +84 |
| skip stock not beating SPY over 15 min | 10 | -36 | -3.59 | 102 | -132 | -1.29 | +36 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 58 | -142 | -2.45 | 54 | -26 | -0.48 | +142 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 44% (28-63) | +2.27 | +1.20 | +32 |  |
| 15-60 | 12 | 50% (25-75) | +0.57 | -2.20 | -26 |  |
| 60-240 | 40 | 28% (16-43) | -1.13 | -2.70 | -108 |  |
| 240-375 | 23 | 35% (19-55) | -2.36 | -4.98 | -115 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 27% (10-57) | -1.30 | -3.13 | -34 |  |
| -0.2 to 0 | 24 | 42% (24-61) | +1.45 | -0.93 | -22 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -1.01 | -2.40 | -103 |  |
| > 0.2 | 34 | 47% (31-63) | +1.92 | -0.23 | -8 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 36 | 31% (18-47) | -0.13 | -2.33 | -84 |  |
| above VWAP | 76 | 42% (32-53) | +0.62 | -1.11 | -84 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 29 | 34% (20-53) | +1.13 | -0.45 | -13 |  |
| (0.136, 0.374] | 29 | 45% (28-62) | -0.94 | -3.21 | -93 |  |
| (0.374, 1.123] | 27 | 30% (16-48) | -0.90 | -3.48 | -94 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 29 | 41% (26-59) | +1.78 | +0.21 | +6 |  |
| (0.185, 0.405] | 28 | 32% (18-51) | -1.26 | -3.75 | -105 |  |
| (0.405, 1.022] | 28 | 36% (21-54) | -1.26 | -3.61 | -101 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.102] | 38 | 34% (21-50) | -0.77 | -3.34 | -127 |  |
| (-0.102, 0.328] | 37 | 43% (29-59) | +1.82 | +0.50 | +18 |  |
| (0.328, 2.633] | 37 | 38% (24-54) | +0.11 | -1.61 | -59 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0604] | 38 | 45% (30-60) | +1.10 | -0.56 | -21 |  |
| (0.0604, 0.142] | 38 | 39% (26-55) | -0.84 | -2.46 | -93 |  |
| (0.142, 0.786] | 36 | 31% (18-47) | +0.90 | -1.48 | -53 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.217] | 38 | 50% (35-65) | +1.73 | +0.53 | +20 |  |
| (0.217, 0.423] | 37 | 27% (15-43) | -1.49 | -4.28 | -158 |  |
| (0.423, 3.871] | 37 | 38% (24-54) | +0.87 | -0.81 | -30 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.545] | 38 | 45% (30-60) | +0.05 | -2.07 | -79 |  |
| (2.545, 4.966] | 37 | 35% (22-51) | +0.61 | -1.32 | -49 |  |
| (4.966, 18.76] | 37 | 35% (22-51) | +0.48 | -1.09 | -40 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 38 | 50% (35-65) | +1.86 | +1.17 | +44 |  |
| (0.0955, 0.145] | 37 | 38% (24-54) | -0.94 | -2.27 | -84 |  |
| (0.145, 0.392] | 37 | 27% (15-43) | +0.17 | -3.47 | -128 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.17%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 16% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 50, trail_stop 44, time_stop 18

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 38 | 26% | 39% | 34% |
| (0.0955, 0.145] | 37 | 51% | 41% | 8% |
| (0.145, 0.392] | 37 | 57% | 38% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
