"""Day 2: download every stock in both SET50 lists and record what free data is missing.

Run:  ./.venv/bin/python audit.py
Out:  data/cache/<SYMBOL>.csv  and  data/audit.csv
"""
from pathlib import Path

import pandas as pd
import yfinance as yf

START = "2012-07-02"  # first trading day the 2012 H2 list was in force
DATA = Path("data")
CACHE = DATA / "cache"


def read_list(name):
    return pd.read_csv(DATA / name, comment="#")["symbol"].tolist()


def download(symbol):
    """Daily prices adjusted for splits and dividends, cached so reruns are offline."""
    path = CACHE / f"{symbol}.csv"
    if path.exists():
        return pd.read_csv(path, index_col=0, parse_dates=True)
    bars = yf.Ticker(f"{symbol}.BK").history(start=START, auto_adjust=True)
    if len(bars):  # a dead or renamed ticker comes back empty, with no dates to fix
        bars.index = bars.index.tz_localize(None)
    bars.to_csv(path)
    return bars


def main():
    CACHE.mkdir(parents=True, exist_ok=True)
    old, new = read_list("set50_2012H2.csv"), read_list("set50_2026H2.csv")
    rows = []
    for symbol in sorted(set(old) | set(new) | {"TDEX"}):
        bars = download(symbol)
        rows.append({
            "symbol": symbol,
            "in_2012": symbol in old,
            "in_2026": symbol in new,
            "bars": len(bars),
            "first": bars.index.min().date() if len(bars) else None,
            "last": bars.index.max().date() if len(bars) else None,
        })
    audit = pd.DataFrame(rows)
    audit.to_csv(DATA / "audit.csv", index=False)

    latest = audit["last"].max()
    print(audit.to_string(index=False))
    print(f"\nNo data at all : {audit.loc[audit.bars == 0, 'symbol'].tolist()}")
    print(f"Stops before {latest}: "
          f"{audit.loc[(audit.bars > 0) & (audit['last'] < latest), 'symbol'].tolist()}")
    print(f"Starts after {START}: "
          f"{audit.loc[audit['first'] > pd.Timestamp(START).date(), 'symbol'].tolist()}")


if __name__ == "__main__":
    main()
