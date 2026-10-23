# Scalp signal analysis (fixed exits)

_156 tagged trades, 17 trading days (2026-10-01 to 2026-10-23). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 156 | 37% (30-45) | -0.22 | -2.31 | -361 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | -21 | -0.92 | 133 | -340 | -2.55 | +21 |
| skip first 30 min | 1 | -6 | -6.31 | 155 | -355 | -2.29 | +6 |
| skip when SPY is down on the day | 62 | -145 | -2.34 | 94 | -216 | -2.29 | +145 |
| skip when SPY is below its VWAP | 64 | -184 | -2.87 | 92 | -177 | -1.93 | +184 |
| skip when SPY fell over the last 15 min | 61 | -148 | -2.42 | 95 | -213 | -2.24 | +148 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 39 | -167 | -4.28 | 117 | -194 | -1.66 | +167 |
| skip stock not beating SPY over 15 min | 24 | -16 | -0.68 | 132 | -345 | -2.61 | +16 |
| skip afternoon entries (2:00-3:45 PM) | 34 | -184 | -5.41 | 122 | -177 | -1.45 | +184 |
| skip volume spikes above 5x average | 27 | -128 | -4.73 | 129 | -233 | -1.81 | +128 |
| skip when the stop is inside normal noise (range > stop) | 6 | -11 | -1.76 | 150 | -350 | -2.34 | +11 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 9 | -30 | -3.36 | 147 | -331 | -2.25 | +30 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 92 | -305 | -3.32 | 64 | -56 | -0.87 | +305 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 22 | 59% (39-77) | +2.81 | +0.42 | +9 | ▲ |
| 60-240 | 66 | 35% (24-47) | -0.50 | -2.21 | -146 |  |
| 240-375 | 45 | 27% (16-41) | -2.09 | -4.51 | -203 |  |
| 375-390 | 23 | 43% (26-63) | +1.37 | -0.92 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 42% (24-61) | +0.50 | -1.25 | -30 |  |
| -0.2 to 0 | 38 | 37% (23-53) | -0.44 | -3.03 | -115 |  |
| 0 to 0.2 | 44 | 36% (24-51) | +0.17 | -1.45 | -64 |  |
| > 0.2 | 50 | 36% (24-50) | -0.73 | -3.04 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 64 | 36% (25-48) | -0.48 | -2.87 | -184 |  |
| above VWAP | 92 | 38% (29-48) | -0.03 | -1.93 | -177 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 52 | 37% (25-50) | -0.13 | -1.76 | -91 |  |
| (0.129, 0.369] | 52 | 40% (28-54) | -0.30 | -2.27 | -118 |  |
| (0.369, 1.555] | 52 | 35% (23-48) | -0.22 | -2.91 | -151 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 52 | 38% (26-52) | -0.23 | -2.03 | -105 |  |
| (0.147, 0.404] | 51 | 43% (31-57) | +1.08 | -1.16 | -59 |  |
| (0.404, 1.281] | 52 | 31% (20-44) | -1.37 | -3.65 | -190 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.252] | 52 | 37% (25-50) | -0.22 | -2.67 | -139 |  |
| (-0.252, 0.387] | 52 | 44% (32-58) | +0.65 | -0.72 | -38 |  |
| (0.387, 2.726] | 52 | 31% (20-44) | -1.08 | -3.55 | -184 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 52 | 38% (26-52) | -0.49 | -2.28 | -119 |  |
| (0.052, 0.122] | 52 | 44% (32-58) | +0.69 | -1.18 | -62 |  |
| (0.122, 0.678] | 52 | 29% (18-42) | -0.84 | -3.47 | -181 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 52 | 44% (32-58) | +0.07 | -1.24 | -65 |  |
| (0.197, 0.303] | 52 | 35% (23-48) | -0.09 | -2.39 | -124 |  |
| (0.303, 0.875] | 52 | 33% (22-46) | -0.63 | -3.31 | -172 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.39] | 52 | 35% (23-48) | -0.14 | -2.11 | -110 |  |
| (2.39, 3.448] | 52 | 48% (35-61) | +0.84 | -1.26 | -65 |  |
| (3.448, 18.76] | 52 | 29% (18-42) | -1.35 | -3.57 | -185 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0962] | 52 | 44% (32-58) | +0.07 | -0.69 | -36 |  |
| (0.0962, 0.148] | 52 | 33% (22-46) | -0.52 | -1.95 | -101 |  |
| (0.148, 0.392] | 52 | 35% (23-48) | -0.20 | -4.30 | -224 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.779] | 10 | 30% (11-60) | -1.70 | -2.69 | -27 |  |
| (-1.779, 0.0478] | 10 | 20% (6-51) | -1.79 | -2.40 | -24 |  |
| (0.0478, 5.305] | 10 | 60% (31-83) | +2.32 | +1.84 | +18 |  |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.473] | 13 | 23% (8-50) | -2.64 | -3.37 | -44 |  |
| (0.473, 0.736] | 12 | 33% (14-61) | -1.01 | -1.70 | -20 |  |
| (0.736, 1.74] | 12 | 50% (25-75) | +1.42 | +0.59 | +7 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.775] | 13 | 46% (23-71) | +0.76 | +0.29 | +4 |  |
| (0.775, 1.178] | 12 | 42% (19-68) | +1.04 | +0.21 | +2 |  |
| (1.178, 3.566] | 12 | 17% (5-45) | -4.32 | -5.28 | -63 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.312] | 13 | 15% (4-42) | -2.66 | -3.31 | -43 |  |
| (0.312, 0.508] | 12 | 58% (32-81) | +1.05 | +0.41 | +5 |  |
| (0.508, 1.14] | 12 | 33% (14-61) | -0.61 | -1.58 | -19 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 81, target 39, time_stop 35, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0962] | 52 | 37% | 15% | 46% |
| (0.0962, 0.148] | 52 | 60% | 29% | 12% |
| (0.148, 0.392] | 52 | 60% | 31% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
