# Scalp signal analysis (trail exits)

_261 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 261 | 42% (36-48) | -0.67 | -2.21 | -577 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -12 | -0.26 | 214 | -565 | -2.64 | +12 |
| skip first 30 min | 3 | -10 | -3.32 | 258 | -567 | -2.20 | +10 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 162 | -309 | -1.91 | +268 |
| skip when SPY is below its VWAP | 112 | -326 | -2.91 | 149 | -251 | -1.68 | +326 |
| skip when SPY fell over the last 15 min | 95 | -205 | -2.16 | 166 | -372 | -2.24 | +205 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 65 | -221 | -3.40 | 196 | -356 | -1.82 | +221 |
| skip stock not beating SPY over 15 min | 42 | -93 | -2.20 | 219 | -485 | -2.21 | +93 |
| skip afternoon entries (2:00-3:45 PM) | 58 | -215 | -3.71 | 203 | -362 | -1.78 | +215 |
| skip volume spikes above 5x average | 49 | -174 | -3.55 | 212 | -403 | -1.90 | +174 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 235 | -536 | -2.28 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 36 | -57 | -1.59 | 225 | -520 | -2.31 | +57 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -416 | -3.35 | 137 | -162 | -1.18 | +416 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 49% (33-64) | -0.33 | -2.03 | -75 |  |
| 60-240 | 103 | 39% (30-48) | -1.06 | -2.40 | -247 |  |
| 240-375 | 74 | 41% (30-52) | -1.51 | -3.28 | -243 |  |
| 375-390 | 47 | 47% (33-61) | +1.25 | -0.26 | -12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 68 | 35% (25-47) | -1.54 | -2.86 | -195 |  |
| > 0.2 | 94 | 48% (38-58) | +0.30 | -1.21 | -114 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 37% (28-46) | -1.25 | -2.91 | -326 |  |
| above VWAP | 149 | 46% (38-54) | -0.23 | -1.68 | -251 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 87 | 40% (31-51) | -0.24 | -1.48 | -128 |  |
| (0.133, 0.379] | 87 | 53% (42-63) | -0.18 | -1.73 | -150 | ▲ |
| (0.379, 5.591] | 87 | 33% (24-44) | -1.58 | -3.43 | -298 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.114] | 86 | 49% (39-59) | +0.43 | -0.76 | -65 |  |
| (0.114, 0.44] | 86 | 41% (31-51) | -1.02 | -2.85 | -245 |  |
| (0.44, 4.846] | 86 | 37% (28-48) | -1.34 | -2.99 | -257 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 87 | 45% (35-55) | -0.86 | -2.60 | -226 |  |
| (-0.367, 0.396] | 87 | 47% (37-58) | +0.47 | -0.66 | -57 |  |
| (0.396, 5.005] | 87 | 34% (25-45) | -1.62 | -3.38 | -294 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 87 | 44% (34-54) | -0.88 | -2.26 | -196 |  |
| (0.0561, 0.126] | 87 | 44% (34-54) | +0.11 | -1.35 | -117 |  |
| (0.126, 0.924] | 87 | 39% (29-50) | -1.23 | -3.03 | -264 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.215] | 87 | 45% (35-55) | +0.15 | -0.92 | -80 |  |
| (0.215, 0.336] | 87 | 45% (35-55) | -0.73 | -2.52 | -219 |  |
| (0.336, 2.663] | 87 | 37% (27-47) | -1.42 | -3.19 | -278 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.344] | 87 | 41% (32-52) | -0.64 | -2.11 | -183 |  |
| (2.344, 3.538] | 87 | 49% (39-60) | +0.60 | -0.98 | -85 |  |
| (3.538, 18.762] | 87 | 36% (26-46) | -1.96 | -3.55 | -309 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 87 | 48% (38-59) | +0.36 | -0.42 | -37 |  |
| (0.103, 0.161] | 87 | 41% (32-52) | -1.20 | -2.38 | -207 |  |
| (0.161, 0.76] | 87 | 37% (27-47) | -1.16 | -3.83 | -334 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 45 | 42% (29-57) | -1.40 | -2.20 | -99 |  |
| (-0.938, 0.615] | 45 | 53% (39-67) | +0.02 | -0.59 | -26 |  |
| (0.615, 7.522] | 45 | 58% (43-71) | -0.29 | -1.03 | -46 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 48 | 50% (36-64) | -0.38 | -1.04 | -50 |  |
| (0.541, 0.837] | 49 | 53% (39-66) | -1.07 | -1.77 | -87 |  |
| (0.837, 3.799] | 45 | 49% (35-63) | -0.53 | -1.37 | -62 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.828] | 48 | 48% (34-62) | -1.26 | -1.85 | -89 |  |
| (0.828, 1.493] | 47 | 53% (39-67) | -0.35 | -1.06 | -50 |  |
| (1.493, 9.058] | 47 | 51% (37-65) | -0.38 | -1.27 | -60 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.374] | 48 | 46% (33-60) | -0.78 | -1.36 | -65 |  |
| (0.374, 0.594] | 47 | 60% (45-72) | -0.44 | -1.20 | -56 | ▲ |
| (0.594, 4.001] | 47 | 47% (33-61) | -0.78 | -1.63 | -77 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 114, trail_stop 109, time_stop 30, eod 8

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 87 | 31% | 33% | 30% |
| (0.103, 0.161] | 87 | 51% | 45% | 2% |
| (0.161, 0.76] | 87 | 49% | 47% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
