import pandas as pd
import yfinance as yf 
from backtest import prices, return_2012, return_2026
from backtest import bothx, load_close


def moves(prices, symbol):
    move = prices[symbol].pct_change().abs()
    x1 = move.nlargest(4)
    return x1
    
for symbol in ["TTB", "BDMS", "TU"]:
    print(symbol)
    print(moves(prices, symbol))

print(prices["TTB"].loc["2021-05-03":"2021-05-11"])

print(prices["GULF"].loc["2025-03-14":"2025-04-03"].dropna().pct_change())
print(prices["INTUCH"].loc["2025-03-14":"2025-04-03"].dropna().pct_change())

print(prices["ADVANC"].loc["2015-12-16":"2015-12-23"].pct_change())

def count_(returns):
    return returns.iloc[1:].notna().sum(axis=1)

count_2012 = count_(return_2012)
count_2026 = count_(return_2026)

print(count_2012.iloc[0], count_2012.iloc[-1], count_2012.loc["2025-03"].iloc[0], count_2012.loc["2025-04"].iloc[0])
print(count_2026.iloc[0], count_2026.iloc[-1], count_2026.loc["2025-03"].iloc[0], count_2026.loc["2025-04"].iloc[0])

for symbol in sorted(bothx): 
    new = yf.Ticker(f"{symbol}.BK").history(
            start="2012-07-02",
            end ="2026-10-23", auto_adjust=True)["Close"]
    new.index = new.index.tz_localize(None)
    old = load_close(symbol)
    shared = pd.concat({"new": new, "old": old}, axis=1).dropna()
    biggest = (shared["new"] / shared["old"] -1 ).abs().max()
    print(symbol, len(shared), biggest)
