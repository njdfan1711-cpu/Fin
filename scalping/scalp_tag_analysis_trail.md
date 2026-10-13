# Scalp signal analysis (trail exits)

_152 tagged trades, 9 trading days (2026-10-01 to 2026-10-13). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 152 | 34% (27-42) | -0.50 | -2.38 | -362 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 52 | +11 | +0.22 | 100 | -373 | -3.73 | -11 |
| skip first 30 min | 38 | -23 | -0.59 | 114 | -339 | -2.97 | +23 |
| skip when SPY is down on the day | 54 | -138 | -2.55 | 98 | -224 | -2.28 | +138 |
| skip when SPY is below its VWAP | 51 | -144 | -2.82 | 101 | -218 | -2.16 | +144 |
| skip when SPY fell over the last 15 min | 47 | -125 | -2.67 | 105 | -236 | -2.25 | +125 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 29 | -146 | -5.03 | 123 | -216 | -1.75 | +146 |
| skip stock not beating SPY over 15 min | 13 | -43 | -3.34 | 139 | -318 | -2.29 | +43 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 77 | -243 | -3.16 | 75 | -118 | -1.58 | +243 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 38 | 37% (23-53) | +0.43 | -0.59 | -23 |  |
| 15-60 | 15 | 47% (25-70) | +0.34 | -2.13 | -32 |  |
| 60-240 | 48 | 25% (15-39) | -1.53 | -3.16 | -151 |  |
| 240-375 | 37 | 32% (20-49) | -2.62 | -5.13 | -190 |  |
| 375-390 | 14 | 50% (27-73) | +5.16 | +2.43 | +34 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 12 | 33% (14-61) | -0.61 | -2.38 | -29 |  |
| -0.2 to 0 | 42 | 36% (23-51) | -0.18 | -2.60 | -109 |  |
| 0 to 0.2 | 60 | 27% (17-39) | -1.87 | -3.17 | -190 |  |
| > 0.2 | 38 | 45% (30-60) | +1.33 | -0.88 | -34 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 51 | 29% (19-43) | -0.46 | -2.82 | -144 |  |
| above VWAP | 101 | 37% (28-46) | -0.53 | -2.16 | -218 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.158] | 38 | 32% (19-47) | +0.50 | -1.24 | -47 |  |
| (0.158, 0.378] | 38 | 42% (28-58) | -1.31 | -3.50 | -133 |  |
| (0.378, 1.555] | 38 | 26% (15-42) | -1.64 | -4.18 | -159 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.184] | 38 | 39% (26-55) | +0.79 | -0.79 | -30 |  |
| (0.184, 0.422] | 38 | 34% (21-50) | -0.86 | -3.46 | -131 |  |
| (0.422, 1.192] | 38 | 26% (15-42) | -2.37 | -4.68 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0943] | 51 | 33% (22-47) | -1.00 | -3.47 | -177 |  |
| (-0.0943, 0.374] | 50 | 44% (31-58) | +1.02 | -0.15 | -7 |  |
| (0.374, 2.726] | 51 | 25% (16-39) | -1.50 | -3.47 | -177 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.00010000000000000005, 0.0563] | 51 | 41% (29-55) | -1.33 | -2.74 | -140 |  |
| (0.0563, 0.135] | 50 | 36% (24-50) | +0.35 | -1.55 | -77 |  |
| (0.135, 0.786] | 51 | 25% (16-39) | -0.51 | -2.84 | -145 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.23] | 51 | 45% (32-59) | +0.62 | -0.54 | -28 |  |
| (0.23, 0.422] | 50 | 26% (16-40) | -1.96 | -4.68 | -234 |  |
| (0.422, 3.871] | 51 | 31% (20-45) | -0.20 | -1.96 | -100 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 51 | 37% (25-51) | -0.99 | -2.99 | -153 |  |
| (2.623, 5.046] | 50 | 38% (26-52) | +0.39 | -1.64 | -82 |  |
| (5.046, 18.76] | 51 | 27% (17-41) | -0.90 | -2.49 | -127 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0945] | 51 | 43% (31-57) | +0.36 | -0.39 | -20 |  |
| (0.0945, 0.145] | 51 | 37% (25-51) | -1.24 | -2.49 | -127 |  |
| (0.145, 0.392] | 50 | 22% (13-35) | -0.63 | -4.30 | -215 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 3% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 76, trail_stop 55, time_stop 21

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0945] | 51 | 35% | 33% | 31% |
| (0.0945, 0.145] | 51 | 55% | 39% | 6% |
| (0.145, 0.392] | 50 | 60% | 36% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
