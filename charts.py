import matplotlib.pyplot as plt
from backtest import net_2012, net_2026, tdex_returns, return_2012, return_2026

growth_2012 = (1 + net_2012).cumprod() * 100
growth_2026 = (1 + net_2026).cumprod() * 100
growth_tdex = (1 + tdex_returns).cumprod() * 100

plt.plot(
    growth_2012,
    label = "2012 list (after costs)",
    color = "#2a78d6",
    linewidth = 2)

plt.plot(
    growth_2026,
    label = "2026 list (after costs)",
    color = "#eb6834",
    linewidth = 2)

plt.plot(
    growth_tdex,
    label = "TDEX (no trading cost)",
    color = "#1baf7a",
    linewidth = 2,
    linestyle = "--")

plt.title("100 Baht Grew to 519 (2026 List), "
    "302 (2012 List) and 220 (TDEX)")
plt.ylabel("Value of 100 baht")
plt.legend()
plt.grid(alpha=0.3)
plt.savefig("charts/chart1.png", dpi=200)
plt.figure()

count_2012 = return_2012.iloc[1:].notna().sum(axis=1)
count_2026 = return_2026.iloc[1:].notna().sum(axis=1)

plt.plot(count_2012,
        label="2012 list",
        color="#2a78d6",
        linewidth=2)


plt.plot(count_2026,
         label="2026 list",
         color="#eb6834",
         linewidth=2)

plt.title("2012 List: 41-42 Stocks Held , 2026 List: 35-49")
plt.ylabel("Stocks held")

plt.ylim(0, 55)
plt.legend()
plt.grid(alpha=0.3)

plt.savefig("charts/chart2.png", dpi=200)

plt.figure()
