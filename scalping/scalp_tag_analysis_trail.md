# Scalp signal analysis (trail exits)

_147 tagged trades, 14 trading days (2026-10-01 to 2026-10-20). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 147 | 33% (26-41) | -0.93 | -3.11 | -458 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 22 | +4 | +0.20 | 125 | -462 | -3.70 | -4 |
| skip first 30 min | 1 | -6 | -6.31 | 146 | -451 | -3.09 | +6 |
| skip when SPY is down on the day | 57 | -255 | -4.48 | 90 | -202 | -2.25 | +255 |
| skip when SPY is below its VWAP | 59 | -274 | -4.65 | 88 | -183 | -2.08 | +274 |
| skip when SPY fell over the last 15 min | 58 | -181 | -3.13 | 89 | -276 | -3.10 | +181 |
| skip over-extended (30-min run in top quarter, > 0.46%) | 37 | -181 | -4.90 | 110 | -276 | -2.51 | +181 |
| skip stock not beating SPY over 15 min | 21 | -61 | -2.89 | 126 | -397 | -3.15 | +61 |
| skip afternoon entries (2:00-3:45 PM) | 32 | -188 | -5.88 | 115 | -269 | -2.34 | +188 |
| skip volume spikes above 5x average | 26 | -138 | -5.30 | 121 | -320 | -2.64 | +138 |
| skip when the stop is inside normal noise (range > stop) | 4 | -2 | -0.40 | 143 | -456 | -3.19 | +2 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 7 | -25 | -3.56 | 140 | -433 | -3.09 | +25 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 90 | -362 | -4.03 | 57 | -95 | -1.67 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 20 | 50% (30-70) | +0.07 | -2.52 | -50 |  |
| 60-240 | 62 | 29% (19-41) | -1.36 | -3.13 | -194 |  |
| 240-375 | 43 | 30% (19-45) | -2.56 | -5.06 | -217 |  |
| 375-390 | 22 | 36% (20-57) | +2.58 | +0.20 | +4 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 22 | 32% (16-53) | -1.38 | -3.24 | -71 |  |
| -0.2 to 0 | 35 | 26% (14-42) | -2.49 | -5.26 | -184 |  |
| 0 to 0.2 | 41 | 32% (20-47) | -1.18 | -2.84 | -116 |  |
| > 0.2 | 49 | 41% (28-55) | +0.59 | -1.75 | -86 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 59 | 22% (13-34) | -2.12 | -4.65 | -274 |  |
| above VWAP | 88 | 41% (31-51) | -0.13 | -2.08 | -183 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.133] | 49 | 31% (20-45) | +0.10 | -1.62 | -79 |  |
| (0.133, 0.371] | 49 | 43% (30-57) | -1.10 | -3.23 | -158 |  |
| (0.371, 1.555] | 49 | 27% (16-40) | -1.79 | -4.49 | -220 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 49 | 33% (21-47) | -0.10 | -1.99 | -97 |  |
| (0.147, 0.404] | 48 | 38% (25-52) | -0.65 | -2.99 | -144 |  |
| (0.404, 1.192] | 49 | 31% (20-45) | -1.94 | -4.29 | -210 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.266] | 49 | 33% (21-47) | -1.38 | -3.95 | -193 |  |
| (-0.266, 0.348] | 49 | 47% (34-61) | +1.08 | -0.34 | -17 | ▲ |
| (0.348, 2.726] | 49 | 20% (11-34) | -2.49 | -5.05 | -247 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.052] | 49 | 33% (21-47) | -1.67 | -3.53 | -173 |  |
| (0.052, 0.123] | 49 | 37% (25-51) | +0.50 | -1.61 | -79 |  |
| (0.123, 0.678] | 49 | 31% (20-45) | -1.63 | -4.19 | -205 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.198] | 49 | 43% (30-57) | +0.36 | -0.98 | -48 |  |
| (0.198, 0.309] | 49 | 29% (18-42) | -1.47 | -3.93 | -192 |  |
| (0.309, 0.875] | 49 | 29% (18-42) | -1.68 | -4.43 | -217 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.407] | 49 | 35% (23-49) | -0.85 | -3.05 | -150 |  |
| (2.407, 3.448] | 49 | 41% (28-55) | -0.50 | -2.52 | -123 |  |
| (3.448, 18.76] | 49 | 24% (15-38) | -1.44 | -3.77 | -185 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0946] | 50 | 44% (31-58) | +0.55 | -0.21 | -11 |  |
| (0.0946, 0.148] | 48 | 31% (20-45) | -1.79 | -3.29 | -158 |  |
| (0.148, 0.392] | 49 | 24% (15-38) | -1.60 | -5.90 | -289 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-5.5520000000000005, -1.088] | 7 | 43% (16-75) | -1.99 | -3.05 | -21 | few trades |
| (-1.088, 0.281] | 7 | 0% (0-35) | -4.62 | -5.15 | -36 | few trades |
| (0.281, 5.305] | 7 | 71% (36-92) | +1.25 | +0.77 | +5 | few trades |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.449] | 10 | 30% (11-60) | -2.33 | -3.08 | -31 |  |
| (0.449, 0.6] | 9 | 22% (6-55) | -3.51 | -4.28 | -39 | few trades |
| (0.6, 1.74] | 9 | 67% (35-88) | -0.24 | -1.04 | -9 | few trades |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.261, 0.736] | 10 | 40% (17-69) | -1.81 | -2.31 | -23 |  |
| (0.736, 1.136] | 9 | 33% (12-65) | -2.04 | -2.97 | -27 | few trades |
| (1.136, 3.566] | 9 | 44% (19-73) | -2.28 | -3.20 | -29 | few trades |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.296] | 10 | 10% (2-40) | -3.39 | -3.98 | -40 |  |
| (0.296, 0.508] | 9 | 56% (27-81) | -1.22 | -1.97 | -18 | few trades |
| (0.508, 0.815] | 9 | 56% (27-81) | -1.36 | -2.35 | -21 | few trades |

## Price path after entry (for tuning exits)

- Median best price reached: +0.11% | median worst: -0.17%
- Reached +0.175% at some point: 42% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 48%
- Exit mix: stop 69, trail_stop 54, time_stop 23, eod 1

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0946] | 50 | 32% | 30% | 36% |
| (0.0946, 0.148] | 48 | 56% | 38% | 6% |
| (0.148, 0.392] | 49 | 53% | 43% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
