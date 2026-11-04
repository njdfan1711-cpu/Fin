# Fin swing-track scorecard
_Generated: 2026-11-04 UTC_  
_Window: 2026-08-19 to 2026-10-28 (51 push days). 1765 ticker-days (415 distinct tickers), from 12560 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=1765, stop 34%, target 5%, avg R -0.07, win 45% (42-47%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 1234 | 238 | 36 | 5 | -0.07 | +0.00 | 45 (42-48) |  |
| `cats:3` | 531 | 230 | 29 | 5 | -0.08 | -0.00 | 43 (39-47) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 531 | 230 | 29 | 5 | -0.08 | -0.00 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 1591 | 346 | 35 | 5 | -0.08 | -0.01 | 44 (42-47) |  |
| `tech:above_rising_50_200ma` | 1326 | 240 | 33 | 5 | -0.04 | +0.03 | 47 (44-49) |  |
| `tech:rsi_overbought` | 916 | 234 | 40 | 5 | -0.15 | -0.08 | 41 (38-44) | ▼ |
| `tech:rs_line_new_high` | 611 | 155 | 35 | 4 | -0.06 | +0.02 | 45 (41-49) |  |
| `tech:all_time_high` | 362 | 86 | 31 | 2 | -0.04 | +0.03 | 47 (42-52) |  |
| `tech:52wk_high_below_ath` | 338 | 111 | 38 | 6 | -0.09 | -0.02 | 44 (39-49) |  |
| `tech:macd_bullish_cross` | 125 | 76 | 30 | 6 | -0.03 | +0.05 | 46 (38-55) |  |
| `tech:ma_20_50_cross` | 115 | 80 | 34 | 8 | +0.01 | +0.08 | 50 (41-59) |  |
| `tech:rsi_oversold` | 101 | 74 | 28 | 8 | +0.03 | +0.10 | 47 (37-56) |  |
| `tech:52wk_high_vol_confirmed` | 96 | 68 | 44 | 5 | -0.16 | -0.08 | 40 (30-50) |  |
| `tech:volume_spike` | 77 | 58 | 39 | 8 | -0.13 | -0.06 | 40 (30-51) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 1457 | 307 | 35 | 4 | -0.07 | -0.00 | 45 (42-48) |  |
| `fund:eps_growth` | 1419 | 287 | 34 | 5 | -0.05 | +0.02 | 46 (43-48) |  |
| `fund:quality_passed` | 1200 | 211 | 35 | 5 | -0.05 | +0.02 | 45 (42-48) |  |
| `fund:analyst_improving` | 343 | 77 | 32 | 3 | -0.08 | -0.01 | 44 (39-50) |  |
| `fund:earnings_beat` | 77 | 47 | 26 | 9 | +0.05 | +0.12 | 48 (37-59) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 743 | 197 | 37 | 4 | -0.11 | -0.04 | 42 (39-46) |  |
| `atr:high(>=4.5%)` | 557 | 153 | 32 | 5 | -0.07 | +0.00 | 46 (42-50) |  |
| `atr:low(<3%)` | 465 | 146 | 33 | 5 | -0.02 | +0.06 | 46 (42-51) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 644 | 145 | 33 | 4 | -0.04 | +0.03 | 46 (42-50) |  |
| `caut:extended_above_ma` | 303 | 88 | 46 | 4 | -0.29 | -0.21 | 32 (27-38) | ▼ |
| `caut:chase` | 232 | 92 | 38 | 4 | -0.06 | +0.01 | 46 (39-52) |  |
| `caut:negative_net_margin` | 125 | 45 | 33 | 6 | -0.08 | -0.00 | 43 (35-52) |  |
| `caut:analyst_deteriorating` | 89 | 39 | 31 | 1 | -0.19 | -0.12 | 34 (25-44) | ▼ |
| `caut:earnings_soon` | 51 | 32 | 51 | 16 | -0.11 | -0.04 | 35 (24-49) |  |
| `caut:earnings_today` | 47 | 42 | 47 | 9 | -0.21 | -0.14 | 32 (20-46) |  |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.67 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 159 | 77 | 36 | 6 | -0.13 | -0.06 | 40 (32-47) |  |
| `volhi:normal_adj(0.8-1.5x)` | 127 | 76 | 28 | 5 | -0.05 | +0.03 | 44 (36-53) |  |
| `volhi:high_adj(>=1.5x)` | 83 | 60 | 43 | 8 | -0.21 | -0.13 | 37 (28-48) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:midday` | 642 | 290 | 32 | 6 | -0.11 | -0.04 | 42 (38-46) |  |
| `time:pre_open` | 569 | 177 | 36 | 3 | -0.04 | +0.03 | 48 (44-52) |  |
| `time:open_hour` | 350 | 182 | 34 | 5 | -0.02 | +0.05 | 46 (41-51) |  |
| `time:after_close` | 98 | 81 | 38 | 4 | -0.20 | -0.13 | 37 (28-47) |  |
| `time:late_session` | 69 | 57 | 26 | 6 | -0.01 | +0.06 | 46 (35-58) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:recurring(2-4d)` | 198 | 83 | 36 | 3 | -0.03 | +0.05 | 51 (44-57) |  |
| `age:stale(5d+)` | 182 | 40 | 51 | 1 | -0.39 | -0.31 | 35 (28-42) | ▼ |
| `runup:<2%` | 178 | 77 | 43 | 2 | -0.17 | -0.10 | 44 (37-52) |  |
| `age:new(1d)` | 157 | 117 | 35 | 8 | +0.04 | +0.12 | 51 (43-59) |  |
| `runup:2-5%` | 110 | 47 | 33 | 4 | -0.04 | +0.04 | 51 (42-60) |  |
| `runup:>=5%` | 88 | 35 | 56 | 0 | -0.43 | -0.36 | 31 (22-41) | ▼ |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 533/807 (66%, 95% CI 63-69%); stop first: 226 (28%)
- Median best price in window: +3.6% vs entry

_47 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
