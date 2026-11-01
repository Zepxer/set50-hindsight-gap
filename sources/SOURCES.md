# Sources

Every outside fact this project uses, where it came from, and when it was read.

## SET50 lists

| List | Source | Read on | Saved copy |
|---|---|---|---|
| **2012 H2** (in force from 2 Jul 2012) | SET market-data page `marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&langauge=en&country=US`, via the Wayback Machine. Snapshot pages carry the SET's own timestamp "04 Sep 2012 16:46:15" | 2026-10-25 | `wayback/set50_20120904.html` |
| 2012 H2, cross-check | Same page, snapshot of 4 Nov 2012: **identical** 50 symbols | 2026-10-25 | `wayback/set50_20121104.html` |
| 2013 H1 (not used; proves the six-monthly review shows up) | Same page, snapshot of 4 Jan 2013: out DCC, HEMRAJ, TPIPL; in JAS, KK, TTW | 2026-10-25 | `wayback/set50_20130104.html` |
| **2026 H2** (in force from 1 Jul 2026) | https://www.set.or.th/en/market/index/set50/overview, 50 symbols. Agrees with the H2 2026 review news (BCP, MRDIYT, TFG, THAI in) | 2026-10-25 | — |

Wayback link for the main snapshot:
https://web.archive.org/web/20120904/http://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&langauge=en&country=US

**Official list files (checked 2026-10-31, RESEARCH_LOG step 21):**
- H2 2012: https://media.set.or.th/set/Documents/2021/Dec/SET50_100_H2_2012-TH.xls (50 of 50 match)
- H2 2026, revised 3 Aug 2026: https://media.set.or.th/set/Documents/2026/Jul/SET50_SET100_H2_2026_revise.pdf (50 of 50 match)
- SET constituents page: https://www.set.or.th/en/market/information/securities-list/constituents-list-set50-set100

**Known weakness:** every 2012 copy comes from the same source (the SET itself). No source outside the SET
(for example a news article listing the H2 2012 changes) has been found.

## Index rules

- The SET50 is reviewed every six months (selection in June and December); the new list takes
  effect on the first trading day of July and January.
  https://en.wikipedia.org/wiki/SET50_Index_and_SET100_Index
- H2 2026 review news: https://www.infoquest.co.th/?p=602340

## Prices

- Yahoo Finance through the `yfinance` Python library, ticker suffix `.BK`, from 2012-07-02.
  Adjusted for splits and dividends (`auto_adjust=True`). Downloaded 2026-10-25; cached in `data/cache/`.
- Benchmark: **TDEX**, an ETF that tracks the SET50. Yahoo has no usable history for the SET50
  index itself (`^SET50.BK` returns one bar).

- **Mendeley dataset** (used for INTUCH, old GULF and BANPU; D-10, D-11): Bui Thanh Khoa & Tran Trong Huynh (2025),
  "Regional Asymmetry in Financial Markets Pricing of Skewness Risk in the Thai Stock Market", Mendeley Data,
  DOI 10.17632/gybmm9t3mr.1, CC BY 4.0. https://data.mendeley.com/datasets/gybmm9t3mr
  File `data/external/data1_THA.csv`, not in Git. It is Yahoo-derived and ends 2025-03-14, so it isn't an independent check.

## Corporate events

- **The 12 missing stocks:** dates, prices, ratios and links are in `notes/research_draft_12_stocks.md`.
- **BANPU/BPP amalgamation** (RESEARCH_LOG steps 12, 21):
  [Daol broker note](https://www.daolsecurities.co.th/assets/d61c73b7-b218-42da-8ef7-6c96d0eb349d/BANPU_260227_CR_DAOL.pdf?quality=75),
  [Kaohoon](https://www.kaohooninternational.com/markets/587876),
  [Mitihoon](https://www.mitihoon.com/2026/08/03/665460/).
- **INTUCH special dividend**, 6.54 baht, XD 2025-02-19 (D-13): [Kaohoon](https://www.kaohoon.com/news/731890).
- **THAI return to trading**, 2025-08-04 (RESEARCH_LOG steps 18, 20):
  [Thai Airways](https://www.thaiairways.com/en-th/content/news-and-announcements/thai-airways-resumes-trading-on-the-stock-exchange-on-4-august),
  [The Nation (216%)](https://www.nationthailand.com/business/corporate/40053575),
  [The Nation (SET)](https://www.nationthailand.com/business/trading-investment/40052922),
  [Aviacionline](https://www.aviacionline.com/following-restructuring-thai-airways-shares-soar-over-200-on-stock-market-return),
  [Kaohoon](https://www.kaohooninternational.com/?p=562518).
- **BEM formation** (D-14, not confirmed which company Yahoo's pre-2016 prices belong to; links seen in search results, not opened):
  [The Nation](https://www.nationthailand.com/business/30275323),
  [Mondo Visione](https://mondovisione.com/media-and-resources/news/thai-bourse-changes-constituents-in-set100-and-sethd-indices-for-first-half-of-20151230/).

## Dividend spot-checks

- **PTT**, 1.20 baht, XD 2024-02-29:
  [SET](https://www.set.or.th/en/market/news-and-alert/newsdetails?id=86033200&symbol=PTT),
  [InfoQuest](https://www.infoquest.co.th/news/2024-iqpf0iq6ds9s9vven5bm40zzs5wetedb).
- **KBANK**, 6.00 baht, XD 2024-04-22:
  [SET](https://www.set.or.th/en/market/news-and-alert/newsdetails?id=86700700&symbol=KBANK).
- **ADVANC**, 4.87 baht, XD 2024-08-19:
  [Trinity](https://www.trinitythai.com/Upload/Research/ADVANC_1732869677_34714.pdf),
  [InnovestX](https://www.innovestx.co.th/knowledge-hub/detail/research-stock-company-update/advance-earnings-2q24),
  [Panphol](https://aio.panphol.com/stock/ADVANC/dividend).

## Method

- Copied from Quantz decision D-048 (`~/Projects/quantz-claude-x/artifacts/stock_universe_experiment.txt`):
  same strategy (equal weight), same dates, two lists. The only difference is the list.
