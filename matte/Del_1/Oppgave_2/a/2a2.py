# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# Setter x-koordinater
# Tallet 0.65*100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(0, 2 * (np.pi), 0.65/100)
# setting the corresponding y - coordinates
y = np.sin(x)

# Setter tittelen på vinduet
plt.title(r'$f(x) = sin(x)$')

# Setter tittelen på x og y akse
plt.xlabel("x")
plt.ylabel("y")

# Plotter punkter
# 0.1 er størrelse
# c = red er farge
plt.scatter(x, y, 0.1, c="red")

# Vis plot
plt.show()