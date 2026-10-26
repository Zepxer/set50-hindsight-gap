# SET50 ZxC: the hindsight gap in Thai stocks

**Question:** how much does testing *today's* SET50 on the past flatter a backtest, compared with the
list an investor could actually have picked in 2012?

Method from Quantz D-048, applied to the Thai market. All code in this project is written by hand by
Ikkyu; Claude explains and reviews.

## Folders

| Path | What |
|---|---|
| `data/` | The two SET50 lists, the audit table, and `cache/` (downloaded prices, not committed) |
| `sources/` | `SOURCES.md` (every outside fact and where it came from) and `wayback/` (saved SET pages) |
| `notes/` | `DECISIONS.md` (every choice and why) and `quantz-lessons.md` (what I learned from Quantz) |
| `audit.py` | Day 2: downloads both lists and records missing data (written by Claude; being retyped) |

## Plan

| Step | Status | What |
|---|---|---|
| 1 | ✅ | Find the 2012 SET50 list |
| 2 | ✅ | Download prices, audit missing data |
| 3.0 | ⬜ | Retype `audit.py` by hand (`audit_mine.py`) |
| 3.1 | ⬜ | `backtest.py`: load prices into one table, fix renamed tickers |
| 3.2 | ⬜ | Daily returns and equal-weight portfolios |
| 3.3 | ⬜ | Bought-out stocks, both ways |
| 3.4 | ⬜ | Scorecard: CAGR, Sharpe, max drawdown, t-statistic |
| 4 | ⬜ | Checks (the hardest step) |
| 5 | ⬜ | `charts.py` |
| 6–7 | ⬜ | Portfolio pages |

## Run

```bash
./.venv/bin/python audit.py 2>/dev/null
```
