# Data Check

Purpose: Can the headline be trusted? Every check,
including the ones that found nothing.

## Summary:

1. BANPU: Yahoo used the wrong company (BPP); replaced it with real BANPU data, ending 14 Mar 2025.
2. Stock Comparison: Compared 50 stocks; BANPU was the only incorrect series.
3. TRUE: Fake +68.6% jump from a stock swap; adjusted prices from 3 Mar 2023 by 0.60018.
4. INTUCH: Dividend was already adjusted; no change needed. The suspected fix would create a fake +5.9% gain.
5. BANPU: Yahoo data matches BPP rather than the actual BANPU series; issue disclosed.
6. Corporate actions: Reviewed ticker changes and stock swaps; unresolved cases disclosed.
7. Price coverage: Checked missing and incomplete price histories; limitations documented.
8. Dividends: All three tested dividends matched official announcements.
9. Stock count: Portfolio sizes changed over time; Sensitivity 1 included.
10. Re-download: All 60 price series reproduced with differences below 0.1%.
11. Official SET lists: Both 50-stock lists matched the available official documents.
12. THAI: +216% on 2025-08-04 was real; data kept and disclosed.

## Headline history
| Version | Gap | t | 95% CI |
|---|---|---|---|
| Before costs | 4.01% | 4.01 | [2.05%, 5.98%] |
| After costs | 4.00% | 4.00 | [2.04%, 5.97%] |
| After BANPU + TRUE fixes | 3.97% | 3.98 | [2.01%, 5.92%] |

# Stock Data Investigation

## 1. BANPU 
- Found: Yahoo's BANPU series was actually tracking BPP.
- Methods: Compared daily returns and price ratios.
- 1.0000 with BPP vs 0.3962 with real BANPU, over 2,037 days
- Did: Replaced Yahoo's data with Mendeley's real BANPU data and stopped holding it after 14 March 2025 (D-11).
- Did not do: Did not extend holdings beyond the last available real BANPU data.

## 2. Stock Comparison 
- Found: BANPU was the only wrong company series identified among the 50 stocks compared.
- Methods: Compared daily returns and correlations between Yahoo and Mendeley.
- Did: Compared the available data to identify mismatched stock series.
- Did not conclude: High correlation does not prove data accuracy. It only shows that both datasets follow the same series. TRUE proves this, as both datasets contain the same incorrect jump.

## 3. TRUE 
- Found: A suspicious jump from 4.873 to 8.217 on 3 March 2023.
- Methods: Checked historical prices, trading suspension, and the reported 0.60018 swap ratio.
- Evidence: Adjusted value was 4.93, suggesting the actual movement was approximately +1.2%.
- What I did: Multiplied prices from 3 March 2023 onward by 0.60018 (D-12).
- Did not do: Did not treat the artificial jump as a genuine return.

## 4. INTUCH 
- Found: Claude suggested that a missing dividend caused the price movement on 12 March 2025. Checking the dividend information showed this was incorrect.
- Methods: Checked the 6.54-baht special dividend, XD date, and Aclose-to-Close ratio.
- Evidence: 0.9341 = 1 − 6.54 ÷ 99.25. GULF also fell 5.58% on 12 March, compared with INTUCH's 5.6% decline.
- Did: Kept the original data unchanged (D-13).
- Did not do: Did not apply another dividend adjustment.
- Also checked: −20% on 21 Dec 2015 looks real. ADVANC fell about 19% that day after the 900MHz auction; INTUCH is its largest shareholder.

## 5. Rerun test
- Did: Ran backtest.py twice on 30 Oct.
- Found: Identical output (3.97%, t = 3.98).
- Limit: Same saved files only. It does not re-download from Yahoo. (See section 10)

