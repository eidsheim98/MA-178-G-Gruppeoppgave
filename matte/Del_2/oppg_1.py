import sympy as sym
from fractions import Fraction
import time

"""
Linja l(x) = ax+b

Vist algoritme x_1 = x_0 - f(x) / f'(x)
"""

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

    x = sym.Symbol('x')
    f_der = sym.diff(3*x**2+4*x-4)
    answer = f_der.subs(x,3)
    return answer

def num_of_zeros(n):
  s = '{:.16f}'.format(n).split('.')[1]
  return len(s) - len(s.lstrip('0'))

x0 = 1 #Setting startnumber
it_number = 0
last_newton_answer = 1

if __name__ == '__main__':
    while True:
        print("\nIteration {}".format(it_number))

        y = f(x0)
        y_der = f_derivert(x0)

        x1 = x0-(y/y_der)
        decimal = float(Fraction(x1))

        #print("f(x): {}".format(y))
        #print("f'(x): {}".format(y_der))
        print("Newton gir x: {:.10f}".format(decimal))

        x0 = x1
        it_number +=1
        error_treshold = 1e-12
        difference = (last_newton_answer / decimal) - 1

        if error_treshold > difference:
            print("Found point")
            quit()

        last_newton_answer = decimal

        print("Error threshold {}".format(error_treshold))
        print("The error difference: 1e-{}".format(num_of_zeros(difference)))

        #input("Press enter to run next iteration")
        time.sleep(1)
