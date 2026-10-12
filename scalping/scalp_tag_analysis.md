# Scalp signal analysis (fixed exits)

_129 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 129 | 39% (31-47) | +0.09 | -1.77 | -228 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 42 | -23 | -0.54 | 87 | -206 | -2.36 | +23 |
| skip first 30 min | 32 | -19 | -0.59 | 97 | -209 | -2.16 | +19 |
| skip when SPY is down on the day | 43 | -49 | -1.14 | 86 | -179 | -2.08 | +49 |
| skip when SPY is below its VWAP | 44 | -100 | -2.26 | 85 | -129 | -1.52 | +100 |
| skip when SPY fell over the last 15 min | 39 | -62 | -1.60 | 90 | -166 | -1.84 | +62 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 24 | -98 | -4.08 | 105 | -131 | -1.24 | +98 |
| skip stock not beating SPY over 15 min | 12 | -37 | -3.05 | 117 | -192 | -1.64 | +37 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 65 | -202 | -3.12 | 64 | -26 | -0.40 | +202 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 32 | 38% (23-55) | +0.41 | -0.59 | -19 |  |
| 15-60 | 13 | 54% (29-77) | +1.80 | -0.82 | -11 |  |
| 60-240 | 46 | 37% (25-51) | -0.15 | -1.81 | -83 |  |
| 240-375 | 28 | 32% (18-51) | -1.40 | -3.98 | -112 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 31 | 45% (29-62) | +1.08 | -1.24 | -39 |  |
| 0 to 0.2 | 49 | 31% (20-45) | -0.77 | -2.06 | -101 |  |
| > 0.2 | 37 | 43% (29-59) | +0.13 | -2.11 | -78 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 44 | 39% (26-53) | -0.10 | -2.26 | -100 |  |
| above VWAP | 85 | 39% (29-49) | +0.18 | -1.52 | -129 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 33 | 36% (22-53) | -0.68 | -2.31 | -76 |  |
| (0.136, 0.374] | 32 | 50% (34-66) | +0.70 | -1.42 | -45 |  |
| (0.374, 1.123] | 32 | 31% (18-49) | -0.05 | -2.74 | -88 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.185] | 33 | 48% (33-65) | +0.80 | -0.83 | -27 |  |
| (0.185, 0.406] | 32 | 34% (20-52) | -0.27 | -2.55 | -82 |  |
| (0.406, 1.022] | 32 | 34% (20-52) | -0.60 | -3.14 | -100 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0885] | 43 | 42% (28-57) | +0.71 | -1.65 | -71 |  |
| (-0.0885, 0.364] | 43 | 37% (24-52) | -0.07 | -1.33 | -57 |  |
| (0.364, 2.726] | 43 | 37% (24-52) | -0.37 | -2.33 | -100 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0546] | 43 | 47% (33-61) | +0.68 | -0.83 | -36 |  |
| (0.0546, 0.14] | 43 | 42% (28-57) | +0.35 | -1.46 | -63 |  |
| (0.14, 0.786] | 43 | 28% (17-43) | -0.77 | -3.02 | -130 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.218] | 43 | 49% (35-63) | +1.09 | -0.02 | -1 |  |
| (0.218, 0.419] | 43 | 37% (24-52) | +0.05 | -2.64 | -113 |  |
| (0.419, 3.871] | 43 | 30% (19-45) | -0.87 | -2.66 | -114 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.546] | 43 | 47% (33-61) | +1.24 | -0.76 | -33 |  |
| (2.546, 5.131] | 43 | 40% (26-54) | -0.28 | -2.18 | -94 |  |
| (5.131, 18.76] | 43 | 30% (19-45) | -0.70 | -2.37 | -102 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0951] | 43 | 51% (37-65) | +1.02 | +0.36 | +15 |  |
| (0.0951, 0.145] | 44 | 36% (24-51) | +0.17 | -1.09 | -48 |  |
| (0.145, 0.392] | 42 | 29% (17-44) | -0.95 | -4.66 | -196 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 9% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 65, target 36, time_stop 28

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0951] | 43 | 30% | 21% | 49% |
| (0.0951, 0.145] | 44 | 57% | 34% | 9% |
| (0.145, 0.392] | 42 | 64% | 29% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
