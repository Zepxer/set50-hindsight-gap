# Decisions

Every choice that changes a number, and why. Newest at the bottom.

## D-1: Start in July 2012 (2026-10-25)
The oldest SET50 list we could confirm is the one in force from 2 Jul 2012. It gives about
14 years (Jul 2012 to Oct 2026), longer than the 2016 option.

## D-2: Compare against the 2026 H2 list (2026-10-25)
Today's SET50, read from the SET website. It is the list someone would pick "knowing who won".

## D-3: Equal weight, no settings (2026-10-25)
Same reason as Quantz D-048: with nothing to tune, nothing can be overfitted, so the list is the
only difference between the two tests.

## D-4: Renamed tickers use the new ticker's data (2026-10-25)
Same company, new name: BGH → BDMS, TMB → TTB, TUF → TU.

## D-5: Bought-out stocks are run two ways, and the range is reported (2026-10-25)
Twelve 2012 stocks have no Yahoo data. Unlike GM in the US study, most Thai ones were **bought out**
(BIGC, HEMRAJ, GLOW, ROBINS, DTAC, INTUCH…), which usually pays shareholders a premium. So:
- (a) **dropped:** their money is split among the remaining stocks;
- (b) **total loss:** their money is counted as lost, the pessimistic end.

Reason (Ikkyu): both (a) and (b) alone just cut the problem out. Showing the range is honest, and
the flaw is realistic and worth reporting.

## D-6: Late listers join on their listing day (2026-10-25)
Stocks in the 2026 list that did not trade in 2012 (OR, SCGP, CRC, AWC, TLI, MRDIYT…) are held
only from their first trading day. Before that, the money is split among the others.

## Open: data problems found in the audit, not yet handled
- **SCB** starts 2022 (became holding company SCB X), **BANPU** starts 2016 (cause unknown),
  **GULF** and **TIDLOR** start 2025 (restructurings).
- **TRUE** is a splice: after the 2023 merger with DTAC it is a different company on the same line.
- **MAKRO → CPAXT** only from 2024; **PS → PSH** only from 2016; **ESSO** no data.
- The buyout stories above are first guesses and still need checking against news.

## D-7: Plan reviewed twice; revised plan doc (2026-10-25)
Revised plan: https://claude.ai/artifact/NWcc18pUX44H3iFfGPLh1b (audit: https://claude.ai/artifact/9wM1inmr4niWkTcFPhsBsJ).
- Headline = average monthly return difference (2026 list minus 2012 list) × 12, with t-stat and 95% CI.
  The CAGR gap is reported beside it, not tested.
- Rebalance monthly (first trading day). Costs 0.15% of traded value, both lists.
- Bought-out stocks cashed out at the takeover price (headline); swaps (DTAC → TRUE, INTUCH → GULF,
  PS → PSH) cashed out at swap value on the event date.
- Stocks held only while Yahoo has data. GULF and TIDLOR (hindsight list only) lose their pre-2025
  years, which biases the gap toward zero; SCB and BANPU are in both lists.
- Power: σ ≈ 8.4%/yr from the Quantz Dow result, so the smallest detectable gap ≈ 6.2%/yr (approximate).
- Authorship: audit.py is disclosed as written with Claude, not retyped. All analysis code is written by Ikkyu.

## D-8: audit.py is now Ikkyu's own (2026-10-26)
Ikkyu wrote `audit.py` himself from a description in words, with hints, without looking at Claude's
version. Its output matches Claude's exactly (72 rows; same 12 no-data and 16 late-start stocks), so
Claude's version was deleted (still in Git history). Supersedes the authorship line of D-7: all code in
the project is written by Ikkyu; Claude explains and reviews.

## D-9: The 8 stocks with no prices are dropped (2026-10-27)
BIGC, HEMRAJ, GLOW, ROBINS, DTAC, PS, ESSO and MAKRO have no daily prices from 2012 until their event,
in Yahoo or in the Mendeley dataset (see `notes/RESEARCH_LOG.md`, steps 1–3). Without prices they
can't be held month by month, so "cashed out at the takeover price" (D-7) can't be run.
- **Headline rule changes to "dropped":** the 2012 list is the 2012 stocks that have prices.
  The 8 are left out from the start, and the money is split among the others.
