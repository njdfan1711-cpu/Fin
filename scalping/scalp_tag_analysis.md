# Scalp signal analysis (fixed exits)

_258 tagged trades, 30 trading days (2026-10-01 to 2026-11-11). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 258 | 40% (35-46) | +0.14 | -1.41 | -364 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 46 | -15 | -0.32 | 212 | -349 | -1.65 | +15 |
| skip first 30 min | 2 | -8 | -4.06 | 256 | -356 | -1.39 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 159 | -265 | -1.67 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 146 | -186 | -1.28 | +178 |
| skip when SPY fell over the last 15 min | 93 | -134 | -1.44 | 165 | -230 | -1.39 | +134 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 64 | -174 | -2.71 | 194 | -191 | -0.98 | +174 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 216 | -325 | -1.50 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 57 | -217 | -3.81 | 201 | -147 | -0.73 | +217 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 210 | -247 | -1.18 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 232 | -358 | -1.54 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 35 | -25 | -0.70 | 223 | -340 | -1.52 | +25 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 134 | -38 | -0.28 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 103 | 39% (30-48) | -0.01 | -1.34 | -138 |  |
| 240-375 | 73 | 32% (22-43) | -1.29 | -3.08 | -225 |  |
| 375-390 | 46 | 48% (34-62) | +1.22 | -0.32 | -15 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 91 | 42% (32-52) | +0.01 | -1.54 | -140 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 146 | 40% (32-48) | +0.19 | -1.28 | -186 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 86 | 41% (31-51) | +0.22 | -1.12 | -96 |  |
| (0.136, 0.382] | 86 | 45% (35-56) | +0.52 | -0.94 | -81 |  |
| (0.382, 5.591] | 86 | 35% (26-45) | -0.31 | -2.18 | -187 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.119] | 86 | 47% (36-57) | +0.75 | -0.46 | -39 |  |
| (0.119, 0.44] | 85 | 40% (30-51) | +0.47 | -1.45 | -123 |  |
| (0.44, 4.846] | 85 | 35% (26-46) | -0.71 | -2.28 | -193 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.371] | 86 | 44% (34-55) | +0.58 | -1.18 | -101 |  |
| (-0.371, 0.388] | 86 | 44% (34-55) | +0.80 | -0.34 | -29 |  |
| (0.388, 5.005] | 86 | 33% (24-43) | -0.95 | -2.72 | -234 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0559] | 86 | 41% (31-51) | -0.10 | -1.48 | -127 |  |
| (0.0559, 0.126] | 86 | 47% (36-57) | +0.74 | -0.73 | -62 |  |
| (0.126, 0.924] | 86 | 34% (25-44) | -0.21 | -2.03 | -174 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.213] | 86 | 43% (33-54) | +0.28 | -0.80 | -69 |  |
| (0.213, 0.333] | 86 | 42% (32-52) | +0.34 | -1.46 | -125 |  |
| (0.333, 2.663] | 86 | 36% (27-47) | -0.19 | -1.98 | -170 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.331] | 86 | 36% (27-47) | -0.14 | -1.62 | -140 |  |
| (2.331, 3.538] | 86 | 49% (39-59) | +1.01 | -0.57 | -49 |  |
| (3.538, 18.762] | 86 | 36% (27-47) | -0.44 | -2.04 | -175 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 87 | 47% (37-58) | +0.55 | -0.23 | -20 |  |
| (0.102, 0.16] | 85 | 36% (27-47) | -0.23 | -1.42 | -120 |  |
| (0.16, 0.76] | 86 | 37% (28-48) | +0.10 | -2.61 | -224 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.008] | 44 | 34% (22-49) | -0.74 | -1.54 | -68 |  |
| (-1.008, 0.589] | 44 | 50% (36-64) | +1.15 | +0.54 | +24 |  |
| (0.589, 7.522] | 44 | 45% (32-60) | +0.93 | +0.18 | +8 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 47 | 45% (31-59) | +0.20 | -0.46 | -22 |  |
| (0.533, 0.832] | 46 | 41% (28-56) | +0.11 | -0.60 | -28 |  |
| (0.832, 3.799] | 46 | 41% (28-56) | +0.59 | -0.25 | -11 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.828] | 47 | 45% (31-59) | +0.42 | -0.17 | -8 |  |
| (0.828, 1.467] | 46 | 43% (30-58) | +0.54 | -0.17 | -8 |  |
| (1.467, 9.058] | 46 | 39% (26-54) | -0.08 | -0.97 | -45 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.374] | 47 | 43% (30-57) | +0.15 | -0.43 | -20 |  |
| (0.374, 0.594] | 46 | 46% (32-60) | +0.71 | -0.05 | -2 |  |
| (0.594, 4.001] | 46 | 39% (26-54) | +0.03 | -0.83 | -38 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 3% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 126, target 67, time_stop 52, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 87 | 34% | 17% | 41% |
| (0.102, 0.16] | 85 | 55% | 27% | 12% |
| (0.16, 0.76] | 86 | 57% | 34% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
