import pandas as pd
import os 


import yfinance as yf



list_2012 = pd.read_csv("data/set50_2012H2.csv", comment="#") 
list_2026 = pd.read_csv("data/set50_2026H2.csv", comment="#")



symbols_2012 = list_2012["symbol"].tolist()
symbols_2026 = list_2026["symbol"].tolist()

set_2012 = set(symbols_2012)
set_2026 = set(symbols_2026)

all_symbols = set_2012 | set_2026
all_symbols.add("TDEX")


def get_prices(symbol):
    path = f"data/cache/{symbol}.csv"
                        
    if os.path.exists(path) :
        return pd.read_csv(path, index_col=0, parse_dates=True)
    else: 
        table = yf.Ticker(f"{symbol}.BK").history(start="2012-07-02",
                                                  end = "2026-10-23", auto_adjust=True)
        if len(table) > 0:
            table.index = table.index.tz_localize(None)
        table.to_csv(path)
        return table


rows = []

for symbol in sorted(all_symbols):
    prices = get_prices(symbol)


    rows.append({
        "symbol": symbol,
        "in_2012": symbol in set_2012,
        "in_2026": symbol in set_2026,
        "bars": len(prices),
        "first": prices.index.min(),
        "last": prices.index.max(),
    })

audit = pd.DataFrame(rows)
audit.to_csv("data/audit.csv",
             index=False)

print(audit)

mask =  (audit["bars"] == 0)
no_data = audit[mask]

print("No Data At All:", no_data["symbol"].tolist())

mask2 = (audit["first"] > pd.Timestamp("2012-07-02"))
after2012 = audit[mask2]

print("After 2012-07-02:", after2012["symbol"].tolist()) 