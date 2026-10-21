# Fin swing-track scorecard
_Generated: 2026-10-21 UTC_  
_Window: 2026-08-19 to 2026-10-14 (41 push days). 1408 ticker-days (370 distinct tickers), from 9380 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=1408, stop 36%, target 5%, avg R -0.11, win 42% (39-44%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 877 | 183 | 40 | 4 | -0.13 | -0.02 | 41 (38-44) |  |
| `cats:3` | 531 | 230 | 29 | 5 | -0.08 | +0.03 | 43 (39-47) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 531 | 230 | 29 | 5 | -0.08 | +0.03 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 1237 | 299 | 37 | 4 | -0.12 | -0.01 | 41 (39-44) |  |
| `tech:above_rising_50_200ma` | 1046 | 210 | 35 | 5 | -0.08 | +0.03 | 43 (41-47) |  |
| `tech:rsi_overbought` | 654 | 188 | 45 | 4 | -0.24 | -0.14 | 35 (31-39) | ▼ |
| `tech:rs_line_new_high` | 462 | 128 | 38 | 4 | -0.12 | -0.02 | 41 (36-45) |  |
| `tech:52wk_high_below_ath` | 267 | 88 | 40 | 6 | -0.12 | -0.02 | 42 (36-48) |  |
| `tech:all_time_high` | 253 | 72 | 36 | 2 | -0.13 | -0.02 | 41 (35-47) |  |
| `tech:macd_bullish_cross` | 102 | 66 | 30 | 7 | +0.00 | +0.11 | 47 (38-57) |  |
| `tech:rsi_oversold` | 101 | 74 | 28 | 8 | +0.03 | +0.14 | 47 (37-56) |  |
| `tech:52wk_high_vol_confirmed` | 64 | 48 | 45 | 5 | -0.19 | -0.08 | 38 (27-50) |  |
| `tech:volume_spike` | 62 | 49 | 37 | 8 | -0.10 | +0.00 | 42 (30-54) |  |
| `tech:ma_20_50_cross` | 58 | 42 | 43 | 7 | -0.19 | -0.08 | 36 (25-49) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 1151 | 270 | 37 | 5 | -0.10 | +0.00 | 42 (40-45) |  |
| `fund:eps_growth` | 1090 | 247 | 36 | 5 | -0.09 | +0.02 | 43 (40-46) |  |
| `fund:quality_passed` | 896 | 179 | 38 | 5 | -0.10 | +0.00 | 42 (38-45) |  |
| `fund:analyst_improving` | 285 | 68 | 33 | 2 | -0.10 | +0.01 | 43 (37-49) |  |
| `fund:earnings_beat` | 55 | 33 | 27 | 7 | -0.04 | +0.07 | 44 (31-57) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 602 | 174 | 38 | 4 | -0.13 | -0.02 | 41 (37-45) |  |
| `atr:high(>=4.5%)` | 491 | 145 | 32 | 5 | -0.08 | +0.02 | 45 (40-49) |  |
| `atr:low(<3%)` | 315 | 115 | 38 | 5 | -0.11 | -0.00 | 40 (35-46) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 496 | 123 | 36 | 4 | -0.11 | +0.00 | 42 (38-47) |  |
| `caut:extended_above_ma` | 279 | 83 | 47 | 4 | -0.32 | -0.21 | 30 (25-35) | ▼ |
| `caut:negative_net_margin` | 122 | 45 | 32 | 6 | -0.06 | +0.05 | 44 (36-53) |  |
| `caut:chase` | 103 | 48 | 51 | 2 | -0.31 | -0.20 | 34 (26-44) |  |
| `caut:analyst_deteriorating` | 69 | 34 | 33 | 1 | -0.25 | -0.14 | 30 (21-42) |  |
| `caut:earnings_today` | 40 | 35 | 48 | 8 | -0.21 | -0.10 | 32 (20-48) |  |
| `caut:earnings_soon` | 31 | 20 | 55 | 6 | -0.33 | -0.22 | 26 (14-43) |  |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.63 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 128 | 66 | 36 | 4 | -0.20 | -0.09 | 35 (27-44) |  |
| `volhi:normal_adj(0.8-1.5x)` | 117 | 67 | 29 | 5 | -0.06 | +0.05 | 43 (34-52) |  |
| `volhi:high_adj(>=1.5x)` | 76 | 53 | 43 | 9 | -0.20 | -0.10 | 37 (27-48) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:midday` | 600 | 271 | 33 | 6 | -0.13 | -0.03 | 40 (36-44) |  |
| `time:pre_open` | 376 | 129 | 39 | 3 | -0.05 | +0.05 | 46 (41-51) |  |
| `time:open_hour` | 237 | 137 | 37 | 4 | -0.11 | -0.00 | 40 (34-46) |  |
| `time:after_close` | 94 | 77 | 37 | 4 | -0.19 | -0.09 | 37 (28-47) |  |
| `time:late_session` | 64 | 52 | 27 | 6 | +0.01 | +0.12 | 47 (35-59) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:stale(5d+)` | 69 | 20 | 84 | 0 | -0.79 | -0.68 | 14 (8-25) | ▼ |
| `runup:<2%` | 58 | 29 | 71 | 2 | -0.59 | -0.49 | 19 (11-31) | ▼ |
| `age:new(1d)` | 57 | 48 | 53 | 2 | -0.24 | -0.13 | 39 (27-52) |  |
| `age:recurring(2-4d)` | 54 | 28 | 57 | 2 | -0.42 | -0.31 | 28 (18-41) | ▼ |
| `runup:>=5%` | 38 | 13 | 84 | 0 | -0.85 | -0.74 | 8 (3-21) | ▼ |
| `runup:2-5%` | 23 | 14 | 57 | 0 | -0.35 | -0.24 | 43 (26-63) | insufficient data |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 278/450 (62%, 95% CI 57-66%); stop first: 152 (34%)
- Median best price in window: +3.7% vs entry

_47 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
