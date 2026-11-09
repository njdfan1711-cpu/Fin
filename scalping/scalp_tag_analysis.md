# Scalp signal analysis (fixed exits)

_247 tagged trades, 27 trading days (2026-10-01 to 2026-11-06). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 247 | 41% (35-47) | +0.23 | -1.36 | -335 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +3 | +0.07 | 204 | -338 | -1.66 | -3 |
| skip first 30 min | 2 | -8 | -4.06 | 245 | -327 | -1.34 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 148 | -236 | -1.59 | +99 |
| skip when SPY is below its VWAP | 111 | -173 | -1.56 | 136 | -162 | -1.19 | +173 |
| skip when SPY fell over the last 15 min | 90 | -131 | -1.46 | 157 | -204 | -1.30 | +131 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 61 | -166 | -2.72 | 186 | -169 | -0.91 | +166 |
| skip stock not beating SPY over 15 min | 39 | -36 | -0.92 | 208 | -299 | -1.44 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 54 | -224 | -4.15 | 193 | -111 | -0.58 | +224 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 199 | -218 | -1.10 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 221 | -329 | -1.49 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 32 | -5 | -0.15 | 215 | -330 | -1.54 | +5 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 119 | -309 | -2.60 | 128 | -26 | -0.21 | +309 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 53% (37-69) | +2.10 | +0.32 | +11 |  |
| 60-240 | 100 | 40% (31-50) | +0.17 | -1.17 | -117 |  |
| 240-375 | 70 | 30% (21-42) | -1.48 | -3.31 | -232 |  |
| 375-390 | 43 | 51% (37-65) | +1.67 | +0.07 | +3 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 66 | 33% (23-45) | -0.38 | -1.70 | -112 |  |
| > 0.2 | 82 | 43% (33-53) | +0.13 | -1.51 | -124 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 111 | 41% (33-51) | +0.12 | -1.56 | -173 |  |
| above VWAP | 136 | 40% (33-49) | +0.32 | -1.19 | -162 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 83 | 41% (31-52) | +0.23 | -1.12 | -93 |  |
| (0.136, 0.383] | 82 | 46% (36-57) | +0.65 | -0.84 | -69 |  |
| (0.383, 5.591] | 82 | 35% (26-46) | -0.19 | -2.12 | -174 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.112] | 82 | 48% (37-58) | +0.95 | -0.26 | -21 |  |
| (0.112, 0.44] | 81 | 40% (30-50) | +0.31 | -1.58 | -128 |  |
| (0.44, 4.846] | 82 | 37% (27-47) | -0.48 | -2.18 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.386] | 83 | 46% (35-56) | +0.77 | -1.04 | -86 |  |
| (-0.386, 0.394] | 82 | 45% (35-56) | +1.01 | -0.11 | -9 |  |
| (0.394, 4.204] | 82 | 32% (23-42) | -1.11 | -2.93 | -240 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 83 | 41% (31-52) | -0.12 | -1.51 | -126 |  |
| (0.056, 0.127] | 83 | 46% (35-56) | +0.71 | -0.77 | -64 |  |
| (0.127, 0.924] | 81 | 36% (26-47) | +0.10 | -1.80 | -145 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 83 | 43% (33-54) | +0.32 | -0.77 | -64 |  |
| (0.212, 0.332] | 82 | 43% (33-53) | +0.48 | -1.36 | -112 |  |
| (0.332, 2.663] | 82 | 37% (27-47) | -0.11 | -1.95 | -160 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.347] | 83 | 39% (29-49) | +0.15 | -1.37 | -113 |  |
| (2.347, 3.637] | 82 | 49% (38-59) | +0.93 | -0.68 | -56 |  |
| (3.637, 18.762] | 82 | 35% (26-46) | -0.38 | -2.03 | -166 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.101] | 83 | 47% (37-58) | +0.53 | -0.23 | -19 |  |
| (0.101, 0.156] | 82 | 37% (27-47) | -0.24 | -1.39 | -114 |  |
| (0.156, 0.76] | 82 | 39% (29-50) | +0.39 | -2.46 | -202 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.078] | 41 | 34% (22-49) | -0.66 | -1.47 | -60 |  |
| (-1.078, 0.577] | 40 | 50% (35-65) | +1.07 | +0.50 | +20 |  |
| (0.577, 7.522] | 40 | 50% (35-65) | +1.57 | +0.84 | +34 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 44 | 43% (30-58) | +0.00 | -0.64 | -28 |  |
| (0.533, 0.832] | 42 | 45% (31-60) | +0.64 | -0.05 | -2 |  |
| (0.832, 3.799] | 42 | 43% (29-58) | +0.82 | -0.03 | -1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.844] | 43 | 44% (30-59) | +0.30 | -0.25 | -11 |  |
| (0.844, 1.463] | 42 | 43% (29-58) | +0.66 | -0.06 | -2 |  |
| (1.463, 9.058] | 43 | 44% (30-59) | +0.47 | -0.43 | -18 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.375] | 43 | 44% (30-59) | +0.33 | -0.23 | -10 |  |
| (0.375, 0.598] | 42 | 45% (31-60) | +0.68 | -0.07 | -3 |  |
| (0.598, 4.001] | 43 | 42% (28-57) | +0.44 | -0.44 | -19 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 119, target 65, time_stop 51, eod 12

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.101] | 83 | 34% | 17% | 42% |
| (0.101, 0.156] | 82 | 56% | 27% | 12% |
| (0.156, 0.76] | 82 | 55% | 35% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
