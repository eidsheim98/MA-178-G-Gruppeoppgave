import numpy as np
from scipy.misc import derivative
from scipy.optimize import newton

# Bruk av newton-raphtons metode i python

def f(x):
    """
    Gir svar på funksjon ut ifra x
    :param x: Verdien til variabel x i stykket
    :return: Svaret på funksjonen
    """
    return 3*x**2+4*x-4

def f_derivert(x):
    """
    Gir svar på funksjon derivert ut ifra x
    :param x: Verdien til variabel x i stykket
    :return: Svaret på funksjon derivert
    """
    return derivative(f(x), x)


newton_raphson = 1.4 - (f(1.4))/(f_derivert(1.4))

print("newton_raphson =", newton_raphson)
print("sqrt(2) =", np.sqrt(2))
