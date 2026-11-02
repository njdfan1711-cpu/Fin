# Scalp signal analysis (fixed exits)

_205 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 205 | 40% (33-46) | +0.03 | -1.74 | -357 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 33 | -4 | -0.12 | 172 | -353 | -2.05 | +4 |
| skip first 30 min | 1 | -6 | -6.31 | 204 | -350 | -1.72 | +6 |
| skip when SPY is down on the day | 86 | -118 | -1.38 | 119 | -238 | -2.00 | +118 |
| skip when SPY is below its VWAP | 89 | -181 | -2.04 | 116 | -175 | -1.51 | +181 |
| skip when SPY fell over the last 15 min | 76 | -120 | -1.58 | 129 | -236 | -1.83 | +120 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 51 | -174 | -3.41 | 154 | -183 | -1.19 | +174 |
| skip stock not beating SPY over 15 min | 34 | -20 | -0.59 | 171 | -337 | -1.97 | +20 |
| skip afternoon entries (2:00-3:45 PM) | 44 | -212 | -4.82 | 161 | -145 | -0.90 | +212 |
| skip volume spikes above 5x average | 39 | -170 | -4.37 | 166 | -186 | -1.12 | +170 |
| skip when the stop is inside normal noise (range > stop) | 12 | -35 | -2.90 | 193 | -322 | -1.67 | +35 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.63%) | 22 | -52 | -2.38 | 183 | -304 | -1.66 | +52 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 109 | -308 | -2.82 | 96 | -49 | -0.51 | +308 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 59% (41-74) | +2.81 | +0.83 | +24 | ▲ |
| 60-240 | 85 | 36% (27-47) | -0.37 | -1.86 | -159 |  |
| 240-375 | 58 | 29% (19-42) | -1.73 | -3.77 | -218 |  |
| 375-390 | 33 | 48% (33-65) | +1.73 | -0.12 | -4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 35 | 46% (30-62) | +0.87 | -0.60 | -21 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 61 | 36% (25-49) | +0.00 | -1.37 | -84 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 89 | 39% (30-50) | -0.13 | -2.04 | -181 |  |
| above VWAP | 116 | 40% (31-49) | +0.15 | -1.51 | -175 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 69 | 39% (28-51) | +0.11 | -1.27 | -88 |  |
| (0.132, 0.374] | 68 | 44% (33-56) | +0.21 | -1.58 | -107 |  |
| (0.374, 1.555] | 68 | 35% (25-47) | -0.22 | -2.38 | -162 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.118] | 68 | 43% (32-54) | +0.35 | -1.04 | -71 |  |
| (0.118, 0.408] | 68 | 43% (32-54) | +0.68 | -1.30 | -88 |  |
| (0.408, 1.352] | 68 | 34% (24-46) | -0.84 | -2.82 | -191 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.349] | 69 | 41% (30-52) | +0.16 | -1.87 | -129 |  |
| (-0.349, 0.338] | 68 | 44% (33-56) | +0.86 | -0.35 | -24 |  |
| (0.338, 2.726] | 68 | 34% (24-46) | -0.93 | -2.99 | -204 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 69 | 41% (30-52) | -0.17 | -1.72 | -118 |  |
| (0.0521, 0.123] | 68 | 46% (34-57) | +0.79 | -0.89 | -61 |  |
| (0.123, 0.678] | 68 | 32% (22-44) | -0.52 | -2.61 | -178 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 69 | 43% (32-55) | +0.13 | -1.08 | -74 |  |
| (0.207, 0.314] | 68 | 40% (29-52) | +0.34 | -1.60 | -109 |  |
| (0.314, 0.979] | 68 | 35% (25-47) | -0.37 | -2.55 | -173 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 69 | 41% (30-52) | +0.44 | -1.24 | -85 |  |
| (2.389, 3.632] | 68 | 49% (37-60) | +0.99 | -0.78 | -53 |  |
| (3.632, 18.762] | 68 | 29% (20-41) | -1.35 | -3.21 | -218 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0978] | 69 | 46% (35-58) | +0.42 | -0.32 | -22 |  |
| (0.0978, 0.147] | 68 | 40% (29-52) | +0.44 | -0.82 | -55 |  |
| (0.147, 0.392] | 68 | 32% (22-44) | -0.76 | -4.10 | -279 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-10.232, -0.876] | 27 | 26% (13-45) | -2.08 | -3.00 | -81 |  |
| (-0.876, 0.444] | 27 | 44% (28-63) | +0.61 | +0.10 | +3 |  |
| (0.444, 5.305] | 25 | 60% (41-77) | +2.73 | +1.99 | +50 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.493] | 30 | 43% (27-61) | +0.22 | -0.41 | -12 |  |
| (0.493, 0.72] | 27 | 44% (28-63) | +0.68 | -0.05 | -1 |  |
| (0.72, 1.74] | 29 | 38% (23-56) | -0.49 | -1.36 | -39 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 29 | 48% (31-66) | +0.84 | +0.35 | +10 |  |
| (0.789, 1.217] | 28 | 39% (24-58) | +0.42 | -0.37 | -10 |  |
| (1.217, 3.566] | 29 | 38% (23-56) | -0.87 | -1.82 | -53 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.354] | 29 | 45% (28-62) | +0.77 | +0.19 | +6 |  |
| (0.354, 0.557] | 28 | 43% (27-61) | +0.20 | -0.57 | -16 |  |
| (0.557, 1.607] | 29 | 38% (23-56) | -0.58 | -1.47 | -43 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 101, target 51, time_stop 46, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0978] | 69 | 33% | 16% | 46% |
| (0.0978, 0.147] | 68 | 53% | 32% | 10% |
| (0.147, 0.392] | 68 | 62% | 26% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
