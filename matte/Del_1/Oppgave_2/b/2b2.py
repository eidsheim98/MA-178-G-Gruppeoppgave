# importing the required modules
import matplotlib.pyplot as plt
# importing the library
from scipy.misc import derivative
import numpy as np

def function(x):
    return np.sin(x)

# Kalkuler den deriverte
def deriv(x):
    return derivative(function, x)

# Setter x-koordinater
# Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(0, 2*np.pi, 0.2/100)

# Setter y-koordinater
y = deriv(x)

# Setter tittelen på vinduet
plt.title(r'$f^\prime(x) = cos(x)$')

# Setter tittelen på x og y akse
plt.xlabel("x")
plt.ylabel("y")

plt.grid()

# plotting its derivative
plt.scatter(x, y, 0.7, c="red")

# function to show the plot
plt.show()