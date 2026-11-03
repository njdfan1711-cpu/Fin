# Scalp signal analysis (trail exits)

_216 tagged trades, 24 trading days (2026-10-01 to 2026-11-03). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 216 | 37% (31-44) | -1.00 | -2.72 | -587 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -8 | -0.23 | 181 | -579 | -3.20 | +8 |
| skip first 30 min | 2 | -3 | -1.70 | 214 | -584 | -2.73 | +3 |
| skip when SPY is down on the day | 89 | -281 | -3.16 | 127 | -306 | -2.41 | +281 |
| skip when SPY is below its VWAP | 94 | -328 | -3.49 | 122 | -259 | -2.12 | +328 |
| skip when SPY fell over the last 15 min | 80 | -198 | -2.47 | 136 | -389 | -2.86 | +198 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 54 | -235 | -4.35 | 162 | -352 | -2.18 | +235 |
| skip stock not beating SPY over 15 min | 37 | -81 | -2.19 | 179 | -506 | -2.83 | +81 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -217 | -4.83 | 171 | -370 | -2.16 | +217 |
| skip volume spikes above 5x average | 40 | -190 | -4.74 | 176 | -398 | -2.26 | +190 |
| skip when the stop is inside normal noise (range > stop) | 14 | -46 | -3.27 | 202 | -541 | -2.68 | +46 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 24 | -80 | -3.32 | 192 | -507 | -2.64 | +80 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 111 | -399 | -3.59 | 105 | -188 | -1.79 | +399 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 33 | 48% (33-65) | -0.32 | -2.12 | -70 |  |
| 60-240 | 88 | 33% (24-43) | -1.47 | -2.94 | -259 |  |
| 240-375 | 60 | 33% (23-46) | -2.17 | -4.17 | -250 |  |
| 375-390 | 35 | 43% (28-59) | +1.54 | -0.23 | -8 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 37% (23-53) | -1.17 | -2.57 | -98 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 65 | 35% (25-48) | -1.50 | -2.82 | -183 |  |
| > 0.2 | 62 | 39% (28-51) | -0.01 | -1.97 | -122 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 94 | 31% (22-41) | -1.65 | -3.49 | -328 |  |
| above VWAP | 122 | 42% (33-51) | -0.50 | -2.12 | -259 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 72 | 35% (25-46) | -0.37 | -1.70 | -123 |  |
| (0.129, 0.375] | 72 | 47% (36-59) | -0.63 | -2.37 | -171 |  |
| (0.375, 1.555] | 72 | 29% (20-41) | -2.02 | -4.08 | -294 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.124] | 72 | 42% (31-53) | +0.01 | -1.33 | -96 |  |
| (0.124, 0.421] | 71 | 41% (30-52) | -0.96 | -2.95 | -210 |  |
| (0.421, 2.453] | 71 | 28% (19-40) | -2.06 | -3.92 | -278 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.35] | 72 | 38% (27-49) | -1.36 | -3.33 | -240 |  |
| (-0.35, 0.348] | 72 | 44% (34-56) | +0.50 | -0.71 | -51 |  |
| (0.348, 2.726] | 72 | 29% (20-41) | -2.14 | -4.11 | -296 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0522] | 72 | 39% (28-50) | -1.21 | -2.73 | -197 |  |
| (0.0522, 0.122] | 72 | 39% (28-50) | -0.01 | -1.52 | -109 |  |
| (0.122, 0.678] | 72 | 33% (24-45) | -1.79 | -3.91 | -281 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.21] | 72 | 42% (31-53) | -0.01 | -1.19 | -85 |  |
| (0.21, 0.315] | 72 | 38% (27-49) | -1.15 | -3.03 | -218 |  |
| (0.315, 0.979] | 72 | 32% (22-43) | -1.85 | -3.93 | -283 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.353] | 72 | 38% (27-49) | -0.71 | -2.34 | -169 |  |
| (2.353, 3.617] | 72 | 46% (35-57) | +0.40 | -1.32 | -95 |  |
| (3.617, 18.762] | 72 | 28% (19-39) | -2.69 | -4.50 | -324 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0985] | 73 | 44% (33-55) | +0.20 | -0.57 | -41 |  |
| (0.0985, 0.15] | 71 | 41% (30-52) | -1.27 | -2.47 | -175 |  |
| (0.15, 0.392] | 72 | 26% (18-38) | -1.96 | -5.14 | -370 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.887] | 30 | 27% (14-44) | -2.88 | -3.75 | -112 |  |
| (-0.887, 0.454] | 30 | 50% (33-67) | -0.48 | -1.01 | -30 |  |
| (0.454, 5.305] | 30 | 53% (36-70) | -0.55 | -1.30 | -39 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.513] | 33 | 45% (30-62) | -0.67 | -1.30 | -43 |  |
| (0.513, 0.747] | 32 | 44% (28-61) | -1.56 | -2.34 | -75 |  |
| (0.747, 1.74] | 32 | 41% (26-58) | -2.02 | -2.83 | -91 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 33 | 45% (30-62) | -1.33 | -1.85 | -61 |  |
| (0.775, 1.2] | 32 | 41% (26-58) | -1.40 | -2.16 | -69 |  |
| (1.2, 5.866] | 32 | 44% (28-61) | -1.51 | -2.44 | -78 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.347] | 33 | 36% (22-53) | -1.41 | -1.99 | -66 |  |
| (0.347, 0.559] | 32 | 56% (39-72) | -0.51 | -1.29 | -41 | ▲ |
| (0.559, 1.659] | 32 | 38% (23-55) | -2.32 | -3.16 | -101 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.17%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 47%
- Exit mix: stop 101, trail_stop 82, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0985] | 73 | 34% | 29% | 33% |
| (0.0985, 0.15] | 71 | 51% | 44% | 4% |
| (0.15, 0.392] | 72 | 56% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
