# importing the required modules
from scipy.misc import derivative
import matplotlib.pyplot as plt
import numpy as np

# Setter x-koordinater
# Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(0, 2, 0.2 / 100)
# Sett deltaX
deltaX = 0.5

# Den faktiske funksjonen
def function(x):
    return 7*x**2-8*x+1

# Kalkuler den deriverte
def deriv(x):
    return derivative(function, x)

def f_x():
    # Setter y-koordinater
    y = function(x)
    return y

def f_derivert():
    # Setter y-koordinater
    y = deriv(x)
    return y

def estimate():
    # Setter y-koordinater
    y = (function(x+deltaX)-function(x))/deltaX
    return y

def error():
    # Setter y-koordinater
    y = abs(f_derivert() - estimate())
    return y

# Setter tittelen på x og y akse
plt.xlabel("x")
plt.ylabel("y")

# Plotter punkter
# c = red er farge
#plt.plot(x, f_x(), c="blue", label=r'$f(x)$')
#plt.plot(x, f_derivert(), c="red", label=r'$f(x)$ derivert')
#plt.plot(x, estimate(), c="green", label=r'$f(x)$ estimat')
plt.plot(x, error(), c="black", label=r'$f(x)$ feilen')
plt.legend(loc='upper left')

# Vis plot
plt.show()
