import matplotlib.pyplot as plt
from backtest import net_2012, net_2026, tdex_returns, return_2012, return_2026, print_gap
from backtest import net_survivor, net_2012_q, net_2026_q

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





headline = print_gap(net_2012, net_2026, "Headline", 12)
sensitivity1 = print_gap(net_2012, net_survivor, "Sensitivity 1", 12)
sensitivity2 = print_gap(net_2012_q, net_2026_q, "Sensitivity 2", 4)
headline_gap, headline_lower, headline_upper = headline
sensitivity1_gap, sensitivity1_lower, sensitivity1_upper = sensitivity1
sensitivity2_gap, sensitivity2_lower, sensitivity2_upper = sensitivity2

name = ["Headline", "Stocks trading in 2012", "Quarterly rebalancing"]
gaps = [
    headline_gap * 100,
    sensitivity1_gap * 100,
    sensitivity2_gap * 100]
distances = [
    (headline_gap - headline_lower) * 100,
    (sensitivity1_gap - sensitivity1_lower) * 100,
    (sensitivity2_gap - sensitivity2_lower) * 100]

plt.errorbar(name, gaps, yerr=distances, fmt="o", capsize=5, color="#52514e")
plt.axhline(0, color="black", linewidth=1)
plt.title("Hindsight Gap Stays Above Zero in All Three Tests (95% CI)")
plt.ylabel("Gap (% per year)")
plt.grid(alpha=0.3)
plt.margins(x=0.2)
plt.savefig("charts/chart3.png", dpi=200)

plt.figure()

monthly_gap = (net_2026 - net_2012) * 100
cumulative_gap = monthly_gap.cumsum()
plt.plot(
    cumulative_gap,
    color="#52514e",
    linewidth=2)
plt.axhline(0, 
            color="black", 
            linewidth=1)
plt.grid(alpha=0.3)
plt.title("Most of the Gap Built Up Before 2020\n(post hoc, not in the frozen plan)")
plt.ylabel("Cumulative gap (percentage points)")
plt.tight_layout()
plt.savefig("charts/chart4.png", dpi=200)
