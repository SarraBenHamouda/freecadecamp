import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # First line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Extend line to 2050
    years_all = pd.Series(range(int(df['Year'].min()), 2051))
    line_all = intercept + slope * years_all
    ax.plot(years_all, line_all, color='red', label='Fit: All Data')

    # Second line of best fit (from year 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    line_recent = intercept_recent + slope_recent * years_recent
    ax.plot(years_recent, line_recent, color='green', label='Fit: 2000+')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Save figure
    fig.savefig('sea_level_plot.png')
    return fig
