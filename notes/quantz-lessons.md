# What I learned from Quantz (8 lessons, 2026-10-25)

Quantz (`~/Projects/quantz-claude-x`) was built by Claude, working on its own from a brief.
I went through it lesson by lesson to understand it. The comparisons marked **(mine)** are my own.

## 1. The big picture
- Question: can a strategy beat simply holding the market (SPY, a fund copying the S&P 500)?
- Answer: no strategy did. The two best were the two that predict nothing.
- "We found no edge" ≠ "there is no edge". The test was too weak to tell either way (see lesson 7).

## 2. Lookahead bias
- Using information that could not have reached you yet. Like betting on yesterday's football match
  after seeing the score.
- A signal from Monday's close can only trade at **Tuesday's open**. The Quantz engine accepts only
  opening prices and always waits one day, with no setting to change it.
- "Delete the code path" beats "write a warning": a warning needs every person to remember it every
  time; deleted code makes the mistake impossible.
- Found in Phase 1: the popular library vectorbt fills at the same bar's close by default.

## 3. The scorecard
- **CAGR**: yearly growth, start to end only; it does not show swings.
- **Max drawdown**: worst fall from a peak. −50% needs +100% to recover.
- **Sharpe**: yearly return ÷ yearly volatility. 0.5 ordinary, 1.0 good, 2.0+ suspicious.
- **t-statistic ≈ Sharpe × √years.** Quantz's bar is t ≥ 3.0 (Harvey, Liu & Zhu 2016), stricter than 2.0
  because testing many strategies lets some pass 2.0 by luck.
- Example: Sharpe 0.6 over 25 years → 0.6 × 5 = 3.0. Time is evidence.

## 4. Overfitting, walk-forward, holdout
- Overfitting: picking the setting that won on past data by luck.
  **(mine)** Betting on a horse after the race: winning one race by luck says nothing about the next.
- Walk-forward: choose using only the past, score on the next unseen year, repeat (12 folds,
  4-year first training window that grows).
- Holdout: the last 20% (2022-07 → 2026-08) locked away on day one and opened once at the end.

## 5. The strategies (21 ETFs: US stocks, sectors, bonds, gold, commodities, international)
- Time-series momentum: is each asset higher than 3/6/12 months ago? Each judged alone.
- Cross-sectional momentum: rank all 21, hold the top 5. Ranked against each other.
- Equal weight: 1/21 each. **The control.** **(mine)** "The gatekeeper": a smart strategy that
  can't beat it isn't worth its complexity.
- Inverse volatility: more money in calm assets. Low drawdown, low growth.
- Turnover costs: cross-sectional traded 53.8× a year; small fees paid thousands of times eat the profit.

## 6. The hindsight gap ⭐
- Today's Dow 30 tested backwards looks great because the list is made of winners (survivorship bias).
  **(mine)** The Portugal academy: we remember Ronaldo, Bruno and Eusébio, not the many prodigies
  who never made it.
- Experiment: Dow 30 of 2008 vs Dow 30 of 2026, same dates (2008-03 → 2026-09), equal weight.
- Result: 17.3%/yr (2026 list) vs 11.9%/yr (2008 list). **Hindsight gap +5.36%/yr**, t = 2.74.
- On the 2026 list all four strategies "pass" t ≥ 3; on the 2008 list none do. The edge was the list.
- Caveats: t = 2.74 is below 3.0; one comparison is one example; old GM has no data (gap likely understated).
- Both lists cover the same dates, so the 2008 crash hit both equally; it cannot explain the gap.

## 7. Statistical power
- Power = the chance a test detects something real.
  **(mine)** An experienced coach spots real talent; a new coach can't tell, so "he's not good" means little.
- Quantz measured it: a market-like strategy (Sharpe 0.4) passes t ≥ 3 over 12 years only **8%** of the time.
- So "failed" means **inconclusive**, not disproven.
- Stricter bar = fewer lucky passes but more missed real edges.
  **(mine)** An academy with low standards lets in more real talent and more lucky players too.

## 8. Paper trading
- Fake money, real prices, going forward. The one test hindsight cannot touch, but it's slow.
- Two accounts (equal weight): ETF basket (55 days, −1.28% on 2026-10-25) and Dow 30 (16 days).
  Too short to mean anything yet.

## Quantz in five sentences
1. It asked whether a strategy could beat holding the market; the honest answer was no.
2. It blocked cheating by design: next-day open fills, walk-forward settings, a sealed holdout.
3. It measured its own weakness: 8% power, so "no edge" means "can't tell yet".
4. Today's Dow 30 tested backwards adds +5.36%/yr of fake performance.
5. The only clean evidence is forward paper trading, still collecting.

---

# Questions about my own code (audit.py, 26 Oct)

## Why a `set` instead of lists for `all_symbols`?
- A **set** is a collection where **each item appears only once**, and order doesn't matter.
  Adding an item that's already inside does nothing.
- The two SET50 lists share **29 stocks**. Joining two plain lists would give **100 entries**,
  with those 29 twice, so they'd be downloaded twice and counted twice in the audit.
- The **union** `set_2012 | set_2026` keeps everything in either list, once:
  50 + 50 − 29 = **71 stocks**, plus TDEX = **72**. That matches the 72 rows of the audit,
  which is a built-in check.
- Sets have other operations that answer research questions directly:
  - `set_2012 & set_2026`, the **intersection**, gives the 29 survivors (in both lists);
  - `set_2012 - set_2026`, the **difference**, gives the 21 that left the SET50.
- `symbol in set_2012` (True/False) is also **fast** with a set: Python jumps straight to the item
  instead of checking the list one by one.
- A set has **no order**, so `sorted(all_symbols)` is used to loop in alphabetical order and keep
  the output the same every run.

## What does `auto_adjust=True` change about the prices?
- It rewrites old prices so **splits and dividends don't look like price moves**.
- **Splits:** PTT split 1 share into 10 on 2018-04-24. Unadjusted, that day looks like a fake
  **−90% crash**. Adjusted, every price before 2018 is divided by 10.
- **Dividends:** old prices are lowered slightly for every dividend paid since, so the series shows
  **total return** (price change + dividends received). Fair for Thai stocks, which pay big dividends.
- That's why PTT shows about 16.68 baht in July 2012 instead of about 300.

## Why does `first > 2012-07-02` find late listers but not the no-data stocks?
- A **late lister** has a real first date after 2 July 2012 (OR: 2021-02-11), so the comparison
  is **True**.
- A **no-data** stock has no dates at all, so its `first` is **NaT** ("Not a Time", an empty date).
  Any comparison with NaT is **False**, so those stocks are left out.
- So the two warning lists don't overlap: each problem gets its own list.
- Related trap: **NaN never equals NaN**, so to test for empty values use `.isna()`, not `== NaN`.
