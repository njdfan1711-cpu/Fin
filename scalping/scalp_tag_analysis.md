# Scalp signal analysis (fixed exits)

_181 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 181 | 39% (32-46) | +0.03 | -1.87 | -339 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | -17 | -0.68 | 156 | -322 | -2.07 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 180 | -333 | -1.85 | +6 |
| skip when SPY is down on the day | 70 | -103 | -1.47 | 111 | -236 | -2.13 | +103 |
| skip when SPY is below its VWAP | 75 | -180 | -2.39 | 106 | -160 | -1.51 | +180 |
| skip when SPY fell over the last 15 min | 68 | -141 | -2.07 | 113 | -199 | -1.76 | +141 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 45 | -162 | -3.60 | 136 | -177 | -1.30 | +162 |
| skip stock not beating SPY over 15 min | 30 | -23 | -0.77 | 151 | -316 | -2.09 | +23 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -195 | -5.26 | 144 | -145 | -1.01 | +195 |
| skip volume spikes above 5x average | 33 | -150 | -4.53 | 148 | -190 | -1.28 | +150 |
| skip when the stop is inside normal noise (range > stop) | 7 | -1 | -0.20 | 174 | -338 | -1.94 | +1 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 16 | -54 | -3.36 | 165 | -285 | -1.73 | +54 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 100 | -282 | -2.82 | 81 | -58 | -0.71 | +282 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 64% (45-80) | +3.57 | +1.39 | +35 | ▲ |
| 60-240 | 81 | 37% (27-48) | -0.28 | -1.81 | -146 |  |
| 240-375 | 50 | 28% (17-42) | -1.96 | -4.21 | -211 |  |
| 375-390 | 25 | 44% (27-63) | +1.47 | -0.68 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 46 | 43% (30-58) | +0.72 | -1.59 | -73 |  |
| 0 to 0.2 | 53 | 36% (24-49) | -0.06 | -1.53 | -81 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 75 | 37% (27-49) | -0.28 | -2.39 | -180 |  |
| above VWAP | 106 | 41% (32-50) | +0.24 | -1.51 | -160 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 61 | 39% (28-52) | +0.22 | -1.25 | -76 |  |
| (0.132, 0.368] | 60 | 43% (32-56) | +0.02 | -1.80 | -108 |  |
| (0.368, 1.555] | 60 | 35% (24-48) | -0.16 | -2.59 | -155 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 60 | 43% (32-56) | +0.34 | -1.29 | -77 |  |
| (0.147, 0.408] | 60 | 42% (30-54) | +0.79 | -1.23 | -74 |  |
| (0.408, 1.281] | 60 | 33% (23-46) | -0.94 | -3.03 | -182 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.288] | 61 | 39% (28-52) | +0.18 | -2.04 | -124 |  |
| (-0.288, 0.364] | 60 | 45% (33-58) | +1.01 | -0.27 | -16 |  |
| (0.364, 2.726] | 60 | 33% (23-46) | -1.11 | -3.32 | -199 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 61 | 41% (30-54) | -0.07 | -1.73 | -106 |  |
| (0.0518, 0.119] | 60 | 47% (35-59) | +1.00 | -0.55 | -33 |  |
| (0.119, 0.678] | 60 | 30% (20-43) | -0.84 | -3.35 | -201 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.201] | 61 | 44% (33-57) | +0.16 | -1.09 | -67 |  |
| (0.201, 0.306] | 60 | 40% (29-53) | +0.45 | -1.57 | -94 |  |
| (0.306, 0.875] | 60 | 33% (23-46) | -0.53 | -2.97 | -178 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 61 | 39% (28-52) | +0.28 | -1.53 | -93 |  |
| (2.389, 3.502] | 60 | 50% (38-62) | +1.35 | -0.55 | -33 |  |
| (3.502, 18.762] | 60 | 28% (19-41) | -1.55 | -3.55 | -213 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0963] | 61 | 46% (34-58) | +0.38 | -0.37 | -22 |  |
| (0.0963, 0.145] | 60 | 37% (26-49) | -0.01 | -1.27 | -76 |  |
| (0.145, 0.392] | 60 | 35% (24-48) | -0.29 | -4.01 | -240 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.53] | 19 | 21% (9-43) | -2.71 | -3.60 | -68 |  |
| (-0.53, 0.474] | 18 | 44% (25-66) | +0.62 | +0.10 | +2 |  |
| (0.474, 5.305] | 18 | 67% (44-84) | +3.76 | +3.10 | +56 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.476] | 21 | 38% (21-59) | -0.42 | -1.07 | -22 |  |
| (0.476, 0.616] | 20 | 40% (22-61) | -0.06 | -0.69 | -14 |  |
| (0.616, 1.74] | 21 | 48% (28-68) | +0.93 | +0.03 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 21 | 52% (32-72) | +1.33 | +0.92 | +19 |  |
| (0.789, 1.196] | 20 | 35% (18-57) | +0.24 | -0.60 | -12 |  |
| (1.196, 3.566] | 21 | 38% (21-59) | -1.10 | -2.04 | -43 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.318] | 21 | 33% (17-55) | -0.59 | -1.16 | -24 |  |
| (0.318, 0.532] | 20 | 55% (34-74) | +1.34 | +0.65 | +13 |  |
| (0.532, 1.14] | 21 | 38% (21-59) | -0.23 | -1.16 | -24 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.19%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 89, target 46, time_stop 43, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0963] | 61 | 33% | 16% | 49% |
| (0.0963, 0.145] | 60 | 55% | 30% | 12% |
| (0.145, 0.392] | 60 | 60% | 30% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
