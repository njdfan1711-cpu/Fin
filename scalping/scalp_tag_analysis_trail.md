# Scalp signal analysis (trail exits)

_105 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 105 | 36% (28-46) | +0.27 | -1.68 | -176 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | +81 | +2.19 | 68 | -257 | -3.78 | -81 |
| skip first 30 min | 27 | +32 | +1.20 | 78 | -209 | -2.68 | -32 |
| skip when SPY is down on the day | 32 | -56 | -1.74 | 73 | -121 | -1.65 | +56 |
| skip when SPY is below its VWAP | 33 | -82 | -2.49 | 72 | -94 | -1.31 | +82 |
| skip when SPY fell over the last 15 min | 29 | -45 | -1.54 | 76 | -132 | -1.73 | +45 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 20 | -90 | -4.48 | 85 | -87 | -1.02 | +90 |
| skip stock not beating SPY over 15 min | 10 | -36 | -3.59 | 95 | -140 | -1.48 | +36 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 56 | -142 | -2.53 | 49 | -35 | -0.71 | +142 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 44% (28-63) | +2.27 | +1.20 | +32 |  |
| 15-60 | 11 | 55% (28-79) | +1.16 | -1.79 | -20 |  |
| 60-240 | 35 | 20% (10-36) | -1.67 | -3.36 | -118 | ▼ |
| 240-375 | 22 | 32% (16-53) | -2.75 | -5.46 | -120 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 22% (6-55) | -1.58 | -3.70 | -33 | few trades |
| -0.2 to 0 | 23 | 39% (22-59) | +1.45 | -0.97 | -22 |  |
| 0 to 0.2 | 41 | 29% (18-44) | -1.20 | -2.63 | -108 |  |
| > 0.2 | 32 | 47% (31-64) | +1.82 | -0.41 | -13 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 33 | 30% (17-47) | -0.16 | -2.49 | -82 |  |
| above VWAP | 72 | 39% (28-50) | +0.47 | -1.31 | -94 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.131] | 26 | 35% (19-54) | +1.23 | -0.13 | -3 |  |
| (0.131, 0.371] | 26 | 38% (22-57) | -1.63 | -4.31 | -112 |  |
| (0.371, 1.123] | 26 | 27% (14-46) | -0.86 | -3.59 | -93 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.193] | 26 | 38% (22-57) | +2.00 | +0.32 | +8 |  |
| (0.193, 0.408] | 26 | 31% (17-50) | -1.58 | -4.20 | -109 |  |
| (0.408, 1.022] | 26 | 31% (17-50) | -1.68 | -4.14 | -108 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0515] | 35 | 29% (16-45) | -1.28 | -4.00 | -140 |  |
| (-0.0515, 0.339] | 35 | 43% (28-59) | +2.03 | +0.68 | +24 |  |
| (0.339, 2.633] | 35 | 37% (23-54) | +0.06 | -1.71 | -60 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0567] | 35 | 43% (28-59) | -0.61 | -2.30 | -81 |  |
| (0.0567, 0.142] | 35 | 34% (21-51) | +0.33 | -1.40 | -49 |  |
| (0.142, 0.786] | 35 | 31% (19-48) | +1.09 | -1.33 | -47 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.218] | 35 | 46% (30-62) | +1.49 | +0.26 | +9 |  |
| (0.218, 0.441] | 35 | 23% (12-39) | -1.93 | -4.96 | -173 |  |
| (0.441, 3.871] | 35 | 40% (26-56) | +1.26 | -0.34 | -12 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.577] | 35 | 43% (28-59) | -0.17 | -2.40 | -84 |  |
| (2.577, 5.213] | 35 | 29% (16-45) | +0.14 | -1.91 | -67 |  |
| (5.213, 18.76] | 35 | 37% (23-54) | +0.85 | -0.72 | -25 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 35 | 46% (30-62) | +1.51 | +0.80 | +28 |  |
| (0.0964, 0.149] | 35 | 34% (21-51) | -1.21 | -2.56 | -90 |  |
| (0.149, 0.392] | 35 | 29% (16-45) | +0.52 | -3.28 | -115 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.18%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 16% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 49, trail_stop 39, time_stop 17

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 35 | 31% | 34% | 34% |
| (0.0964, 0.149] | 35 | 54% | 37% | 9% |
| (0.149, 0.392] | 35 | 54% | 40% | 6% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
