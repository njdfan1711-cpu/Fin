# Scalp signal analysis (fixed exits)

_267 tagged trades, 31 trading days (2026-10-01 to 2026-11-12). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 267 | 41% (35-47) | +0.17 | -1.35 | -362 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 48 | -28 | -0.58 | 219 | -334 | -1.52 | +28 |
| skip first 30 min | 3 | -15 | -4.90 | 264 | -347 | -1.31 | +15 |
| skip when SPY is down on the day | 99 | -99 | -1.00 | 168 | -262 | -1.56 | +99 |
| skip when SPY is below its VWAP | 115 | -174 | -1.52 | 152 | -187 | -1.23 | +174 |
| skip when SPY fell over the last 15 min | 97 | -128 | -1.32 | 170 | -234 | -1.37 | +128 |
| skip over-extended (30-min run in top quarter, > 0.54%) | 66 | -170 | -2.58 | 201 | -191 | -0.95 | +170 |
| skip stock not beating SPY over 15 min | 42 | -40 | -0.94 | 225 | -322 | -1.43 | +40 |
| skip afternoon entries (2:00-3:45 PM) | 59 | -206 | -3.49 | 208 | -156 | -0.75 | +206 |
| skip volume spikes above 5x average | 52 | -104 | -2.01 | 215 | -257 | -1.20 | +104 |
| skip when the stop is inside normal noise (range > stop) | 26 | -7 | -0.26 | 241 | -355 | -1.47 | +7 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.68%) | 37 | -22 | -0.59 | 230 | -340 | -1.48 | +22 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 124 | -326 | -2.63 | 143 | -35 | -0.25 | +326 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 37 | 51% (36-67) | +1.89 | +0.19 | +7 |  |
| 60-240 | 107 | 40% (31-50) | +0.11 | -1.19 | -127 |  |
| 240-375 | 75 | 33% (24-45) | -1.09 | -2.84 | -213 |  |
| 375-390 | 48 | 46% (33-60) | +0.92 | -0.58 | -28 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 48 | 48% (34-62) | +1.22 | -0.04 | -2 |  |
| -0.2 to 0 | 51 | 41% (29-55) | +0.24 | -1.91 | -98 |  |
| 0 to 0.2 | 68 | 32% (22-44) | -0.51 | -1.83 | -125 |  |
| > 0.2 | 100 | 43% (34-53) | +0.08 | -1.38 | -138 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 115 | 42% (33-51) | +0.12 | -1.52 | -174 |  |
| above VWAP | 152 | 40% (33-48) | +0.20 | -1.23 | -187 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 89 | 40% (31-51) | +0.18 | -1.03 | -92 |  |
| (0.133, 0.382] | 89 | 46% (36-56) | +0.56 | -0.97 | -86 |  |
| (0.382, 5.591] | 89 | 36% (27-46) | -0.24 | -2.06 | -183 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.119] | 88 | 47% (37-57) | +0.78 | -0.41 | -36 |  |
| (0.119, 0.441] | 88 | 42% (32-52) | +0.59 | -1.29 | -113 |  |
| (0.441, 4.846] | 88 | 35% (26-46) | -0.71 | -2.24 | -197 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.367] | 89 | 45% (35-55) | +0.65 | -1.07 | -95 |  |
| (-0.367, 0.41] | 89 | 45% (35-55) | +0.88 | -0.24 | -21 |  |
| (0.41, 5.005] | 89 | 33% (24-43) | -1.03 | -2.76 | -245 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0007000000000000001, 0.0561] | 89 | 42% (32-52) | -0.04 | -1.40 | -124 |  |
| (0.0561, 0.127] | 90 | 44% (35-55) | +0.55 | -0.87 | -79 |  |
| (0.127, 0.924] | 88 | 36% (27-47) | -0.02 | -1.80 | -159 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.217] | 89 | 44% (34-54) | +0.30 | -0.76 | -68 |  |
| (0.217, 0.339] | 89 | 43% (33-53) | +0.53 | -1.22 | -109 |  |
| (0.339, 2.663] | 89 | 36% (27-46) | -0.33 | -2.07 | -185 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.354] | 89 | 38% (29-49) | +0.03 | -1.44 | -128 |  |
| (2.354, 3.61] | 89 | 46% (36-56) | +0.66 | -0.87 | -78 |  |
| (3.61, 18.762] | 89 | 38% (29-49) | -0.19 | -1.75 | -156 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.103] | 89 | 48% (38-59) | +0.64 | -0.13 | -11 |  |
| (0.103, 0.162] | 89 | 35% (26-45) | -0.49 | -1.67 | -148 |  |
| (0.162, 0.76] | 89 | 39% (30-50) | +0.35 | -2.27 | -202 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.938] | 47 | 36% (24-50) | -0.41 | -1.20 | -56 |  |
| (-0.938, 0.615] | 47 | 51% (37-65) | +1.27 | +0.67 | +32 |  |
| (0.615, 7.522] | 47 | 45% (31-59) | +0.55 | -0.18 | -9 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.541] | 50 | 48% (35-61) | +0.57 | -0.07 | -4 |  |
| (0.541, 0.837] | 51 | 41% (29-55) | -0.01 | -0.71 | -36 |  |
| (0.837, 3.799] | 47 | 40% (28-55) | +0.45 | -0.38 | -18 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.849] | 50 | 44% (31-58) | +0.29 | -0.29 | -15 |  |
| (0.849, 1.457] | 49 | 45% (32-59) | +0.79 | +0.08 | +4 |  |
| (1.457, 9.058] | 49 | 41% (28-55) | -0.09 | -0.96 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.381] | 50 | 42% (29-56) | +0.05 | -0.53 | -27 |  |
| (0.381, 0.594] | 49 | 47% (34-61) | +0.66 | -0.08 | -4 |  |
| (0.594, 4.001] | 49 | 41% (28-55) | +0.28 | -0.56 | -27 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.20%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 26% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 49%
- Exit mix: stop 130, target 69, time_stop 55, eod 13

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.103] | 89 | 34% | 17% | 43% |
| (0.103, 0.162] | 89 | 57% | 26% | 11% |
| (0.162, 0.76] | 89 | 55% | 35% | 8% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
