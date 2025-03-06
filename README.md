# swap_adjusted_abs_yield_tool

- This Python tool calculates the adjusted yield of an Asset-Backed Security (ABS) portfolio hedged with interest rate swaps, using Monte Carlo simulations to model uncertainty in swap rates and ABS cash flows.
- It takes inputs like swap fixed/floating rates, ABS coupon rates, and asset cash flows (e.g., from mortgages, auto loans), then runs thousands of scenarios to estimate a distribution of net yields.

---

## Files
- `swap_adjusted_abs_yield_mc_tool.py`: Main script for simulating swap-adjusted ABS yields with Monte Carlo methods and visualizing the yield distribution with Plotly.
- `output.png`: Plot

---

## Libraries Used
- `numpy`
- `pandas`
- `plotly`

---

## Features
- **Simulation Setup**: Configures 10,000 Monte Carlo simulations over 12 monthly periods with inputs like ABS coupon (e.g., 5%), swap fixed rate (e.g., 3%), and floating rate mean/volatility.
- **Randomization**: Generates normally distributed floating swap rates to introduce uncertainty.
- **Yield Calculation**: Computes net cash flows by adjusting ABS yields with swap costs, then calculates portfolio yield as a percentage return.
- **Statistics**: Extracts median yield and 95% confidence intervals (2.5th and 97.5th percentiles) from the yield distribution.
- **Visualization**: Plots a probability histogram of yields with median and confidence interval lines using Plotly.
