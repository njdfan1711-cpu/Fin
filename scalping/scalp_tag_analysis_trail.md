# Scalp signal analysis (trail exits)

_247 tagged trades, 27 trading days (2026-10-01 to 2026-11-06). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 247 | 42% (36-48) | -0.65 | -2.23 | -552 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 43 | +2 | +0.05 | 204 | -554 | -2.72 | -2 |
| skip first 30 min | 2 | -3 | -1.70 | 245 | -549 | -2.24 | +3 |
| skip when SPY is down on the day | 99 | -268 | -2.71 | 148 | -283 | -1.92 | +268 |
| skip when SPY is below its VWAP | 111 | -321 | -2.89 | 136 | -231 | -1.70 | +321 |
| skip when SPY fell over the last 15 min | 91 | -197 | -2.17 | 156 | -355 | -2.27 | +197 |
| skip over-extended (30-min run in top quarter, > 0.52%) | 61 | -225 | -3.68 | 186 | -327 | -1.76 | +225 |
| skip stock not beating SPY over 15 min | 39 | -82 | -2.10 | 208 | -470 | -2.26 | +82 |
| skip afternoon entries (2:00-3:45 PM) | 54 | -228 | -4.21 | 193 | -324 | -1.68 | +228 |
| skip volume spikes above 5x average | 48 | -167 | -3.48 | 199 | -385 | -1.93 | +167 |
| skip when the stop is inside normal noise (range > stop) | 26 | -41 | -1.57 | 221 | -511 | -2.31 | +41 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.69%) | 32 | -49 | -1.52 | 215 | -503 | -2.34 | +49 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 119 | -410 | -3.45 | 128 | -142 | -1.11 | +410 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 34 | 50% (34-66) | -0.11 | -1.89 | -64 |  |
| 60-240 | 100 | 39% (30-49) | -1.00 | -2.34 | -234 |  |
| 240-375 | 70 | 37% (27-49) | -1.82 | -3.65 | -256 |  |
| 375-390 | 43 | 49% (35-63) | +1.65 | +0.05 | +2 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 46% (33-60) | -0.50 | -1.76 | -84 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 66 | 35% (24-47) | -1.56 | -2.89 | -191 |  |
| > 0.2 | 82 | 48% (37-58) | +0.50 | -1.13 | -93 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 111 | 37% (29-46) | -1.22 | -2.89 | -321 |  |
| above VWAP | 136 | 46% (37-54) | -0.18 | -1.70 | -231 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 83 | 40% (30-51) | -0.13 | -1.47 | -122 |  |
| (0.136, 0.383] | 82 | 52% (42-63) | -0.20 | -1.70 | -139 | ▲ |
| (0.383, 5.591] | 82 | 33% (24-44) | -1.62 | -3.55 | -291 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.112] | 82 | 50% (39-61) | +0.61 | -0.59 | -49 |  |
| (0.112, 0.44] | 81 | 40% (30-50) | -1.06 | -2.95 | -239 |  |
| (0.44, 4.846] | 82 | 35% (26-46) | -1.48 | -3.18 | -261 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.386] | 83 | 46% (35-56) | -0.76 | -2.57 | -214 |  |
| (-0.386, 0.394] | 82 | 46% (36-57) | +0.54 | -0.59 | -48 |  |
| (0.394, 4.204] | 82 | 33% (24-44) | -1.71 | -3.53 | -290 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.056] | 83 | 42% (32-53) | -1.00 | -2.39 | -198 |  |
| (0.056, 0.127] | 83 | 46% (35-56) | +0.35 | -1.13 | -94 |  |
| (0.127, 0.924] | 81 | 37% (27-48) | -1.31 | -3.21 | -260 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.212] | 83 | 45% (34-55) | +0.23 | -0.86 | -71 |  |
| (0.212, 0.332] | 82 | 44% (34-55) | -0.80 | -2.64 | -216 |  |
| (0.332, 2.663] | 82 | 37% (27-47) | -1.38 | -3.23 | -265 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.347] | 83 | 42% (32-53) | -0.43 | -1.94 | -161 |  |
| (2.347, 3.637] | 82 | 48% (37-58) | +0.39 | -1.21 | -99 |  |
| (3.637, 18.762] | 82 | 35% (26-46) | -1.91 | -3.55 | -291 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.101] | 83 | 48% (38-59) | +0.32 | -0.44 | -37 |  |
| (0.101, 0.156] | 82 | 41% (31-52) | -1.14 | -2.29 | -188 |  |
| (0.156, 0.76] | 82 | 35% (26-46) | -1.14 | -3.99 | -328 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -1.078] | 41 | 41% (28-57) | -1.49 | -2.31 | -95 |  |
| (-1.078, 0.577] | 40 | 55% (40-69) | +0.17 | -0.40 | -16 |  |
| (0.577, 7.522] | 40 | 58% (42-71) | -0.16 | -0.89 | -36 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.533] | 44 | 48% (34-62) | -0.63 | -1.27 | -56 |  |
| (0.533, 0.832] | 42 | 55% (40-69) | -0.83 | -1.52 | -64 |  |
| (0.832, 3.799] | 42 | 50% (36-64) | -0.42 | -1.27 | -53 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.844] | 43 | 49% (35-63) | -1.23 | -1.78 | -77 |  |
| (0.844, 1.463] | 42 | 52% (38-67) | -0.26 | -0.97 | -41 |  |
| (1.463, 9.058] | 43 | 51% (37-65) | -0.39 | -1.29 | -55 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.375] | 43 | 49% (35-63) | -0.42 | -0.97 | -42 |  |
| (0.375, 0.598] | 42 | 60% (44-73) | -0.39 | -1.13 | -48 | ▲ |
| (0.598, 4.001] | 43 | 44% (30-59) | -1.07 | -1.95 | -84 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.14% | median worst: -0.15%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 0% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 108, trail_stop 103, time_stop 29, eod 7

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.101] | 83 | 31% | 33% | 30% |
| (0.101, 0.156] | 82 | 50% | 46% | 2% |
| (0.156, 0.76] | 82 | 50% | 46% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
