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

real_BANPU = load_mendeley("BANPU")
prices["BANPU"] = real_BANPU

prices.loc["2023-03-03":, "TRUE"] *= 0.60018

monthly = prices.resample("ME").last()

returns = monthly.pct_change()

return_2012 = returns[sorted(hold_2012)]
return_2026 = returns[sorted(set_2026)]
port_2012 = return_2012.mean(axis=1)
port_2026 = return_2026.mean(axis=1)

port_2012 = port_2012.dropna()
port_2026 = port_2026.dropna()

growth_2012 = (1 + port_2012).prod()
growth_2026 = (1 + port_2026).prod()
#CAGR_2012 = growth_2012 ** (12 / len(port_2012)) -1
#CAGR_2026 = growth_2026 ** (12 / len(port_2026)) -1


def cagr(port):
    growth = (1 + port).prod()
    months = len(port)
    return growth ** (12 / months) -1



def sharpe(port):
    average = port.mean()
    standard_deviation = port.std()
    return (average / standard_deviation) * (12 ** 0.5)



def max_drawdown(port):
    growth_line = (1 + port).cumprod()
    peak = (growth_line).cummax()
    return (growth_line / peak -1).min()




def net_returns(returns, port):
    stocks_held = returns.iloc[1:]
    held = stocks_held.notna()
    count = held.sum(axis = 1)
    weight = held.div(count, axis=0)

    filled_stocks = stocks_held.fillna(0)
    grown = weight * (1+ filled_stocks)
    drift = grown.div(1+port, axis = 0)

    last_drift = drift.shift(1)
    last_driftx = last_drift.fillna(0)

    turnover = ((weight - last_driftx).abs()
                .sum(axis = 1))


    cost_each_month = 0.0015 * turnover
    net_portfolio = port - cost_each_month
    return net_portfolio



net_2012 = net_returns(return_2012, port_2012)
net_2026 = net_returns(return_2026, port_2026)
diff = net_2026 - net_2012
avg = diff.mean()
std = diff.std()
n = len(diff)

standard_error = std / (n ** 0.5)
t_stats = avg / standard_error
percent_ci1 = avg - (1.96 * standard_error)
percent_ci2 = avg + (1.96 * standard_error)


print(
    f"Gap: {avg * 12:.2%}/yr, "
    f"t-stat = {t_stats:.2f}, "
    f"95% CI [{percent_ci1 * 12:.2%}, {percent_ci2 * 12:.2%}]"
)

print(f"CAGR    2012: {cagr(net_2012):.2%}   2026: {cagr(net_2026):.2%}")
print(f"Sharpe  2012: {sharpe(net_2012):.2f}    2026: {sharpe(net_2026):.2f}")
print(f"Max DD  2012: {max_drawdown(net_2012):.2%}  2026: {max_drawdown(net_2026):.2%}")




