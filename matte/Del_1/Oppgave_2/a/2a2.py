# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x = np.arange(0, 2 * (np.pi), 0.01)
# setting the corresponding y - coordinates
y = np.sin(x)

plt.title(r'$f(x) = sin(x)$')

plt.xlabel("x")
plt.ylabel("y")

# poltting the points
plt.plot(x, y)
plt.grid()

# function to show the plot
plt.show()