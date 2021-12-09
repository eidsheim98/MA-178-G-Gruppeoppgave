# importing the required modules
from scipy.misc import derivative
import matplotlib.pyplot as plt
import numpy as np
from numpy import sqrt

machine_derivation = False

f_ = input("Sett inn funksjon f(x): ")
f = lambda x: eval(f_)

f_d_ = input("Input den deriverte, eller trykk enter for maskinderivasjon: ")
f_d = lambda x: eval(f_d_)

# Set user derivative if wanted
if f_d_ == '':
    print("Maskinderivasjon utføres med scipiy")
    machine_derivation = True

x0 = eval(input("X startkoordinat: "))
xS = eval(input("X stoppkoordinat: "))
points = eval(input("Antall punkter: "))
deltaX = eval(input("delta x: "))

# Setter x-koordinater
# Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(x0, xS, 0.4 / 100)
v = points / x.size
x = np.arange(x0, xS, 0.4 / 100 * v)

print("\nKalkulerer")
print("Plotter graf f(x): {}".format(f_))
if not machine_derivation:
    print("Plotter graf f'(x): {}".format(f_d_))
else:
    print("Plotter graf f'(x) med maskinderivasjon")
print("Mellom x={} og x={} med {} evalueringspunkter".format(x0, xS, points))
print("Delta x satt til: {}".format(deltaX))
input("Trykk enter for å fortsette")

# Setter x-verdier
x = np.arange(x0, xS, 0.4 / 100)

def deriv():
    """Kalkuler den deriverte"""
    if machine_derivation:                  #Hvis man velger at python skal derivere
        return derivative(f, x)
    else:
        return f_d(x)                       #Hvis man har valgt å legge inn den deriverte selv

def f_x():
    """ Funskjonen f(x)"""
    # Setter y-koordinater
    y = f(x)
    return y

def f_derivert():
    """Funksjonen f'(x)"""
    # Setter y-koordinater
    y = deriv()
    return y

def estimate():
    """Regner ut tilnærmingen med Newton-Raphsons metode"""
    # Setter y-koordinater
    y = (f(x+deltaX)-f(x))/deltaX
    return y

def error():
    """Regner ut feilen"""
    # Setter y-koordinater
    y = abs(f_derivert() - estimate())
    return y

fig, ax = plt.subplots()

# Setter tittelen på x og y akse
ax2 = plt.twinx()
ax.set_xlabel("x-akse")
ax.set_ylabel("y-akse")
ax2.set_ylabel("y-akse for feilen")
ax2.margins(x=0, y=0.5)

# Plotter punkter
# c = red er farge
ax2.plot(x, error(), c="red", label=r'$f(x)$ feilen')
ax2.spines['right'].set_color('red')
ax.spines['right'].set_color('red')
ax.plot(x, f_x(), c="black", label=r'$f(x)$')
ax.plot(x, f_derivert(), c="magenta", label=r'$f(x)$ derivert')
ax.plot(x, estimate(), ":", linewidth=4, c="green", label=r'derivert estimat')

fig.legend(loc='upper left')

# Vis plot
plt.show()
