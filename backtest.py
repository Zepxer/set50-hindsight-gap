import pandas as pd


list_2012 = pd.read_csv("data/set50_2012H2.csv", comment="#") 
list_2026 = pd.read_csv("data/set50_2026H2.csv", comment="#")
symbols_2012 = list_2012["symbol"].tolist()
symbols_2026 = list_2026["symbol"].tolist()
set_2012 = set(symbols_2012)
set_2026 = set(symbols_2026)


rename = {"BGH": "BDMS",
          "TMB": "TTB",
          "TUF": "TU"}


new_set2012 = set()

for symbol in sorted(set_2012):
    if symbol in rename:
        new_set2012.add(rename[symbol])
    else:
        new_set2012.add(symbol)

dropped = {"BIGC", "HEMRAJ", "GLOW",
         "DTAC", "PS", "ESSO", "MAKRO", "ROBINS"}

hold_2012 = new_set2012 - dropped
print(len(hold_2012 & set_2026))

print(len(hold_2012 - set_2026))
print(len(set_2026 - hold_2012))

def load_close(symbol):
    path = f"data/cache/{symbol}.csv"
    table = pd.read_csv(path , 
                        index_col=0, parse_dates=True)
    return(table["Close"])

print(load_close("PTT").tail())

git add -A && git commit -m "backtest.py: load_close; PLAN.md: swap ratios"
