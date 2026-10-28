# Frozen Plan: SET50 Survivorship Bias Backtest

**Freeze date:** 27 October 2026
**Status:** To be committed to Git before any backtest code runs.

Once committed, this plan is binding. No choices below will be changed after the backtest results are seen.

## Research Question

How much higher is the yearly return of today's SET50, tested backwards, than the SET50 an investor could actually have selected in July 2012?

## 1. Fixed Choices


| Item                              | Fixed choice                                                                                                                                                      |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Honest list                       | SET50 constituents in force from 2 July 2012 (50 stocks). Renamed tickers are mapped as follows: BGH → BDMS, TMB → TTB, and TUF → TU.                             |
| Hindsight list                    | SET50 constituents in force from 1 July 2026 (50 stocks).                                                                                                         |
| Period                            | 2 July 2012 to 22 October 2026, the last close in the saved data.                                                                                                 |
| Strategy                          | Equal-weight the stocks and rebalance on the first trading day of each month.                                                                                     |
| Late listers                      | A stock joins at the first monthly rebalance after its first trading day.                                                                                         |
| Prices                            | Yahoo daily closes adjusted for splits and dividends, supplemented by Mendeley data for INTUCH and historical GULF prices (D-10). Data are saved once and reused. |
| Costs                             | Transaction = 0.15% of traded value, applied equally to both lists.                                                                                               |
| Bought-out stocks (headline rule) | Dropped from the start (D-9).                                                                                                                                     |
| Benchmark                         | TDEX                                                                                                                                                              |




## 2. Known Biases, Stated in Advance

- Stocks are held only while usable price data are available.
- Mendeley data fix the missing historical prices for GULF. TIDLOR, listed in 2021, still lacks its pre-2025 history. The hindsight list therefore misses some of TIDLOR's earlier returns, which biases the hindsight gap toward zero, but less than it would without the GULF fix.
- Eight stocks dropped under the headline rule have an unknown bias direction. Their exclusion may raise or lower the measured return gap; the direction will not be assumed in advance.
- SCB and BANPU are included in both lists. Their missing historical data may affect both portfolios, but the effects are not guaranteed to cancel. BANPU remains subject to Thursday's data check.
- The swaps DTAC → TRUE and PS → PSH are handled under the dropped rule rather than cashed out at their swap values.
- Swap: Old TRUE → new TRUE at 0.60018, Old GULF → new GULF at 1.02974, INTUCH → new GULF at 1.69335
- These limitations will be disclosed alongside the results. No bias adjustment will be invented after seeing the results.



## 3. Headline Result

The headline hindsight gap is:

> Average monthly return difference (2026 list minus 2012 list) × 12, under the dropped rule.

The headline will report:

- The annualized arithmetic return gap.
- The t-statistic for the mean monthly return difference.
- The 95% confidence interval for the mean difference, annualized consistently.

The CAGR gap will be reported alongside the headline result as a descriptive comparison. It will not be statistically tested.

## 4. Statistical Test

Calculate monthly return differences:

> Difference = 2026-list monthly return − 2012-list monthly return.

Apply a plain one-sample t-test to the mean of these monthly differences.

Report results against both pre-specified reference bars:

- **t ≥ 2.0:** The primary planned-test threshold.
- **t ≥ 3.0:** The more demanding Quantz reference threshold.

These thresholds are reference bars, not guarantees that the result is economically meaningful. The effect size and confidence interval will remain central to interpretation.

## 5. Statistical Power, Written Before Running

The approximate smallest annualized gap detectable with 80% power is:

> 2.8 × σ ÷ √14.3

where σ is the annualized volatility of the monthly return difference, and 14.3 is the approximate number of years in the test period.

Using the Quantz Dow 30 result as a stand-in—an annualized gap of 5.36%, a t-statistic of 2.74, and a period of 18.5 years—gives an estimated σ of approximately 8.4% per year.

This implies an approximate detectable gap of 6.2% per year.

A real gap smaller than this may fail to reach t ≥ 2.0. Therefore, the confidence interval and estimated effect size—not merely whether the test crosses a threshold—will carry the interpretation.

This power estimate is approximate and depends on the volatility estimate and assumptions underlying the calculation.

## 6. Sensitivity Checks

Sensitivity checks will be clearly labelled and will not replace the headline result.

- **Hindsight list restricted to stocks trading in July 2012:** Separates the effect of surviving stocks from the effect of including later listings.
- **Quarterly rather than monthly rebalancing:** Tests whether the result depends materially on the rebalancing frequency.

The total-loss scenario for the eight dropped stocks is excluded from the main sensitivity checks. Treating all eight as worthless is an extreme bound, not a realistic estimate of their returns. The direction of the bias from dropping them remains unknown.

## 7. Final Results Page

The finished results page will lead with one sentence in the following form. Every bracketed value will be filled only after the frozen backtest has been run:

> The 2026 SET50 hindsight list outperformed/underperformed the July 2012 SET50 list by [X] percentage points per year in annualized arithmetic returns (t = [T], 95% CI [L, U]), under the pre-committed dropped-stock rule.

The results page will also report the CAGR gap, the TDEX contextual benchmark, both t-statistic reference bars, and the pre-specified limitations and sensitivity checks.

## 8. Commitment Rule

This plan must be committed to Git on 27 October 2026, before any backtest code runs.

After commitment:

- No rules, thresholds, data-source choices, or sensitivity checks may be changed in response to the observed results.
- Any later exploratory analysis must be labelled as post hoc and kept separate from the frozen headline result.
- Missing data and corporate actions must be handled consistently with the rules above.
- Any implementation limitation or deviation must be disclosed rather than silently changing the plan.

