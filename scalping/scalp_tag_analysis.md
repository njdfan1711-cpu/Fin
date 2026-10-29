# Scalp signal analysis (fixed exits)

_185 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 185 | 39% (32-46) | -0.01 | -1.89 | -350 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | -8 | -0.31 | 159 | -342 | -2.15 | +8 |
| skip first 30 min | 1 | -6 | -6.31 | 184 | -344 | -1.87 | +6 |
| skip when SPY is down on the day | 71 | -110 | -1.55 | 114 | -240 | -2.11 | +110 |
| skip when SPY is below its VWAP | 76 | -186 | -2.45 | 109 | -164 | -1.50 | +186 |
| skip when SPY fell over the last 15 min | 68 | -141 | -2.07 | 117 | -210 | -1.79 | +141 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 46 | -153 | -3.33 | 139 | -197 | -1.42 | +153 |
| skip stock not beating SPY over 15 min | 31 | -30 | -0.96 | 154 | -321 | -2.08 | +30 |
| skip afternoon entries (2:00-3:45 PM) | 40 | -215 | -5.37 | 145 | -136 | -0.94 | +215 |
| skip volume spikes above 5x average | 33 | -150 | -4.53 | 152 | -201 | -1.32 | +150 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 178 | -349 | -1.96 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.60%) | 17 | -45 | -2.66 | 168 | -305 | -1.82 | +45 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 102 | -279 | -2.74 | 83 | -71 | -0.86 | +279 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 64% (45-80) | +3.57 | +1.39 | +35 | ▲ |
| 60-240 | 81 | 37% (27-48) | -0.28 | -1.81 | -146 |  |
| 240-375 | 53 | 26% (16-40) | -2.19 | -4.35 | -231 |  |
| 375-390 | 26 | 46% (29-65) | +1.81 | -0.31 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 47 | 43% (30-57) | +0.58 | -1.70 | -80 |  |
| 0 to 0.2 | 56 | 36% (24-49) | -0.09 | -1.53 | -86 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 76 | 37% (27-48) | -0.35 | -2.45 | -186 |  |
| above VWAP | 109 | 40% (32-50) | +0.22 | -1.50 | -164 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 62 | 39% (28-51) | +0.12 | -1.34 | -83 |  |
| (0.133, 0.372] | 61 | 43% (31-55) | -0.08 | -1.95 | -119 |  |
| (0.372, 1.555] | 62 | 35% (25-48) | -0.08 | -2.40 | -149 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.148] | 62 | 44% (32-56) | +0.40 | -1.24 | -77 |  |
| (0.148, 0.412] | 61 | 39% (28-52) | +0.41 | -1.62 | -99 |  |
| (0.412, 1.281] | 61 | 34% (24-47) | -0.76 | -2.76 | -168 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.29] | 62 | 39% (28-51) | +0.09 | -2.12 | -132 |  |
| (-0.29, 0.364] | 61 | 44% (33-57) | +0.98 | -0.28 | -17 |  |
| (0.364, 2.726] | 62 | 34% (23-46) | -1.09 | -3.25 | -201 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 62 | 40% (29-53) | -0.17 | -1.81 | -112 |  |
| (0.0519, 0.12] | 61 | 46% (34-58) | +0.88 | -0.78 | -48 |  |
| (0.12, 0.678] | 62 | 31% (21-43) | -0.74 | -3.07 | -191 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.204] | 62 | 44% (32-56) | +0.07 | -1.17 | -73 |  |
| (0.204, 0.311] | 61 | 39% (28-52) | +0.34 | -1.70 | -104 |  |
| (0.311, 0.875] | 62 | 34% (23-46) | -0.44 | -2.80 | -174 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.392] | 62 | 40% (29-53) | +0.43 | -1.35 | -84 |  |
| (2.392, 3.589] | 61 | 48% (36-60) | +0.98 | -0.91 | -56 |  |
| (3.589, 18.762] | 62 | 29% (19-41) | -1.43 | -3.40 | -211 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 62 | 45% (33-57) | +0.28 | -0.47 | -29 |  |
| (0.0964, 0.145] | 61 | 36% (25-49) | -0.11 | -1.35 | -82 |  |
| (0.145, 0.392] | 62 | 35% (25-48) | -0.21 | -3.86 | -239 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.496] | 20 | 25% (11-47) | -2.06 | -2.97 | -59 |  |
| (-0.496, 0.543] | 19 | 42% (23-64) | +0.27 | -0.25 | -5 |  |
| (0.543, 5.305] | 20 | 60% (39-78) | +2.79 | +2.10 | +42 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.48] | 22 | 36% (20-57) | -0.67 | -1.31 | -29 |  |
| (0.48, 0.684] | 22 | 41% (23-61) | +0.14 | -0.53 | -12 |  |
| (0.684, 1.74] | 22 | 45% (27-65) | +0.63 | -0.28 | -6 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.784] | 22 | 50% (31-69) | +1.01 | +0.56 | +12 |  |
| (0.784, 1.203] | 22 | 32% (16-53) | -0.30 | -1.15 | -25 |  |
| (1.203, 3.566] | 22 | 41% (23-61) | -0.61 | -1.53 | -34 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.332] | 22 | 36% (20-57) | -0.46 | -1.02 | -22 |  |
| (0.332, 0.545] | 22 | 55% (35-73) | +1.76 | +1.04 | +23 |  |
| (0.545, 1.21] | 22 | 32% (16-53) | -1.20 | -2.14 | -47 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 92, target 47, time_stop 43, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 62 | 34% | 16% | 48% |
| (0.0964, 0.145] | 61 | 56% | 30% | 11% |
| (0.145, 0.392] | 62 | 60% | 31% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
