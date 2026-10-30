import pandas as pd
from backtest import prices

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