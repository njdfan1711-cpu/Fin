# Scalp signal analysis (trail exits)

_173 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 173 | 36% (30-44) | -0.83 | -2.78 | -481 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 148 | -492 | -3.33 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 172 | -474 | -2.76 | +6 |
| skip when SPY is down on the day | 67 | -255 | -3.80 | 106 | -226 | -2.13 | +255 |
| skip when SPY is below its VWAP | 74 | -290 | -3.91 | 99 | -191 | -1.93 | +290 |
| skip when SPY fell over the last 15 min | 67 | -185 | -2.77 | 106 | -295 | -2.79 | +185 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 43 | -191 | -4.44 | 130 | -290 | -2.23 | +191 |
| skip stock not beating SPY over 15 min | 28 | -48 | -1.70 | 145 | -433 | -2.98 | +48 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 136 | -279 | -2.05 | +202 |
| skip volume spikes above 5x average | 31 | -146 | -4.70 | 142 | -335 | -2.36 | +146 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 166 | -472 | -2.84 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 14 | -42 | -2.99 | 159 | -439 | -2.76 | +42 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 96 | -360 | -3.75 | 77 | -121 | -1.57 | +360 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 56% (37-73) | +0.76 | -1.43 | -36 | ▲ |
| 60-240 | 74 | 32% (23-44) | -1.37 | -2.96 | -219 |  |
| 240-375 | 49 | 31% (20-45) | -2.56 | -4.85 | -237 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 43 | 33% (20-47) | -1.85 | -4.25 | -183 |  |
| 0 to 0.2 | 48 | 35% (23-50) | -1.15 | -2.70 | -130 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 74 | 27% (18-38) | -1.77 | -3.91 | -290 |  |
| above VWAP | 99 | 43% (34-53) | -0.12 | -1.93 | -191 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 58 | 38% (27-51) | +0.32 | -1.20 | -70 |  |
| (0.133, 0.368] | 57 | 44% (32-57) | -0.89 | -2.76 | -157 |  |
| (0.368, 1.555] | 58 | 28% (18-40) | -1.91 | -4.37 | -254 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.148] | 58 | 38% (27-51) | +0.26 | -1.44 | -84 |  |
| (0.148, 0.405] | 57 | 42% (30-55) | -0.67 | -2.71 | -154 |  |
| (0.405, 1.281] | 57 | 30% (20-43) | -2.00 | -4.14 | -236 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.276] | 58 | 33% (22-46) | -1.45 | -3.73 | -216 |  |
| (-0.276, 0.377] | 57 | 47% (35-60) | +1.03 | -0.29 | -16 |  |
| (0.377, 2.726] | 58 | 29% (19-42) | -2.02 | -4.27 | -248 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0519] | 58 | 36% (25-49) | -1.41 | -3.10 | -180 |  |
| (0.0519, 0.12] | 57 | 40% (29-53) | +0.52 | -1.07 | -61 |  |
| (0.12, 0.678] | 58 | 33% (22-46) | -1.57 | -4.14 | -240 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.2] | 58 | 43% (31-56) | +0.18 | -1.09 | -63 |  |
| (0.2, 0.3] | 57 | 39% (27-52) | -1.01 | -3.13 | -178 |  |
| (0.3, 0.875] | 58 | 28% (18-40) | -1.65 | -4.12 | -239 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.374] | 58 | 34% (24-47) | -0.94 | -2.78 | -161 |  |
| (2.374, 3.475] | 57 | 44% (32-57) | -0.25 | -2.21 | -126 |  |
| (3.475, 18.762] | 58 | 31% (21-44) | -1.28 | -3.34 | -194 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0964] | 58 | 45% (33-58) | +0.36 | -0.39 | -23 |  |
| (0.0964, 0.145] | 58 | 38% (27-51) | -1.19 | -2.51 | -146 |  |
| (0.145, 0.392] | 57 | 26% (17-39) | -1.66 | -5.48 | -312 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.719] | 16 | 31% (14-56) | -2.38 | -3.27 | -52 |  |
| (-0.719, 0.423] | 15 | 40% (20-64) | -1.50 | -1.97 | -30 |  |
| (0.423, 5.305] | 16 | 69% (44-86) | +1.04 | +0.43 | +7 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.48] | 18 | 39% (20-61) | -1.34 | -1.97 | -35 |  |
| (0.48, 0.613] | 18 | 44% (25-66) | -1.36 | -1.99 | -36 |  |
| (0.613, 1.74] | 18 | 56% (34-75) | -0.83 | -1.68 | -30 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.769] | 18 | 50% (29-71) | -0.50 | -0.90 | -16 |  |
| (0.769, 1.181] | 18 | 44% (25-66) | -1.41 | -2.19 | -39 |  |
| (1.181, 3.566] | 18 | 44% (25-66) | -1.62 | -2.56 | -46 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.316] | 18 | 28% (12-51) | -2.35 | -2.96 | -53 |  |
| (0.316, 0.483] | 18 | 61% (39-80) | +0.22 | -0.35 | -6 | ▲ |
| (0.483, 1.14] | 18 | 50% (29-71) | -1.40 | -2.33 | -42 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.16%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 46%
- Exit mix: stop 78, trail_stop 66, time_stop 27, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0964] | 58 | 33% | 28% | 38% |
| (0.0964, 0.145] | 58 | 50% | 43% | 5% |
| (0.145, 0.392] | 57 | 53% | 44% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
