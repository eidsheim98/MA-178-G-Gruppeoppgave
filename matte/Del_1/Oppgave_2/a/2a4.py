# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# Setter x-koordinater
# Tallet 0.2/100 gjør at det blir 1000 punkter, som kravet i oppgaven
x = np.arange(0, 10, 0.00628)
# Setter y-koordinater
y = np.sqrt(1+x**2)

# Setter tittelen på vinduet
plt.title(r'$f(x) = \sqrt{1+x^2}$')

# Setter tittelen på x og y akse
plt.xlabel("x")
plt.ylabel("y")

# Plotter punkter
# 0.1 er størrelse
# c = red er farge
plt.scatter(x, y, 0.5, c="red")

# Vis plot
plt.show()