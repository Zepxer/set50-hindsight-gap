# Research log

One entry per step: what was done, what was found, what it means.

---

## 27 Oct: the missing-price problem

### Step 1: Research pass on the 12 missing stocks (Claude, web search)
- **Result:** events, dates and prices are in `notes/research_draft_12_stocks.md` (not verified yet).
- **Problem found:** 9 of the 12 have no Yahoo prices from 2012 until their event: BIGC, HEMRAJ, GLOW,
  ROBINS, DTAC, INTUCH, PS, ESSO, and MAKRO (missing until 2024).
  - The rule "cashed out at the takeover price" only covers the last day.
  - Without monthly prices before that day, these stocks can't be held in the backtest.
  - The 3 renames (BGH, TMB, TUF) are fine, because the new tickers carry the full history.
- **Options:**
  - A: find another free price source.
  - B: headline = "dropped", with the bias stated.
  - C: buy SET data (USD 400 per year of data).
- **Decision (Ikkyu):** try A first; B is the fallback.

### Step 2: Check the Mendeley dataset (metadata only, no download)
- **Dataset:** "Regional Asymmetry in Financial Markets Pricing of Skewness Risk in the Thai Stock Market",
  by Bui Thanh Khoa and Tran Trong Huynh (FPT University), published 18 Aug 2025.
  - DOI: 10.17632/gybmm9t3mr.1
  - Licence: CC BY 4.0 (free to use with credit).
  - Link: https://data.mendeley.com/datasets/gybmm9t3mr
- **Contents:** one file, `data1_THA.csv`, 238.5 MB.
  - 2,337,955 rows of daily SET data, Jan 2000 – Mar 2025.
  - Columns: Date, Open, High, Low, Close, Vol, Aclose (adjusted close), id.
- **Warning sign:** tickers are written as `AJ.BK`, the Yahoo format. The data was probably downloaded from Yahoo.
  Yahoo drops delisted stocks, so it may have the **same holes** we have.
  - Exception: the authors may have downloaded before some delistings, so stocks delisted after their
    download could still be there.
- **Size check:**
  - 2.34M rows ÷ ~6,200 trading days ≈ 380 stocks on an average day.
  - SET lists ~800 stocks today, so the dataset is not complete either way.
