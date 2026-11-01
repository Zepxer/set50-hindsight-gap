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
|| `notes/` | `RESULTS.md` (the final results), `DATA_CHECKS.md` (every data check), `DECISIONS.md` (every choice and why), `RESEARCH_LOG.md` (every research step), `SCHEDULE.md`, `quantz-lessons.md` |
| `PLAN.md` | The frozen plan, committed before any backtest code |
| `backtest.py` | The backtest: prints the headline and scorecard (written by Ikkyu) |
| `checks.py` | The data checks (written by Ikkyu) |
| `audit.py` | Downloads both lists and records missing data (written by Ikkyu from a description, 26 Oct; replaced Claude's first version) |
| `charts.py` | Makes the four charts (written by Ikkyu) |
| `charts/` | The four saved charts |

## Plan

| Step | Status | What |
|---|---|---|
| 1 | ✅ | Find the 2012 SET50 list |
| 2 | ✅ | Download prices, audit missing data |
| 2.5 | ✅ | Research the 12 missing stocks; Mendeley check; `PLAN.md` frozen (27 Oct) |
| 3.0 | ✅ | Write my own `audit.py` (matches the original exactly) |
| 3.1 | ✅ | `backtest.py`: one price table, 3482 days × 61 stocks (renames, drops, INTUCH/GULF chains) |
| 3.2 | ✅ | Monthly returns and equal-weight portfolios (171 monthly returns) |
| 3.3 | ✅ | Trading costs (0.15%) at each rebalance |
| 3.4 | ✅ | Scorecard: CAGR, Sharpe, max drawdown, t-statistic; headline printed |
| 4 | ✅ | Checks (`notes/DATA_CHECKS.md`): 12 checks, including what wasn't checked |
| 4.5 | ✅ | Sensitivity: 2026 list limited to July 2012 stocks; quarterly rebalancing |
| 5 | ✅ | `charts.py` |
| 5.5 | ✅ | `notes/RESULTS.md` |
| 6–7 | ⬜ | Portfolio pages (SET50 is the flagship, decided 29 Oct) |

## External Dataset (Required)
- The backtest requires an external Mendeley dataset that is not included in this repository because data/external/ is gitignored.
- Authors: Bui Thanh Khoa & Tran Trong Huynh (2025)
- License: CC BY 4.0
- DOI: 10.17632/gybmm9t3mr.1
- Required filename: data1_THA.csv
- Save location: data/external/data1_THA.csv
- SHA-256: 0cb504f42206604bf7f8a149a70098c4b2bef10bcfe83a4827c804327f1890f7
- After downloading, place the CSV at the specified location before running the backtest.

## Run

```bash
python3 -m venv .venv
```

```bash
./.venv/bin/pip install -r requirements.txt
```

```bash
./.venv/bin/python audit.py 2>/dev/null
```

```bash
./.venv/bin/python backtest.py 2>/dev/null
```

```bash
./.venv/bin/python charts.py 2>/dev/null
```
