import numpy as np
import matplotlib.pyplot as plt

f = lambda x: 3*x**2+4*x-4
df = lambda x: 6 * x + 4

def plot():
    # Setter x-koordinater
    # Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
    x = np.arange(-5, 5, 0.2/20)
    # Setter y-koordinater
    y = [newton_raphson(f, df, num, 1e-12) for num in x]

    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()
    plt.scatter(x,y,0.5,c='red')
    plt.show()
    return x, y

def newton_raphson(f, df, x0, tol):
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
        return newton_raphson(f, df, x0 - f(x0) / df(x0), tol)

if __name__ == '__main__':
    startnumbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    for startnumber in startnumbers:
        estimate = newton_raphson(f, df, startnumber, 1e-12)
        print("Estimat med tall {}: {}".format(startnumber, estimate))
    plot()