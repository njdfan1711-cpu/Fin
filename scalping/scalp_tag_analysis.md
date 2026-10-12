# Scalp signal analysis (fixed exits)

_132 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 132 | 39% (31-47) | +0.08 | -1.84 | -242 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 42 | -23 | -0.54 | 90 | -220 | -2.44 | +23 |
| skip first 30 min | 32 | -19 | -0.59 | 100 | -223 | -2.23 | +19 |
| skip when SPY is down on the day | 46 | -63 | -1.37 | 86 | -179 | -2.08 | +63 |
| skip when SPY is below its VWAP | 47 | -114 | -2.42 | 85 | -129 | -1.52 | +114 |
| skip when SPY fell over the last 15 min | 41 | -85 | -2.07 | 91 | -158 | -1.73 | +85 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 25 | -90 | -3.59 | 107 | -153 | -1.43 | +90 |
| skip stock not beating SPY over 15 min | 12 | -37 | -3.05 | 120 | -206 | -1.72 | +37 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 68 | -217 | -3.18 | 64 | -26 | -0.40 | +217 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 32 | 38% (23-55) | +0.41 | -0.59 | -19 |  |
| 15-60 | 13 | 54% (29-77) | +1.80 | -0.82 | -11 |  |
| 60-240 | 46 | 37% (25-51) | -0.15 | -1.81 | -83 |  |
| 240-375 | 31 | 32% (19-50) | -1.31 | -4.05 | -126 |  |
| 375-390 | 10 | 50% (24-76) | +2.11 | -0.38 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 42% (19-68) | +0.89 | -0.88 | -11 |  |
| -0.2 to 0 | 34 | 44% (29-61) | +0.94 | -1.55 | -53 |  |
| 0 to 0.2 | 49 | 31% (20-45) | -0.77 | -2.06 | -101 |  |
| > 0.2 | 37 | 43% (29-59) | +0.13 | -2.11 | -78 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 47 | 38% (26-53) | -0.12 | -2.42 | -114 |  |
| above VWAP | 85 | 39% (29-49) | +0.18 | -1.52 | -129 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 34 | 35% (21-52) | -0.83 | -2.46 | -84 |  |
| (0.136, 0.374] | 33 | 48% (33-65) | +0.50 | -1.83 | -60 |  |
| (0.374, 1.123] | 33 | 33% (20-50) | +0.27 | -2.41 | -80 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.181] | 34 | 47% (31-63) | +0.60 | -1.02 | -35 |  |
| (0.181, 0.406] | 33 | 33% (20-50) | -0.45 | -2.93 | -97 |  |
| (0.406, 1.022] | 33 | 36% (22-53) | -0.27 | -2.80 | -92 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.104] | 44 | 41% (28-56) | +0.51 | -2.06 | -91 |  |
| (-0.104, 0.348] | 44 | 39% (26-53) | +0.21 | -1.04 | -46 |  |
| (0.348, 2.726] | 44 | 36% (24-51) | -0.49 | -2.41 | -106 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0567] | 44 | 48% (34-62) | +0.89 | -0.60 | -26 |  |
| (0.0567, 0.14] | 44 | 41% (28-56) | +0.22 | -1.62 | -71 |  |
| (0.14, 0.786] | 44 | 27% (16-42) | -0.89 | -3.29 | -145 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.22] | 44 | 50% (36-64) | +1.10 | +0.01 | +1 |  |
| (0.22, 0.416] | 44 | 34% (22-49) | -0.26 | -3.14 | -138 |  |
| (0.416, 3.871] | 44 | 32% (20-47) | -0.62 | -2.39 | -105 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.541] | 44 | 45% (32-60) | +1.08 | -1.09 | -48 |  |
| (2.541, 5.1] | 44 | 41% (28-56) | -0.03 | -1.92 | -84 |  |
| (5.1, 18.76] | 44 | 30% (18-44) | -0.82 | -2.50 | -110 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0941] | 44 | 50% (36-64) | +0.87 | +0.16 | +7 |  |
| (0.0941, 0.145] | 45 | 38% (25-52) | +0.39 | -0.86 | -39 |  |
| (0.145, 0.392] | 43 | 28% (17-43) | -1.07 | -4.90 | -211 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 28% of trades
- Reached +0.5% at some point: 8% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 67, target 37, time_stop 28

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0941] | 44 | 32% | 20% | 48% |
| (0.0941, 0.145] | 45 | 56% | 36% | 9% |
| (0.145, 0.392] | 43 | 65% | 28% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
