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

def load_close(symbol):
    path = f"data/cache/{symbol}.csv"
    table = pd.read_csv(path , 
                        index_col=0, parse_dates=True)
    return(table["Close"])

bothx = hold_2012 | set_2026
bothx.add("TDEX")
bothx.remove("INTUCH")
closes = {}
for symbol in sorted(bothx):
    closes[symbol] = load_close(symbol)

prices = pd.concat(closes, axis=1)

mendeley=pd.read_csv("data/external/data1_THA.csv",
                     parse_dates=["Date"])

def load_mendeley(symbol):
    mask = mendeley["id"] == symbol + ".BK"
    df = mendeley[mask].set_index("Date")
    return df["Aclose"]


intuch = load_mendeley("INTUCH")
old_gulf = load_mendeley("GULF")


new_gulf = prices["GULF"].dropna()
after_INTUCH = new_gulf * 1.69335
after_GULF = new_gulf * 1.02974

prices["INTUCH"] = pd.concat([intuch, after_INTUCH])
prices["GULF"] = pd.concat([old_gulf, after_GULF])

