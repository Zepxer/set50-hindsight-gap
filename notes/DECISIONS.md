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
