# Scalp signal analysis (trail exits)

_104 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 104 | 37% (28-46) | +0.29 | -1.68 | -174 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | +81 | +2.19 | 67 | -255 | -3.81 | -81 |
| skip first 30 min | 27 | +32 | +1.20 | 77 | -207 | -2.69 | -32 |
| skip when SPY is down on the day | 32 | -56 | -1.74 | 72 | -119 | -1.65 | +56 |
| skip when SPY is below its VWAP | 33 | -82 | -2.49 | 71 | -92 | -1.30 | +82 |
| skip when SPY fell over the last 15 min | 29 | -45 | -1.54 | 75 | -130 | -1.73 | +45 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 19 | -87 | -4.55 | 85 | -88 | -1.03 | +87 |
| skip stock not beating SPY over 15 min | 10 | -36 | -3.59 | 94 | -139 | -1.47 | +36 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 56 | -142 | -2.53 | 48 | -33 | -0.68 | +142 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 44% (28-63) | +2.27 | +1.20 | +32 |  |
| 15-60 | 11 | 55% (28-79) | +1.16 | -1.79 | -20 |  |
| 60-240 | 34 | 21% (10-37) | -1.67 | -3.40 | -116 |  |
| 240-375 | 22 | 32% (16-53) | -2.75 | -5.46 | -120 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 22% (6-55) | -1.58 | -3.70 | -33 | few trades |
| -0.2 to 0 | 23 | 39% (22-59) | +1.45 | -0.97 | -22 |  |
| 0 to 0.2 | 40 | 30% (18-45) | -1.18 | -2.64 | -106 |  |
| > 0.2 | 32 | 47% (31-64) | +1.82 | -0.41 | -13 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 33 | 30% (17-47) | -0.16 | -2.49 | -82 |  |
| above VWAP | 71 | 39% (29-51) | +0.50 | -1.30 | -92 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 26 | 35% (19-54) | +1.07 | -0.63 | -16 |  |
| (0.136, 0.372] | 25 | 40% (23-59) | -1.45 | -3.88 | -97 |  |
| (0.372, 1.123] | 26 | 27% (14-46) | -0.86 | -3.59 | -93 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.189] | 26 | 38% (22-57) | +2.00 | +0.32 | +8 |  |
| (0.189, 0.41] | 25 | 32% (17-52) | -1.57 | -4.29 | -107 |  |
| (0.41, 1.022] | 26 | 31% (17-50) | -1.68 | -4.14 | -108 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-2.266, -0.0575] | 35 | 29% (16-45) | -1.28 | -4.00 | -140 |  |
| (-0.0575, 0.34] | 34 | 44% (29-61) | +2.15 | +0.75 | +26 |  |
| (0.34, 2.633] | 35 | 37% (23-54) | +0.06 | -1.71 | -60 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0563] | 35 | 43% (28-59) | -0.61 | -2.30 | -81 |  |
| (0.0563, 0.142] | 34 | 35% (21-52) | +0.40 | -1.38 | -47 |  |
| (0.142, 0.786] | 35 | 31% (19-48) | +1.09 | -1.33 | -47 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.215] | 35 | 46% (30-62) | +1.49 | +0.26 | +9 |  |
| (0.215, 0.441] | 34 | 24% (12-40) | -1.93 | -5.04 | -172 |  |
| (0.441, 3.871] | 35 | 40% (26-56) | +1.26 | -0.34 | -12 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.562] | 35 | 43% (28-59) | -0.17 | -2.40 | -84 |  |
| (2.562, 5.133] | 34 | 29% (17-46) | +0.31 | -1.77 | -60 |  |
| (5.133, 18.76] | 35 | 37% (23-54) | +0.73 | -0.86 | -30 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0973] | 35 | 46% (30-62) | +1.40 | +0.69 | +24 |  |
| (0.0973, 0.151] | 34 | 35% (21-52) | -1.08 | -2.45 | -83 |  |
| (0.151, 0.392] | 35 | 29% (16-45) | +0.52 | -3.28 | -115 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.18%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 16% of trades
- Reached +0.5% at some point: 7% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 49, trail_stop 39, time_stop 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0973] | 35 | 34% | 34% | 31% |
| (0.0973, 0.151] | 34 | 53% | 38% | 9% |
| (0.151, 0.392] | 35 | 54% | 40% | 6% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
