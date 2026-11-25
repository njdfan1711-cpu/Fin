# Scalp signal analysis (fixed exits)

_331 tagged trades, 40 trading days (2026-10-01 to 2026-11-25). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 331 | 40% (34-45) | +0.01 | -1.34 | -445 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 62 | +0 | +0.01 | 269 | -445 | -1.66 | -0 |
| skip first 30 min | 4 | -21 | -5.34 | 327 | -423 | -1.29 | +21 |
| skip when SPY is down on the day | 154 | -170 | -1.11 | 177 | -274 | -1.55 | +170 |
| skip when SPY is below its VWAP | 142 | -198 | -1.39 | 189 | -247 | -1.31 | +198 |
| skip when SPY fell over the last 15 min | 109 | -128 | -1.18 | 222 | -316 | -1.43 | +128 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 82 | -163 | -1.99 | 249 | -282 | -1.13 | +163 |
| skip stock not beating SPY over 15 min | 52 | -88 | -1.69 | 279 | -357 | -1.28 | +88 |
| skip afternoon entries (2:00-3:45 PM) | 70 | -227 | -3.25 | 261 | -218 | -0.83 | +227 |
| skip volume spikes above 5x average | 71 | -167 | -2.35 | 260 | -278 | -1.07 | +167 |
| skip when the stop is inside normal noise (range > stop) | 49 | -36 | -0.74 | 282 | -408 | -1.45 | +36 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 53 | -51 | -0.95 | 278 | -394 | -1.42 | +51 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 140 | -361 | -2.58 | 191 | -84 | -0.44 | +361 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 40 | 50% (35-65) | +1.68 | +0.08 | +3 |  |
| 60-240 | 140 | 38% (30-46) | -0.26 | -1.39 | -195 |  |
| 240-375 | 89 | 31% (23-42) | -1.25 | -2.85 | -254 |  |
| 375-390 | 62 | 48% (36-61) | +1.36 | +0.01 | +0 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 96 | 40% (30-50) | +0.08 | -0.89 | -86 |  |
| -0.2 to 0 | 58 | 43% (31-56) | +0.50 | -1.46 | -85 |  |
| 0 to 0.2 | 70 | 33% (23-44) | -0.44 | -1.75 | -122 |  |
| > 0.2 | 107 | 42% (33-52) | -0.02 | -1.42 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 142 | 41% (33-49) | +0.06 | -1.39 | -198 |  |
| above VWAP | 189 | 39% (32-46) | -0.03 | -1.31 | -247 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.536, 0.117] | 111 | 38% (29-47) | -0.31 | -1.30 | -144 |  |
| (0.117, 0.37] | 110 | 42% (33-51) | +0.20 | -1.22 | -134 |  |
| (0.37, 5.591] | 110 | 39% (30-48) | +0.14 | -1.52 | -167 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.958, 0.139] | 109 | 48% (39-57) | +0.89 | -0.19 | -21 |  |
| (0.139, 0.446] | 109 | 38% (29-47) | -0.03 | -1.65 | -180 |  |
| (0.446, 4.846] | 109 | 35% (27-44) | -0.66 | -2.04 | -222 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.576] | 111 | 43% (34-53) | +0.35 | -1.05 | -117 |  |
| (-0.576, 0.291] | 110 | 38% (30-48) | +0.18 | -0.96 | -106 |  |
| (0.291, 9.926] | 110 | 37% (29-47) | -0.50 | -2.02 | -222 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0561] | 111 | 38% (29-47) | -0.54 | -1.75 | -194 |  |
| (0.0561, 0.126] | 110 | 45% (36-54) | +0.55 | -0.71 | -78 |  |
| (0.126, 0.924] | 110 | 36% (28-46) | +0.02 | -1.57 | -173 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.221] | 111 | 43% (34-53) | +0.33 | -0.65 | -72 |  |
| (0.221, 0.35] | 110 | 39% (30-48) | -0.05 | -1.67 | -184 |  |
| (0.35, 2.663] | 110 | 36% (28-46) | -0.25 | -1.72 | -189 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 111 | 36% (28-45) | -0.20 | -1.53 | -170 |  |
| (2.39, 3.611] | 110 | 48% (39-57) | +0.95 | -0.44 | -48 |  |
| (3.611, 19.488] | 110 | 35% (26-44) | -0.72 | -2.06 | -227 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 111 | 45% (36-54) | +0.35 | -0.38 | -42 |  |
| (0.104, 0.167] | 110 | 35% (27-45) | -0.48 | -1.64 | -180 |  |
| (0.167, 0.76] | 110 | 38% (30-48) | +0.16 | -2.02 | -223 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.92] | 69 | 32% (22-44) | -0.99 | -1.79 | -123 |  |
| (-0.92, 0.624] | 68 | 46% (34-57) | +0.66 | +0.10 | +7 |  |
| (0.624, 14.989] | 68 | 46% (34-57) | +0.72 | -0.00 | -0 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.546] | 71 | 44% (33-55) | +0.15 | -0.47 | -33 |  |
| (0.546, 0.887] | 70 | 41% (31-53) | -0.10 | -0.80 | -56 |  |
| (0.887, 3.799] | 71 | 37% (26-48) | +0.06 | -0.73 | -52 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.952] | 72 | 43% (32-55) | -0.01 | -0.58 | -42 |  |
| (0.952, 1.68] | 69 | 42% (31-54) | +0.34 | -0.35 | -24 |  |
| (1.68, 9.058] | 71 | 37% (26-48) | -0.22 | -1.06 | -75 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.409] | 71 | 37% (26-48) | -0.47 | -1.04 | -74 |  |
| (0.409, 0.624] | 70 | 49% (37-60) | +0.80 | +0.09 | +6 |  |
| (0.624, 4.001] | 71 | 37% (26-48) | -0.22 | -1.03 | -73 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.16% | median worst: -0.20%
- Reached +0.175% at some point: 49% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 51%
- Exit mix: stop 168, target 84, time_stop 63, eod 16

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 111 | 38% | 18% | 39% |
| (0.104, 0.167] | 110 | 57% | 25% | 11% |
| (0.167, 0.76] | 110 | 57% | 34% | 7% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
