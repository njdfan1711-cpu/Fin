# Scalp signal analysis (trail exits)

_167 tagged trades, 11 trading days (2026-10-01 to 2026-10-15). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 167 | 35% (28-43) | -0.45 | -2.29 | -382 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 60 | -6 | -0.09 | 107 | -376 | -3.52 | +6 |
| skip first 30 min | 41 | -19 | -0.47 | 126 | -363 | -2.88 | +19 |
| skip when SPY is down on the day | 59 | -138 | -2.35 | 108 | -244 | -2.26 | +138 |
| skip when SPY is below its VWAP | 56 | -144 | -2.57 | 111 | -238 | -2.15 | +144 |
| skip when SPY fell over the last 15 min | 51 | -129 | -2.52 | 116 | -253 | -2.19 | +129 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 32 | -155 | -4.84 | 135 | -227 | -1.68 | +155 |
| skip stock not beating SPY over 15 min | 14 | -41 | -2.93 | 153 | -341 | -2.23 | +41 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 86 | -246 | -2.86 | 81 | -136 | -1.68 | +246 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 41 | 37% (24-52) | +0.51 | -0.47 | -19 |  |
| 15-60 | 17 | 53% (31-74) | +0.73 | -1.74 | -30 |  |
| 60-240 | 51 | 27% (17-41) | -1.47 | -3.15 | -161 |  |
| 240-375 | 39 | 33% (21-49) | -2.38 | -4.77 | -186 |  |
| 375-390 | 19 | 42% (23-64) | +3.14 | +0.73 | +14 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 15 | 33% (15-58) | -1.12 | -2.62 | -39 |  |
| -0.2 to 0 | 44 | 36% (24-51) | +0.07 | -2.25 | -99 |  |
| 0 to 0.2 | 67 | 28% (19-40) | -1.64 | -2.98 | -200 |  |
| > 0.2 | 41 | 46% (32-61) | +1.19 | -1.07 | -44 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 56 | 30% (20-43) | -0.40 | -2.57 | -144 |  |
| above VWAP | 111 | 38% (29-47) | -0.47 | -2.15 | -238 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 42 | 33% (21-48) | +0.51 | -1.43 | -60 |  |
| (0.136, 0.371] | 42 | 43% (29-58) | -1.30 | -3.31 | -139 |  |
| (0.371, 1.555] | 42 | 29% (17-44) | -1.48 | -3.89 | -163 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.153] | 42 | 40% (27-56) | +0.85 | -0.83 | -35 |  |
| (0.153, 0.408] | 42 | 36% (23-51) | -0.78 | -3.27 | -137 |  |
| (0.408, 1.192] | 42 | 29% (17-44) | -2.34 | -4.53 | -190 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.101] | 56 | 38% (26-51) | -0.65 | -2.96 | -166 |  |
| (-0.101, 0.374] | 55 | 45% (33-58) | +0.97 | -0.19 | -10 |  |
| (0.374, 2.726] | 56 | 23% (14-36) | -1.64 | -3.67 | -206 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0605] | 56 | 41% (29-54) | -0.28 | -1.79 | -100 |  |
| (0.0605, 0.136] | 55 | 38% (27-51) | -0.74 | -2.52 | -139 |  |
| (0.136, 0.786] | 56 | 27% (17-40) | -0.32 | -2.55 | -143 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.15, 0.224] | 56 | 45% (32-58) | +0.45 | -0.68 | -38 |  |
| (0.224, 0.417] | 55 | 29% (19-42) | -1.78 | -4.38 | -241 |  |
| (0.417, 3.871] | 56 | 32% (21-45) | -0.04 | -1.84 | -103 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.623] | 56 | 39% (28-52) | -0.68 | -2.64 | -148 |  |
| (2.623, 4.926] | 55 | 40% (28-53) | +0.55 | -1.46 | -80 |  |
| (4.926, 18.76] | 56 | 27% (17-40) | -1.20 | -2.75 | -154 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0956] | 56 | 45% (32-58) | +0.38 | -0.28 | -16 |  |
| (0.0956, 0.145] | 56 | 36% (24-49) | -1.32 | -2.65 | -149 |  |
| (0.145, 0.392] | 55 | 25% (16-38) | -0.41 | -3.96 | -218 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.13% | median worst: -0.20%
- Reached +0.175% at some point: 45% of trades
- Reached +0.35% at some point: 13% of trades
- Reached +0.5% at some point: 5% of trades
- Reached +0.75% at some point: 2% of trades
- Fell to -0.20% or worse at some point: 50%
- Exit mix: stop 82, trail_stop 62, time_stop 23

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0956] | 56 | 36% | 32% | 32% |
| (0.0956, 0.145] | 56 | 54% | 41% | 5% |
| (0.145, 0.392] | 55 | 58% | 38% | 4% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