- **Bias, stated in advance:** the direction is unknown. These 8 were mostly **taken over**
  (often at a premium), not failures, so dropping them may remove winners as well as losers.
  This is not the same as the GM case in the US study.
- Supersedes the bought-out rule of D-7. The renames (BGH → BDMS, TMB → TTB, TUF → TU) are unaffected.
- SET's paid data (USD 400 per year of data) would fix this; it's noted as future work.

## D-10: Mendeley dataset used for INTUCH and old GULF (2026-10-27)
Source: Bui Thanh Khoa & Tran Trong Huynh (2025), "Regional Asymmetry in Financial Markets Pricing of
Skewness Risk in the Thai Stock Market", Mendeley Data, DOI 10.17632/gybmm9t3mr.1, CC BY 4.0.
- File `data/external/data1_THA.csv` (238.5 MB, not in Git; SHA-256 0cb504f42206604bf7f8a149a70098c4b2bef10bcfe83a4827c804327f1890f7).
- It is Yahoo data (PTT matches our cache exactly), frozen on 2025-03-14.
- **INTUCH** (2012 list): prices 1995 → 2025-03-14; then swapped into new GULF at 1 INTUCH → 1.69335.
- **Old GULF** (2026 list): prices 2017-12-06 → 2025-03-14; then 1 old GULF → 1.02974 new GULF
  (Yahoo, from 2025-04-03).
- This removes most of the GULF bias in D-7. TIDLOR's pre-2025 years are still missing
  (Ngern Tid Lor isn't in the file).
- **BANPU** (both lists) also has a full series in Mendeley, but it disagrees with Yahoo on shared days
  (return correlation 0.40). Not used until Thursday's data check settles which one is right.

## D-11: BANPU uses Mendeley; Yahoo's series is BPP (2026-10-30)
Yahoo's `BANPU.BK` is BPP's price history (`notes/RESEARCH_LOG.md`, step 12). Ikkyu chose option A before seeing
the effect on the headline: use Mendeley's real BANPU to 2025-03-14, then stop holding it, under PLAN.md's rule
"held only while usable price data are available". BANPU is in both lists.

## D-12: TRUE's merger jump removed (2026-10-30)
Prices from 2023-03-03 are multiplied by 0.60018, the swap ratio already in PLAN.md (RESEARCH_LOG step 14).
This removes a fake +68.6% day.

## D-13: No INTUCH dividend fix (2026-10-30)
Claude's Step 10 was wrong: the 6.54-baht special dividend went XD on 2025-02-19 and is already in Mendeley's
Aclose (ratio 0.9341 = 1 − 6.54/99.25). The −5.6% on 2025-03-12 is a real price move; GULF fell −5.6% that day too.
Ikkyu's earlier "fix" choice is withdrawn because its premise was false (RESEARCH_LOG step 15).

## D-14: Sensitivity 1 keeps SCB, 36 stocks (2026-10-31)
Ikkyu chose this before any Sensitivity 1 returns were run. PLAN.md says "stocks trading in July 2012", and SCB was,
though its price data only starts 2022-04-20. Under PLAN.md's rule it's held only while usable prices exist, so from 2022.
The check is meant to remove later listings, and SCB isn't one. The other 35 have a price in July 2012; 14 don't and are left out:
AWC, COM7, CRC, GPSC, GULF, MRDIYT, MTC, OR, OSP, SCGP, TFG, TIDLOR, TLI, WHA.
**Not checked:** BEM was formed from BECL and BMCL around the end of 2015, but Yahoo shows prices from 2012, probably a
predecessor's history. It stays in, and it's in the 2026 list for the headline too.

## D-15: Sensitivity 2 uses quarters ending Jan, Apr, Jul, Oct (2026-10-31)
Ikkyu chose this before any quarterly returns were run. `resample("QE-OCT")` gives 57 quarterly returns from
2012-07-31 to 2026-10-31, the same start and end as the monthly test, and keeps BANPU's last price.
Calendar quarters would start returns in Oct 2012 and cut the last quarter short.
