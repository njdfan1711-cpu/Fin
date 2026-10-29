# Scalp signal analysis (trail exits)

_185 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 185 | 37% (30-44) | -0.84 | -2.72 | -503 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 26 | +16 | +0.60 | 159 | -519 | -3.26 | -16 |
| skip first 30 min | 1 | -6 | -6.31 | 184 | -497 | -2.70 | +6 |
| skip when SPY is down on the day | 71 | -247 | -3.48 | 114 | -256 | -2.25 | +247 |
| skip when SPY is below its VWAP | 76 | -294 | -3.87 | 109 | -209 | -1.92 | +294 |
| skip when SPY fell over the last 15 min | 68 | -177 | -2.60 | 117 | -326 | -2.79 | +177 |
| skip over-extended (30-min run in top quarter, > 0.48%) | 46 | -185 | -4.03 | 139 | -318 | -2.29 | +185 |
| skip stock not beating SPY over 15 min | 31 | -64 | -2.06 | 154 | -439 | -2.85 | +64 |
| skip afternoon entries (2:00-3:45 PM) | 40 | -222 | -5.55 | 145 | -281 | -1.94 | +222 |
| skip volume spikes above 5x average | 33 | -155 | -4.70 | 152 | -348 | -2.29 | +155 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 178 | -494 | -2.78 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.60%) | 17 | -66 | -3.90 | 168 | -437 | -2.60 | +66 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 102 | -365 | -3.57 | 83 | -139 | -1.67 | +365 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 56% (37-73) | +0.76 | -1.43 | -36 | ▲ |
| 60-240 | 81 | 33% (24-44) | -1.29 | -2.82 | -228 |  |
| 240-375 | 53 | 30% (20-44) | -2.64 | -4.81 | -255 |  |
| 375-390 | 26 | 42% (26-61) | +2.71 | +0.60 | +16 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 47 | 36% (24-50) | -1.44 | -3.72 | -175 |  |
| 0 to 0.2 | 56 | 34% (23-47) | -1.42 | -2.85 | -160 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 76 | 28% (19-39) | -1.76 | -3.87 | -294 |  |
| above VWAP | 109 | 43% (34-52) | -0.19 | -1.92 | -209 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 62 | 37% (26-50) | +0.11 | -1.35 | -84 |  |
| (0.133, 0.372] | 61 | 44% (33-57) | -0.85 | -2.72 | -166 |  |
| (0.372, 1.555] | 62 | 29% (19-41) | -1.78 | -4.09 | -254 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.148] | 62 | 39% (28-51) | +0.15 | -1.48 | -92 |  |
| (0.148, 0.412] | 61 | 41% (30-54) | -0.82 | -2.86 | -175 |  |
| (0.412, 1.281] | 61 | 31% (21-44) | -1.77 | -3.77 | -230 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.29] | 62 | 35% (25-48) | -1.22 | -3.43 | -213 |  |
| (-0.29, 0.364] | 61 | 46% (34-58) | +0.83 | -0.43 | -27 |  |
| (0.364, 2.726] | 62 | 29% (19-41) | -2.10 | -4.26 | -264 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 62 | 39% (28-51) | -1.13 | -2.77 | -171 |  |
| (0.0519, 0.12] | 61 | 39% (28-52) | +0.30 | -1.37 | -83 |  |
| (0.12, 0.678] | 62 | 32% (22-45) | -1.67 | -4.00 | -248 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.204] | 62 | 44% (32-56) | +0.19 | -1.05 | -65 |  |
| (0.204, 0.311] | 61 | 39% (28-52) | -0.74 | -2.79 | -170 |  |
| (0.311, 0.875] | 62 | 27% (18-40) | -1.95 | -4.32 | -268 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.392] | 62 | 39% (28-51) | -0.60 | -2.38 | -148 |  |
| (2.392, 3.589] | 61 | 43% (31-55) | +0.64 | -1.25 | -76 |  |
| (3.589, 18.762] | 62 | 29% (19-41) | -2.53 | -4.50 | -279 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 62 | 45% (33-57) | +0.40 | -0.34 | -21 |  |
| (0.0964, 0.145] | 61 | 39% (28-52) | -1.14 | -2.38 | -145 |  |
| (0.145, 0.392] | 62 | 26% (17-38) | -1.78 | -5.43 | -337 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.496] | 20 | 30% (15-52) | -2.53 | -3.43 | -69 |  |
| (-0.496, 0.543] | 19 | 47% (27-68) | -0.24 | -0.76 | -15 |  |
| (0.543, 5.305] | 20 | 60% (39-78) | -0.04 | -0.73 | -15 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.48] | 22 | 41% (23-61) | -0.90 | -1.55 | -34 |  |
| (0.48, 0.684] | 22 | 45% (27-65) | -1.34 | -2.00 | -44 |  |
| (0.684, 1.74] | 22 | 50% (31-69) | -1.19 | -2.10 | -46 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.784] | 22 | 50% (31-69) | -0.71 | -1.15 | -25 |  |
| (0.784, 1.203] | 22 | 36% (20-57) | -1.71 | -2.56 | -56 |  |
| (1.203, 3.566] | 22 | 50% (31-69) | -1.02 | -1.94 | -43 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.332] | 22 | 36% (20-57) | -1.51 | -2.07 | -45 |  |
| (0.332, 0.545] | 22 | 64% (43-80) | +0.55 | -0.17 | -4 | ▲ |
| (0.545, 1.21] | 22 | 36% (20-57) | -2.47 | -3.41 | -75 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 84, trail_stop 70, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 62 | 32% | 27% | 39% |
| (0.0964, 0.145] | 61 | 49% | 44% | 5% |
| (0.145, 0.392] | 62 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
