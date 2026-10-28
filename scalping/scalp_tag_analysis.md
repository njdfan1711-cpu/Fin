# Scalp signal analysis (fixed exits)

_173 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 173 | 39% (32-46) | -0.09 | -2.04 | -353 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 148 | -336 | -2.27 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 172 | -347 | -2.02 | +6 |
| skip when SPY is down on the day | 67 | -130 | -1.94 | 106 | -223 | -2.10 | +130 |
| skip when SPY is below its VWAP | 74 | -189 | -2.56 | 99 | -164 | -1.65 | +189 |
| skip when SPY fell over the last 15 min | 67 | -150 | -2.23 | 106 | -203 | -1.92 | +150 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 43 | -164 | -3.82 | 130 | -189 | -1.45 | +164 |
| skip stock not beating SPY over 15 min | 28 | -13 | -0.48 | 145 | -340 | -2.34 | +13 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -195 | -5.26 | 136 | -158 | -1.17 | +195 |
| skip volume spikes above 5x average | 31 | -140 | -4.52 | 142 | -213 | -1.50 | +140 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 166 | -352 | -2.12 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 14 | -24 | -1.75 | 159 | -328 | -2.07 | +24 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 96 | -285 | -2.97 | 77 | -68 | -0.88 | +285 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 64% (45-80) | +3.57 | +1.39 | +35 | ▲ |
| 60-240 | 74 | 36% (26-48) | -0.45 | -2.03 | -150 |  |
| 240-375 | 49 | 27% (16-40) | -2.21 | -4.50 | -220 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 43 | 40% (26-54) | +0.06 | -2.33 | -100 |  |
| 0 to 0.2 | 48 | 38% (25-52) | +0.13 | -1.41 | -68 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 74 | 36% (26-48) | -0.42 | -2.56 | -189 |  |
| above VWAP | 99 | 40% (31-50) | +0.16 | -1.65 | -164 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 58 | 40% (28-53) | +0.20 | -1.32 | -76 |  |
| (0.133, 0.368] | 57 | 42% (30-55) | -0.09 | -1.96 | -112 |  |
| (0.368, 1.555] | 58 | 34% (24-47) | -0.38 | -2.84 | -165 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.148] | 58 | 43% (31-56) | +0.28 | -1.43 | -83 |  |
| (0.148, 0.405] | 57 | 42% (30-55) | +0.80 | -1.24 | -71 |  |
| (0.405, 1.281] | 57 | 32% (21-44) | -1.25 | -3.39 | -193 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.276] | 58 | 36% (25-49) | -0.24 | -2.51 | -146 |  |
| (-0.276, 0.377] | 57 | 46% (33-58) | +0.93 | -0.39 | -22 |  |
| (0.377, 2.726] | 58 | 34% (24-47) | -0.94 | -3.19 | -185 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 58 | 38% (27-51) | -0.60 | -2.29 | -133 |  |
| (0.0519, 0.12] | 57 | 47% (35-60) | +1.02 | -0.58 | -33 |  |
| (0.12, 0.678] | 58 | 31% (21-44) | -0.66 | -3.23 | -187 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.2] | 58 | 43% (31-56) | -0.09 | -1.36 | -79 |  |
| (0.2, 0.3] | 57 | 39% (27-52) | +0.14 | -1.97 | -112 |  |
| (0.3, 0.875] | 58 | 34% (24-47) | -0.32 | -2.79 | -162 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 58 | 36% (25-49) | -0.23 | -2.07 | -120 |  |
| (2.374, 3.475] | 57 | 49% (37-62) | +1.19 | -0.76 | -44 |  |
| (3.475, 18.762] | 58 | 31% (21-44) | -1.20 | -3.26 | -189 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 58 | 45% (33-58) | +0.09 | -0.66 | -38 |  |
| (0.0964, 0.145] | 58 | 36% (25-49) | -0.08 | -1.40 | -81 |  |
| (0.145, 0.392] | 57 | 35% (24-48) | -0.28 | -4.10 | -234 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.719] | 16 | 25% (10-49) | -2.12 | -3.01 | -48 |  |
| (-0.719, 0.423] | 15 | 33% (15-58) | -1.04 | -1.51 | -23 |  |
| (0.423, 5.305] | 16 | 69% (44-86) | +3.50 | +2.89 | +46 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.48] | 18 | 33% (16-56) | -1.49 | -2.12 | -38 |  |
| (0.48, 0.613] | 18 | 39% (20-61) | -0.31 | -0.95 | -17 |  |
| (0.613, 1.74] | 18 | 50% (29-71) | +1.19 | +0.34 | +6 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 18 | 50% (29-71) | +1.17 | +0.78 | +14 |  |
| (0.769, 1.181] | 18 | 39% (20-61) | +0.29 | -0.49 | -9 |  |
| (1.181, 3.566] | 18 | 33% (16-56) | -2.08 | -3.03 | -54 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.316] | 18 | 28% (12-51) | -1.66 | -2.27 | -41 |  |
| (0.316, 0.483] | 18 | 56% (34-75) | +1.44 | +0.87 | +16 |  |
| (0.483, 1.14] | 18 | 39% (20-61) | -0.40 | -1.33 | -24 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 86, time_stop 42, target 42, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 58 | 34% | 14% | 50% |
| (0.0964, 0.145] | 58 | 55% | 29% | 12% |
| (0.145, 0.392] | 57 | 60% | 30% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
