import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Load your CSVs
df1 = pd.read_csv('SPY ETF Stock Price History.csv')
df2 = pd.read_csv('formatted_SPY_Dividend.csv')

fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Stock Price')
line2, = ax.plot([], [], label='Dividend')
ax.legend()

#Homogenizing date formats
df1['Date'] = pd.to_datetime(df1['Date'])
df2['Date'] = pd.to_datetime(df2['Date'])

df = pd.merge(df1[['Date', 'Price']], df2[['Date', 'Amount']], on='Date', how='outer')
df.sort_values('Date', inplace=True)

df['Price'] = df['Price'].ffill()
df['Amount'] = df['Amount'].fillna(0)


xdata = df['Date']
ydata1 = df['Price']
ydata2 = df['Amount']

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    step = 5  # or whatever speed you prefer
    idx = frame * step

    if idx < 1:
        return line1, line2

    # Slice data up to current frame
    x = xdata[:idx]
    y1 = ydata1[:idx]
    y2 = ydata2[:idx]

    # Update line data
    line1.set_data(x, y1)
    line2.set_data(x, y2)

    # Dynamically update x and y limits
    ax.set_xlim(x.min(), x.max())
    y_min = y2.min()
    y_max = y2.max()
    ax.set_ylim(y_min * 0.95, y_max * 1.05)  # add a little padding

    return line1, line2

step = 5
ani = animation.FuncAnimation(fig, update, frames=int(len(xdata)/step), init_func=init, blit=True)
ani.save("line_chart.mp4", fps=200, dpi=200)