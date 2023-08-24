import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lbf = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_ax = pd.Series([i for i in range(1880, 2051)])
    y_ax = lbf.slope * x_ax + lbf.intercept
    plt.plot(x_ax, y_ax, "r")

    # Create second line of best fit
    new_df = df.loc[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    new_lbf = linregress(new_x, new_y)
    x_ax2 = pd.Series([i for i in range(2000, 2051)])
    y_ax2 = new_lbf.slope * x_ax2 + new_lbf.intercept  
    plt.plot(x_ax2, y_ax2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
