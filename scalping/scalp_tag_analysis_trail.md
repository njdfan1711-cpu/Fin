# Scalp signal analysis (trail exits)

_132 tagged trades, 8 trading days (2026-10-01 to 2026-10-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 132 | 36% (29-45) | -0.13 | -2.04 | -270 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 42 | +58 | +1.38 | 90 | -328 | -3.64 | -58 |
| skip first 30 min | 32 | +9 | +0.29 | 100 | -279 | -2.79 | -9 |
| skip when SPY is down on the day | 46 | -111 | -2.41 | 86 | -159 | -1.85 | +111 |
| skip when SPY is below its VWAP | 47 | -138 | -2.94 | 85 | -132 | -1.55 | +138 |
| skip when SPY fell over the last 15 min | 41 | -102 | -2.48 | 91 | -168 | -1.85 | +102 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 25 | -123 | -4.91 | 107 | -147 | -1.37 | +123 |
| skip stock not beating SPY over 15 min | 12 | -45 | -3.77 | 120 | -225 | -1.87 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 68 | -205 | -3.02 | 64 | -65 | -1.01 | +205 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 32 | 41% (26-58) | +1.29 | +0.29 | +9 |  |
| 15-60 | 13 | 46% (23-71) | +0.08 | -2.54 | -33 |  |
| 60-240 | 46 | 26% (16-40) | -1.41 | -3.07 | -141 |  |
| 240-375 | 31 | 35% (21-53) | -2.21 | -4.95 | -153 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.38 | -29 |  |
| -0.2 to 0 | 34 | 35% (21-52) | +0.07 | -2.42 | -82 |  |
| 0 to 0.2 | 49 | 31% (20-45) | -1.40 | -2.70 | -132 |  |
| > 0.2 | 37 | 46% (31-62) | +1.52 | -0.73 | -27 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 47 | 30% (19-44) | -0.64 | -2.94 | -138 |  |
| above VWAP | 85 | 40% (30-51) | +0.15 | -1.55 | -132 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 34 | 29% (17-46) | +0.35 | -1.27 | -43 |  |
| (0.136, 0.374] | 33 | 48% (33-65) | -0.69 | -3.02 | -100 |  |
| (0.374, 1.123] | 33 | 27% (15-44) | -1.46 | -4.13 | -136 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.181] | 34 | 38% (24-55) | +0.88 | -0.75 | -25 |  |
| (0.181, 0.406] | 33 | 36% (22-53) | -0.84 | -3.32 | -109 |  |
| (0.406, 1.022] | 33 | 30% (17-47) | -1.85 | -4.37 | -144 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.104] | 44 | 34% (22-49) | -1.03 | -3.59 | -158 |  |
| (-0.104, 0.348] | 44 | 45% (32-60) | +1.56 | +0.31 | +14 |  |
| (0.348, 2.726] | 44 | 30% (18-44) | -0.93 | -2.85 | -125 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0567] | 44 | 43% (30-58) | -0.95 | -2.44 | -107 |  |
| (0.0567, 0.14] | 44 | 39% (26-53) | +0.66 | -1.19 | -52 |  |
| (0.14, 0.786] | 44 | 27% (16-42) | -0.10 | -2.51 | -110 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.22] | 44 | 50% (36-64) | +1.27 | +0.17 | +8 |  |
| (0.22, 0.416] | 44 | 25% (15-39) | -1.79 | -4.67 | -205 |  |
| (0.416, 3.871] | 44 | 34% (22-49) | +0.13 | -1.64 | -72 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.541] | 44 | 41% (28-56) | -0.47 | -2.64 | -116 |  |
| (2.541, 5.1] | 44 | 36% (24-51) | +0.20 | -1.69 | -74 |  |
| (5.1, 18.76] | 44 | 32% (20-47) | -0.12 | -1.81 | -80 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0941] | 44 | 48% (34-62) | +1.11 | +0.41 | +18 |  |
| (0.0941, 0.145] | 45 | 38% (25-52) | -1.01 | -2.26 | -102 |  |
| (0.145, 0.392] | 43 | 23% (13-38) | -0.49 | -4.32 | -186 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 14% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 63, trail_stop 49, time_stop 20

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0941] | 44 | 30% | 36% | 34% |
| (0.0941, 0.145] | 45 | 53% | 40% | 7% |
| (0.145, 0.392] | 43 | 60% | 35% | 5% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
