# Scalp signal analysis (fixed exits)

_190 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 190 | 38% (32-46) | -0.07 | -1.92 | -364 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | -8 | -0.31 | 164 | -356 | -2.17 | +8 |
| skip first 30 min | 1 | -6 | -6.31 | 189 | -358 | -1.89 | +6 |
| skip when SPY is down on the day | 73 | -123 | -1.69 | 117 | -241 | -2.06 | +123 |
| skip when SPY is below its VWAP | 77 | -193 | -2.51 | 113 | -171 | -1.52 | +193 |
| skip when SPY fell over the last 15 min | 70 | -138 | -1.97 | 120 | -227 | -1.89 | +138 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 47 | -160 | -3.40 | 143 | -204 | -1.43 | +160 |
| skip stock not beating SPY over 15 min | 32 | -36 | -1.12 | 158 | -328 | -2.08 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 41 | -221 | -5.40 | 149 | -143 | -0.96 | +221 |
| skip volume spikes above 5x average | 35 | -147 | -4.19 | 155 | -218 | -1.41 | +147 |
| skip when the stop is inside normal noise (range > stop) | 8 | -8 | -0.99 | 182 | -356 | -1.96 | +8 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 18 | -51 | -2.83 | 172 | -314 | -1.82 | +51 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 103 | -286 | -2.78 | 87 | -78 | -0.90 | +286 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 63% (44-78) | +3.45 | +1.40 | +38 | ▲ |
| 60-240 | 83 | 36% (27-47) | -0.38 | -1.89 | -157 |  |
| 240-375 | 54 | 26% (16-39) | -2.25 | -4.40 | -238 |  |
| 375-390 | 26 | 46% (29-65) | +1.81 | -0.31 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 49 | 41% (28-55) | +0.32 | -1.90 | -93 |  |
| 0 to 0.2 | 59 | 36% (25-48) | -0.07 | -1.46 | -86 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 77 | 36% (27-48) | -0.42 | -2.51 | -193 |  |
| above VWAP | 113 | 40% (31-49) | +0.17 | -1.52 | -171 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 64 | 39% (28-51) | +0.08 | -1.36 | -87 |  |
| (0.133, 0.37] | 63 | 41% (30-54) | -0.11 | -1.94 | -122 |  |
| (0.37, 1.555] | 63 | 35% (24-47) | -0.18 | -2.46 | -155 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.139] | 63 | 41% (30-54) | +0.20 | -1.24 | -78 |  |
| (0.139, 0.405] | 63 | 41% (30-54) | +0.61 | -1.48 | -93 |  |
| (0.405, 1.281] | 63 | 33% (23-46) | -0.92 | -2.97 | -187 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.291] | 64 | 39% (28-51) | +0.14 | -2.01 | -129 |  |
| (-0.291, 0.364] | 63 | 44% (33-57) | +0.93 | -0.31 | -19 |  |
| (0.364, 2.726] | 63 | 32% (22-44) | -1.29 | -3.44 | -216 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 64 | 39% (28-51) | -0.35 | -1.96 | -125 |  |
| (0.0521, 0.122] | 63 | 46% (34-58) | +0.93 | -0.71 | -45 |  |
| (0.122, 0.678] | 63 | 30% (20-42) | -0.78 | -3.09 | -194 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 64 | 42% (31-54) | -0.04 | -1.30 | -83 |  |
| (0.207, 0.312] | 63 | 41% (30-54) | +0.57 | -1.45 | -91 |  |
| (0.312, 0.875] | 63 | 32% (22-44) | -0.74 | -3.02 | -190 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 64 | 39% (28-51) | +0.24 | -1.52 | -97 |  |
| (2.39, 3.632] | 63 | 46% (34-58) | +0.81 | -1.06 | -67 |  |
| (3.632, 18.762] | 63 | 30% (20-42) | -1.25 | -3.19 | -201 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 64 | 45% (34-57) | +0.23 | -0.53 | -34 |  |
| (0.0971, 0.145] | 63 | 37% (26-49) | +0.08 | -1.20 | -76 |  |
| (0.145, 0.392] | 63 | 33% (23-46) | -0.52 | -4.04 | -255 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.53] | 22 | 23% (10-43) | -2.28 | -3.17 | -70 |  |
| (-0.53, 0.474] | 21 | 43% (24-63) | +0.43 | -0.08 | -2 |  |
| (0.474, 5.305] | 21 | 57% (37-76) | +2.38 | +1.68 | +35 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 24 | 38% (21-57) | -0.71 | -1.41 | -34 |  |
| (0.486, 0.694] | 24 | 42% (24-61) | +0.58 | -0.12 | -3 |  |
| (0.694, 1.74] | 23 | 39% (22-59) | -0.24 | -1.05 | -24 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 24 | 50% (31-69) | +1.09 | +0.63 | +15 |  |
| (0.779, 1.196] | 23 | 30% (16-51) | -0.56 | -1.37 | -31 |  |
| (1.196, 3.566] | 24 | 38% (21-57) | -0.91 | -1.85 | -44 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.348] | 24 | 38% (21-57) | -0.23 | -0.83 | -20 |  |
| (0.348, 0.552] | 23 | 48% (29-67) | +0.85 | +0.14 | +3 |  |
| (0.552, 1.21] | 24 | 33% (18-53) | -0.94 | -1.84 | -44 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 95, target 48, time_stop 44, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 64 | 34% | 16% | 48% |
| (0.0971, 0.145] | 63 | 56% | 32% | 10% |
| (0.145, 0.392] | 63 | 60% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
