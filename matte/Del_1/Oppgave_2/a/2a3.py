# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x = np.arange(-2, 2, 0.01)
# setting the corresponding y - coordinates
y = (1-x)/(x+3)**2

plt.title(r'$f(x) = (1-x)/(x+3)^2$')

plt.xlabel("x")
plt.ylabel("y")

# poltting the points
plt.plot(x, y)
plt.grid()

# function to show the plot
plt.show()