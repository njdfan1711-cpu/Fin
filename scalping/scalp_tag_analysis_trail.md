# Scalp signal analysis (trail exits)

_110 tagged trades, 7 trading days (2026-10-01 to 2026-10-09). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 110 | 38% (30-48) | +0.39 | -1.52 | -167 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 37 | +81 | +2.19 | 73 | -248 | -3.39 | -81 |
| skip first 30 min | 27 | +32 | +1.20 | 83 | -199 | -2.40 | -32 |
| skip when SPY is down on the day | 33 | -56 | -1.68 | 77 | -111 | -1.44 | +56 |
| skip when SPY is below its VWAP | 34 | -83 | -2.43 | 76 | -84 | -1.11 | +83 |
| skip when SPY fell over the last 15 min | 32 | -41 | -1.27 | 78 | -126 | -1.62 | +41 |
| skip over-extended (30-min run in top quarter, > 0.45%) | 21 | -84 | -4.00 | 89 | -83 | -0.93 | +84 |
| skip stock not beating SPY over 15 min | 10 | -36 | -3.59 | 100 | -131 | -1.31 | +36 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 58 | -142 | -2.45 | 52 | -25 | -0.48 | +142 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 0-15 | 27 | 44% (28-63) | +2.27 | +1.20 | +32 |  |
| 15-60 | 11 | 55% (28-79) | +1.16 | -1.79 | -20 |  |
| 60-240 | 39 | 26% (15-41) | -1.31 | -2.91 | -114 |  |
| 240-375 | 23 | 35% (19-55) | -2.36 | -4.98 | -115 |  |
| 375-390 | 10 | 60% (31-83) | +7.35 | +4.86 | +49 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 9 | 22% (6-55) | -1.58 | -3.70 | -33 | few trades |
| -0.2 to 0 | 24 | 42% (24-61) | +1.45 | -0.93 | -22 |  |
| 0 to 0.2 | 43 | 33% (20-47) | -1.01 | -2.40 | -103 |  |
| > 0.2 | 34 | 47% (31-63) | +1.92 | -0.23 | -8 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 34 | 29% (17-46) | -0.14 | -2.43 | -83 |  |
| above VWAP | 76 | 42% (32-53) | +0.62 | -1.11 | -84 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.136] | 28 | 32% (18-51) | +0.95 | -0.67 | -19 |  |
| (0.136, 0.372] | 27 | 44% (28-63) | -1.14 | -3.46 | -94 |  |
| (0.372, 1.123] | 28 | 32% (18-51) | -0.53 | -3.10 | -87 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.719, 0.189] | 28 | 43% (27-61) | +2.06 | +0.45 | +13 |  |
| (0.189, 0.406] | 27 | 30% (16-48) | -1.53 | -4.10 | -111 |  |
| (0.406, 1.022] | 28 | 36% (21-54) | -1.26 | -3.61 | -101 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.174, -0.0763] | 37 | 32% (20-49) | -0.94 | -3.56 | -132 |  |
| (-0.0763, 0.335] | 36 | 44% (30-60) | +2.02 | +0.67 | +24 |  |
| (0.335, 2.633] | 37 | 38% (24-54) | +0.11 | -1.61 | -59 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.0029, 0.0583] | 37 | 43% (29-59) | -0.70 | -2.37 | -88 |  |
| (0.0583, 0.142] | 36 | 39% (25-55) | +0.89 | -0.79 | -29 |  |
| (0.142, 0.786] | 37 | 32% (20-49) | +0.97 | -1.37 | -51 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.153, 0.218] | 37 | 49% (33-64) | +1.61 | +0.40 | +15 |  |
| (0.218, 0.422] | 36 | 28% (16-44) | -1.37 | -4.17 | -150 |  |
| (0.422, 3.871] | 37 | 38% (24-54) | +0.86 | -0.85 | -31 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0060000000000002, 2.562] | 37 | 43% (29-59) | -0.10 | -2.28 | -84 |  |
| (2.562, 5.075] | 36 | 36% (22-52) | +0.79 | -1.17 | -42 |  |
| (5.075, 18.76] | 37 | 35% (22-51) | +0.48 | -1.09 | -40 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0956] | 37 | 49% (33-64) | +1.75 | +1.05 | +39 |  |
| (0.0956, 0.145] | 37 | 38% (24-54) | -0.94 | -2.27 | -84 |  |
| (0.145, 0.392] | 36 | 28% (16-44) | +0.34 | -3.38 | -122 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.15% | median worst: -0.17%
- Reached +0.175% at some point: 48% of trades
- Reached +0.35% at some point: 16% of trades
- Reached +0.5% at some point: 6% of trades
- Reached +0.75% at some point: 4% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 49, trail_stop 44, time_stop 17

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0956] | 37 | 27% | 41% | 32% |
| (0.0956, 0.145] | 37 | 51% | 41% | 8% |
| (0.145, 0.392] | 36 | 56% | 39% | 6% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
