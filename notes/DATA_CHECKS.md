# Data Check

Purpose: Can the headline be trusted? Every check,
including the ones that found nothing.

## Summary:

1. BANPU: Yahoo used the wrong company (BPP); replaced it with real BANPU data, ending 14 Mar 2025.
2. Stock Comparison: Compared 50 stocks; BANPU was the only incorrect series.
3. TRUE: Fake +68.6% jump from a stock swap; adjusted prices from 3 Mar 2023 by 0.60018.
4. INTUCH: Dividend was already adjusted; no change needed. The suspected fix would create a fake +5.9% gain.

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
- Limit: Same saved files only. It does not re-download from Yahoo.

## 6. Renames (TTB, BDMS, TU)
- Methods: Listed each stock's 4 largest daily moves, and printed TTB around 7 May 2021.
- Found: No fake jump at the rename dates. TTB stays near 0.846 on 5–11 May 2021. Most of the largest moves are in the COVID crash period (Feb–Mar 2020).
- Limit: BDMS's rename date is unconfirmed. Not investigated: BDMS 2020-11-10 (12.4%), BDMS 2013-01-17 (10.2%), TU 2021-05-10 (10.5%), TU 2015-08-13 (9.4%).

## 7. Chains (INTUCH, GULF)
- Methods: Compared prices on 14 Mar and 3 Apr 2025, across the swap.
- Found: INTUCH 77.00 → 78.22 (+1.59%). GULF 46.75 → 47.57 (+1.75%). Similar moves, as expected for two companies merging into one, with no sign of a wrong ratio.
- Limit: The two ratios come from news reports, and the 4 trading days before the suspension are missing from Mendeley.

## Not checked
- 10 stocks could not be compared. ( AWC, CRC, GULF, MRDIYT, OR, SCGP, TDEX, TIDLOR, TLI, TTB ), not in Mendeley, or too little overlap.
- Data independence: Mendeley is not an independent source of truth; TRUE contains the same Yahoo price jump.
- Nothing after 14 March 2025 could be compared because Mendeley's data ends there.
- The explanation that Yahoo shows BPP's history is inferred, not confirmed.
- BANPU's last 19 months are missing from both lists.
- BANPU and TRUE correction effects were measured only together.
- Piece B checks: Not done yet: renames, chains, dividend spot-checks, stock count..



