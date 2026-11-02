# Scalp signal analysis (trail exits)

_210 tagged trades, 23 trading days (2026-10-01 to 2026-11-02). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 210 | 38% (31-44) | -0.91 | -2.65 | -557 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 175 | -549 | -3.14 | +8 |
| skip first 30 min | 1 | -6 | -6.31 | 209 | -551 | -2.64 | +6 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 121 | -276 | -2.28 | +281 |
| skip when SPY is below its VWAP | 93 | -321 | -3.46 | 117 | -236 | -2.02 | +321 |
| skip when SPY fell over the last 15 min | 78 | -185 | -2.38 | 132 | -372 | -2.82 | +185 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 52 | -216 | -4.15 | 158 | -341 | -2.16 | +216 |
| skip stock not beating SPY over 15 min | 36 | -75 | -2.07 | 174 | -483 | -2.77 | +75 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -217 | -4.83 | 165 | -340 | -2.06 | +217 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 170 | -368 | -2.16 | +190 |
| skip when the stop is inside normal noise (range > stop) | 13 | -49 | -3.74 | 197 | -509 | -2.58 | +49 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 23 | -83 | -3.63 | 187 | -474 | -2.53 | +83 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -386 | -3.54 | 101 | -172 | -1.70 | +386 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 30 | 50% (33-67) | -0.07 | -2.00 | -60 |  |
| 60-240 | 86 | 34% (25-44) | -1.37 | -2.85 | -245 |  |
| 240-375 | 59 | 34% (23-47) | -2.12 | -4.13 | -244 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 63 | 35% (24-47) | -1.50 | -2.85 | -180 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 93 | 31% (23-41) | -1.60 | -3.46 | -321 |  |
| above VWAP | 117 | 43% (34-52) | -0.36 | -2.02 | -236 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 70 | 36% (26-47) | -0.21 | -1.56 | -109 |  |
| (0.129, 0.374] | 70 | 47% (36-59) | -0.60 | -2.36 | -165 |  |
| (0.374, 1.555] | 70 | 30% (21-42) | -1.92 | -4.03 | -282 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.12] | 70 | 43% (32-55) | +0.18 | -1.18 | -83 |  |
| (0.12, 0.41] | 69 | 41% (30-52) | -0.92 | -2.88 | -199 |  |
| (0.41, 2.453] | 70 | 30% (21-42) | -1.92 | -3.85 | -269 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.357] | 70 | 37% (27-49) | -1.46 | -3.47 | -243 |  |
| (-0.357, 0.339] | 70 | 44% (33-56) | +0.57 | -0.64 | -45 |  |
| (0.339, 2.726] | 70 | 31% (22-43) | -1.83 | -3.85 | -270 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.054] | 70 | 40% (29-52) | -1.08 | -2.63 | -184 |  |
| (0.054, 0.124] | 70 | 40% (29-52) | +0.18 | -1.47 | -103 |  |
| (0.124, 0.678] | 70 | 33% (23-44) | -1.83 | -3.86 | -270 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.21] | 70 | 43% (32-55) | +0.16 | -1.03 | -72 |  |
| (0.21, 0.314] | 70 | 37% (27-49) | -1.16 | -3.08 | -215 |  |
| (0.314, 0.979] | 70 | 33% (23-44) | -1.72 | -3.85 | -270 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.382] | 70 | 39% (28-50) | -0.58 | -2.25 | -157 |  |
| (2.382, 3.634] | 70 | 46% (35-57) | +0.47 | -1.28 | -89 |  |
| (3.634, 18.762] | 70 | 29% (19-40) | -2.61 | -4.44 | -311 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0982] | 70 | 46% (35-57) | +0.36 | -0.38 | -26 |  |
| (0.0982, 0.15] | 70 | 41% (31-53) | -1.10 | -2.34 | -164 |  |
| (0.15, 0.392] | 70 | 26% (17-37) | -1.99 | -5.25 | -367 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 28 | 29% (15-47) | -2.67 | -3.55 | -100 |  |
| (-0.912, 0.444] | 29 | 48% (31-66) | -0.61 | -1.14 | -33 |  |
| (0.444, 5.305] | 27 | 59% (41-75) | +0.02 | -0.71 | -19 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.493] | 31 | 45% (29-62) | -0.59 | -1.22 | -38 |  |
| (0.493, 0.747] | 30 | 50% (33-67) | -1.02 | -1.77 | -53 |  |
| (0.747, 1.74] | 30 | 40% (25-58) | -2.10 | -2.92 | -88 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 31 | 45% (29-62) | -1.33 | -1.83 | -57 |  |
| (0.789, 1.21] | 30 | 43% (27-61) | -1.10 | -1.87 | -56 |  |
| (1.21, 5.866] | 30 | 47% (30-64) | -1.25 | -2.19 | -66 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.353] | 31 | 42% (26-59) | -0.74 | -1.31 | -41 |  |
| (0.353, 0.559] | 30 | 57% (39-73) | -0.54 | -1.32 | -40 | ▲ |
| (0.559, 1.659] | 30 | 37% (22-54) | -2.41 | -3.27 | -98 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 96, trail_stop 81, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0982] | 70 | 33% | 29% | 34% |
| (0.0982, 0.15] | 70 | 49% | 46% | 4% |
| (0.15, 0.392] | 70 | 56% | 41% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
