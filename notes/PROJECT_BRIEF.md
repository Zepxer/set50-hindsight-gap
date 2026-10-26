# The Hindsight Gap in Thai Stocks: project brief

*A student research project (SET50, 2012–2026). Written to be reviewed: please find the holes.*

## 1. The question

If you take **today's** SET50 (the 50 biggest Thai stocks) and test it on the past, it looks
great, because today's list is made of companies that *already won*. An investor in 2012 couldn't
have known which ones those would be.

**How much does this hindsight make a Thai backtest look better than reality?**

This effect is called **survivorship bias**. A comparison: if you only study the football academy
that produced Ronaldo, the academy looks perfect, because you never see the many young players who
didn't make it.

## 2. Where the idea comes from

This repeats an experiment from a US quant research project (Quantz). It compared:
- the Dow Jones 30 **as it stood in 2008** (what an investor could actually have picked), and
- the Dow Jones 30 **of 2026** (picked knowing who won),

with the same strategy, over the same dates (2008–2026).

Result: today's list earned **17.3% a year** and the 2008 list **11.9%**. That is a **hindsight gap
of +5.36% a year** (t-statistic 2.74). On today's list, four different trading strategies all looked
statistically significant. On the 2008 list, none did. The "edge" came from choosing the list, not
from the strategies.

**This project asks whether the same thing happens in Thailand, and how big it is.**

## 3. The method

Two lists, one strategy, same dates. **The only difference is the list.**

| | List | Represents |
|---|---|---|
| **Honest list** | SET50 in force from **2 July 2012** | What an investor in 2012 could actually pick |
| **Hindsight list** | SET50 in force from **1 July 2026** | Picked knowing who won |
| **Benchmark** | TDEX (an ETF that tracks the SET50) | What simply buying the index earned |

- **Period:** 2 July 2012 → October 2026 (about 14 years).
- **Strategy:** equal weight. Each stock gets the same share of the money, rebalanced regularly.
  It has **no settings to tune**, so nothing can be overfitted, and any difference must come from
  the list.
- **Prices:** Yahoo Finance daily prices, adjusted for splits and dividends (total return).
- **Measured:** yearly growth (CAGR), Sharpe ratio, maximum drawdown, and the **gap** between the
  two lists, with a t-statistic to judge whether the gap could be luck. The bar used is t ≥ 3.0
  (stricter than the usual 2.0, following Harvey, Liu & Zhu 2016).

## 4. The data, and where it came from

- **The 2012 list:** an archived copy of the Stock Exchange of Thailand's own SET50 page, saved by
  the Wayback Machine on 4 Sep 2012 and again on 4 Nov 2012 (identical). A 4 Jan 2013 copy shows the
  expected six-monthly changes (3 out, 3 in), which confirms the snapshots behave correctly.
- **The 2026 list:** the SET website, read 25 Oct 2026. It matches the news of the H2 2026 review.
- **Prices:** 72 tickers downloaded and audited.

## 5. Problems found so far (this is where the project gets interesting)

Free data hides exactly the companies that matter most.

**12 of the 50 stocks in the 2012 list have no price data at all.** They fall into three groups:

| Group | Stocks | Handling |
|---|---|---|
| **Renamed** (same company) | BGH → BDMS, TMB → TTB, TUF → TU | Use the new ticker's data |
| **Bought out / merged** | BIGC, HEMRAJ, GLOW, ROBINS, DTAC, INTUCH | See below |
| **Restructured** | MAKRO, PS, ESSO | History cut off at the change |

**A key difference from the US study:** the missing US company (General Motors) went **bankrupt**,
so counting it as a total loss was fair. Most missing Thai companies were **bought out**, which
usually pays shareholders a premium. Counting them as a total loss would be unfair, and dropping
them would ignore the problem. So the project runs **both** and reports the range:
- **(a) dropped:** their money is split among the remaining stocks;
- **(b) total loss:** the pessimistic end.

**Other data problems:**
- Some stocks that are still alive have broken history on Yahoo: SCB starts in 2022 (after becoming
  the holding company SCB X), BANPU in 2016, GULF and TIDLOR in 2025.
- TRUE is a **splice**: after the 2023 merger with DTAC, it is a different company on the same price line.
- Many 2026 stocks didn't exist in 2012 (OR, SCGP, CRC, AWC, TLI, MRDIYT). They join the portfolio
  on their listing day.

## 6. What a good result looks like

Any of these is a real finding:
- **A large gap** (like the US +5%): Thai backtests on today's SET50 are badly flattered.
- **A small or zero gap:** the Thai market behaves differently. A possible reason: survivors are
  replaced by buyouts rather than bankruptcies.
- **A gap that can't be measured cleanly:** free Thai data is too broken to answer the question,
  which is itself a warning for anyone backtesting Thai stocks.

Whatever the number, it gets reported with its range and its weaknesses.

## 7. Known weaknesses

1. **One comparison is one example, not a law.** It's two lists over 14 years.
2. **Statistical power is low.** 14 years may not be enough to prove a gap of a few percent.
3. **The 2012 list has one source** (the SET's own website, via two archived copies). No independent
   second source has been found yet.
4. **Missing companies** mean the honest list is incomplete, hence the (a)/(b) range.
5. **Yahoo's data errors** (splices, cut-off histories) may push the result either way.
6. **The two lists share many stocks** (29 tickers, 32 counting renames), which limits how different
   they can be.

## 8. Questions for a reviewer

1. Is equal weight the right strategy for isolating the effect of the list?
2. For bought-out companies, is "dropped vs total loss" a fair range? Would it be better to model
   them as **cashed out at the takeover price**, if the prices can be found?
3. Should the hindsight list only include stocks that already traded in 2012, to make the comparison
   cleaner? Or does that remove part of the very effect being measured?
4. Is TDEX a fair benchmark, given that it has fees and tracking error?
5. What would you check first to see if the result is wrong?

## 9. Who does what

The method comes from the Quantz project, which was built by an AI coding agent (Claude). I studied
it to understand it. **This Thai extension is my own:** I make the decisions and write all the code by
hand, with Claude explaining concepts and reviewing.
