# Scalp signal analysis (trail exits)

_181 tagged trades, 20 trading days (2026-10-01 to 2026-10-28). Costs: measured median spread per symbol (flat 2c fallback)._

**Hypotheses, not findings.** Many features are tested on a small sample from a few days of one market regime, and trades cluster in time and in a few symbols. ▲/▼ mean the win-rate interval excludes the baseline. Do not retune thresholds from this yet.

## Baseline
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| all trades | 181 | 37% (30-44) | -0.79 | -2.69 | -487 |  |

## What-if filters (judged by what they would have removed)

A rule helps when the *removed* trades have a clearly negative average net and the total net of the kept trades improves.

| rule | removed | removed total net | removed avg net | kept | kept total net | kept avg net | change in total net |
|---|--:|--:|--:|--:|--:|--:|--:|
| skip first 15 min and last 15 min | 25 | +12 | +0.47 | 156 | -499 | -3.20 | -12 |
| skip first 30 min | 1 | -6 | -6.31 | 180 | -481 | -2.67 | +6 |
| skip when SPY is down on the day | 70 | -240 | -3.43 | 111 | -247 | -2.22 | +240 |
| skip when SPY is below its VWAP | 75 | -287 | -3.83 | 106 | -200 | -1.89 | +287 |
| skip when SPY fell over the last 15 min | 68 | -177 | -2.60 | 113 | -310 | -2.75 | +177 |
| skip over-extended (30-min run in top quarter, > 0.47%) | 45 | -189 | -4.21 | 136 | -298 | -2.19 | +189 |
| skip stock not beating SPY over 15 min | 30 | -57 | -1.92 | 151 | -429 | -2.84 | +57 |
| skip afternoon entries (2:00-3:45 PM) | 37 | -202 | -5.45 | 144 | -285 | -1.98 | +202 |
| skip volume spikes above 5x average | 33 | -155 | -4.70 | 148 | -332 | -2.24 | +155 |
| skip when the stop is inside normal noise (range > stop) | 7 | -9 | -1.25 | 174 | -478 | -2.75 | +9 |
| skip entries after a big burst (10-min bounce in top quarter, > 0.56%) | 16 | -63 | -3.92 | 165 | -424 | -2.57 | +63 |
| trade only tight spreads (<= 0.03%) -- unmeasured symbols kept | 100 | -362 | -3.62 | 81 | -125 | -1.55 | +362 |

## Results by market condition

### Minutes since the open
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| 15-60 | 25 | 56% (37-73) | +0.76 | -1.43 | -36 | ▲ |
| 60-240 | 81 | 33% (24-44) | -1.29 | -2.82 | -228 |  |
| 240-375 | 50 | 32% (21-46) | -2.45 | -4.70 | -235 |  |
| 375-390 | 25 | 40% (23-59) | +2.61 | +0.47 | +12 |  |

### SPY return since the open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| < -0.2 | 24 | 33% (18-53) | -1.26 | -3.01 | -72 |  |
| -0.2 to 0 | 46 | 37% (25-51) | -1.34 | -3.65 | -168 |  |
| 0 to 0.2 | 53 | 34% (23-47) | -1.37 | -2.84 | -151 |  |
| > 0.2 | 58 | 41% (30-54) | +0.38 | -1.66 | -96 |  |

### SPY vs its VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| below VWAP | 75 | 28% (19-39) | -1.71 | -3.83 | -287 |  |
| above VWAP | 106 | 43% (34-53) | -0.14 | -1.89 | -200 |  |

### Stock minus SPY, last 15 min (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.512, 0.132] | 61 | 38% (27-50) | +0.21 | -1.26 | -77 |  |
| (0.132, 0.368] | 60 | 45% (33-58) | -0.76 | -2.58 | -155 |  |
| (0.368, 1.555] | 60 | 28% (19-41) | -1.83 | -4.25 | -255 |  |

### Stock move over the last 30 min (%) -- how extended
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.795, 0.147] | 60 | 40% (29-53) | +0.22 | -1.41 | -85 |  |
| (0.147, 0.408] | 60 | 42% (30-54) | -0.61 | -2.62 | -157 |  |
| (0.408, 1.281] | 60 | 30% (20-43) | -1.89 | -3.98 | -239 |  |

### Stock move since its day open (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-4.589, -0.288] | 61 | 36% (25-49) | -1.18 | -3.40 | -207 |  |
| (-0.288, 0.364] | 60 | 47% (35-59) | +0.97 | -0.30 | -18 |  |
| (0.364, 2.726] | 60 | 28% (19-41) | -2.15 | -4.36 | -262 |  |

