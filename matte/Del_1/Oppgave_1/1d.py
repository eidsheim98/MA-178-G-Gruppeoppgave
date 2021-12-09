import numpy as np
from scipy.misc import derivative

e = 1e-3

start_deltax = 1
start_E = 1

f_ = input("Sett inn funksjon f(x): ")
f = lambda x: eval(f_)

df_ = input("Input den deriverte: ")
df = lambda x: eval(df_)

x0 = input("Sett inn x0")
x0 = lambda x: eval(x0)


def find_deltaX(deltaX, E):
    """
    Itererer gjennom Newton-Raphsons metode og finner en deltaX som gjør at E blir mindre enn 0.001
    :param deltaX: Verdien deltaX som blir testet
    :param E: Feilen som oppstår
    :return: None
    """
    # Hvis feilen er større enn 0.001
    if E >= 0.001:
        # Regner ut funskjonen g(x)
        g = (f(x0 + deltaX)-f(x0))/deltaX
        # Regner ut feilen
        E = abs(df(x0)-g)
        print(E)
        # Kjører programmet en gang til rekursivt med nye verdier
        find_deltaX(deltaX/1.1, E)
    else:
        # Setter deltaX til to signifikante desimaler
        deltaX = np.format_float_positional(deltaX, precision=2, unique=False, fractional=False, trim='k')
        # Setter feilen til to signifikante desimaler
        E = np.format_float_positional(E, precision=2, unique=False, fractional=False, trim='k')
        # Printer funnet
        print("\ndeltaX", deltaX, "gir feilmargin på", E)

find_deltaX(start_deltax, start_E)

