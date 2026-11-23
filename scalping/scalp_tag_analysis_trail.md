# Scalp signal analysis (trail exits)

_314 tagged trades, 38 trading days (2026-10-01 to 2026-11-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 314 | 43% (38-49) | -0.66 | -2.05 | -645 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | +29 | +0.48 | 254 | -674 | -2.65 | -29 |
| skip first 30 min | 4 | -17 | -4.16 | 310 | -629 | -2.03 | +17 |
| skip when SPY is down on the day | 144 | -315 | -2.19 | 170 | -330 | -1.94 | +315 |
| skip when SPY is below its VWAP | 138 | -336 | -2.44 | 176 | -309 | -1.76 | +336 |
| skip when SPY fell over the last 15 min | 104 | -212 | -2.04 | 210 | -433 | -2.06 | +212 |
| skip over-extended (30-min run in top quarter, > 0.55%) | 78 | -220 | -2.83 | 236 | -425 | -1.80 | +220 |
| skip stock not beating SPY over 15 min | 49 | -114 | -2.32 | 265 | -532 | -2.01 | +114 |
| skip afternoon entries (2:00-3:45 PM) | 68 | -249 | -3.66 | 246 | -396 | -1.61 | +249 |
| skip volume spikes above 5x average | 67 | -237 | -3.53 | 247 | -409 | -1.65 | +237 |
| skip when the stop is inside normal noise (range > stop) | 42 | -65 | -1.55 | 272 | -580 | -2.13 | +65 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.72%) | 49 | -79 | -1.60 | 265 | -567 | -2.14 | +79 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 138 | -419 | -3.04 | 176 | -226 | -1.29 | +419 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 39 | 49% (34-64) | -0.41 | -2.04 | -80 |  |
| 60-240 | 128 | 38% (30-47) | -1.31 | -2.48 | -318 |  |
| 240-375 | 87 | 40% (31-51) | -1.55 | -3.17 | -276 |  |
| 375-390 | 60 | 53% (41-65) | +1.85 | +0.48 | +29 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 89 | 46% (36-56) | -0.47 | -1.46 | -130 |  |
| -0.2 to 0 | 55 | 40% (28-53) | -1.34 | -3.37 | -185 |  |
| 0 to 0.2 | 69 | 35% (25-47) | -1.60 | -2.92 | -201 |  |
| > 0.2 | 101 | 48% (38-57) | +0.17 | -1.27 | -128 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 138 | 41% (33-49) | -0.96 | -2.44 | -336 |  |
| above VWAP | 176 | 45% (38-52) | -0.43 | -1.76 | -309 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.123] | 105 | 41% (32-51) | -0.35 | -1.45 | -152 |  |
| (0.123, 0.374] | 104 | 50% (41-59) | -0.39 | -1.80 | -187 |  |
| (0.374, 5.591] | 105 | 38% (29-48) | -1.24 | -2.91 | -306 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.824, 0.133] | 104 | 51% (41-60) | +0.33 | -0.77 | -80 |  |
| (0.133, 0.451] | 103 | 40% (31-49) | -1.03 | -2.72 | -280 |  |
| (0.451, 4.846] | 103 | 39% (30-48) | -1.19 | -2.61 | -269 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-7.547000000000001, -0.574] | 105 | 47% (37-56) | -0.51 | -1.96 | -205 |  |
| (-0.574, 0.332] | 104 | 44% (35-54) | -0.06 | -1.21 | -126 |  |
| (0.332, 9.926] | 105 | 38% (29-48) | -1.42 | -2.99 | -314 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0009, 0.056] | 105 | 43% (34-52) | -1.02 | -2.27 | -238 |  |
| (0.056, 0.127] | 105 | 48% (38-57) | +0.19 | -1.10 | -115 |  |
| (0.127, 0.924] | 104 | 38% (30-48) | -1.16 | -2.81 | -292 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.219] | 105 | 46% (37-55) | +0.12 | -0.87 | -92 |  |
| (0.219, 0.348] | 104 | 46% (37-56) | -0.65 | -2.25 | -234 |  |
| (0.348, 2.663] | 105 | 37% (29-47) | -1.47 | -3.05 | -320 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.378] | 105 | 44% (35-53) | -0.47 | -1.84 | -193 |  |
| (2.378, 3.635] | 104 | 50% (41-59) | +0.59 | -0.84 | -87 |  |
| (3.635, 19.488] | 105 | 35% (27-45) | -2.10 | -3.47 | -365 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.104] | 105 | 47% (37-56) | +0.05 | -0.68 | -71 |  |
| (0.104, 0.166] | 104 | 44% (35-54) | -0.97 | -2.11 | -220 |  |
| (0.166, 0.76] | 105 | 38% (29-48) | -1.08 | -3.37 | -354 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-26.103, -0.748] | 63 | 41% (30-54) | -1.41 | -2.20 | -139 |  |
| (-0.748, 0.658] | 63 | 52% (40-64) | +0.00 | -0.55 | -35 |  |
| (0.658, 14.989] | 62 | 56% (44-68) | -0.33 | -1.07 | -66 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.55] | 65 | 48% (36-60) | -0.64 | -1.25 | -81 |  |
| (0.55, 0.859] | 65 | 54% (42-65) | -0.65 | -1.36 | -88 |  |
| (0.859, 3.799] | 65 | 48% (36-60) | -0.69 | -1.49 | -97 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.909] | 65 | 49% (37-61) | -1.15 | -1.73 | -113 |  |
| (0.909, 1.631] | 65 | 51% (39-63) | -0.46 | -1.15 | -75 |  |
| (1.631, 9.058] | 65 | 49% (37-61) | -0.37 | -1.22 | -79 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.168, 0.404] | 65 | 45% (33-57) | -0.85 | -1.41 | -92 |  |
| (0.404, 0.62] | 65 | 62% (49-72) | -0.04 | -0.75 | -49 | ▲ |
| (0.62, 4.001] | 65 | 43% (32-55) | -1.09 | -1.93 | -126 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.15%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 11% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 44%
- Exit mix: stop 137, trail_stop 132, time_stop 35, eod 10

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.104] | 105 | 34% | 32% | 29% |
| (0.104, 0.166] | 104 | 47% | 46% | 3% |
| (0.166, 0.76] | 105 | 50% | 48% | 2% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