### Entry distance above VWAP (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-0.0006000000000000001, 0.0518] | 61 | 39% (28-52) | -1.05 | -2.71 | -165 |  |
| (0.0518, 0.119] | 60 | 40% (29-53) | +0.40 | -1.14 | -69 |  |
| (0.119, 0.678] | 60 | 32% (21-44) | -1.71 | -4.22 | -253 |  |

### 3-minute momentum at entry (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.149, 0.201] | 61 | 44% (33-57) | +0.28 | -0.97 | -59 |  |
| (0.201, 0.306] | 60 | 40% (29-53) | -0.79 | -2.82 | -169 |  |
| (0.306, 0.875] | 60 | 27% (17-39) | -1.87 | -4.31 | -259 |  |

### Volume vs 20-minute average (x)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (2.0, 2.389] | 61 | 38% (27-50) | -0.62 | -2.43 | -148 |  |
| (2.389, 3.502] | 60 | 45% (33-58) | +0.86 | -1.04 | -62 |  |
| (3.502, 18.762] | 60 | 28% (19-41) | -2.60 | -4.60 | -276 |  |

### Recent volatility (avg 1-min range, % of price)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.033299999999999996, 0.0963] | 61 | 46% (34-58) | +0.51 | -0.24 | -15 |  |
| (0.0963, 0.145] | 60 | 40% (29-53) | -1.01 | -2.28 | -137 |  |
| (0.145, 0.392] | 60 | 25% (16-37) | -1.88 | -5.59 | -336 |  |

### Gap at the open vs yesterday's close (%)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (-6.706, -0.53] | 19 | 26% (12-49) | -2.93 | -3.82 | -73 |  |
| (-0.53, 0.474] | 18 | 50% (29-71) | +0.07 | -0.45 | -8 |  |
| (0.474, 5.305] | 18 | 67% (44-84) | +0.61 | -0.05 | -1 | ▲ |

### Recent 1-min range / stop distance (x; > 1 = stop inside noise)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.223, 0.476] | 21 | 43% (24-63) | -0.67 | -1.32 | -28 |  |
| (0.476, 0.616] | 20 | 45% (26-66) | -1.35 | -1.98 | -40 |  |
| (0.616, 1.74] | 21 | 52% (32-72) | -1.04 | -1.95 | -41 |  |

### Distance below the day's high so far (%; 0 = at the high)
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.173, 0.789] | 21 | 52% (32-72) | -0.47 | -0.88 | -19 |  |
| (0.789, 1.196] | 20 | 40% (22-61) | -1.31 | -2.15 | -43 |  |
| (1.196, 3.566] | 21 | 48% (28-68) | -1.28 | -2.22 | -47 |  |

### Bounce off the last 10 minutes' low (%) -- buying after the burst
| bucket | trades | win% (95% CI) | avg gross | avg net | total net | |
|---|--:|---|--:|--:|--:|---|
| (0.216, 0.318] | 21 | 33% (17-55) | -1.69 | -2.26 | -47 |  |
| (0.318, 0.532] | 20 | 65% (43-82) | +0.62 | -0.07 | -1 | ▲ |
| (0.532, 1.14] | 21 | 43% (24-63) | -1.90 | -2.83 | -59 |  |

## Price path after entry (for tuning exits)

- Median best price reached: +0.12% | median worst: -0.15%
- Reached +0.175% at some point: 44% of trades
- Reached +0.35% at some point: 9% of trades
- Reached +0.5% at some point: 2% of trades
- Reached +0.75% at some point: 1% of trades
- Fell to -0.20% or worse at some point: 45%
- Exit mix: stop 81, trail_stop 69, time_stop 29, eod 2

Stop-outs by volatility (a fixed 0.20% stop may be too tight for jumpy stocks):

| volatility bucket | trades | stopped out | hit target / trail | timed out |
|---|--:|--:|--:|--:|
| (0.033299999999999996, 0.0963] | 61 | 31% | 28% | 39% |
| (0.0963, 0.145] | 60 | 48% | 45% | 5% |
| (0.145, 0.392] | 60 | 55% | 42% | 3% |

_Limits: tags exist only for trades found since tagging began (yfinance keeps 7 days of 1-minute bars). The backtest allows one position per symbol at a time, while the live bot will hold one position in total, so competing simultaneous signals are all counted here._
