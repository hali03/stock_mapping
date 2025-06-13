import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Load your CSVs
df1 = pd.read_csv('SPY ETF Stock Price History.csv')
df2 = pd.read_csv('formatted_SPY_Dividend.csv')

fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Data 1')
line2, = ax.plot([], [], label='Data 2')
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
    ax.set_xlim(xdata.min(), xdata.max())
    ax.set_ylim(min(ydata1.min(), ydata2.min()), 620)
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

def update(frame):
    line1.set_data(xdata[:frame], ydata1[:frame])
    line2.set_data(xdata[:frame], ydata2[:frame])
    return line1, line2

ani = animation.FuncAnimation(fig, update, frames=len(xdata), init_func=init, blit=True)
ani.save("line_chart.mp4", fps=200, dpi=200)