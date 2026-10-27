# Raw plan (Ikkyu's first draft, 27 Oct)

## Question

How much higher is the yearly return of today's SET50, tested backwards, than the SET50 an investor could actually have selected in July 2012?

## Fixed choices

- Honest list: SET50 in force from 2 Jul 2012 (50 stocks); map BGH → BDMS, TMB → TTB, TUF → TU.
- Hindsight list: SET50 in force from 1 Jul 2026 (50 stocks).
- Period: 2 Jul 2012 to 22 Oct 2026, last close in saved data.
- Equal weight; rebalance on the first trading day of each month.
- Late listers join at the first monthly rebalance after their first trading day.
- Prices: Yahoo daily closes adjusted for splits and dividends; Mendeley prices for INTUCH and old GULF (D-10).
- Trading costs: 0.15% of traded value, applied equally to both lists.
- Headline bought-out-stock rule: drop the affected stocks from the start (D-9).
- TDEX is context only.

## Known data issues and handling

- GULF fixed with Mendeley data.
- TIDLOR need/ lack data from before 2025
- 8 Stocks dropped under headline rule

## Headline and test

- (List in 2026 - 2012) x 12
- Report t stats
- Report 95% confidence interval
- Show CAGR

For t test, have two:

- t ≥ 2 ( average, but might get caught with luck)
- t ≥ 3 ( Quantz bar )

## Power

Use the rough 80% power estimate: minimum detectable annualized gap ≈ 2.8 × monthly standard deviation of the differences ÷ √14, ×12 to express it annually. Use Quantz as a stand-in for the monthly standard deviation if needed; it is not this SET50 sample, so mark the estimate as rough and dependent on that proxy.

## Sensitivities

- Limit the hindsight list to stocks already present in July 2012.
- Rebalance quarterly instead of monthly.
- Leave the total-loss case out of the main sensitivities; treating all eight dropped stocks as worthless is an extreme bound, not a realistic estimate.
