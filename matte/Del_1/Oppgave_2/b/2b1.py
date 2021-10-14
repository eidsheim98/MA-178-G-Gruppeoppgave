# importing the required modules
import matplotlib.pyplot as plt
# importing the library
from scipy.misc import derivative
import numpy as np

# setting the x - coordinates
y = np.linspace(-6, 6)
# setting the corresponding y - coordinates
def function(x):
    return 7*x**2-8*x+1

# calculating its derivative
def deriv(x):
    return derivative(function, x)

plt.title(r'$f(x) = 7x^2-8x+1$')

plt.xlabel("x")
plt.ylabel("y")

# plotting the function
#plt.plot(y, function(y), color='purple', label='Function')

# plotting its derivative
plt.plot(y, deriv(y), color='green', label='Derivative')

plt.grid()

# function to show the plot
plt.show()