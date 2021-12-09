# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# Setter x-koordinater
# Tallet 0.004 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(-2, 2, 0.004)
# setting the corresponding y - coordinates
y = (1-x)/(x+3)**2

# Setter tittelen på vinduet
plt.title(r'$f(x) = \frac{(1-x)}{(x+3)^2}$')

# Setter tittelen på x og y akse
plt.xlabel("x")
plt.ylabel("y")

# Plotter punkter
# 0.1 er størrelse
# c = red er farge
plt.scatter(x, y, 0.5, c="red")

# Vis plot
plt.show()