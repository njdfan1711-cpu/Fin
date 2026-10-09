# Scalp signal analysis (trail exits)

_79 tagged trades, 6 trading days (2026-10-01 to 2026-10-08). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 79 | 38% (28-49) | +0.01 | -2.06 | -163 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | +45 | +1.96 | 56 | -208 | -3.71 | -45 |
| skip first 30 min | 17 | +52 | +3.09 | 62 | -215 | -3.47 | -52 |
| skip when SPY is down on the day | 26 | -44 | -1.70 | 53 | -119 | -2.24 | +44 |
| skip when SPY is below its VWAP | 27 | -60 | -2.22 | 52 | -103 | -1.97 | +60 |
| skip when SPY fell over the last 15 min | 20 | -71 | -3.54 | 59 | -92 | -1.56 | +71 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 16 | -65 | -4.04 | 63 | -98 | -1.56 | +65 |
| skip stock not beating SPY over 15 min | 7 | -25 | -3.53 | 72 | -138 | -1.92 | +25 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 45 | -156 | -3.46 | 34 | -7 | -0.20 | +156 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 17 | 53% (31-74) | +4.45 | +3.09 | +52 |  |
| 15-60 | 10 | 50% (24-76) | +0.55 | -2.57 | -26 |  |
| 60-240 | 29 | 24% (12-42) | -1.54 | -3.47 | -101 |  |
| 240-375 | 17 | 35% (17-59) | -2.30 | -4.78 | -81 |  |
| 375-390 | 6 | 50% (19-81) | +0.58 | -1.25 | -8 | few trades |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 22% (6-55) | -1.58 | -3.70 | -33 | few trades |
| -0.2 to 0 | 17 | 41% (22-64) | +1.90 | -0.64 | -11 |  |
| 0 to 0.2 | 30 | 33% (19-51) | -0.71 | -2.47 | -74 |  |
| > 0.2 | 23 | 48% (29-67) | +0.18 | -1.93 | -44 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 27 | 30% (16-48) | +0.18 | -2.22 | -60 |  |
| above VWAP | 52 | 42% (30-56) | -0.08 | -1.97 | -103 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.231, 0.241] | 21 | 43% (24-63) | -1.36 | -3.10 | -65 |  |
| (0.241, 0.381] | 20 | 40% (22-61) | -0.89 | -2.98 | -60 |  |
| (0.381, 1.123] | 21 | 19% (8-40) | -1.35 | -4.31 | -90 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.213] | 21 | 43% (24-63) | +0.62 | -1.07 | -23 |  |
| (0.213, 0.434] | 20 | 25% (11-47) | -2.64 | -5.61 | -112 |  |
| (0.434, 1.022] | 21 | 33% (17-55) | -1.67 | -3.83 | -80 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0828] | 27 | 22% (11-41) | -1.86 | -4.78 | -129 |  |
| (-0.0828, 0.284] | 26 | 46% (29-65) | +0.64 | -1.04 | -27 |  |
| (0.284, 2.633] | 26 | 46% (29-65) | +1.32 | -0.24 | -6 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.011200000000000002, 0.0558] | 27 | 44% (28-63) | -0.56 | -2.37 | -64 |  |
| (0.0558, 0.142] | 26 | 38% (22-57) | -1.42 | -3.34 | -87 |  |
| (0.142, 0.678] | 26 | 31% (17-50) | +2.03 | -0.46 | -12 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.208] | 27 | 48% (31-66) | -0.25 | -1.62 | -44 |  |
| (0.208, 0.414] | 26 | 27% (14-46) | -1.56 | -4.46 | -116 |  |
| (0.414, 3.871] | 26 | 38% (22-57) | +1.85 | -0.11 | -3 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.546] | 27 | 48% (31-66) | +0.61 | -1.84 | -50 |  |
| (2.546, 5.135] | 26 | 27% (14-46) | -2.07 | -4.05 | -105 |  |
| (5.135, 18.76] | 26 | 38% (22-57) | +1.47 | -0.29 | -8 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.101] | 27 | 48% (31-66) | -0.55 | -1.43 | -39 |  |
| (0.101, 0.158] | 26 | 31% (17-50) | -1.34 | -2.78 | -72 |  |
| (0.158, 0.392] | 26 | 35% (19-54) | +1.94 | -1.98 | -52 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.17%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 16% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 36, trail_stop 31, time_stop 12

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.101] | 27 | 33% | 37% | 30% |
| (0.101, 0.158] | 26 | 58% | 35% | 8% |
| (0.158, 0.392] | 26 | 46% | 46% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
