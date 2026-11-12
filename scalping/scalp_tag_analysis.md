# Scalp signal analysis (fixed exits)

_266 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 266 | 41% (35-47) | +0.19 | -1.33 | -355 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 47 | -21 | -0.45 | 219 | -334 | -1.52 | +21 |
| skip first 30 min | 3 | -15 | -4.90 | 263 | -340 | -1.29 | +15 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 167 | -256 | -1.53 | +99 |
| skip when SPY is below its VWAP | 114 | -168 | -1.47 | 152 | -187 | -1.23 | +168 |
| skip when SPY fell over the last 15 min | 96 | -121 | -1.27 | 170 | -234 | -1.37 | +121 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 66 | -171 | -2.59 | 200 | -184 | -0.92 | +171 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 224 | -315 | -1.41 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 59 | -206 | -3.49 | 207 | -149 | -0.72 | +206 |
| skip volume spikes above 5x average | 52 | -104 | -2.01 | 214 | -251 | -1.17 | +104 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 240 | -348 | -1.45 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 37 | -22 | -0.60 | 229 | -333 | -1.45 | +22 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 142 | -29 | -0.20 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 107 | 40% (31-50) | +0.11 | -1.19 | -127 |  |
| 240-375 | 75 | 33% (24-45) | -1.09 | -2.84 | -213 |  |
| 375-390 | 47 | 47% (33-61) | +1.07 | -0.45 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 99 | 43% (34-53) | +0.14 | -1.32 | -131 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 114 | 42% (33-51) | +0.18 | -1.47 | -168 |  |
| above VWAP | 152 | 40% (33-48) | +0.20 | -1.23 | -187 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 89 | 40% (31-51) | +0.18 | -1.03 | -92 |  |
| (0.133, 0.38] | 88 | 45% (35-56) | +0.46 | -1.07 | -94 |  |
| (0.38, 5.591] | 89 | 37% (28-47) | -0.08 | -1.90 | -169 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.118] | 88 | 47% (37-57) | +0.78 | -0.41 | -36 |  |
| (0.118, 0.44] | 87 | 43% (33-53) | +0.67 | -1.13 | -98 |  |
| (0.44, 4.846] | 88 | 35% (26-46) | -0.71 | -2.34 | -206 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 89 | 45% (35-55) | +0.65 | -1.07 | -95 |  |
| (-0.367, 0.401] | 88 | 45% (35-56) | +0.96 | -0.16 | -15 |  |
| (0.401, 5.005] | 89 | 33% (24-43) | -1.03 | -2.76 | -246 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 89 | 42% (32-52) | -0.04 | -1.40 | -124 |  |
| (0.056, 0.127] | 88 | 45% (35-56) | +0.66 | -0.78 | -69 |  |
| (0.127, 0.924] | 89 | 36% (27-46) | -0.05 | -1.82 | -162 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.216] | 89 | 44% (34-54) | +0.30 | -0.76 | -68 |  |
| (0.216, 0.337] | 88 | 42% (32-52) | +0.47 | -1.29 | -114 |  |
| (0.337, 2.663] | 89 | 37% (28-47) | -0.20 | -1.94 | -173 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.353] | 89 | 38% (29-49) | +0.03 | -1.44 | -128 |  |
| (2.353, 3.611] | 88 | 47% (37-57) | +0.73 | -0.81 | -71 |  |
| (3.611, 18.762] | 89 | 38% (29-49) | -0.19 | -1.75 | -156 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 89 | 48% (38-59) | +0.64 | -0.13 | -11 |  |
| (0.103, 0.161] | 88 | 35% (26-46) | -0.42 | -1.59 | -140 |  |
| (0.161, 0.76] | 89 | 39% (30-50) | +0.34 | -2.29 | -203 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.956] | 47 | 36% (24-50) | -0.41 | -1.20 | -56 |  |
| (-0.956, 0.601] | 46 | 52% (38-66) | +1.30 | +0.70 | +32 |  |
| (0.601, 7.522] | 47 | 45% (31-59) | +0.68 | -0.05 | -3 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.538] | 49 | 47% (34-61) | +0.37 | -0.27 | -13 |  |
| (0.538, 0.834] | 49 | 41% (28-55) | +0.05 | -0.64 | -32 |  |
| (0.834, 3.799] | 49 | 43% (30-57) | +0.69 | -0.13 | -6 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.846] | 49 | 45% (32-59) | +0.42 | -0.17 | -8 |  |
| (0.846, 1.46] | 49 | 45% (32-59) | +0.78 | +0.08 | +4 |  |
| (1.46, 9.058] | 49 | 41% (28-55) | -0.09 | -0.96 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.38] | 49 | 43% (30-57) | +0.17 | -0.41 | -20 |  |
| (0.38, 0.589] | 49 | 47% (34-61) | +0.61 | -0.13 | -6 |  |
| (0.589, 4.001] | 49 | 41% (28-55) | +0.33 | -0.51 | -25 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.19%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 129, target 69, time_stop 55, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 89 | 34% | 17% | 43% |
| (0.103, 0.161] | 88 | 57% | 26% | 11% |
| (0.161, 0.76] | 89 | 55% | 35% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
