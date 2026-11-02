# Scalp signal analysis (trail exits)

_205 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 205 | 39% (32-45) | -0.79 | -2.56 | -525 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 33 | +4 | +0.14 | 172 | -530 | -3.08 | -4 |
| skip first 30 min | 1 | -6 | -6.31 | 204 | -519 | -2.54 | +6 |
| skip when SPY is down on the day | 86 | -263 | -3.05 | 119 | -263 | -2.21 | +263 |
| skip when SPY is below its VWAP | 89 | -296 | -3.33 | 116 | -229 | -1.98 | +296 |
| skip when SPY fell over the last 15 min | 77 | -179 | -2.32 | 128 | -347 | -2.71 | +179 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 51 | -209 | -4.10 | 154 | -316 | -2.05 | +209 |
| skip stock not beating SPY over 15 min | 34 | -62 | -1.82 | 171 | -463 | -2.71 | +62 |
| skip afternoon entries (2:00-3:45 PM) | 44 | -211 | -4.80 | 161 | -314 | -1.95 | +211 |
| skip volume spikes above 5x average | 39 | -183 | -4.70 | 166 | -342 | -2.06 | +183 |
| skip when the stop is inside normal noise (range > stop) | 12 | -42 | -3.51 | 193 | -483 | -2.50 | +42 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 22 | -77 | -3.50 | 183 | -448 | -2.45 | +77 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -386 | -3.54 | 96 | -140 | -1.46 | +386 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 52% (34-69) | +0.13 | -1.85 | -54 |  |
| 60-240 | 85 | 34% (25-45) | -1.32 | -2.81 | -239 |  |
| 240-375 | 58 | 34% (24-47) | -2.06 | -4.10 | -238 |  |
| 375-390 | 33 | 45% (30-62) | +1.98 | +0.14 | +4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 35 | 40% (26-56) | -0.78 | -2.25 | -79 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 61 | 36% (25-49) | -1.36 | -2.73 | -167 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 89 | 33% (24-43) | -1.41 | -3.33 | -296 |  |
| above VWAP | 116 | 43% (34-52) | -0.31 | -1.98 | -229 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 69 | 38% (27-49) | -0.01 | -1.39 | -96 |  |
| (0.132, 0.374] | 68 | 47% (36-59) | -0.56 | -2.35 | -160 |  |
| (0.374, 1.555] | 68 | 31% (21-43) | -1.81 | -3.97 | -270 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 68 | 43% (32-54) | +0.23 | -1.15 | -78 |  |
| (0.118, 0.408] | 68 | 43% (32-54) | -0.73 | -2.71 | -184 |  |
| (0.408, 1.352] | 68 | 31% (21-43) | -1.80 | -3.78 | -257 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 69 | 38% (27-49) | -1.30 | -3.33 | -230 |  |
| (-0.349, 0.338] | 68 | 46% (34-57) | +0.66 | -0.56 | -38 |  |
| (0.338, 2.726] | 68 | 32% (22-44) | -1.72 | -3.78 | -257 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 69 | 41% (30-52) | -1.01 | -2.55 | -176 |  |
| (0.0521, 0.123] | 68 | 40% (29-52) | +0.19 | -1.49 | -102 |  |
| (0.123, 0.678] | 68 | 35% (25-47) | -1.55 | -3.64 | -248 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 69 | 43% (32-55) | +0.19 | -1.02 | -70 |  |
| (0.207, 0.314] | 68 | 38% (28-50) | -0.97 | -2.91 | -198 |  |
| (0.314, 0.979] | 68 | 34% (24-46) | -1.60 | -3.78 | -257 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 69 | 41% (30-52) | -0.40 | -2.08 | -144 |  |
| (2.389, 3.632] | 68 | 46% (34-57) | +0.54 | -1.23 | -84 |  |
| (3.632, 18.762] | 68 | 29% (20-41) | -2.52 | -4.38 | -298 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0978] | 69 | 46% (35-58) | +0.45 | -0.29 | -20 |  |
| (0.0978, 0.147] | 68 | 43% (32-54) | -0.97 | -2.22 | -151 |  |
| (0.147, 0.392] | 68 | 26% (17-38) | -1.88 | -5.22 | -355 | ▼ |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-10.232, -0.876] | 27 | 33% (19-52) | -2.16 | -3.08 | -83 |  |
| (-0.876, 0.444] | 27 | 48% (31-66) | -0.63 | -1.14 | -31 |  |
| (0.444, 5.305] | 25 | 64% (45-80) | +0.50 | -0.24 | -6 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.493] | 30 | 47% (30-64) | -0.41 | -1.04 | -31 |  |
| (0.493, 0.72] | 27 | 52% (34-69) | -0.80 | -1.54 | -41 |  |
| (0.72, 1.74] | 29 | 45% (28-62) | -1.68 | -2.54 | -74 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 29 | 48% (31-66) | -1.01 | -1.50 | -44 |  |
| (0.789, 1.217] | 28 | 46% (30-64) | -0.78 | -1.56 | -44 |  |
| (1.217, 3.566] | 29 | 48% (31-66) | -1.09 | -2.04 | -59 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 29 | 45% (28-62) | -0.39 | -0.97 | -28 |  |
| (0.354, 0.557] | 28 | 57% (39-73) | -0.44 | -1.20 | -34 | ▲ |
| (0.557, 1.607] | 29 | 41% (26-59) | -2.03 | -2.92 | -85 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 91, trail_stop 81, time_stop 29, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0978] | 69 | 32% | 29% | 35% |
| (0.0978, 0.147] | 68 | 47% | 47% | 4% |
| (0.147, 0.392] | 68 | 54% | 43% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
