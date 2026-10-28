import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)

def triangle(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)

def trapezoid(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)), 0)

def gaussian(x, c, s):
    return np.exp(-((x-c)**2)/(2*s**2))

low = triangle(x, 0, 20, 40)
medium = trapezoid(x, 20, 35, 50, 70)
high = gaussian(x, 80, 12)

plt.plot(x, low, label="Low Traffic")
plt.plot(x, medium, label="Medium Traffic")
plt.plot(x, high, label="High Traffic")

plt.xlabel("Traffic Density (%)")
plt.ylabel("Membership Degree")
plt.title("Traffic Density Membership Functions")
plt.legend()
plt.grid()
plt.show()