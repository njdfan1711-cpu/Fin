# Scalp signal analysis (fixed exits)

_112 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 112 | 40% (32-49) | +0.40 | -1.48 | -166 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | -8 | -0.22 | 75 | -158 | -2.10 | +8 |
| skip first 30 min | 27 | -4 | -0.16 | 85 | -162 | -1.90 | +4 |
| skip when SPY is down on the day | 35 | -26 | -0.74 | 77 | -140 | -1.82 | +26 |
| skip when SPY is below its VWAP | 36 | -76 | -2.12 | 76 | -90 | -1.18 | +76 |
| skip when SPY fell over the last 15 min | 34 | -33 | -0.96 | 78 | -133 | -1.71 | +33 |
| skip over-extended (30-min run in top quarter, > 0.44%) | 21 | -47 | -2.22 | 91 | -119 | -1.31 | +47 |
| skip stock not beating SPY over 15 min | 10 | -35 | -3.52 | 102 | -131 | -1.28 | +35 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 58 | -169 | -2.92 | 54 | +4 | +0.07 | +169 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 41% (25-59) | +0.91 | -0.16 | -4 |  |
| 15-60 | 12 | 58% (32-81) | +2.44 | -0.33 | -4 |  |
| 60-240 | 40 | 38% (24-53) | +0.11 | -1.47 | -59 |  |
| 240-375 | 23 | 30% (16-51) | -1.51 | -4.13 | -95 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 11 | 36% (15-65) | +0.01 | -1.82 | -20 |  |
| -0.2 to 0 | 24 | 50% (31-69) | +2.12 | -0.25 | -6 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -0.48 | -1.88 | -81 |  |
| > 0.2 | 34 | 44% (29-61) | +0.41 | -1.74 | -59 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 36 | 39% (25-55) | +0.08 | -2.12 | -76 |  |
| above VWAP | 76 | 41% (30-52) | +0.55 | -1.18 | -90 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 29 | 38% (23-56) | -0.54 | -2.12 | -61 |  |
| (0.136, 0.374] | 29 | 45% (28-62) | +0.27 | -2.00 | -58 |  |
| (0.374, 1.123] | 27 | 37% (22-56) | +1.03 | -1.55 | -42 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 29 | 48% (31-66) | +0.87 | -0.71 | -20 |  |
| (0.185, 0.405] | 28 | 32% (18-51) | -0.33 | -2.82 | -79 |  |
| (0.405, 1.022] | 28 | 39% (24-58) | +0.14 | -2.21 | -62 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.102] | 38 | 42% (28-58) | +0.89 | -1.68 | -64 |  |
| (-0.102, 0.328] | 37 | 35% (22-51) | -0.20 | -1.53 | -56 |  |
| (0.328, 2.633] | 37 | 43% (29-59) | +0.48 | -1.24 | -46 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0604] | 38 | 50% (35-65) | +1.45 | -0.21 | -8 |  |
| (0.0604, 0.142] | 38 | 37% (23-53) | -0.43 | -2.05 | -78 |  |
| (0.142, 0.786] | 36 | 33% (20-50) | +0.16 | -2.22 | -80 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.217] | 38 | 50% (35-65) | +1.30 | +0.10 | +4 |  |
| (0.217, 0.423] | 37 | 35% (22-51) | -0.09 | -2.87 | -106 |  |
| (0.423, 3.871] | 37 | 35% (22-51) | -0.05 | -1.72 | -64 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.545] | 38 | 50% (35-65) | +1.75 | -0.37 | -14 |  |
| (2.545, 4.966] | 37 | 41% (26-57) | +0.19 | -1.74 | -64 |  |
| (4.966, 18.76] | 37 | 30% (17-46) | -0.79 | -2.36 | -87 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0955] | 38 | 53% (37-68) | +1.43 | +0.74 | +28 |  |
| (0.0955, 0.145] | 37 | 38% (24-54) | +0.44 | -0.89 | -33 |  |
| (0.145, 0.392] | 37 | 30% (17-46) | -0.71 | -4.35 | -161 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 29% of trades
- Reached +0.5% at some point: 10% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 54, target 33, time_stop 25

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0955] | 38 | 29% | 24% | 47% |
| (0.0955, 0.145] | 37 | 54% | 35% | 11% |
| (0.145, 0.392] | 37 | 62% | 30% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
