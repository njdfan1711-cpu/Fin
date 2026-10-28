# Fin swing-track scorecard
_Generated: 2026-10-28 UTC_  
_Window: 2026-08-19 to 2026-10-21 (46 push days). 1582 ticker-days (397 distinct tickers), from 10980 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=1582, stop 35%, target 4%, avg R -0.08, win 44% (41-46%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 1051 | 212 | 37 | 4 | -0.08 | -0.00 | 44 (41-47) |  |
| `cats:3` | 531 | 230 | 29 | 5 | -0.08 | +0.01 | 43 (39-47) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 531 | 230 | 29 | 5 | -0.08 | +0.01 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 1409 | 326 | 36 | 4 | -0.09 | -0.01 | 43 (41-46) |  |
| `tech:above_rising_50_200ma` | 1174 | 228 | 34 | 5 | -0.05 | +0.04 | 46 (43-49) |  |
| `tech:rsi_overbought` | 784 | 214 | 41 | 4 | -0.18 | -0.09 | 39 (36-42) | ▼ |
| `tech:rs_line_new_high` | 531 | 141 | 35 | 4 | -0.07 | +0.02 | 44 (39-48) |  |
| `tech:all_time_high` | 309 | 81 | 32 | 2 | -0.05 | +0.03 | 45 (40-51) |  |
| `tech:52wk_high_below_ath` | 295 | 96 | 38 | 5 | -0.09 | -0.01 | 43 (38-49) |  |
| `tech:macd_bullish_cross` | 113 | 72 | 32 | 6 | -0.04 | +0.05 | 45 (36-54) |  |
| `tech:rsi_oversold` | 101 | 74 | 28 | 8 | +0.03 | +0.11 | 47 (37-56) |  |
| `tech:ma_20_50_cross` | 81 | 57 | 36 | 7 | -0.01 | +0.07 | 46 (35-56) |  |
| `tech:52wk_high_vol_confirmed` | 78 | 58 | 42 | 5 | -0.15 | -0.07 | 38 (28-50) |  |
| `tech:volume_spike` | 68 | 53 | 37 | 9 | -0.09 | -0.01 | 41 (30-53) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 1304 | 293 | 36 | 4 | -0.08 | +0.00 | 44 (41-47) |  |
| `fund:eps_growth` | 1252 | 271 | 35 | 5 | -0.06 | +0.02 | 45 (42-48) |  |
| `fund:quality_passed` | 1046 | 198 | 36 | 5 | -0.07 | +0.02 | 44 (41-47) |  |
| `fund:analyst_improving` | 312 | 70 | 33 | 2 | -0.10 | -0.02 | 44 (38-49) |  |
| `fund:earnings_beat` | 59 | 36 | 27 | 8 | -0.00 | +0.08 | 46 (34-58) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 663 | 183 | 37 | 4 | -0.12 | -0.04 | 42 (38-45) |  |
| `atr:high(>=4.5%)` | 529 | 150 | 32 | 5 | -0.08 | +0.00 | 45 (41-49) |  |
| `atr:low(<3%)` | 390 | 136 | 34 | 5 | -0.03 | +0.06 | 45 (40-50) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 566 | 135 | 34 | 4 | -0.05 | +0.03 | 45 (41-49) |  |
| `caut:extended_above_ma` | 293 | 85 | 46 | 4 | -0.30 | -0.22 | 31 (26-37) | ▼ |
| `caut:chase` | 165 | 71 | 38 | 2 | -0.07 | +0.01 | 46 (39-54) |  |
| `caut:negative_net_margin` | 123 | 45 | 32 | 6 | -0.06 | +0.02 | 44 (35-53) |  |
| `caut:analyst_deteriorating` | 80 | 35 | 32 | 1 | -0.18 | -0.10 | 34 (24-45) |  |
| `caut:earnings_today` | 40 | 35 | 48 | 8 | -0.21 | -0.13 | 32 (20-48) |  |
| `caut:earnings_soon` | 33 | 22 | 58 | 6 | -0.37 | -0.29 | 24 (13-41) | ▼ |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.66 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 141 | 70 | 36 | 4 | -0.19 | -0.10 | 37 (29-45) |  |
| `volhi:normal_adj(0.8-1.5x)` | 122 | 71 | 29 | 5 | -0.05 | +0.03 | 43 (34-51) |  |
| `volhi:high_adj(>=1.5x)` | 79 | 56 | 43 | 9 | -0.21 | -0.13 | 37 (27-48) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:midday` | 619 | 282 | 33 | 5 | -0.12 | -0.04 | 41 (37-45) |  |
| `time:pre_open` | 472 | 157 | 36 | 3 | -0.03 | +0.06 | 48 (44-53) | ▲ |
| `time:open_hour` | 294 | 164 | 35 | 4 | -0.05 | +0.03 | 44 (38-50) |  |
| `time:after_close` | 94 | 77 | 37 | 4 | -0.19 | -0.11 | 37 (28-47) |  |
| `time:late_session` | 66 | 54 | 27 | 6 | -0.00 | +0.08 | 47 (35-59) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:recurring(2-4d)` | 130 | 60 | 36 | 2 | -0.03 | +0.06 | 50 (42-58) |  |
| `runup:<2%` | 128 | 62 | 48 | 2 | -0.25 | -0.17 | 40 (32-49) |  |
| `age:stale(5d+)` | 117 | 31 | 63 | 0 | -0.53 | -0.45 | 28 (21-37) | ▼ |
| `age:new(1d)` | 107 | 87 | 40 | 5 | -0.04 | +0.04 | 46 (37-55) |  |
| `runup:2-5%` | 65 | 30 | 35 | 2 | -0.02 | +0.07 | 54 (42-65) |  |
| `runup:>=5%` | 50 | 18 | 66 | 0 | -0.60 | -0.51 | 22 (13-35) | ▼ |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 402/624 (64%, 95% CI 61-68%); stop first: 188 (30%)
- Median best price in window: +3.7% vs entry

_47 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
