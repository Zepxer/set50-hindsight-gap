## Data Check

Purpose: Can the Headline trustworthy? Every check,
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

## Not checked
- 10 stocks could not be compared due to limited shared data. ( AWC, CRC, GULF, MRDIYT, OR, SCGP, TDEX, TIDLOR, TLI, TTB ), not in Mendeley, or too little overlap.
- Data independence: Mendeley is not an independent source of truth; TRUE contains the same Yahoo price jump.
- Nothing after 14 March 2025 could be compared because Mendeley's data ends there.
- The explanation that Yahoo shows BPP's history is infered, not confirmed.
- BANPU's last 19 months are missing from both lists.
- BANPU and TRUE correction effects were measured only together.
- Piece B checks: Not done yet.


