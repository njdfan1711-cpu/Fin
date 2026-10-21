# Scalp signal analysis (fixed exits)

_150 tagged trades, 15 trading days (2026-10-01 to 2026-10-21). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 150 | 37% (29-45) | -0.27 | -2.42 | -362 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | -31 | -1.41 | 128 | -331 | -2.59 | +31 |
| skip first 30 min | 1 | -6 | -6.31 | 149 | -356 | -2.39 | +6 |
| skip when SPY is down on the day | 58 | -151 | -2.61 | 92 | -211 | -2.29 | +151 |
| skip when SPY is below its VWAP | 59 | -193 | -3.27 | 91 | -170 | -1.87 | +193 |
| skip when SPY fell over the last 15 min | 58 | -154 | -2.65 | 92 | -209 | -2.27 | +154 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -147 | -3.96 | 113 | -216 | -1.91 | +147 |
| skip stock not beating SPY over 15 min | 22 | -36 | -1.63 | 128 | -327 | -2.55 | +36 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -180 | -5.62 | 118 | -183 | -1.55 | +180 |
| skip volume spikes above 5x average | 27 | -128 | -4.73 | 123 | -235 | -1.91 | +128 |
| skip when the stop is inside normal noise (range > stop) | 4 | +4 | +0.89 | 146 | -366 | -2.51 | -4 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 8 | -7 | -0.88 | 142 | -355 | -2.50 | +7 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -301 | -3.34 | 60 | -62 | -1.03 | +301 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 60% (39-78) | +2.90 | +0.31 | +6 | ▲ |
| 60-240 | 65 | 35% (25-48) | -0.42 | -2.13 | -138 |  |
| 240-375 | 43 | 26% (15-40) | -2.14 | -4.63 | -199 |  |
| 375-390 | 22 | 41% (23-61) | +0.97 | -1.41 | -31 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 41% (23-61) | +0.35 | -1.51 | -33 |  |
| -0.2 to 0 | 36 | 36% (22-52) | -0.57 | -3.28 | -118 |  |
| 0 to 0.2 | 42 | 36% (23-51) | +0.22 | -1.41 | -59 |  |
| > 0.2 | 50 | 36% (24-50) | -0.73 | -3.04 | -152 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 34% (23-47) | -0.73 | -3.27 | -193 |  |
| above VWAP | 91 | 38% (29-49) | +0.03 | -1.87 | -170 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.129] | 50 | 34% (22-48) | -0.54 | -2.22 | -111 |  |
| (0.129, 0.369] | 50 | 42% (29-56) | -0.08 | -2.09 | -105 |  |
| (0.369, 1.555] | 50 | 34% (22-48) | -0.19 | -2.93 | -147 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 50 | 36% (24-50) | -0.64 | -2.50 | -125 |  |
| (0.147, 0.403] | 49 | 43% (30-57) | +1.03 | -1.26 | -62 |  |
| (0.403, 1.192] | 50 | 32% (21-46) | -1.06 | -3.38 | -169 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.266] | 50 | 38% (26-52) | -0.08 | -2.61 | -130 |  |
| (-0.266, 0.364] | 50 | 42% (29-56) | +0.62 | -0.77 | -39 |  |
| (0.364, 2.726] | 50 | 30% (19-44) | -1.34 | -3.87 | -193 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 50 | 38% (26-52) | -0.60 | -2.44 | -122 |  |
| (0.052, 0.122] | 50 | 42% (29-56) | +0.44 | -1.48 | -74 |  |
| (0.122, 0.678] | 50 | 30% (19-44) | -0.64 | -3.33 | -166 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 50 | 44% (31-58) | +0.03 | -1.30 | -65 |  |
| (0.198, 0.309] | 50 | 32% (21-46) | -0.42 | -2.83 | -141 |  |
| (0.309, 0.875] | 50 | 34% (22-48) | -0.42 | -3.12 | -156 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.407] | 50 | 36% (24-50) | +0.08 | -2.09 | -104 |  |
| (2.407, 3.547] | 50 | 48% (35-61) | +0.89 | -1.11 | -55 |  |
| (3.547, 18.76] | 50 | 26% (16-40) | -1.78 | -4.05 | -203 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 51 | 45% (32-59) | +0.19 | -0.57 | -29 |  |
| (0.0946, 0.148] | 49 | 29% (18-42) | -1.05 | -2.53 | -124 |  |
| (0.148, 0.392] | 50 | 36% (24-50) | +0.03 | -4.19 | -210 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.612, -1.088] | 8 | 25% (7-59) | -1.83 | -2.82 | -23 | few trades |
| (-1.088, 0.281] | 8 | 0% (0-32) | -4.78 | -5.29 | -42 | few trades |
| (0.281, 5.305] | 8 | 75% (41-93) | +4.33 | +3.85 | +31 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.449] | 11 | 27% (10-57) | -2.59 | -3.31 | -36 |  |
| (0.449, 0.736] | 10 | 10% (2-40) | -3.62 | -4.36 | -44 |  |
| (0.736, 1.74] | 10 | 60% (31-83) | +2.90 | +2.12 | +21 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.757] | 11 | 36% (15-65) | -0.23 | -0.72 | -8 |  |
| (0.757, 1.136] | 10 | 40% (17-69) | +0.05 | -0.83 | -8 |  |
| (1.136, 3.566] | 10 | 20% (6-51) | -3.38 | -4.25 | -43 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 11 | 9% (2-38) | -3.51 | -4.18 | -46 |  |
| (0.296, 0.508] | 10 | 50% (24-76) | -0.18 | -0.81 | -8 |  |
| (0.508, 0.815] | 10 | 40% (17-69) | +0.45 | -0.48 | -5 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.20%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 25% of trades
- Reached +0.5% at some point: 4% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 53%
- Exit mix: stop 78, target 37, time_stop 34, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 51 | 35% | 16% | 47% |
| (0.0946, 0.148] | 49 | 63% | 27% | 10% |
| (0.148, 0.392] | 50 | 58% | 32% | 10% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
