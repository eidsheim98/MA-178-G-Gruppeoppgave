# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# Setter x-koordinater
# Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(0, 2, 0.2/100)
# Setter y-koordinater
y = 7*x**2-8*x+1

dots = 10

plt.title(r'$f(x) = 7x^2-8x+1$')

plt.xlabel("x")
plt.ylabel("y")

# plotting the points
plt.scatter(x, y)

# function to show the plot
plt.show()