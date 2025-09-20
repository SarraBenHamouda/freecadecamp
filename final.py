import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

 
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')


    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
 
    years_all = pd.Series(range(int(df['Year'].min()), 2051))
    line_all = intercept + slope * years_all
    ax.plot(years_all, line_all, color='red', label='Fit: All Data')

    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    line_recent = intercept_recent + slope_recent * years_recent
    ax.plot(years_recent, line_recent, color='green', label='Fit: 2000+')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return fig
