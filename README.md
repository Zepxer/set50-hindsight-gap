# SET50 ZxC: the hindsight gap in Thai stocks

**Question:** how much does testing *today's* SET50 on the past flatter a backtest, compared with the
list an investor could actually have picked in 2012?

Method from Quantz D-048, applied to the Thai market. All code in this project is written by Ikkyu;
Claude explains and reviews.

## Folders

| Path | What |
|---|---|
| `data/` | The two SET50 lists, the audit table, and `cache/` (downloaded prices, not committed) |
| `sources/` | `SOURCES.md` (every outside fact and where it came from) and `wayback/` (saved SET pages) |
| `notes/` | `DECISIONS.md` (every choice and why), `RESEARCH_LOG.md` (every research step), `SCHEDULE.md`, `quantz-lessons.md` |
| `PLAN.md` | The frozen plan, committed before any backtest code |
| `audit.py` | Downloads both lists and records missing data (written by Ikkyu from a description, 26 Oct; replaced Claude's first version) |

## Plan

| Step | Status | What |
|---|---|---|
| 1 | ✅ | Find the 2012 SET50 list |
| 2 | ✅ | Download prices, audit missing data |
| 2.5 | ✅ | Research the 12 missing stocks; Mendeley check; `PLAN.md` frozen (27 Oct) |
| 3.0 | ✅ | Write my own `audit.py` (matches the original exactly) |
| 3.1 | ✅ | `backtest.py`: one price table, 3482 days × 61 stocks (renames, drops, INTUCH/GULF chains) |
| 3.2 | ✅ | Monthly returns and equal-weight portfolios (172 months) |
| 3.3 | ⬜ | Trading costs (0.15%) at each rebalance |
| 3.4 | ✅ | Scorecard: CAGR, Sharpe, max drawdown, t-statistic; headline printed |
| 4 | ⬜ | Checks (the hardest step) |
| 5 | ⬜ | `charts.py` |
| 6–7 | ⬜ | Portfolio pages |

## Run

```bash
./.venv/bin/python audit.py 2>/dev/null
```
