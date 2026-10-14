# Fin swing-track scorecard
_Generated: 2026-10-14 UTC_  
_Window: 2026-08-19 to 2026-10-07 (36 push days). 1231 ticker-days (359 distinct tickers), from 7780 raw push records._

**How to read this.** One sample per ticker per day. Avg R is the headline (stop = -1R, full target = +2R, otherwise marked at the day-7 close). Win% is the share with R > 0, with a 95% Wilson interval. Anything under 30 samples is *insufficient data*. ▲/▼ means the win% interval excludes the baseline -- treat as a hypothesis, not a finding: with this many features tested, a few will look significant by chance, the sample is a few weeks of one market regime, and same-ticker repeats on consecutive days are correlated. Don't retune thresholds from this yet.

**Baseline (all):** n=1231, stop 31%, target 5%, avg R -0.05, win 44% (42-47%)

## Conviction
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cats:2` | 716 | 171 | 33 | 5 | -0.03 | +0.02 | 45 (42-49) |  |
| `cats:3` | 515 | 228 | 29 | 5 | -0.08 | -0.03 | 43 (39-47) |  |

## Signal categories
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `cat:news` | 515 | 228 | 29 | 5 | -0.08 | -0.03 | 43 (39-47) |  |

## Technical findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `tech:outperform_sp500` | 1068 | 289 | 32 | 5 | -0.05 | -0.00 | 44 (41-47) |  |
| `tech:above_rising_50_200ma` | 899 | 204 | 30 | 5 | -0.00 | +0.05 | 46 (43-50) |  |
| `tech:rsi_overbought` | 555 | 175 | 40 | 5 | -0.19 | -0.14 | 37 (33-41) | ▼ |
| `tech:rs_line_new_high` | 394 | 120 | 34 | 4 | -0.08 | -0.03 | 42 (37-47) |  |
| `tech:52wk_high_below_ath` | 240 | 85 | 38 | 6 | -0.10 | -0.06 | 42 (36-48) |  |
| `tech:all_time_high` | 199 | 64 | 29 | 3 | -0.04 | +0.01 | 44 (37-51) |  |
| `tech:rsi_oversold` | 95 | 69 | 27 | 8 | +0.01 | +0.06 | 45 (36-55) |  |
| `tech:macd_bullish_cross` | 94 | 61 | 29 | 7 | +0.03 | +0.08 | 48 (38-58) |  |
| `tech:volume_spike` | 60 | 47 | 37 | 8 | -0.11 | -0.06 | 42 (30-54) |  |
| `tech:52wk_high_vol_confirmed` | 53 | 41 | 49 | 4 | -0.30 | -0.25 | 30 (20-44) | ▼ |
| `tech:ma_20_50_cross` | 47 | 35 | 40 | 9 | -0.11 | -0.06 | 43 (30-57) |  |

## Fundamental findings
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `fund:revenue_growth` | 982 | 259 | 31 | 5 | -0.03 | +0.02 | 46 (43-49) |  |
| `fund:eps_growth` | 922 | 239 | 30 | 6 | -0.01 | +0.04 | 46 (43-50) |  |
| `fund:quality_passed` | 747 | 171 | 32 | 6 | -0.01 | +0.04 | 45 (42-49) |  |
| `fund:analyst_improving` | 258 | 67 | 27 | 3 | -0.03 | +0.02 | 47 (41-53) |  |
| `fund:earnings_beat` | 52 | 32 | 27 | 8 | -0.03 | +0.02 | 44 (32-58) |  |

## Volatility (ATR % of price)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `atr:mid(3-4.5%)` | 520 | 168 | 33 | 5 | -0.06 | -0.01 | 43 (39-47) |  |
| `atr:high(>=4.5%)` | 432 | 142 | 26 | 6 | -0.00 | +0.05 | 48 (43-53) |  |
| `atr:low(<3%)` | 279 | 108 | 36 | 5 | -0.10 | -0.05 | 41 (35-46) |  |

## Cautions
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `caut:high_on_light_volume` | 426 | 116 | 31 | 5 | -0.04 | +0.01 | 45 (40-50) |  |
| `caut:extended_above_ma` | 239 | 76 | 44 | 4 | -0.28 | -0.23 | 31 (25-37) | ▼ |
| `caut:negative_net_margin` | 121 | 45 | 31 | 6 | -0.05 | -0.00 | 45 (36-54) |  |
| `caut:analyst_deteriorating` | 64 | 33 | 34 | 2 | -0.28 | -0.23 | 30 (20-42) | ▼ |
| `caut:chase` | 50 | 32 | 52 | 2 | -0.32 | -0.27 | 36 (24-50) |  |
| `caut:earnings_today` | 38 | 33 | 50 | 8 | -0.26 | -0.22 | 29 (17-45) |  |
| `caut:earnings_soon` | 29 | 18 | 55 | 7 | -0.37 | -0.32 | 24 (12-42) | insufficient data |
| `caut:news_caution` | 2 | 2 | 50 | 0 | -0.74 | -0.69 | 0 (0-66) | insufficient data |

## Volume at 52-wk high (time-adjusted)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `volhi:low_adj(<0.8x)` | 115 | 63 | 34 | 4 | -0.17 | -0.12 | 37 (28-46) |  |
| `volhi:normal_adj(0.8-1.5x)` | 108 | 60 | 29 | 6 | -0.05 | -0.00 | 44 (35-53) |  |
| `volhi:high_adj(>=1.5x)` | 72 | 49 | 44 | 8 | -0.24 | -0.20 | 35 (25-46) |  |

## Push timing (ET)
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `time:midday` | 573 | 263 | 32 | 6 | -0.12 | -0.07 | 41 (37-45) |  |
| `time:pre_open` | 283 | 117 | 27 | 4 | +0.14 | +0.18 | 54 (49-60) | ▲ |
| `time:open_hour` | 189 | 121 | 29 | 5 | -0.02 | +0.03 | 44 (37-51) |  |
| `time:after_close` | 90 | 75 | 37 | 4 | -0.19 | -0.14 | 37 (27-47) |  |
| `time:late_session` | 59 | 48 | 29 | 7 | -0.01 | +0.04 | 44 (32-57) |  |

## Signal age / run-up since first push
| Feature | n | tickers | stop% | target% | avg R | R vs base | win% (95% CI) | |
|---|--:|--:|--:|--:|--:|--:|---|---|
| `age:recurring(2-4d)` | 2 | 2 | 50 | 0 | -0.10 | -0.06 | 50 (9-91) | insufficient data |
| `age:new(1d)` | 1 | 1 | 0 | 0 | +0.64 | +0.69 | 100 (21-100) | insufficient data |
| `runup:2-5%` | 1 | 1 | 100 | 0 | -1.00 | -0.95 | 0 (0-79) | insufficient data |
| `runup:<2%` | 1 | 1 | 0 | 0 | +0.79 | +0.84 | 100 (21-100) | insufficient data |

## Take-profit check (entries with path data)
- Take-profit touched before the stop: 201/273 (74%, 95% CI 68-78%); stop first: 56 (21%)
- Median best price in window: +5.2% vs entry

_45 distinct features tracked; always-present (hidden): cat:fundamentals, cat:technical, tier:STRONG. Raw push records without recoverable features are excluded._
