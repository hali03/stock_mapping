import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Generate exponential data
xdata = np.linspace(0, 5, 100)  # Smaller x-range to prevent huge y-values
ydata = np.exp(xdata)

# Setup the plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2, color='green')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    x = xdata[:frame]
    y = ydata[:frame]

    line.set_data(x, y)

    if len(x) > 0:
        xmin, xmax = x.min(), x.max()

        if xmin == xmax:
            xmax = xmax + .1

        ax.set_xlim(xmin, xmax)
        y_min, y_max = y.min(), y.max()
        # Add padding while handling exponential growth
        ax.set_ylim(y_min * 0.9, y_max * 1.1)

    return line,

ani = animation.FuncAnimation(
    fig, update, frames=len(xdata), init_func=init,
    blit=True, interval=50, repeat=False
)

ani.save("test_line.mp4", fps=60, dpi=200)

#plt.title("Exponential Growth")
#plt.xlabel("X")
#plt.ylabel("exp(X)")
#plt.grid(True)
#plt.show()