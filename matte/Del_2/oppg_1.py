import numpy as np

f = lambda x: 3*x**2+4*x-4
f_prime = lambda x: 6*x+4

def my_newton(f, df, x0, tol):
    """
    Regner ut et estimat ved bruk av Newton-Raphsons metode
    :param f: Funksjonen f
    :param df: Funksjonen f derivert
    :param x0: Startpunkt for x
    :param tol: Toleanse for når programmet skal skal si seg fornøyd
    :return:
    """
    if abs(f(x0)) < tol:
        return x0
    else:
        return my_newton(f, df, x0 - f(x0)/df(x0), tol)

if __name__ == '__main__':
    startnumbers = [-3, -2, -1, 0, 1, 2, 3]
    last_estimate = 0
    for startnumber in startnumbers:
        estimate = my_newton(f, f_prime, startnumber, 1e-12)
        if estimate != last_estimate:
            print("Estimat med tall {}: {}".format(startnumber, last_estimate))
            last_estimate = estimate