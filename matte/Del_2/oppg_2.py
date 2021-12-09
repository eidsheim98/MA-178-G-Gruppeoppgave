import numpy as np
import matplotlib.pyplot as plt
import sys

theta1 = 0

f = lambda x: (10-(2*np.cos(theta1)+8.5*np.cos(x)))**2+(6-(2*np.sin(theta1) + 8.5*np.sin(x)))**2 -49
f_prime = lambda x: 2*((10-2 * np.cos(theta1)-8.5 * np.cos(x))*(8.5 * np.sin(x)) + (6-2 * np.sin(theta1)-8.5 * np.sin(x))*(-8.5 * np.cos(x)))

def function(x):
    return (10 - (2 * np.cos(theta1) + 8.5 * np.cos(x))) ** 2 + (6 - (2 * np.sin(theta1) + 8.5 * np.sin(x))) ** 2 - 49

# Plot med delta x på ene aksen og feilen på y-aksen

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

def plot(x_values):
    y_values = [0 for i in range(len(x_values))]
    print(x_values)
    print(y_values)

    plt.title("Test")
    plt.plot(x_values, y_values)
    plt.show()

def plot_(alt_x = None):
    """
    Regner ut funksjonene f(x) og theta_2(x)
    :param alt_x: En liste med nye x-verdier hvis noen må fjernes fordi grafen ikke konvergerer
    :return: None
    """
    try:
        # Hvis dette er første gang funksjonen kalles, sett x-verdier i ei liste
        if alt_x == None:
            x = np.arange(0, np.pi*2, 0.2)
    except:
        # if-statement feiler hvis altx != null, derfor settes x til nye verdier på denne måten istedenfor ved \\
        # bruk av else-statement
        x = alt_x
    y = []
    for i in range(len(x)):
        try:
            # Setter y-koordinater i egen liste for hver x-koordinat i lista
            num = x[i]
            estimate = my_newton(f, f_prime, num, 1e-12)
            y.append(estimate)

        except RecursionError:
            # Hvis rekursjon maks treffes, prøv igjen med færre x-verdier
            print("Recursion error on x=", num)
            x = np.delete(x, i)
            plot_(x)

        except IndexError:
            # Hvis x-verdi ikke finnes, registrer feil
            print("Index error on x=", num)



    sine_x = x
    sine_y = f(x)

    fig, ax = plt.subplots()
    ax2 = plt.twinx()
    ax2.set_ylabel("y")

    plt.title(r'$\theta_1 = {}$'.format(theta1))
    ax.set_xlabel("x")
    ax.set_ylabel(r"$\theta_2$")

    ax2.margins(x=0, y=0.01)

    ax2.spines['right'].set_color('orange')
    ax.spines['right'].set_color('orange')
    ax2.spines['left'].set_color('blue')
    ax.spines['left'].set_color('blue')


    ax.plot(x,y, c="blue", label=r"$f(\theta_2)$")
    ax2.plot(sine_x, sine_y, c="orange", label=r"$f(x)$")

    fig.legend(loc='upper left')

    plt.show()


if __name__ == '__main__':
    startnumbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    x_values = []
    for startnumber in startnumbers:
        estimate = my_newton(f, f_prime, startnumber, 1e-12)

        print("Estimat med tall {}: {}".format(startnumber, estimate))
        x_values.append(estimate)

    plot_()
    #print(sys.getrecursionlimit())

