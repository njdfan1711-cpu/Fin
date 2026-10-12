# Trade drawdown report

Generated 2026-10-12 22:47 UTC. Source: open_positions.json (Fin Trade Log) + Yahoo daily bars.

Stop used: entry minus 1.5 x ATR(14) as of the day before entry (Fin's default plan, not your actual stop).

## Summary (closed trades with enough data)

- Trades analyzed: 14 of 16 closed
- Dipped below entry at some point: 9
- Dipped 2% or more: 5; 3% or more: 5; 5% or more: 2
- Median worst dip: -0.5%; deepest: -15.5%
- **Trades where Fin's stop level was reached before you exited: 2**
- Closed with a gain: 14 of 14

Stop reached on: PSIX, CDNA. On those, holding past Fin's stop turned a would-be loss into a win.

## Closed trades

| Symbol | Entry | Exit / now | Held (cal. days) | Worst dip | $ at worst | Closes under entry | Stop level | Stop reached? | Result |
|---|---|---|---|---|---|---|---|---|---|
| PSIX | 2026-08-13 @ $41.03 | 2026-09-08 | 26 | -15.5% (2026-09-01) | -$477 | 16 | $36.24 (-11.7%) | YES | +0.8% +$23 (exit) |
| B | 2026-08-20 @ $46.15 | 2026-08-24 | 4 | none (2026-08-20) | $0 | 0 | $43.41 (-5.9%) | no | +4.1% +$44 (exit) |
| CHYM | 2026-08-24 @ $32.92 | 2026-08-26 | 2 | -1.6% (2026-08-25) | -$17 | 0 | $30.08 (-8.6%) | no | +0.6% +$6 (exit) |
| SSRM | 2026-08-26 @ $38.28 | 2026-08-27 | 1 | -0.5% (2026-08-26) | -$5 | 0 | $35.90 (-6.2%) | no | +1.2% +$13 (exit) |
| CDNA | 2026-08-28 @ $51.38 | 2026-09-14 | 17 | -9.1% (2026-08-31) | -$103 | 9 | $48.15 (-6.3%) | YES | +0.6% +$7 (exit) |
| A | 2026-09-08 @ $147.53 | 2026-09-15 | 7 | -4.3% (2026-09-10) | -$132 | 4 | $139.77 (-5.3%) | no | +2.0% +$62 (exit) |
| STNG | 2026-09-15 @ $85.72 | 2026-09-17 | 2 | -0.5% (2026-09-16) | -$17 | 1 | $82.34 (-3.9%) | no | +3.2% +$100 (exit) |
| PINS | 2026-09-18 @ $18.39 | 2026-09-21 | 3 | none (2026-09-18) | $0 | 0 | $17.08 (-7.1%) | no | +2.3% +$76 (exit) |
| HPE | 2026-09-23 @ $61.99 | 2026-09-24 | 1 | none (2026-09-23) | $0 | 0 | $55.66 (-10.2%) | no | +1.4% +$45 (exit) |
| S | 2026-09-24 @ $23.94 | 2026-09-24 | 0 | none (2026-09-24) | $0 | 0 | $22.30 (-6.8%) | no | +1.3% +$44 (exit) |
| AVT | 2026-09-25 @ $103.41 | 2026-10-02 | 7 | -4.7% (2026-10-01) | -$160 | 4 | $97.68 (-5.5%) | no | +2.8% +$95 (exit) |
| NAT | 2026-10-05 @ $8.41 | 2026-10-07 | 2 | -3.3% (2026-10-06) | -$115 | 2 | $7.90 (-6.0%) | no | +0.2% +$8 (exit) |
| INSW | 2026-10-07 @ $118.44 | 2026-10-08 | 1 | -1.3% (2026-10-07) | -$43 | 0 | $111.11 (-6.2%) | no | +2.2% +$77 (exit) |
| PENG | 2026-10-09 @ $72.84 | 2026-10-09 | 0 | none (2026-10-09) | $0 | 0 | $66.41 (-8.8%) | no | +0.9% +$31 (exit) |

## Open positions (marked to latest close)

| Symbol | Entry | Exit / now | Held (cal. days) | Worst dip | $ at worst | Closes under entry | Stop level | Stop reached? | Result |
|---|---|---|---|---|---|---|---|---|---|
| SLDE | 2026-09-14 @ $26.09 | open | 28 | -14.7% (2026-10-01) | -$165 | 19 | $25.06 (-4.0%) | YES | -2.1% -$24 (latest close) |
| PAYS | 2026-10-12 @ $15.38 | open | 0 | -1.4% (2026-10-12) | -$50 | 0 | $14.38 (-6.5%) | no | -1.4% -$50 (latest close) |

## Not analyzed

- ETOR: entry date missing in log
- A: entry date missing in log

## How to read this

- Daily bars can't show intraday order, so entry and exit days use closes only; the real worst dip may be slightly deeper than shown.
- 'Stop reached' compares the lowest price while held to Fin's default stop. If you set a different stop, the answer changes.
- A closed-trade win rate counts only trades that recovered. Check the open positions too.
