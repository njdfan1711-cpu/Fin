# Scalp signal analysis (fixed exits)

_194 tagged trades, 22 trading days (2026-10-01 to 2026-10-30). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 194 | 39% (33-46) | +0.02 | -1.81 | -350 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 28 | -5 | -0.19 | 166 | -345 | -2.08 | +5 |
| skip first 30 min | 1 | -6 | -6.31 | 193 | -344 | -1.78 | +6 |
| skip when SPY is down on the day | 75 | -112 | -1.49 | 119 | -238 | -2.00 | +112 |
| skip when SPY is below its VWAP | 79 | -182 | -2.30 | 115 | -169 | -1.47 | +182 |
| skip when SPY fell over the last 15 min | 72 | -126 | -1.75 | 122 | -224 | -1.84 | +126 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 48 | -151 | -3.14 | 146 | -199 | -1.37 | +151 |
| skip stock not beating SPY over 15 min | 32 | -36 | -1.12 | 162 | -314 | -1.94 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 42 | -215 | -5.12 | 152 | -135 | -0.89 | +215 |
| skip volume spikes above 5x average | 35 | -147 | -4.19 | 159 | -204 | -1.28 | +147 |
| skip when the stop is inside normal noise (range > stop) | 8 | -8 | -0.99 | 186 | -342 | -1.84 | +8 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.62%) | 19 | -42 | -2.20 | 175 | -308 | -1.76 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 104 | -277 | -2.66 | 90 | -73 | -0.81 | +277 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 27 | 63% (44-78) | +3.45 | +1.40 | +38 | ▲ |
| 60-240 | 84 | 37% (27-48) | -0.31 | -1.81 | -152 |  |
| 240-375 | 55 | 27% (17-40) | -2.09 | -4.20 | -231 |  |
| 375-390 | 28 | 46% (30-64) | +1.83 | -0.19 | -5 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 26 | 46% (29-65) | +0.94 | -0.71 | -19 |  |
| -0.2 to 0 | 49 | 41% (28-55) | +0.32 | -1.90 | -93 |  |
| 0 to 0.2 | 61 | 36% (25-49) | +0.00 | -1.37 | -84 |  |
| > 0.2 | 58 | 38% (27-51) | -0.63 | -2.67 | -155 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 79 | 38% (28-49) | -0.25 | -2.30 | -182 |  |
| above VWAP | 115 | 40% (32-49) | +0.21 | -1.47 | -169 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.134] | 65 | 38% (28-51) | -0.01 | -1.44 | -93 |  |
| (0.134, 0.374] | 65 | 43% (32-55) | +0.10 | -1.72 | -112 |  |
| (0.374, 1.555] | 64 | 36% (25-48) | -0.03 | -2.26 | -145 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.133] | 65 | 42% (30-54) | +0.19 | -1.23 | -80 |  |
| (0.133, 0.405] | 64 | 42% (31-54) | +0.71 | -1.35 | -86 |  |
| (0.405, 1.281] | 64 | 34% (24-47) | -0.75 | -2.78 | -178 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.326] | 65 | 42% (30-54) | +0.41 | -1.69 | -110 |  |
| (-0.326, 0.356] | 64 | 44% (32-56) | +0.92 | -0.35 | -22 |  |
| (0.356, 2.726] | 65 | 32% (22-44) | -1.26 | -3.35 | -218 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0521] | 65 | 40% (29-52) | -0.26 | -1.85 | -120 |  |
| (0.0521, 0.122] | 64 | 45% (34-57) | +0.82 | -0.80 | -51 |  |
| (0.122, 0.678] | 65 | 32% (22-44) | -0.49 | -2.75 | -179 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.207] | 65 | 42% (30-54) | -0.13 | -1.37 | -89 |  |
| (0.207, 0.314] | 64 | 41% (29-53) | +0.47 | -1.53 | -98 |  |
| (0.314, 0.875] | 65 | 35% (25-48) | -0.28 | -2.50 | -163 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 65 | 38% (28-51) | +0.15 | -1.60 | -104 |  |
| (2.389, 3.589] | 64 | 48% (37-60) | +1.12 | -0.70 | -45 |  |
| (3.589, 18.762] | 65 | 31% (21-43) | -1.20 | -3.10 | -201 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0972] | 65 | 46% (35-58) | +0.34 | -0.42 | -27 |  |
| (0.0972, 0.145] | 64 | 38% (27-50) | +0.16 | -1.07 | -68 |  |
| (0.145, 0.392] | 65 | 34% (24-46) | -0.44 | -3.92 | -254 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.514] | 23 | 22% (10-42) | -2.44 | -3.30 | -76 |  |
| (-0.514, 0.464] | 22 | 45% (27-65) | +0.65 | +0.15 | +3 |  |
| (0.464, 5.305] | 23 | 61% (41-78) | +2.94 | +2.21 | +51 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.487] | 25 | 40% (23-59) | -0.41 | -1.09 | -27 |  |
| (0.487, 0.694] | 26 | 42% (26-61) | +0.52 | -0.16 | -4 |  |
| (0.694, 1.74] | 24 | 42% (24-61) | +0.20 | -0.63 | -15 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 25 | 52% (33-70) | +1.44 | +0.99 | +25 |  |
| (0.769, 1.203] | 25 | 32% (17-52) | -0.63 | -1.46 | -36 |  |
| (1.203, 3.566] | 25 | 40% (23-59) | -0.48 | -1.39 | -35 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.35] | 25 | 36% (20-55) | -0.46 | -1.05 | -26 |  |
| (0.35, 0.56] | 25 | 52% (33-70) | +1.57 | +0.84 | +21 |  |
| (0.56, 1.21] | 25 | 36% (20-55) | -0.79 | -1.65 | -41 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 96, target 49, time_stop 46, eod 3

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0972] | 65 | 34% | 15% | 49% |
| (0.0972, 0.145] | 64 | 55% | 31% | 11% |
| (0.145, 0.392] | 65 | 60% | 29% | 11% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
