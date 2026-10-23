# Scalp signal analysis (fixed exits)

_152 tagged trades, 16 trading days (2026-10-01 to 2026-10-22). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 152 | 38% (30-45) | -0.17 | -2.30 | -350 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 23 | -21 | -0.92 | 129 | -329 | -2.55 | +21 |
| skip first 30 min | 1 | -6 | -6.31 | 151 | -344 | -2.28 | +6 |
| skip when SPY is down on the day | 59 | -142 | -2.40 | 93 | -208 | -2.24 | +142 |
| skip when SPY is below its VWAP | 61 | -180 | -2.95 | 91 | -170 | -1.87 | +180 |
| skip when SPY fell over the last 15 min | 59 | -151 | -2.56 | 93 | -199 | -2.14 | +151 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 38 | -144 | -3.79 | 114 | -206 | -1.81 | +144 |
| skip stock not beating SPY over 15 min | 23 | -26 | -1.13 | 129 | -324 | -2.51 | +26 |
| skip afternoon entries (2:00-3:45 PM) | 33 | -177 | -5.37 | 119 | -173 | -1.45 | +177 |
| skip volume spikes above 5x average | 27 | -128 | -4.73 | 125 | -222 | -1.78 | +128 |
| skip when the stop is inside normal noise (range > stop) | 4 | +4 | +0.89 | 148 | -354 | -2.39 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.55%) | 8 | -7 | -0.88 | 144 | -343 | -2.38 | +7 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 91 | -298 | -3.27 | 61 | -52 | -0.85 | +298 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 65 | 35% (25-48) | -0.42 | -2.13 | -138 |  |
| 240-375 | 44 | 27% (16-42) | -2.00 | -4.47 | -197 |  |
| 375-390 | 23 | 43% (26-63) | +1.37 | -0.92 | -21 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 23 | 43% (26-63) | +0.78 | -1.02 | -23 |  |
| -0.2 to 0 | 36 | 36% (22-52) | -0.57 | -3.28 | -118 |  |
| 0 to 0.2 | 43 | 37% (24-52) | +0.31 | -1.31 | -57 |  |
| > 0.2 | 50 | 36% (24-50) | -0.73 | -3.04 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 61 | 36% (25-49) | -0.47 | -2.95 | -180 |  |
| above VWAP | 91 | 38% (29-49) | +0.03 | -1.87 | -170 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.126] | 51 | 35% (24-49) | -0.33 | -1.98 | -101 |  |
| (0.126, 0.369] | 50 | 42% (29-56) | -0.08 | -2.09 | -105 |  |
| (0.369, 1.555] | 51 | 35% (24-49) | -0.11 | -2.82 | -144 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.146] | 51 | 37% (25-51) | -0.43 | -2.26 | -115 |  |
| (0.146, 0.403] | 50 | 44% (31-58) | +1.22 | -1.05 | -53 |  |
| (0.403, 1.192] | 50 | 32% (21-46) | -1.18 | -3.52 | -176 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.254] | 51 | 37% (25-51) | -0.11 | -2.59 | -132 |  |
| (-0.254, 0.377] | 50 | 44% (31-58) | +0.74 | -0.64 | -32 |  |
| (0.377, 2.726] | 51 | 31% (20-45) | -1.13 | -3.64 | -185 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 51 | 39% (27-53) | -0.39 | -2.20 | -112 |  |
| (0.0519, 0.122] | 50 | 44% (31-58) | +0.64 | -1.30 | -65 |  |
| (0.122, 0.678] | 51 | 29% (19-43) | -0.74 | -3.39 | -173 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.197] | 51 | 45% (32-59) | +0.11 | -1.22 | -62 |  |
| (0.197, 0.305] | 50 | 34% (22-48) | -0.10 | -2.46 | -123 |  |
| (0.305, 0.875] | 51 | 33% (22-47) | -0.52 | -3.23 | -165 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.405] | 51 | 37% (25-51) | +0.28 | -1.85 | -94 |  |
| (2.405, 3.475] | 50 | 48% (35-61) | +0.80 | -1.21 | -60 |  |
| (3.475, 18.76] | 51 | 27% (17-41) | -1.57 | -3.83 | -195 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.095] | 51 | 45% (32-59) | +0.19 | -0.57 | -29 |  |
| (0.095, 0.147] | 50 | 32% (21-46) | -0.62 | -2.10 | -105 |  |
| (0.147, 0.392] | 51 | 35% (24-49) | -0.08 | -4.23 | -216 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -1.264] | 9 | 33% (12-65) | -1.18 | -2.21 | -20 | few trades |
| (-1.264, 0.129] | 8 | 12% (2-47) | -2.79 | -3.31 | -26 | few trades |
| (0.129, 5.305] | 9 | 67% (35-88) | +3.23 | +2.75 | +25 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.465] | 11 | 27% (10-57) | -2.59 | -3.31 | -36 |  |
| (0.465, 0.645] | 11 | 27% (10-57) | -1.45 | -2.25 | -25 |  |
| (0.645, 1.74] | 11 | 55% (28-79) | +2.10 | +1.35 | +15 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.769] | 11 | 36% (15-65) | -0.23 | -0.72 | -8 |  |
| (0.769, 1.15] | 11 | 45% (21-72) | +0.98 | +0.14 | +2 |  |
| (1.15, 3.566] | 11 | 27% (10-57) | -2.70 | -3.62 | -40 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.307] | 11 | 9% (2-38) | -3.51 | -4.18 | -46 |  |
| (0.307, 0.483] | 11 | 64% (35-85) | +1.63 | +1.03 | +11 |  |
| (0.483, 0.815] | 11 | 36% (15-65) | -0.08 | -1.05 | -12 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 43% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 52%
- Exit mix: stop 78, target 38, time_stop 35, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.095] | 51 | 35% | 16% | 47% |
| (0.095, 0.147] | 50 | 60% | 28% | 12% |
| (0.147, 0.392] | 51 | 59% | 31% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