## 6. Renames (TTB, BDMS, TU)
- Methods: Listed each stock's 4 largest daily moves, and printed TTB around 7 May 2021.
- Found: No fake jump at the rename dates. TTB stays near 0.846 on 5–11 May 2021. Most of the largest moves are in the COVID crash period (Feb–Mar 2020).
- Limit: BDMS's rename date is unconfirmed. Not investigated: BDMS 2020-11-10 (12.4%), BDMS 2013-01-17 (10.2%), TU 2021-05-10 (10.5%), TU 2015-08-13 (9.4%).

## 7. Chains (INTUCH, GULF)
- Methods: Compared prices on 14 Mar and 3 Apr 2025, across the swap.
- Found: INTUCH 77.00 → 78.22 (+1.59%). GULF 46.75 → 47.57 (+1.75%). Similar moves, as expected for two companies merging into one, with no sign of a wrong ratio.
- Limit: The two ratios come from news reports, and the 4 trading days before the suspension are missing from Mendeley.

## 8. Dividends
- Methods: Compared Yahoo Finance dividend data with official announcements for three stocks.
- Found:
-   PTT: ฿1.20, XD 2024-02-29
-   KBANK: ฿6.00, XD 2024-04-22
-   ADVANC: ฿4.87, XD 2024-08-19
All three matched the announced amounts and dates.

- Did: Recorded all three as successful checks.
- Limit: Only three dividends were checked, all from 2024 and large companies. Older dividends and smaller stocks remain untested.

## 9. Stock Count

- Methods: Checked the number of stocks in each portfolio throughout the backtest.
- Found:
-   2012 list: Started with 41, reached 42, and ended with 41 stocks.
-   2026 list: Started with 35 and ended with 49 stocks.
Later-listed stocks joined over time, so the portfolio sizes changed.

- Did: Included Sensitivity 1 to examine the effect of these differences.
- Limit: The portfolios did not have the same number of stocks throughout the test.

## 10. Re-download Test

- Methods: Re-downloaded all 60 Yahoo Finance price series and compared them with the saved data.
- Found: The largest difference was 0.00008% for IVL. No difference exceeded 0.1%.
- Did: Confirmed that the saved data could be reproduced.
- Limit: Reproducible data are not necessarily correct. Yahoo’s BANPU still matches BPP, which is why the backtest uses Mendeley’s BANPU instead (D-11).
## 11. Official SET List Check

- Methods: Compared both stock lists with official SET documents.
- Found:
-   2012: All 50 stocks matched the second-half 2012 list.
-   2026: All 50 stocks matched the revised second-half 2026 list.
The only revision was BANPUU → BANPU, which refers to the same company and does not affect the backtest.
- Did: Verified both lists against the available official documents.
- Limit: The revised August 2026 file was checked, not the original July file. For 2012, the September and November snapshots also showed the same 50 stocks, but other changes during the period may not be captured.

## 12. THAI Price Jump
- Methods: Checked THAI's price jump on its return to trading and compared it with news reports.
- Found: On 2025-08-04, THAI rose approximately 216%, from a pre-suspension price of ฿3.32 to a closing price of ฿10.30. News reports confirmed that the jump was real, not a Yahoo Finance error. Its estimated effect on the annual performance gap was +0.04 percentage points per year.
- Did: Kept the original data and disclosed the event.
- Limit: The exact outcome of the old shares under the restructuring has not been confirmed through a filing.

## Not checked
- 10 stocks could not be compared. ( AWC, CRC, GULF, MRDIYT, OR, SCGP, TDEX, TIDLOR, TLI, TTB ), not in Mendeley, or too little overlap.
- Data independence: Mendeley is not an independent source of truth; TRUE contains the same Yahoo price jump.
- Nothing after 14 March 2025 could be compared because Mendeley's data ends there.
- The explanation that Yahoo shows BPP's history is inferred, not confirmed.
- BANPU's last 19 months are missing from both lists.
- BANPU and TRUE correction effects were measured only together.
- BEM was fromed around 2015, but Yahoo shows prices from 2012. Not confirm.



