import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("./epa-sea-level.csv")

    # Create scatter plot
    x_full = df['Year'].to_numpy()
    y_full = df['CSIRO Adjusted Sea Level'].to_numpy()

    plt.scatter(x_full, y_full)

    # Create first line of best fit
    fit1 = linregress(x=x_full,y=y_full)

    year_range = np.arange(x_full.min(), 2051)

    plt.plot(
        year_range,
        fit1.intercept + fit1.slope * year_range,
        color='r'
    )

    # Create second line of best fit
    df_trimmed = df[df['Year'] >= 2000]

    x_trimmed = df_trimmed['Year'].to_numpy()
    y_trimmed = df_trimmed['CSIRO Adjusted Sea Level'].to_numpy()

    fit2 = linregress(x=x_trimmed,y=y_trimmed)

    year_range = np.arange(2000, 2051)

    plt.plot(
        year_range,
        fit2.intercept + fit2.slope * year_range,
        color='g'
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.xlim((1850, 2051))
    plt.xticks(np.arange(1850, 2076, 25))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()