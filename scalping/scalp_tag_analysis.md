# Scalp signal analysis (fixed exits)

_209 tagged trades, 23 trading days (2026-10-01 to 2026-11-02). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 209 | 39% (32-46) | -0.08 | -1.83 | -382 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 35 | -17 | -0.47 | 174 | -366 | -2.10 | +17 |
| skip first 30 min | 1 | -6 | -6.31 | 208 | -376 | -1.81 | +6 |
| skip when SPY is down on the day | 89 | -137 | -1.54 | 120 | -245 | -2.04 | +137 |
| skip when SPY is below its VWAP | 92 | -200 | -2.18 | 117 | -182 | -1.55 | +200 |
| skip when SPY fell over the last 15 min | 76 | -120 | -1.58 | 133 | -262 | -1.97 | +120 |
| skip over-extended (30-min run in top quarter, > 0.49%) | 52 | -181 | -3.47 | 157 | -202 | -1.28 | +181 |
| skip stock not beating SPY over 15 min | 36 | -33 | -0.91 | 173 | -350 | -2.02 | +33 |
| skip afternoon entries (2:00-3:45 PM) | 45 | -218 | -4.85 | 164 | -164 | -1.00 | +218 |
| skip volume spikes above 5x average | 39 | -170 | -4.37 | 170 | -212 | -1.25 | +170 |
| skip when the stop is inside normal noise (range > stop) | 13 | -41 | -3.18 | 196 | -341 | -1.74 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.64%) | 23 | -59 | -2.56 | 186 | -323 | -1.74 | +59 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -308 | -2.82 | 100 | -74 | -0.74 | +308 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 30 | 57% (39-73) | +2.52 | +0.59 | +18 | ▲ |
| 60-240 | 85 | 36% (27-47) | -0.37 | -1.86 | -159 |  |
| 240-375 | 59 | 29% (19-41) | -1.79 | -3.81 | -225 |  |
| 375-390 | 35 | 46% (30-62) | +1.30 | -0.47 | -17 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 38 | 42% (28-58) | +0.35 | -1.04 | -40 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 62 | 35% (25-48) | -0.09 | -1.45 | -90 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 92 | 38% (29-48) | -0.31 | -2.18 | -200 |  |
| above VWAP | 117 | 39% (31-48) | +0.10 | -1.55 | -182 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 70 | 37% (27-49) | -0.20 | -1.56 | -109 |  |
| (0.126, 0.374] | 69 | 45% (34-57) | +0.36 | -1.42 | -98 |  |
| (0.374, 1.555] | 70 | 34% (24-46) | -0.38 | -2.50 | -175 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.119] | 70 | 43% (32-55) | +0.29 | -1.07 | -75 |  |
| (0.119, 0.412] | 69 | 41% (30-52) | +0.46 | -1.56 | -108 |  |
| (0.412, 2.453] | 69 | 33% (23-45) | -0.91 | -2.80 | -193 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.351] | 70 | 40% (29-52) | +0.07 | -1.94 | -136 |  |
| (-0.351, 0.34] | 69 | 43% (32-55) | +0.77 | -0.44 | -31 |  |
| (0.34, 2.726] | 70 | 33% (23-44) | -1.07 | -3.08 | -216 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0531] | 70 | 40% (29-52) | -0.25 | -1.81 | -126 |  |
| (0.0531, 0.124] | 69 | 46% (35-58) | +0.93 | -0.73 | -50 |  |
| (0.124, 0.678] | 70 | 30% (21-42) | -0.90 | -2.94 | -206 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.209] | 70 | 43% (32-55) | +0.10 | -1.09 | -76 |  |
| (0.209, 0.314] | 69 | 39% (28-51) | +0.19 | -1.73 | -120 |  |
| (0.314, 0.979] | 70 | 34% (24-46) | -0.53 | -2.66 | -186 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 70 | 39% (28-50) | +0.13 | -1.54 | -108 |  |
| (2.374, 3.625] | 69 | 49% (38-61) | +1.12 | -0.63 | -43 |  |
| (3.625, 18.762] | 70 | 29% (19-40) | -1.47 | -3.30 | -231 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0984] | 70 | 47% (36-59) | +0.55 | -0.19 | -13 |  |
| (0.0984, 0.15] | 69 | 38% (27-49) | +0.12 | -1.12 | -77 |  |
| (0.15, 0.392] | 70 | 31% (22-43) | -0.91 | -4.16 | -292 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.912] | 28 | 21% (10-40) | -2.78 | -3.66 | -102 |  |
| (-0.912, 0.441] | 27 | 44% (28-63) | +0.78 | +0.25 | +7 |  |
| (0.441, 5.305] | 28 | 57% (39-73) | +2.22 | +1.50 | +42 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.502] | 30 | 43% (27-61) | +0.22 | -0.41 | -12 |  |
| (0.502, 0.747] | 30 | 43% (27-61) | +0.57 | -0.18 | -5 |  |
| (0.747, 1.74] | 30 | 33% (19-51) | -1.20 | -2.03 | -61 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 30 | 47% (30-64) | +0.62 | +0.12 | +4 |  |
| (0.789, 1.214] | 30 | 37% (22-54) | +0.01 | -0.75 | -23 |  |
| (1.214, 5.866] | 30 | 37% (22-54) | -1.04 | -1.98 | -59 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.355] | 30 | 43% (27-61) | +0.56 | -0.02 | -1 |  |
| (0.355, 0.56] | 30 | 43% (27-61) | +0.33 | -0.45 | -13 |  |
| (0.56, 1.659] | 30 | 33% (19-51) | -1.29 | -2.15 | -65 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 24% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 105, target 51, time_stop 46, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0984] | 70 | 33% | 17% | 46% |
| (0.0984, 0.15] | 69 | 55% | 30% | 10% |
| (0.15, 0.392] | 70 | 63% | 26% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
