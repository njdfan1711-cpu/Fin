# Scalp signal analysis (fixed exits)

_250 tagged trades, 28 trading days (2026-10-01 to 2026-11-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 250 | 41% (35-47) | +0.23 | -1.35 | -338 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 44 | -2 | -0.05 | 206 | -336 | -1.63 | +2 |
| skip first 30 min | 2 | -8 | -4.06 | 248 | -330 | -1.33 | +8 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 151 | -239 | -1.58 | +99 |
| skip when SPY is below its VWAP | 112 | -178 | -1.59 | 138 | -160 | -1.16 | +178 |
| skip when SPY fell over the last 15 min | 91 | -136 | -1.50 | 159 | -201 | -1.27 | +136 |
| skip over-extended (30-min run in top quarter, > 0.51%) | 62 | -174 | -2.80 | 188 | -164 | -0.87 | +174 |
| skip stock not beating SPY over 15 min | 41 | -32 | -0.79 | 209 | -306 | -1.46 | +32 |
| skip afternoon entries (2:00-3:45 PM) | 54 | -224 | -4.15 | 196 | -114 | -0.58 | +224 |
| skip volume spikes above 5x average | 48 | -117 | -2.44 | 202 | -221 | -1.09 | +117 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 224 | -331 | -1.48 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 33 | -12 | -0.36 | 217 | -326 | -1.50 | +12 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 121 | -305 | -2.52 | 129 | -33 | -0.25 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 36 | 53% (37-68) | +2.11 | +0.38 | +14 |  |
| 60-240 | 100 | 40% (31-50) | +0.17 | -1.17 | -117 |  |
| 240-375 | 70 | 30% (21-42) | -1.48 | -3.31 | -232 |  |
| 375-390 | 44 | 50% (36-64) | +1.54 | -0.05 | -2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 67 | 33% (23-45) | -0.43 | -1.75 | -118 |  |
| > 0.2 | 84 | 43% (33-54) | +0.18 | -1.44 | -121 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 112 | 41% (32-50) | +0.08 | -1.59 | -178 |  |
| above VWAP | 138 | 41% (33-49) | +0.35 | -1.16 | -160 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 84 | 42% (32-52) | +0.37 | -0.88 | -74 |  |
| (0.133, 0.382] | 83 | 46% (35-56) | +0.57 | -1.01 | -84 |  |
| (0.382, 5.591] | 83 | 35% (26-46) | -0.26 | -2.17 | -180 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.108] | 83 | 46% (35-56) | +0.79 | -0.41 | -34 |  |
| (0.108, 0.433] | 82 | 41% (31-52) | +0.53 | -1.35 | -111 |  |
| (0.433, 4.846] | 83 | 36% (27-47) | -0.54 | -2.23 | -185 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.379] | 84 | 45% (35-56) | +0.73 | -1.06 | -89 |  |
| (-0.379, 0.394] | 83 | 46% (35-56) | +1.09 | -0.04 | -4 |  |
| (0.394, 4.204] | 83 | 31% (22-42) | -1.14 | -2.95 | -245 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 84 | 42% (32-52) | +0.01 | -1.39 | -117 |  |
| (0.056, 0.127] | 84 | 45% (35-56) | +0.65 | -0.83 | -70 |  |
| (0.127, 0.924] | 82 | 35% (26-46) | +0.02 | -1.85 | -152 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 84 | 43% (33-54) | +0.25 | -0.84 | -70 |  |
| (0.212, 0.335] | 83 | 43% (33-54) | +0.62 | -1.22 | -101 |  |
| (0.335, 2.663] | 83 | 36% (27-47) | -0.18 | -2.01 | -166 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.318] | 84 | 37% (27-48) | -0.00 | -1.50 | -126 |  |
| (2.318, 3.632] | 83 | 49% (39-60) | +1.04 | -0.58 | -48 |  |
| (3.632, 18.762] | 83 | 36% (27-47) | -0.35 | -1.98 | -164 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.102] | 85 | 46% (36-56) | +0.39 | -0.39 | -33 |  |
| (0.102, 0.16] | 82 | 38% (28-49) | -0.02 | -1.21 | -99 |  |
| (0.16, 0.76] | 83 | 39% (29-49) | +0.31 | -2.47 | -205 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.974] | 42 | 33% (21-48) | -0.78 | -1.59 | -67 |  |
| (-0.974, 0.613] | 41 | 51% (36-66) | +1.44 | +0.85 | +35 |  |
| (0.613, 7.522] | 41 | 49% (34-64) | +1.28 | +0.55 | +22 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.536] | 44 | 43% (30-58) | +0.00 | -0.64 | -28 |  |
| (0.536, 0.835] | 43 | 44% (30-59) | +0.53 | -0.18 | -8 |  |
| (0.835, 3.799] | 44 | 43% (30-58) | +0.88 | +0.03 | +1 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.832] | 44 | 43% (30-58) | +0.25 | -0.32 | -14 |  |
| (0.832, 1.463] | 43 | 44% (30-59) | +0.80 | +0.09 | +4 |  |
| (1.463, 9.058] | 44 | 43% (30-58) | +0.37 | -0.54 | -24 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.375] | 44 | 43% (30-58) | +0.22 | -0.34 | -15 |  |
| (0.375, 0.594] | 43 | 44% (30-59) | +0.56 | -0.19 | -8 |  |
| (0.594, 4.001] | 44 | 43% (30-58) | +0.63 | -0.24 | -11 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.19%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 120, target 66, time_stop 51, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.102] | 85 | 35% | 16% | 41% |
| (0.102, 0.16] | 82 | 54% | 28% | 12% |
| (0.16, 0.76] | 83 | 55% | 35% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
