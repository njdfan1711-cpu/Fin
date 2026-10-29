# Scalp signal analysis (trail exits)

_190 tagged trades, 21 trading days (2026-10-01 to 2026-10-29). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 190 | 37% (31-44) | -0.83 | -2.68 | -510 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | +16 | +0.60 | 164 | -526 | -3.20 | -16 |
| skip first 30 min | 1 | -6 | -6.31 | 189 | -504 | -2.66 | +6 |
| skip when SPY is down on the day | 73 | -252 | -3.45 | 117 | -258 | -2.20 | +252 |
| skip when SPY is below its VWAP | 77 | -292 | -3.79 | 113 | -218 | -1.93 | +292 |
| skip when SPY fell over the last 15 min | 70 | -181 | -2.59 | 120 | -329 | -2.74 | +181 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 47 | -192 | -4.09 | 143 | -318 | -2.22 | +192 |
| skip stock not beating SPY over 15 min | 32 | -70 | -2.19 | 158 | -440 | -2.78 | +70 |
| skip afternoon entries (2:00-3:45 PM) | 41 | -220 | -5.37 | 149 | -290 | -1.94 | +220 |
| skip volume spikes above 5x average | 35 | -159 | -4.55 | 155 | -351 | -2.26 | +159 |
| skip when the stop is inside normal noise (range > stop) | 8 | -15 | -1.91 | 182 | -495 | -2.72 | +15 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 18 | -72 | -4.00 | 172 | -438 | -2.55 | +72 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 103 | -363 | -3.52 | 87 | -147 | -1.69 | +363 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 56% (37-72) | +0.58 | -1.48 | -40 |  |
| 60-240 | 83 | 34% (24-44) | -1.29 | -2.80 | -232 |  |
| 240-375 | 54 | 31% (21-45) | -2.55 | -4.69 | -253 |  |
| 375-390 | 26 | 42% (26-61) | +2.71 | +0.60 | +16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 49 | 37% (25-51) | -1.45 | -3.67 | -180 |  |
| 0 to 0.2 | 59 | 36% (25-48) | -1.35 | -2.74 | -162 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 77 | 29% (20-39) | -1.71 | -3.79 | -292 |  |
| above VWAP | 113 | 43% (35-53) | -0.24 | -1.93 | -218 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 64 | 36% (25-48) | +0.03 | -1.41 | -90 |  |
| (0.133, 0.37] | 63 | 48% (36-60) | -0.70 | -2.53 | -160 |  |
| (0.37, 1.555] | 63 | 29% (19-41) | -1.84 | -4.13 | -260 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.139] | 63 | 41% (30-54) | +0.20 | -1.24 | -78 |  |
| (0.139, 0.405] | 63 | 40% (29-52) | -0.85 | -2.93 | -185 |  |
| (0.405, 1.281] | 63 | 32% (22-44) | -1.78 | -3.82 | -241 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.291] | 64 | 36% (25-48) | -1.23 | -3.39 | -217 |  |
| (-0.291, 0.364] | 63 | 46% (34-58) | +0.79 | -0.45 | -28 |  |
| (0.364, 2.726] | 63 | 30% (20-42) | -2.05 | -4.20 | -265 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 64 | 39% (28-51) | -1.17 | -2.77 | -178 |  |
| (0.0521, 0.122] | 63 | 40% (29-52) | +0.33 | -1.31 | -83 |  |
| (0.122, 0.678] | 63 | 33% (23-46) | -1.66 | -3.96 | -250 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 64 | 42% (31-54) | +0.11 | -1.14 | -73 |  |
| (0.207, 0.312] | 63 | 40% (29-52) | -0.76 | -2.78 | -175 |  |
| (0.312, 0.875] | 63 | 30% (20-42) | -1.87 | -4.15 | -261 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 64 | 39% (28-51) | -0.63 | -2.39 | -153 |  |
| (2.39, 3.632] | 63 | 43% (31-55) | +0.58 | -1.29 | -81 |  |
| (3.632, 18.762] | 63 | 30% (20-42) | -2.45 | -4.38 | -276 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0971] | 64 | 45% (34-57) | +0.38 | -0.38 | -24 |  |
| (0.0971, 0.145] | 63 | 40% (29-52) | -1.12 | -2.40 | -151 |  |
| (0.145, 0.392] | 63 | 27% (18-39) | -1.79 | -5.31 | -335 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.53] | 22 | 32% (16-53) | -2.43 | -3.31 | -73 |  |
| (-0.53, 0.474] | 21 | 48% (28-68) | -0.37 | -0.89 | -19 |  |
| (0.474, 5.305] | 21 | 62% (41-79) | +0.09 | -0.62 | -13 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.486] | 24 | 42% (24-61) | -0.85 | -1.54 | -37 |  |
| (0.486, 0.694] | 24 | 50% (31-69) | -0.93 | -1.63 | -39 |  |
| (0.694, 1.74] | 23 | 48% (29-67) | -1.58 | -2.39 | -55 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.779] | 24 | 50% (31-69) | -0.78 | -1.24 | -30 |  |
| (0.779, 1.196] | 23 | 39% (22-59) | -1.54 | -2.35 | -54 |  |
| (1.196, 3.566] | 24 | 50% (31-69) | -1.03 | -1.97 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.348] | 24 | 38% (21-57) | -1.21 | -1.81 | -43 |  |
| (0.348, 0.552] | 23 | 65% (45-81) | +0.34 | -0.36 | -8 | ▲ |
| (0.552, 1.21] | 24 | 38% (21-57) | -2.41 | -3.30 | -79 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 8% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 86, trail_stop 73, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0971] | 64 | 33% | 28% | 38% |
| (0.0971, 0.145] | 63 | 49% | 44% | 5% |
| (0.145, 0.392] | 63 | 54% | 43% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
