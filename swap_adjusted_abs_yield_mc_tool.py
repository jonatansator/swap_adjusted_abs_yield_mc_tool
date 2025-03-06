import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Constants
N_SIMS = 10000
PERIODS = 12  # Monthly periods for one year
COLOR_ACTUAL = '#FF6B6B'  # Reddish for actual data
COLOR_FORECAST = '#4ECDC4'  # Teal for forecasted data

def simulate_yields(abs_coupon, swap_fixed, swap_float_mean, swap_float_std, cash_flows):
    # Step 1: Initialize input data
    cf = np.array(cash_flows)
    n_periods = len(cf)
    
    # Step 2: Generate random swap floating rates
    float_rates = np.random.normal(swap_float_mean, swap_float_std, (N_SIMS, n_periods))
    
    # Step 3: Calculate swap-adjusted cash flows
    swap_cost = swap_fixed - float_rates
    abs_yield = abs_coupon / 100
    net_cf = cf * (1 + abs_yield) - (cf * swap_cost / 100)
    
    # Step 4: Compute total portfolio yield per simulation
    total_investment = cf.sum()
    yields = (net_cf.sum(axis=1) - total_investment) / total_investment * 100
    
    # Step 5: Derive statistics
    median_yield = np.median(yields)
    ci_lower = np.percentile(yields, 2.5)
    ci_upper = np.percentile(yields, 97.5)
    
    return yields, median_yield, ci_lower, ci_upper

def plot_yield_distribution(yields, median_yield, ci_lower, ci_upper):
    # Step 6: Create histogram with Plotly
    fig = go.Figure()
    
    # Histogram of yields
    fig.add_trace(go.Histogram(
        x=yields,
        histnorm='probability',
        name='Yield Distribution',
        marker_color=COLOR_FORECAST,
        opacity=0.7
    ))
    
    # Vertical line for median
    fig.add_vline(x=median_yield, line_dash='dash', line_color=COLOR_ACTUAL, name='Median Yield')
    
    # Confidence interval lines
    fig.add_vline(x=ci_lower, line_dash='dash', line_color=COLOR_ACTUAL, name='95% CI Lower')
    fig.add_vline(x=ci_upper, line_dash='dash', line_color=COLOR_ACTUAL, name='95% CI Upper')
    
    # Update layout with dark theme
    fig.update_layout(
        title=dict(text='ABS Swap-Adjusted Yield Distribution', font_color='white'),
        xaxis_title=dict(text='Yield (%)', font_color='white'),
        yaxis_title=dict(text='Probability', font_color='white'),
        plot_bgcolor='rgb(40, 40, 40)',
        paper_bgcolor='rgb(40, 40, 40)',
        font_color='white',
        xaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
        yaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', gridwidth=0.5),
        showlegend=True,
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    fig.show()

# Example usage
if __name__ == "__main__":
    # Sample inputs
    abs_coupon = 5.0  # 5% ABS coupon rate
    swap_fixed = 3.0  # 3% fixed swap rate
    swap_float_mean = 2.5  # Mean floating rate
    swap_float_std = 0.5  # Volatility of floating rate
    cash_flows = [1000] * PERIODS  # Simplified monthly cash flows
    
    # Run simulation
    yields, med_yield, ci_low, ci_high = simulate_yields(
        abs_coupon, swap_fixed, swap_float_mean, swap_float_std, cash_flows
    )
    
    # Print results
    print(f"Median Yield: {med_yield:.2f}%")
    print(f"95% CI: [{ci_low:.2f}%, {ci_high:.2f}%]")
    
    # Plot distribution
    plot_yield_distribution(yields, med_yield, ci_low, ci_high)