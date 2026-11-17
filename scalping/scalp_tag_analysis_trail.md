# Scalp signal analysis (trail exits)

_288 tagged trades, 34 trading days (2026-10-01 to 2026-11-17). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 288 | 41% (35-47) | -0.79 | -2.25 | -648 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 51 | -14 | -0.27 | 237 | -634 | -2.68 | +14 |
| skip first 30 min | 4 | -17 | -4.16 | 284 | -631 | -2.22 | +17 |
| skip when SPY is down on the day | 118 | -318 | -2.70 | 170 | -330 | -1.94 | +318 |
| skip when SPY is below its VWAP | 123 | -362 | -2.95 | 165 | -285 | -1.73 | +362 |
| skip when SPY fell over the last 15 min | 101 | -227 | -2.25 | 187 | -420 | -2.25 | +227 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 71 | -238 | -3.36 | 217 | -410 | -1.89 | +238 |
| skip stock not beating SPY over 15 min | 46 | -109 | -2.38 | 242 | -538 | -2.23 | +109 |
| skip afternoon entries (2:00-3:45 PM) | 62 | -230 | -3.71 | 226 | -418 | -1.85 | +230 |
| skip volume spikes above 5x average | 59 | -212 | -3.60 | 229 | -435 | -1.90 | +212 |
| skip when the stop is inside normal noise (range > stop) | 35 | -90 | -2.56 | 253 | -558 | -2.21 | +90 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.71%) | 42 | -105 | -2.50 | 246 | -543 | -2.21 | +105 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 132 | -438 | -3.32 | 156 | -210 | -1.34 | +438 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 38 | 47% (32-63) | -0.47 | -2.15 | -82 |  |
| 60-240 | 120 | 38% (30-47) | -1.23 | -2.45 | -294 |  |
| 240-375 | 79 | 39% (29-50) | -1.55 | -3.27 | -258 |  |
| 375-390 | 51 | 45% (32-59) | +1.20 | -0.27 | -14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 67 | 40% (29-52) | -0.89 | -2.00 | -134 |  |
| -0.2 to 0 | 51 | 37% (25-51) | -1.45 | -3.61 | -184 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 123 | 36% (28-45) | -1.38 | -2.95 | -362 |  |
| above VWAP | 165 | 45% (37-52) | -0.35 | -1.73 | -285 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 96 | 39% (29-49) | -0.39 | -1.56 | -149 |  |
| (0.129, 0.374] | 96 | 50% (40-60) | -0.39 | -1.86 | -179 |  |
| (0.374, 5.591] | 96 | 34% (26-44) | -1.58 | -3.33 | -320 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.128] | 95 | 47% (38-57) | +0.19 | -0.97 | -92 |  |
| (0.128, 0.446] | 94 | 43% (33-53) | -0.74 | -2.54 | -239 |  |
| (0.446, 4.846] | 95 | 34% (25-44) | -1.70 | -3.16 | -301 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.444] | 96 | 43% (33-53) | -0.91 | -2.47 | -237 |  |
| (-0.444, 0.384] | 96 | 46% (36-56) | +0.24 | -0.95 | -91 |  |
| (0.384, 9.926] | 96 | 34% (26-44) | -1.69 | -3.34 | -320 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.0559] | 96 | 43% (33-53) | -0.96 | -2.27 | -218 |  |
| (0.0559, 0.127] | 96 | 45% (35-55) | +0.11 | -1.26 | -121 |  |
| (0.127, 0.924] | 96 | 35% (27-45) | -1.51 | -3.22 | -310 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.218] | 96 | 45% (35-55) | +0.16 | -0.88 | -85 |  |
| (0.218, 0.346] | 96 | 46% (36-56) | -0.63 | -2.31 | -222 |  |
| (0.346, 2.663] | 96 | 32% (24-42) | -1.89 | -3.55 | -341 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 96 | 41% (31-51) | -0.63 | -2.06 | -198 |  |
| (2.374, 3.634] | 96 | 47% (37-57) | +0.28 | -1.21 | -116 |  |
| (3.634, 19.488] | 96 | 35% (27-45) | -2.00 | -3.48 | -334 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 96 | 48% (38-58) | +0.25 | -0.51 | -49 |  |
| (0.104, 0.166] | 96 | 42% (32-52) | -1.08 | -2.28 | -219 |  |
| (0.166, 0.76] | 96 | 33% (25-43) | -1.53 | -3.95 | -379 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.915] | 54 | 41% (29-54) | -1.34 | -2.17 | -117 |  |
| (-0.915, 0.589] | 54 | 50% (37-63) | -0.28 | -0.85 | -46 |  |
| (0.589, 7.522] | 54 | 52% (39-65) | -0.74 | -1.47 | -79 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.555] | 57 | 49% (37-62) | -0.54 | -1.19 | -68 |  |
| (0.555, 0.843] | 56 | 54% (41-66) | -0.62 | -1.34 | -75 |  |
| (0.843, 3.799] | 56 | 39% (28-52) | -1.45 | -2.25 | -126 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.884] | 57 | 46% (33-58) | -1.48 | -2.08 | -119 |  |
| (0.884, 1.613] | 56 | 54% (41-66) | -0.11 | -0.84 | -47 |  |
| (1.613, 9.058] | 56 | 43% (31-56) | -1.01 | -1.84 | -103 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.397] | 57 | 44% (32-57) | -0.78 | -1.38 | -78 |  |
| (0.397, 0.618] | 56 | 62% (49-74) | -0.05 | -0.78 | -44 | ▲ |
| (0.618, 4.001] | 56 | 36% (24-49) | -1.79 | -2.62 | -147 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.16%
- Reached +0.175% at some point: 47% of trades
- Reached +0.35% at some point: 10% of trades
- Reached +0.5% at some point: 1% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 129, trail_stop 116, time_stop 34, eod 9

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 96 | 32% | 32% | 30% |
| (0.104, 0.166] | 96 | 49% | 45% | 3% |
| (0.166, 0.76] | 96 | 53% | 44% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
