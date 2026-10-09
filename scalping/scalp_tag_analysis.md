# Scalp signal analysis (fixed exits)

_79 tagged trades, 6 trading days (2026-10-01 to 2026-10-08). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 79 | 39% (29-50) | +0.22 | -1.85 | -146 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | +9 | +0.38 | 56 | -155 | -2.76 | -9 |
| skip first 30 min | 17 | +6 | +0.35 | 62 | -152 | -2.45 | -6 |
| skip when SPY is down on the day | 26 | -34 | -1.31 | 53 | -112 | -2.11 | +34 |
| skip when SPY is below its VWAP | 27 | -55 | -2.02 | 52 | -91 | -1.76 | +55 |
| skip when SPY fell over the last 15 min | 20 | -12 | -0.60 | 59 | -134 | -2.27 | +12 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 16 | -40 | -2.53 | 63 | -106 | -1.68 | +40 |
| skip stock not beating SPY over 15 min | 7 | -27 | -3.89 | 72 | -119 | -1.65 | +27 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 45 | -144 | -3.20 | 34 | -2 | -0.05 | +144 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 17 | 47% (26-69) | +1.71 | +0.35 | +6 |  |
| 15-60 | 10 | 60% (31-83) | +2.48 | -0.64 | -6 |  |
| 60-240 | 29 | 31% (17-49) | -0.91 | -2.84 | -82 |  |
| 240-375 | 17 | 29% (13-53) | -1.40 | -3.88 | -66 |  |
| 375-390 | 6 | 50% (19-81) | +2.29 | +0.46 | +3 | few trades |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 33% (12-65) | +0.01 | -2.10 | -19 | few trades |
| -0.2 to 0 | 17 | 47% (26-69) | +1.65 | -0.89 | -15 |  |
| 0 to 0.2 | 30 | 33% (19-51) | -0.65 | -2.41 | -72 |  |
| > 0.2 | 23 | 43% (26-63) | +0.38 | -1.72 | -40 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 27 | 37% (22-56) | +0.38 | -2.02 | -55 |  |
| above VWAP | 52 | 40% (28-54) | +0.14 | -1.76 | -91 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.231, 0.241] | 21 | 33% (17-55) | -1.82 | -3.55 | -75 |  |
| (0.241, 0.381] | 20 | 45% (26-66) | +0.59 | -1.50 | -30 |  |
| (0.381, 1.123] | 21 | 33% (17-55) | +0.71 | -2.25 | -47 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.213] | 21 | 52% (32-72) | +1.50 | -0.19 | -4 |  |
| (0.213, 0.434] | 20 | 20% (8-42) | -1.72 | -4.69 | -94 |  |
| (0.434, 1.022] | 21 | 38% (21-59) | -0.42 | -2.57 | -54 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0828] | 27 | 33% (19-52) | -0.27 | -3.19 | -86 |  |
| (-0.0828, 0.284] | 26 | 35% (19-54) | -0.54 | -2.23 | -58 |  |
| (0.284, 2.633] | 26 | 50% (32-68) | +1.50 | -0.07 | -2 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.011200000000000002, 0.0558] | 27 | 52% (34-69) | +1.29 | -0.52 | -14 |  |
| (0.0558, 0.142] | 26 | 27% (14-46) | -1.82 | -3.74 | -97 |  |
| (0.142, 0.678] | 26 | 38% (22-57) | +1.15 | -1.34 | -35 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.208] | 27 | 44% (28-63) | +0.36 | -1.01 | -27 |  |
| (0.208, 0.414] | 26 | 35% (19-54) | -0.18 | -3.08 | -80 |  |
| (0.414, 3.871] | 26 | 38% (22-57) | +0.48 | -1.48 | -39 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.546] | 27 | 52% (34-69) | +2.34 | -0.11 | -3 |  |
| (2.546, 5.135] | 26 | 35% (19-54) | -1.05 | -3.02 | -79 |  |
| (5.135, 18.76] | 26 | 31% (17-50) | -0.71 | -2.48 | -64 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.101] | 27 | 48% (31-66) | +0.57 | -0.32 | -9 |  |
| (0.101, 0.158] | 26 | 31% (17-50) | -0.52 | -1.97 | -51 |  |
| (0.158, 0.392] | 26 | 38% (22-57) | +0.60 | -3.32 | -86 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 9% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 39, target 23, time_stop 17

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.101] | 27 | 37% | 22% | 41% |
| (0.101, 0.158] | 26 | 58% | 27% | 15% |
| (0.158, 0.392] | 26 | 54% | 38% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
