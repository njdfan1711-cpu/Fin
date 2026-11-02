# Scalp signal analysis (trail exits)

_211 tagged trades, 23 trading days (2026-10-01 to 2026-11-02). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 211 | 37% (31-44) | -0.93 | -2.67 | -564 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 176 | -556 | -3.16 | +8 |
| skip first 30 min | 1 | -6 | -6.31 | 210 | -558 | -2.66 | +6 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 122 | -282 | -2.32 | +281 |
| skip when SPY is below its VWAP | 94 | -328 | -3.49 | 117 | -236 | -2.02 | +328 |
| skip when SPY fell over the last 15 min | 79 | -192 | -2.43 | 132 | -372 | -2.82 | +192 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 53 | -222 | -4.19 | 158 | -342 | -2.16 | +222 |
| skip stock not beating SPY over 15 min | 36 | -75 | -2.07 | 175 | -489 | -2.80 | +75 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -217 | -4.83 | 166 | -347 | -2.09 | +217 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 171 | -374 | -2.19 | +190 |
| skip when the stop is inside normal noise (range > stop) | 13 | -49 | -3.74 | 198 | -515 | -2.60 | +49 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 23 | -83 | -3.63 | 188 | -480 | -2.56 | +83 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -386 | -3.54 | 102 | -178 | -1.75 | +386 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 30 | 50% (33-67) | -0.07 | -2.00 | -60 |  |
| 60-240 | 87 | 33% (24-44) | -1.42 | -2.89 | -252 |  |
| 240-375 | 59 | 34% (23-47) | -2.12 | -4.13 | -244 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 64 | 34% (24-47) | -1.57 | -2.91 | -186 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 31% (22-41) | -1.65 | -3.49 | -328 |  |
| above VWAP | 117 | 43% (34-52) | -0.36 | -2.02 | -236 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.122] | 71 | 35% (25-47) | -0.29 | -1.64 | -116 |  |
| (0.122, 0.374] | 70 | 47% (36-59) | -0.60 | -2.36 | -165 |  |
| (0.374, 1.555] | 70 | 30% (21-42) | -1.92 | -4.03 | -282 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 70 | 41% (31-53) | +0.06 | -1.31 | -91 |  |
| (0.118, 0.408] | 70 | 41% (31-53) | -0.87 | -2.81 | -197 |  |
| (0.408, 2.453] | 70 | 30% (21-42) | -1.92 | -3.85 | -269 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.352] | 71 | 37% (26-48) | -1.43 | -3.42 | -243 |  |
| (-0.352, 0.34] | 70 | 46% (35-57) | +0.67 | -0.56 | -39 |  |
| (0.34, 2.726] | 70 | 30% (21-42) | -2.03 | -4.03 | -282 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 71 | 39% (29-51) | -1.15 | -2.69 | -191 |  |
| (0.0522, 0.124] | 70 | 40% (29-52) | +0.18 | -1.47 | -103 |  |
| (0.124, 0.678] | 70 | 33% (23-44) | -1.83 | -3.86 | -270 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.208] | 71 | 42% (31-54) | +0.07 | -1.11 | -79 |  |
| (0.208, 0.314] | 70 | 37% (27-49) | -1.16 | -3.08 | -215 |  |
| (0.314, 0.979] | 70 | 33% (23-44) | -1.72 | -3.85 | -270 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.367] | 71 | 38% (28-50) | -0.66 | -2.31 | -164 |  |
| (2.367, 3.632] | 70 | 46% (35-57) | +0.47 | -1.28 | -89 |  |
| (3.632, 18.762] | 70 | 29% (19-40) | -2.61 | -4.44 | -311 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0984] | 71 | 45% (34-57) | +0.37 | -0.38 | -27 |  |
| (0.0984, 0.15] | 70 | 41% (31-53) | -1.20 | -2.43 | -170 |  |
| (0.15, 0.392] | 70 | 26% (17-37) | -1.99 | -5.25 | -367 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.911] | 29 | 28% (15-46) | -2.78 | -3.65 | -106 |  |
| (-0.911, 0.444] | 28 | 50% (33-67) | -0.42 | -0.96 | -27 |  |
| (0.444, 5.305] | 28 | 57% (39-73) | -0.19 | -0.92 | -26 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.498] | 31 | 45% (29-62) | -0.59 | -1.22 | -38 |  |
| (0.498, 0.743] | 30 | 50% (33-67) | -1.03 | -1.77 | -53 |  |
| (0.743, 1.74] | 31 | 39% (24-56) | -2.21 | -3.04 | -94 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 31 | 45% (29-62) | -1.33 | -1.83 | -57 |  |
| (0.789, 1.206] | 30 | 43% (27-61) | -1.10 | -1.88 | -56 |  |
| (1.206, 5.866] | 31 | 45% (29-62) | -1.40 | -2.33 | -72 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.349] | 31 | 39% (24-56) | -1.12 | -1.71 | -53 |  |
| (0.349, 0.557] | 30 | 57% (39-73) | -0.41 | -1.16 | -35 | ▲ |
| (0.557, 1.659] | 31 | 39% (24-56) | -2.27 | -3.14 | -97 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 97, trail_stop 81, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0984] | 71 | 32% | 30% | 34% |
| (0.0984, 0.15] | 70 | 50% | 44% | 4% |
| (0.15, 0.392] | 70 | 56% | 41% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
