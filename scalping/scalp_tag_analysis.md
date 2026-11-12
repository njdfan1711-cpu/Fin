# Scalp signal analysis (fixed exits)

_261 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 261 | 40% (34-46) | +0.11 | -1.44 | -375 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -21 | -0.45 | 214 | -354 | -1.65 | +21 |
| skip first 30 min | 3 | -15 | -4.90 | 258 | -360 | -1.40 | +15 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 162 | -276 | -1.70 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 149 | -197 | -1.32 | +178 |
| skip when SPY fell over the last 15 min | 94 | -132 | -1.40 | 167 | -243 | -1.46 | +132 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 65 | -180 | -2.78 | 196 | -195 | -0.99 | +180 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 219 | -335 | -1.53 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 203 | -160 | -0.79 | +215 |
| skip volume spikes above 5x average | 49 | -124 | -2.53 | 212 | -251 | -1.18 | +124 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 235 | -368 | -1.57 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 36 | -31 | -0.87 | 225 | -344 | -1.53 | +31 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 137 | -49 | -0.35 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 103 | 39% (30-48) | -0.01 | -1.34 | -138 |  |
| 240-375 | 74 | 32% (23-44) | -1.24 | -3.01 | -222 |  |
| 375-390 | 47 | 47% (33-61) | +1.07 | -0.45 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 94 | 41% (32-52) | -0.09 | -1.61 | -151 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 149 | 40% (32-48) | +0.13 | -1.32 | -197 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 87 | 40% (31-51) | +0.15 | -1.09 | -94 |  |
| (0.133, 0.379] | 87 | 45% (35-55) | +0.38 | -1.17 | -102 |  |
| (0.379, 5.591] | 87 | 36% (26-46) | -0.21 | -2.06 | -179 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.114] | 86 | 47% (36-57) | +0.75 | -0.43 | -37 |  |
| (0.114, 0.44] | 86 | 41% (31-51) | +0.50 | -1.34 | -115 |  |
| (0.44, 4.846] | 86 | 35% (26-45) | -0.77 | -2.42 | -208 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 87 | 44% (34-54) | +0.56 | -1.19 | -103 |  |
| (-0.367, 0.396] | 87 | 45% (35-55) | +0.85 | -0.28 | -24 |  |
| (0.396, 5.005] | 87 | 32% (23-43) | -1.09 | -2.84 | -248 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 87 | 41% (32-52) | -0.06 | -1.44 | -125 |  |
| (0.0561, 0.126] | 87 | 45% (35-55) | +0.56 | -0.90 | -78 |  |
| (0.126, 0.924] | 87 | 34% (25-45) | -0.18 | -1.98 | -172 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.215] | 87 | 44% (34-54) | +0.34 | -0.73 | -64 |  |
| (0.215, 0.336] | 87 | 41% (32-52) | +0.32 | -1.47 | -128 |  |
| (0.336, 2.663] | 87 | 36% (26-46) | -0.34 | -2.11 | -183 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.344] | 87 | 37% (27-47) | -0.11 | -1.58 | -138 |  |
| (2.344, 3.538] | 87 | 48% (38-59) | +0.94 | -0.64 | -55 |  |
| (3.538, 18.762] | 87 | 36% (26-46) | -0.51 | -2.09 | -182 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 87 | 47% (37-58) | +0.55 | -0.23 | -20 |  |
| (0.103, 0.161] | 87 | 36% (26-46) | -0.36 | -1.54 | -134 |  |
| (0.161, 0.76] | 87 | 38% (28-48) | +0.13 | -2.55 | -222 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 45 | 33% (21-48) | -0.85 | -1.65 | -74 |  |
| (-0.938, 0.615] | 45 | 49% (35-63) | +1.12 | +0.52 | +23 |  |
| (0.615, 7.522] | 45 | 47% (33-61) | +0.84 | +0.10 | +4 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 48 | 46% (33-60) | +0.40 | -0.25 | -12 |  |
| (0.541, 0.837] | 49 | 41% (28-55) | -0.09 | -0.79 | -39 |  |
| (0.837, 3.799] | 45 | 40% (27-55) | +0.39 | -0.46 | -21 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.828] | 48 | 44% (31-58) | +0.29 | -0.30 | -14 |  |
| (0.828, 1.493] | 47 | 43% (30-57) | +0.41 | -0.30 | -14 |  |
| (1.493, 9.058] | 47 | 40% (28-55) | -0.02 | -0.91 | -43 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.374] | 48 | 42% (29-56) | +0.03 | -0.55 | -27 |  |
| (0.374, 0.594] | 47 | 45% (31-59) | +0.44 | -0.31 | -15 |  |
| (0.594, 4.001] | 47 | 40% (28-55) | +0.22 | -0.64 | -30 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.20%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 3% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 128, target 67, time_stop 53, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 87 | 34% | 17% | 41% |
| (0.103, 0.161] | 87 | 56% | 26% | 11% |
| (0.161, 0.76] | 87 | 56% | 33% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
