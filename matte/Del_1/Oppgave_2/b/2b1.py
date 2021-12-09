# importing the required modules
import matplotlib.pyplot as plt
# importing the library
from scipy.misc import derivative
import numpy as np

def function(x):
    return 7*x**2-8*x+1

# Kalkuler den deriverte
def deriv(x):
    return derivative(function, x)

# Setter x-koordinater
# Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(0, 2, 0.2/100)
print(x.size)
# Setter y-koordinater
y = deriv(x)

# Setter tittelen på vinduet
plt.title(r'$f^\prime(x) = 14x-8$')

# Setter tittelen på x og y akse
plt.xlabel("x")
plt.ylabel("y")

plt.grid()

# plotting its derivative
plt.scatter(x, y, 0.7, c="red")

# function to show the plot
plt.show()