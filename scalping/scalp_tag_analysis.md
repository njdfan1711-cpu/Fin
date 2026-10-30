# Scalp signal analysis (fixed exits)

_200 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 200 | 40% (33-46) | +0.05 | -1.74 | -349 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 29 | -3 | -0.10 | 171 | -346 | -2.02 | +3 |
| skip first 30 min | 1 | -6 | -6.31 | 199 | -342 | -1.72 | +6 |
| skip when SPY is down on the day | 81 | -110 | -1.36 | 119 | -238 | -2.00 | +110 |
| skip when SPY is below its VWAP | 84 | -173 | -2.06 | 116 | -175 | -1.51 | +173 |
| skip when SPY fell over the last 15 min | 76 | -120 | -1.58 | 124 | -228 | -1.84 | +120 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 50 | -164 | -3.28 | 150 | -185 | -1.23 | +164 |
| skip stock not beating SPY over 15 min | 33 | -26 | -0.79 | 167 | -323 | -1.93 | +26 |
| skip afternoon entries (2:00-3:45 PM) | 43 | -205 | -4.77 | 157 | -144 | -0.92 | +205 |
| skip volume spikes above 5x average | 38 | -167 | -4.39 | 162 | -182 | -1.12 | +167 |
| skip when the stop is inside normal noise (range > stop) | 11 | -28 | -2.58 | 189 | -320 | -1.69 | +28 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 20 | -32 | -1.62 | 180 | -316 | -1.76 | +32 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 106 | -291 | -2.75 | 94 | -58 | -0.61 | +291 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 29 | 59% (41-74) | +2.81 | +0.83 | +24 | ▲ |
| 60-240 | 85 | 36% (27-47) | -0.37 | -1.86 | -159 |  |
| 240-375 | 57 | 30% (20-43) | -1.65 | -3.71 | -211 |  |
| 375-390 | 29 | 48% (31-66) | +1.87 | -0.10 | -3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 30 | 47% (30-64) | +1.11 | -0.43 | -13 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 61 | 36% (25-49) | +0.00 | -1.37 | -84 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 84 | 39% (30-50) | -0.10 | -2.06 | -173 |  |
| above VWAP | 116 | 40% (31-49) | +0.15 | -1.51 | -175 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 67 | 39% (28-51) | +0.05 | -1.34 | -90 |  |
| (0.133, 0.372] | 66 | 42% (31-54) | +0.01 | -1.78 | -118 |  |
| (0.372, 1.555] | 67 | 37% (27-49) | +0.08 | -2.11 | -141 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.116] | 67 | 42% (31-54) | +0.25 | -1.14 | -77 |  |
| (0.116, 0.403] | 66 | 44% (33-56) | +0.88 | -1.12 | -74 |  |
| (0.403, 1.281] | 66 | 33% (23-45) | -0.90 | -2.91 | -192 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.346] | 67 | 40% (29-52) | +0.13 | -1.94 | -130 |  |
| (-0.346, 0.34] | 66 | 44% (33-56) | +0.94 | -0.29 | -19 |  |
| (0.34, 2.726] | 67 | 34% (24-46) | -0.92 | -2.99 | -200 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 67 | 40% (29-52) | -0.19 | -1.75 | -117 |  |
| (0.0521, 0.122] | 66 | 47% (35-59) | +1.00 | -0.60 | -40 |  |
| (0.122, 0.678] | 67 | 31% (22-43) | -0.65 | -2.86 | -192 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.204] | 67 | 45% (33-57) | +0.23 | -0.96 | -64 |  |
| (0.204, 0.311] | 66 | 38% (27-50) | +0.11 | -1.83 | -121 |  |
| (0.311, 0.875] | 67 | 36% (25-48) | -0.20 | -2.45 | -164 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 67 | 40% (29-52) | +0.45 | -1.26 | -84 |  |
| (2.389, 3.635] | 66 | 48% (37-60) | +1.04 | -0.75 | -50 |  |
| (3.635, 18.762] | 67 | 30% (20-42) | -1.33 | -3.20 | -215 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0972] | 67 | 48% (36-60) | +0.53 | -0.22 | -15 |  |
| (0.0972, 0.145] | 67 | 39% (28-51) | +0.37 | -0.88 | -59 |  |
| (0.145, 0.392] | 66 | 32% (22-44) | -0.76 | -4.17 | -275 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.941000000000001, -0.719] | 25 | 24% (11-43) | -2.07 | -2.95 | -74 |  |
| (-0.719, 0.444] | 25 | 44% (27-63) | +0.52 | +0.00 | +0 |  |
| (0.444, 5.305] | 24 | 62% (43-79) | +2.93 | +2.22 | +53 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.487] | 27 | 44% (28-63) | +0.12 | -0.55 | -15 |  |
| (0.487, 0.702] | 27 | 44% (28-63) | +0.87 | +0.20 | +5 |  |
| (0.702, 1.74] | 27 | 37% (22-56) | -0.47 | -1.32 | -36 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.784] | 27 | 52% (34-69) | +1.21 | +0.74 | +20 |  |
| (0.784, 1.203] | 27 | 37% (22-56) | +0.19 | -0.60 | -16 |  |
| (1.203, 3.566] | 27 | 37% (22-56) | -0.87 | -1.80 | -49 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.342] | 27 | 44% (28-63) | +0.66 | +0.08 | +2 |  |
| (0.342, 0.551] | 27 | 41% (25-59) | -0.14 | -0.88 | -24 |  |
| (0.551, 1.21] | 27 | 41% (25-59) | +0.00 | -0.87 | -24 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 99, target 51, time_stop 46, eod 4

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0972] | 67 | 33% | 16% | 48% |
| (0.0972, 0.145] | 67 | 54% | 33% | 10% |
| (0.145, 0.392] | 66 | 62% | 27% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
