import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)

# Triangular membership function
def triangle(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)

# Trapezoidal membership function
def trapezoid(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)), 0)

# Gaussian membership function
def gaussian(x, c, s):
    return np.exp(-((x-c)**2)/(2*s**2))

light = triangle(x, 0, 20, 40)
moderate = trapezoid(x, 20, 35, 50, 70)
heavy = gaussian(x, 80, 12)

plt.plot(x, light, label="Lightly Soiled")
plt.plot(x, moderate, label="Moderately Soiled")
plt.plot(x, heavy, label="Heavily Soiled")

plt.xlabel("Soil Level")
plt.ylabel("Membership Degree")
plt.title("Washing Machine Fuzzy Membership")
plt.legend()
plt.grid()
plt.show()