- **Still unknown:** whether BIGC, GLOW, DTAC, etc. are in it. The only way to know is to download the file.
- **Next:** download it (needs Ikkyu's OK) and count the rows for each of the 9 stocks.

### Step 3: Download the Mendeley file and check it (approved by Ikkyu)
- **Downloaded:** `data1_THA.csv`, 238,546,418 bytes, on 27 Oct at 11:56.
  - SHA-256 `0cb504f4…890f7`, which matches the hash Mendeley publishes, so the file is complete and unchanged.
  - Kept in a temporary folder, not in the project. It can be downloaded again from the DOI.
- **Contents:** 477 stocks.
  - **Every stock's last date is 2025-03-14.** The file is a snapshot of stocks still listed in March 2025,
    so it has the same survivorship problem as Yahoo.
  - Only stocks still alive on that date are in it.
- **Confirmed it's Yahoo data:** PTT's daily returns match our Yahoo cache exactly
  (3,096 shared days, correlation 1.0000, median difference 0).
- **The 9 missing stocks:**
  - **INTUCH: found**, 1995-01-03 → 2025-03-14 (7,555 days). It was still listed in Mar 2025.
  - **Not found (8):** BIGC, HEMRAJ, GLOW, ROBINS, DTAC, PS, ESSO, MAKRO. All were delisted or
    renamed before Mar 2025. (BSRC, ESSO's new name, isn't in it either.)
- **Bonus finds:**
  - **Old GULF: 2017-12-06 → 2025-03-14 (1,768 days).** This fills the GULF hole.
    - Splice check: old GULF closed 46.75 on 14 Mar 2025.
    - ÷ 1.02974 (the swap ratio) = 45.40.
    - New GULF first close on 3 Apr 2025 = 46.195. Close; the gap covers 4 missing trading days plus the suspension.
  - **BANPU: 2000 → 2025, no gap.** Yahoo's BANPU starts 2016-10-28.
    - ⚠️ But on the shared days, Mendeley's and Yahoo's BANPU daily returns only correlate **0.40**.
      For PTT and SCB it's 1.00. One of the two BANPU series is wrong. Not solved yet; on the list for Thursday's checks.
  - SCB: same as Yahoo (starts 2022-04-20), so no help.
  - TIDLOR: old Ngern Tid Lor is not in it, so no help.
- **Verdict on option A:** **failed for 8 of the 9.** The dataset was built the same way as ours (from Yahoo,
  stocks alive today), so it can't fill survivorship holes. It **does** help with INTUCH and old GULF, and
  maybe BANPU.
- **Lesson for the portfolio:** a free dataset built from Yahoo has Yahoo's survivorship bias. Check where
  data comes from before trusting it to fix a bias.
- **Next:** Ikkyu decides:
  1. Should the 8 still-missing stocks use option B (dropped, with the bias stated)?
  2. Should Mendeley be used for INTUCH and old GULF (and BANPU after a check)?

### Step 4: Decisions (Ikkyu)
- The 8 still-missing stocks are **dropped** (option B). Written up as D-9 in `notes/DECISIONS.md`.
- **Mendeley is used** for INTUCH and old GULF. Written up as D-10.
  - The file was moved to `data/external/data1_THA.csv`.
  - `data/external/` was added to `.gitignore` (too big for Git; the DOI + hash make it reproducible).
- BANPU: wait for Thursday's check.

### Step 5: Link checks, first batch (Ikkyu)
- **TMB → TTB:** ✔ InfoQuest confirms it.
- **HEMRAJ:** ✔ event confirmed. 4.50 baht was WHA's price for the 22.53% block (and the VTO).
  The delisting tender price is still unknown, which is OK because HEMRAJ is dropped (D-9).
- **BGH → BDMS:** ? The Bangkok Post article is paywalled. Wikipedia was given as a second try.
  - The date doesn't change the backtest: Yahoo's BDMS series already covers 2012 → today.
- **TUF → TU:** ✘ the Thai Union IR link is dead. Two new links were added (EGM 2015 invitation, Thai Union history).
- **BIGC:** not checked yet.

### Step 6: Link checks, second batch
- **BIGC:** ✔ (Ikkyu). The sources only give the tender offer as "at most 252.88 baht"; the final price
  is unknown. OK, because BIGC is dropped (D-9).
- **TUF → TU:** none of the links opened for Ikkyu.
  - Claude tested them: the two added links return 404 (dead) and were removed.
  - The original Thai Union IR link works from the command line, and its text says:
    "Effective 23rd September 2015, the new stock ticker symbol of 'TUF' will be changed to 'TU'."
  - ✔ by Claude, marked as such. It probably didn't load in Ikkyu's browser for a site reason.
  - Backtest impact: none. Yahoo's TU series covers 2012 → today.

### Step 7: Link checks, third batch (Ikkyu)
- **GLOW:** ✔ confirmed.
- **ROBINS:** ✔ confirmed: 66.50 baht per share, paid in CRC shares.
  - Extra from The Nation: ROBINS closed at 63.75 baht that Tuesday morning (+3.50, +5.81%).
  - So the offer was about 4% above the market price.

### Step 8: Link checks, last batch (Ikkyu)
- ✔ INTUCH (1.69335, last trading 20 Mar 2025), GULF (1.02974, new GULF from 3 Apr 2025),
  DTAC, MAKRO, PS, ESSO.
- **Totals:** 11 rows ✔ and 1 `?` (BGH's rename date: paywalled source, no effect on the backtest).
- 12-stock table box ticked in SCHEDULE.md. Next: PLAN.md.

### Step 9: PLAN.md frozen (Ikkyu)
- Written by Ikkyu. Claude converted it from RTF to Markdown (formatting only).
  The raw first draft is kept in `notes/Raw_PLAN.md`.
- Committed as `dc0cd4a` on 27 Oct at 16:59, before any backtest code exists.

## 28 Oct: found while building backtest.py

### Step 10: INTUCH's special dividend may be missing from Mendeley's Aclose (for Thursday's checks)
- INTUCH fell from 80.75 to 76.25 on **2025-03-12**: −4.50 baht (−5.6%), exactly the 4.50-baht special dividend.
- Mendeley's `Aclose` equals `Close` on both days, so that dividend is **not** adjusted for.
  The backtest would show a fake −5.6% day for INTUCH.
- Size: INTUCH is 1 of 42 stocks, so about −0.13% for the 2012 list in March 2025. Small, but it's a known error.
- To decide on Thursday (Ikkyu): add the 4.50 back on the ex-date, or leave it and disclose it.
  Either way, write it in `notes/DATA_CHECKS.md`.
- Chain check: INTUCH's last close of 77.00 ÷ 1.69335 = 45.47 vs new GULF's first close of 46.19. Consistent.

### Step 11: BANPU's Yahoo series has a second problem (for Thursday's checks)
- Yahoo's BANPU **stops trading on 2026-08-11** (last close 14.6). After that there are only 2 empty rows
  (2026-09-11 and 2026-10-22).
- So BANPU has **no return** in the last months for both lists. Is this a suspension, a corporate action,
  or a Yahoo error? To be found out.
- Together with Step 3 (Mendeley vs Yahoo correlation 0.40) and its start in 2016, BANPU is the least
  trustworthy series. Thursday decides: fix, use Mendeley, or drop it from both lists and disclose.

## 30 Oct: data checks, piece A

### Step 12: Yahoo's "BANPU" is the wrong company
- **Finding:** Yahoo's `BANPU.BK` from 2016-10-28 to mid-2026 is really the price history of **BPP (Banpu Power)**,
  Banpu's subsidiary.
  - Daily returns vs Mendeley's `BPP.BK`: correlation **1.0000** over 2,037 days (ratio constant at 0.902).
  - Vs Mendeley's real `BANPU.BK`: only 0.3962.
  - 2016-10-28, the first date of Yahoo's series, is BPP's first date in Mendeley too.
- **Likely cause:** BANPU and BPP amalgamated into a new company in 2026, keeping the ticker BANPU
  (1 BANPU → 0.38242 new, 1 BPP → 0.80208 new). Yahoo appears to have attached BPP's history to the ticker.
  The cause is inferred; the mismatch itself is measured.
- This explains all three BANPU problems: the 2016 start, the 0.40 correlation, and the break in Aug 2026.
- **So Mendeley's BANPU is the real one** (2000 → 2025-03-14). It's in both lists.
- **Decision:** to be made by Ikkyu **before** looking at the effect on the headline.
- Sources: [Daol broker note](https://www.daolsecurities.co.th/assets/d61c73b7-b218-42da-8ef7-6c96d0eb349d/BANPU_260227_CR_DAOL.pdf?quality=75),
  [Kaohoon: BANPU redebuts](https://www.kaohooninternational.com/markets/587876).

### Step 13: Every Yahoo series compared with Mendeley
- 50 stocks have enough shared days. Correlation of daily returns: all ≥ 0.998 except BANPU (WHA 0.9984).
- So **BANPU is the only wrong-company series among the 50 that could be compared**.
- Not comparable (not in Mendeley, or too little overlap): AWC, CRC, GULF, MRDIYT, OR, SCGP, TDEX, TIDLOR, TLI, TTB.

### Step 14: TRUE has a fake +68.6% jump on 2023-03-03
- Yahoo's TRUE goes from 4.873 to 8.217 on the day the merged company started trading. The old prices weren't adjusted.
- Real value: 8.217 × 0.60018 = 4.93, so the real move was about +1.2%.
- TRUE is in both lists, so both portfolios get a fake boost that month. PLAN.md already has the rule (0.60018).

### Step 15: Correction to Step 10 (INTUCH dividend): Claude's inference was wrong
- Step 10 said the −4.50 baht on 2025-03-12 was the special dividend, and that Mendeley hadn't adjusted for it.
  That was inferred from the amount matching a 4.50 forecast. It was never checked against a source.
- The actual special dividend was **6.54 baht, XD 19 Feb 2025, paid 4 Mar 2025**
  ([Kaohoon](https://www.kaohoon.com/news/731890)).
- Mendeley's `Aclose` already reflects it: Aclose/Close reaches 1.0 on 2025-02-19.
- **So there is nothing to fix.** Adding 4.50 back would have put a fake +5.9% into INTUCH.
  Ikkyu's "fix" decision was based on Claude's wrong premise and is withdrawn.

### Step 16: The Mendeley comparison can't catch shared errors (TRUE proves it)
- TRUE **passed** the comparison in Step 13 (correlation 1.0000 over 3,096 days), even though it has the fake jump.
- Reason: Mendeley's TRUE has the same jump (5.10 → 8.60 on 2023-03-03), because both come from Yahoo.
- So a high correlation means "same series as Yahoo", not "correct". TRUE's jump was only found by looking at
  the merger date directly. The comparison finds wrong series, not bad data.

## 31 Oct: data checks, continued

### Step 17: Dividend spot-checks (Ikkyu, with ChatGPT search)
Yahoo's `Dividends` column vs SET announcements. All three match on amount and XD date.
- **PTT:** 1.20 baht, XD 2024-02-29, record 2024-03-01, paid 2024-04-30.
  [SET](https://www.set.or.th/en/market/news-and-alert/newsdetails?id=86033200&symbol=PTT),
  [InfoQuest](https://www.infoquest.co.th/news/2024-iqpf0iq6ds9s9vven5bm40zzs5wetedb)
- **KBANK:** 6.00 baht, XD 2024-04-22, record 2024-04-23, paid 2024-05-10; announced 2024-02-29.
  [SET](https://www.set.or.th/en/market/news-and-alert/newsdetails?id=86700700&symbol=KBANK)
- **ADVANC:** 4.87 baht, XD 2024-08-19, record 2024-08-20, paid 2024-09-03. **Link still needed.**
- **Limit:** only 3 dividends out of many, all from 2024, all large companies. It supports Yahoo's dividend data
  but doesn't prove it for every stock and year. Older or smaller stocks weren't tested.

### Step 18: Outside review, 31 Oct (reviewer's points checked by Claude against the data)
- **THAI:** confirmed. Flat at 3.207 until 2025-08-01, then 10.141 on 2025-08-04 (+216%); +273.5% for the month,
  the largest monthly move in the data.
  - News reports the same +216% first-day rise on its return to trading, from 3.32 to 10.50
    ([Aviacionline](https://www.aviacionline.com/following-restructuring-thai-airways-shares-soar-over-200-on-stock-market-return),
    [Kaohoon](https://www.kaohooninternational.com/?p=562518)).
  - So it looks like a real price move, not a Yahoo error. Not yet settled: whether the restructuring changed what
    an old share was worth.
  - THAI is in both lists. That month adds +0.55 pp to the monthly difference, about +0.04 pp/yr to the gap.
- **Power:** confirmed. Real σ of the difference 3.77%/yr, so the detectable gap is 2.79%/yr (plan: 8.4%, 6.2%).
- **Gap by period:** confirmed. Sum of the monthly gap: 2012–2019 +49.8 pp, 2020–2026 +6.7 pp (2020–2023 about −0.3 pp).
  This split was **not in PLAN.md**, so it must be labelled post hoc (PLAN.md section 8).
- **pandas 3.1.0:** confirmed as the installed version. The reviewer's point about 2.x filling gaps wasn't tested here.
- **Other points:** README 172 → 171 (fixed; Claude's wording). Returns start Aug 2012. TDEX isn't reported yet.
  Sharpe has no risk-free rate.
- **Small correction to the review:** the lists share 32 stocks after renames (29 before).

### Step 19: Re-download test (Ikkyu's code, 31 Oct)
- Downloaded all 60 Yahoo series again with the same dates, in memory, and compared with `data/cache/`.
- Largest difference in any stock: 0.00008% (IVL, rounding). 0 of 60 exceed 0.1%.
- So the saved data is what Yahoo serves today, and anyone rerunning the download gets the same prices.
- **Limit:** this proves the data can be reproduced, not that it's correct. Yahoo's BANPU still matches our saved BPP series.

### Step 20: ADVANC dividend and THAI links (found by Claude, confirmed by Ikkyu, 31 Oct)
- **ADVANC:** 4.87 baht, XD 2024-08-19.
  [Trinity](https://www.trinitythai.com/Upload/Research/ADVANC_1732869677_34714.pdf),
  [InnovestX](https://www.innovestx.co.th/knowledge-hub/detail/research-stock-company-update/advance-earnings-2q24),
  [Panphol](https://aio.panphol.com/stock/ADVANC/dividend).
- **THAI:** returned to trading 2025-08-04: 3.32 before suspension, opened 10.50, closed 10.30.
  [Thai Airways](https://www.thaiairways.com/en-th/content/news-and-announcements/thai-airways-resumes-trading-on-the-stock-exchange-on-4-august),
  [The Nation (216%)](https://www.nationthailand.com/business/corporate/40053575),
  [The Nation (SET)](https://www.nationthailand.com/business/trading-investment/40052922).
  The jump is real, not a Yahoo error. What an old share became in the restructuring isn't confirmed by a filing.
- **SET archive found:** official files for H2 2012 and the revised H2 2026 list, on SET's constituents page.

### Step 21: Both lists checked against SET's own files (found by Claude, confirmed by Ikkyu, 31 Oct)
- **2012 list:** SET's file "For calculating the index during July 1, 2012 - December 31, 2012", sheet SET50-EN.
  50 of 50 names match `data/set50_2012H2.csv`, no differences. The file's 5 replacement names (KK, KSL, LPN, STA, TTW)
  are a separate reserve list and aren't constituents. Our list came from Wayback snapshots of SET's page (Sep and Nov 2012),
  so the official file is a real second look.
  [SET file](https://media.set.or.th/set/Documents/2021/Dec/SET50_100_H2_2012-TH.xls)
- **2026 list:** SET's revised PDF "For calculating the index during July 1 - December 31, 2026, Update on August 3, 2026".
  50 of 50 names match `data/set50_2026H2.csv`, no differences.
  [SET file](https://media.set.or.th/set/Documents/2026/Jul/SET50_SET100_H2_2026_revise.pdf),
  [SET constituents page](https://www.set.or.th/en/market/information/securities-list/constituents-list-set50-set100)
- **One revision:** the PDF's only change is Inclusion BANPU, Exclusion BANPUU, both named Banpu Public Company Limited.
  This fits the BANPU/BPP amalgamation (Step 12). The new company trades as BANPU, first trading 4 Aug 2026.
  [Kaohoon](https://www.kaohooninternational.com/markets/587876),
  [Mitihoon](https://www.mitihoon.com/2026/08/03/665460/).
  The temporary BANPUU ticker itself is thinly sourced outside SET's PDF.
- **Effect on the backtest:** none. Same company, and D-11 already stops holding BANPU after 2025-03-14.
- **Limits:** we read the August revision, not the original July file; the original list is inferred from the one stated change.
  Replacements made during H2 2012 wouldn't show in the 2012 file, though the Sep and Nov 2012 snapshots show the same 50.
  This checks who was on the lists, not their prices. Replaces audit #12's search for 2012 news.

### Step 22: TDEX added to the scorecard (Ikkyu's code, 31 Oct)
- **Result:** CAGR 5.70%, Sharpe 0.44, max drawdown −30.20%, on the same 171 months as both lists, with no missing months.
- **Data look:** no gaps over 10 days. The largest daily moves are all in March–April 2020 (largest −10.29% on 2020-03-12).
- **Costs:** no trading cost is taken from TDEX because it's a single fund that is held, while both lists pay 0.15%.
- **Not comparable as skill:** TDEX is below the 2012 list, but the 2012 list is equal-weight and has 8 stocks dropped.
- **Not checked:** whether Yahoo's adjusted TDEX prices include every fund distribution.

### Step 23: Rerun setup (Ikkyu, 31 Oct)
- Added `requirements.txt` (pandas, yfinance, matplotlib pinned) and the install, audit and backtest commands to the README.
- README records the Mendeley source, DOI, licence, save location and SHA-256. The saved file's hash matches.
- **Reproducibility fix:** `audit.py` had no end date, so a fresh download would run past 22 Oct and change the results.
  Added `end="2026-10-23"` (exclusive), matching the re-download test. Saved results didn't change.

### Step 24: Sensitivity 1, stocks trading in July 2012 (Ikkyu's code, 31 Oct)
- 36 stocks (D-14), 171 months. Holds 35 at both ends: BANPU but no SCB at the start, SCB but no BANPU at the end.
- **Result:** gap 3.00%/yr, t = 4.40, 95% CI [1.66%, 4.34%]. Headline stays 3.97%, t = 3.98.
- The gap falls about 1 point a year without the 14 later listings. This is an estimate, not the exact effect of those
  stocks, because removing them also changes every other stock's equal weight.
- The gap calculation is now a function, `print_gap`, tested by reproducing the headline exactly.

### Step 25: Sensitivity 2, quarterly rebalancing (Ikkyu's code, 31 Oct)
- Quarters end Jan, Apr, Jul, Oct (D-15). 57 quarterly returns from 2012-07-31 to 2026-10-31, using both full lists.
- **Result:** gap 3.75%/yr, t = 3.81, 95% CI [1.82%, 5.68%]. Headline stays 3.97%, t = 3.98.
- Rebalancing frequency barely changes the gap. Noise in the yearly difference stays about the same (about 3.7%/yr vs 3.77%/yr).
- `print_gap` now takes periods per year. `cagr` and `sharpe` still assume 12, so they aren't used on the quarterly series.

### Step 26: Charts (Ikkyu's code, `charts.py`, 31 Oct–1 Nov)
- **Chart 1:** growth of 100 baht, ending at 519 (2026 list), 302 (2012 list), 220 (TDEX). The first point is end of Aug 2012, so lines start near 103.
- **Chart 2:** stocks held. The 2012 list holds 41–42; the 2026 list goes from 35 to 49, crossing around 2018.
- **Chart 3:** headline and both sensitivities with 95% CIs. No bar touches zero. All three share the same data, so they aren't separate proofs.
- **Chart 4 (post hoc):** cumulative gap, +49.8 points by end 2019 and +56.5 at the end. Shows when the gap appeared, not why, and not that it has ended.
- **Colours:** blue and orange follow each list across charts; TDEX is dashed green; differences are grey. The three colours passed a colour-blind check.
