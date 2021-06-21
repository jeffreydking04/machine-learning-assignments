import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa_sea_level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig, ax = plt.subplots(1, 1, figsize=(25, 10))
    ax.scatter(x, y)

    # Create first line of best fit
    slope, intercept, n, m, o = linregress(x, y)
    line_x = np.arange(1880, 2051)
    line_y = slope * line_x + intercept
    ax.plot(line_x, line_y)

    # Create second line of best fit
    df_2 = df[df['Year'] >= 2000]
    x_2 = df_2['Year']
    y_2 = df_2['CSIRO Adjusted Sea Level']

    slope_2, intercept_2, m_2, n_2, o_2 = linregress(x_2, y_2)
    line_x_2 = np.arange(2000, 2051)
    line_y_2 = slope_2 * line_x_2 + intercept_2
    ax.plot(line_x_2, line_y_2)

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlim(xmin=1850, xmax=2075)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
