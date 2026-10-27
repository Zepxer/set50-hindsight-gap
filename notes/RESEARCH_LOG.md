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
