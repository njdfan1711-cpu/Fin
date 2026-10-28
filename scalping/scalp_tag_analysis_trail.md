# Scalp signal analysis (trail exits)

_184 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 184 | 36% (30-44) | -0.87 | -2.76 | -507 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 159 | -519 | -3.26 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 183 | -501 | -2.74 | +6 |
| skip when SPY is down on the day | 71 | -247 | -3.48 | 113 | -260 | -2.30 | +247 |
| skip when SPY is below its VWAP | 76 | -294 | -3.87 | 108 | -213 | -1.98 | +294 |
| skip when SPY fell over the last 15 min | 68 | -177 | -2.60 | 116 | -330 | -2.85 | +177 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 46 | -196 | -4.27 | 138 | -311 | -2.25 | +196 |
| skip stock not beating SPY over 15 min | 31 | -64 | -2.06 | 153 | -443 | -2.90 | +64 |
| skip afternoon entries (2:00-3:45 PM) | 40 | -222 | -5.55 | 144 | -285 | -1.98 | +222 |
| skip volume spikes above 5x average | 33 | -155 | -4.70 | 151 | -352 | -2.33 | +155 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 177 | -498 | -2.82 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.57%) | 16 | -70 | -4.39 | 168 | -437 | -2.60 | +70 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 101 | -369 | -3.65 | 83 | -139 | -1.67 | +369 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 56% (37-73) | +0.76 | -1.43 | -36 | ▲ |
| 60-240 | 81 | 33% (24-44) | -1.29 | -2.82 | -228 |  |
| 240-375 | 53 | 30% (20-44) | -2.64 | -4.81 | -255 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 47 | 36% (24-50) | -1.44 | -3.72 | -175 |  |
| 0 to 0.2 | 55 | 33% (22-46) | -1.54 | -2.98 | -164 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 76 | 28% (19-39) | -1.76 | -3.87 | -294 |  |
| above VWAP | 108 | 43% (34-52) | -0.24 | -1.98 | -213 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 62 | 37% (26-50) | +0.11 | -1.35 | -84 |  |
| (0.132, 0.37] | 61 | 44% (33-57) | -0.85 | -2.72 | -166 |  |
| (0.37, 1.555] | 61 | 28% (18-40) | -1.89 | -4.22 | -258 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 61 | 39% (28-52) | +0.12 | -1.49 | -91 |  |
| (0.147, 0.408] | 61 | 41% (30-54) | -0.69 | -2.69 | -164 |  |
| (0.408, 1.281] | 61 | 30% (20-42) | -1.96 | -4.02 | -246 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.288] | 62 | 35% (25-48) | -1.25 | -3.45 | -214 |  |
| (-0.288, 0.364] | 61 | 46% (34-58) | +0.86 | -0.40 | -25 |  |
| (0.364, 2.726] | 61 | 28% (18-40) | -2.21 | -4.40 | -268 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 62 | 39% (28-51) | -1.13 | -2.77 | -171 |  |
| (0.0518, 0.12] | 61 | 39% (28-52) | +0.30 | -1.37 | -83 |  |
| (0.12, 0.678] | 61 | 31% (21-44) | -1.78 | -4.13 | -252 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.203] | 62 | 44% (32-56) | +0.19 | -1.05 | -65 |  |
| (0.203, 0.307] | 61 | 39% (28-52) | -0.74 | -2.79 | -170 |  |
| (0.307, 0.875] | 61 | 26% (17-38) | -2.07 | -4.45 | -272 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 62 | 39% (28-51) | -0.60 | -2.38 | -148 |  |
| (2.39, 3.502] | 61 | 43% (31-55) | +0.64 | -1.25 | -76 |  |
| (3.502, 18.762] | 61 | 28% (18-40) | -2.66 | -4.64 | -283 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0963] | 62 | 45% (33-57) | +0.40 | -0.34 | -21 |  |
| (0.0963, 0.145] | 61 | 39% (28-52) | -1.09 | -2.35 | -143 |  |
| (0.145, 0.392] | 61 | 25% (16-37) | -1.94 | -5.61 | -342 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.427] | 20 | 30% (15-52) | -2.61 | -3.51 | -70 |  |
| (-0.427, 0.577] | 19 | 47% (27-68) | -0.29 | -0.79 | -15 |  |
| (0.577, 5.305] | 19 | 58% (36-77) | -0.18 | -0.87 | -16 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.476] | 22 | 41% (23-61) | -0.90 | -1.55 | -34 |  |
| (0.476, 0.661] | 21 | 43% (24-63) | -1.56 | -2.18 | -46 |  |
| (0.661, 1.74] | 22 | 50% (31-69) | -1.28 | -2.20 | -48 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 22 | 50% (31-69) | -0.71 | -1.15 | -25 |  |
| (0.779, 1.196] | 21 | 38% (21-59) | -1.53 | -2.35 | -49 |  |
| (1.196, 3.566] | 22 | 45% (27-65) | -1.50 | -2.43 | -53 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.326] | 22 | 36% (20-57) | -1.51 | -2.07 | -45 |  |
| (0.326, 0.54] | 21 | 62% (41-79) | +0.35 | -0.34 | -7 | ▲ |
| (0.54, 1.21] | 22 | 36% (20-57) | -2.49 | -3.44 | -76 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 84, trail_stop 69, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0963] | 62 | 32% | 27% | 39% |
| (0.0963, 0.145] | 61 | 49% | 44% | 5% |
| (0.145, 0.392] | 61 | 56% | 41% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
