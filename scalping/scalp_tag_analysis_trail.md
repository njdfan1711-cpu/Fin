# Scalp signal analysis (trail exits)

_147 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 147 | 35% (28-43) | -0.34 | -2.23 | -328 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 52 | +11 | +0.22 | 95 | -340 | -3.58 | -11 |
| skip first 30 min | 38 | -23 | -0.59 | 109 | -306 | -2.80 | +23 |
| skip when SPY is down on the day | 53 | -130 | -2.45 | 94 | -198 | -2.11 | +130 |
| skip when SPY is below its VWAP | 51 | -144 | -2.82 | 96 | -184 | -1.92 | +144 |
| skip when SPY fell over the last 15 min | 45 | -114 | -2.53 | 102 | -214 | -2.10 | +114 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 27 | -131 | -4.85 | 120 | -197 | -1.64 | +131 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.34 | 134 | -285 | -2.12 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 74 | -220 | -2.98 | 73 | -108 | -1.48 | +220 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 37% (23-53) | +0.43 | -0.59 | -23 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.13 | -32 |  |
| 60-240 | 47 | 26% (15-40) | -1.50 | -3.14 | -148 |  |
| 240-375 | 33 | 36% (22-53) | -2.22 | -4.85 | -160 |  |
| 375-390 | 14 | 50% (27-73) | +5.16 | +2.43 | +34 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.38 | -29 |  |
| -0.2 to 0 | 41 | 37% (24-52) | -0.04 | -2.47 | -101 |  |
| 0 to 0.2 | 56 | 29% (18-41) | -1.64 | -2.94 | -165 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.88 | -34 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 29% (19-43) | -0.46 | -2.82 | -144 |  |
| above VWAP | 96 | 39% (29-49) | -0.28 | -1.92 | -184 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 37 | 32% (20-49) | +0.67 | -1.11 | -41 |  |
| (0.136, 0.374] | 36 | 44% (30-60) | -1.12 | -3.32 | -120 |  |
| (0.374, 1.555] | 36 | 28% (16-44) | -1.41 | -4.03 | -145 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.166] | 37 | 41% (26-57) | +0.88 | -0.72 | -27 |  |
| (0.166, 0.406] | 36 | 33% (20-50) | -0.77 | -3.33 | -120 |  |
| (0.406, 1.192] | 36 | 31% (18-47) | -1.98 | -4.42 | -159 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.104] | 49 | 33% (21-47) | -1.09 | -3.64 | -178 |  |
| (-0.104, 0.367] | 49 | 45% (32-59) | +1.20 | +0.03 | +1 |  |
| (0.367, 2.726] | 49 | 29% (18-42) | -1.13 | -3.09 | -151 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0567] | 49 | 43% (30-57) | -1.15 | -2.55 | -125 |  |
| (0.0567, 0.137] | 49 | 39% (26-53) | +0.65 | -1.29 | -63 |  |
| (0.137, 0.786] | 49 | 24% (15-38) | -0.53 | -2.85 | -140 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.23] | 49 | 47% (34-61) | +0.82 | -0.33 | -16 |  |
| (0.23, 0.422] | 49 | 27% (16-40) | -1.88 | -4.63 | -227 |  |
| (0.422, 3.871] | 49 | 33% (21-47) | +0.03 | -1.74 | -85 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.577] | 49 | 39% (26-53) | -0.86 | -2.89 | -141 |  |
| (2.577, 5.1] | 49 | 39% (26-53) | +0.54 | -1.50 | -74 |  |
| (5.1, 18.76] | 49 | 29% (18-42) | -0.71 | -2.31 | -113 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0952] | 49 | 45% (32-59) | +0.55 | -0.16 | -8 |  |
| (0.0952, 0.146] | 49 | 39% (26-53) | -1.05 | -2.29 | -112 |  |
| (0.146, 0.392] | 49 | 22% (13-36) | -0.53 | -4.25 | -208 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 46% of trades
- Reached +0.35% at some point: 14% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 72, trail_stop 55, time_stop 20

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0952] | 49 | 35% | 35% | 31% |
| (0.0952, 0.146] | 49 | 53% | 41% | 6% |
| (0.146, 0.392] | 49 | 59% | 37% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
