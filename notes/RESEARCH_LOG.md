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
