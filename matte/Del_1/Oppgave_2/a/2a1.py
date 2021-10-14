# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x - coordinates
x = np.arange(0, 2, 0.01)
# setting the corresponding y - coordinates
y = 7*x**2-8*x+1

plt.title(r'$f(x) = 7x^2-8x+1$')

plt.xlabel("x")
plt.ylabel("y")

# poltting the points
plt.plot(x, y)
plt.grid()

# function to show the plot
plt.show()