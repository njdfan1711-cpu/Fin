# Scalp signal analysis (fixed exits)

_184 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 184 | 39% (32-46) | -0.07 | -1.95 | -359 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 159 | -342 | -2.15 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 183 | -353 | -1.93 | +6 |
| skip when SPY is down on the day | 71 | -110 | -1.55 | 113 | -249 | -2.21 | +110 |
| skip when SPY is below its VWAP | 76 | -186 | -2.45 | 108 | -173 | -1.60 | +186 |
| skip when SPY fell over the last 15 min | 68 | -141 | -2.07 | 116 | -219 | -1.89 | +141 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 46 | -169 | -3.68 | 138 | -190 | -1.38 | +169 |
| skip stock not beating SPY over 15 min | 31 | -30 | -0.96 | 153 | -330 | -2.16 | +30 |
| skip afternoon entries (2:00-3:45 PM) | 40 | -215 | -5.37 | 144 | -145 | -1.01 | +215 |
| skip volume spikes above 5x average | 33 | -150 | -4.53 | 151 | -210 | -1.39 | +150 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 177 | -358 | -2.02 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.57%) | 16 | -54 | -3.39 | 168 | -305 | -1.82 | +54 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 101 | -288 | -2.86 | 83 | -71 | -0.86 | +288 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 64% (45-80) | +3.57 | +1.39 | +35 | ▲ |
| 60-240 | 81 | 37% (27-48) | -0.28 | -1.81 | -146 |  |
| 240-375 | 53 | 26% (16-40) | -2.19 | -4.35 | -231 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 47 | 43% (30-57) | +0.58 | -1.70 | -80 |  |
| 0 to 0.2 | 55 | 35% (23-48) | -0.28 | -1.72 | -95 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 76 | 37% (27-48) | -0.35 | -2.45 | -186 |  |
| above VWAP | 108 | 40% (31-49) | +0.13 | -1.60 | -173 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 62 | 39% (28-51) | +0.12 | -1.34 | -83 |  |
| (0.132, 0.37] | 61 | 43% (31-55) | -0.08 | -1.95 | -119 |  |
| (0.37, 1.555] | 61 | 34% (24-47) | -0.25 | -2.58 | -158 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 61 | 43% (31-55) | +0.24 | -1.38 | -84 |  |
| (0.147, 0.408] | 61 | 41% (30-54) | +0.68 | -1.32 | -81 |  |
| (0.408, 1.281] | 61 | 33% (22-45) | -1.03 | -3.09 | -189 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.288] | 62 | 39% (28-51) | +0.08 | -2.11 | -131 |  |
| (-0.288, 0.364] | 61 | 44% (33-57) | +0.89 | -0.37 | -23 |  |
| (0.364, 2.726] | 61 | 33% (22-45) | -1.18 | -3.37 | -206 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 62 | 40% (29-53) | -0.17 | -1.81 | -112 |  |
| (0.0518, 0.12] | 61 | 46% (34-58) | +0.88 | -0.78 | -48 |  |
| (0.12, 0.678] | 61 | 30% (20-42) | -0.92 | -3.27 | -200 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.203] | 62 | 44% (32-56) | +0.07 | -1.17 | -73 |  |
| (0.203, 0.307] | 61 | 39% (28-52) | +0.34 | -1.70 | -104 |  |
| (0.307, 0.875] | 61 | 33% (22-45) | -0.62 | -3.00 | -183 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 62 | 40% (29-53) | +0.43 | -1.35 | -84 |  |
| (2.39, 3.502] | 61 | 48% (36-60) | +0.98 | -0.91 | -56 |  |
| (3.502, 18.762] | 61 | 28% (18-40) | -1.62 | -3.61 | -220 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0963] | 62 | 45% (33-57) | +0.28 | -0.47 | -29 |  |
| (0.0963, 0.145] | 61 | 36% (25-49) | -0.11 | -1.37 | -83 |  |
| (0.145, 0.392] | 61 | 34% (24-47) | -0.38 | -4.05 | -247 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.427] | 20 | 25% (11-47) | -2.50 | -3.40 | -68 |  |
| (-0.427, 0.577] | 19 | 42% (23-64) | +0.33 | -0.17 | -3 |  |
| (0.577, 5.305] | 19 | 58% (36-77) | +2.80 | +2.11 | +40 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.476] | 22 | 36% (20-57) | -0.67 | -1.31 | -29 |  |
| (0.476, 0.661] | 21 | 38% (21-59) | -0.33 | -0.95 | -20 |  |
| (0.661, 1.74] | 22 | 45% (27-65) | +0.61 | -0.31 | -7 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 22 | 50% (31-69) | +1.01 | +0.56 | +12 |  |
| (0.779, 1.196] | 21 | 33% (17-55) | -0.05 | -0.88 | -18 |  |
| (1.196, 3.566] | 22 | 36% (20-57) | -1.33 | -2.26 | -50 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.326] | 22 | 36% (20-57) | -0.46 | -1.02 | -22 |  |
| (0.326, 0.54] | 21 | 52% (32-72) | +1.37 | +0.68 | +14 |  |
| (0.54, 1.21] | 22 | 32% (16-53) | -1.22 | -2.17 | -48 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 92, target 46, time_stop 43, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0963] | 62 | 34% | 16% | 48% |
| (0.0963, 0.145] | 61 | 56% | 30% | 11% |
| (0.145, 0.392] | 61 | 61% | 30% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
