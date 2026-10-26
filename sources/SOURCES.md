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

**Known weakness:** both 2012 copies come from the same source (the SET's own site). No independent
second source (for example a news article listing the H2 2012 changes) has been found yet.

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

## Method

- Copied from Quantz decision D-048 (`~/Projects/quantz-claude-x/artifacts/stock_universe_experiment.txt`):
  same strategy (equal weight), same dates, two lists. The only difference is the list.
