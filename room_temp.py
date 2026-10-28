import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 40, 100)

def triangle(x, a, b, c):
    return np.maximum(np.minimum((x-a)/(b-a), (c-x)/(c-b)), 0)

def trapezoid(x, a, b, c, d):
    return np.maximum(np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)), 0)

def gaussian(x, c, s):
    return np.exp(-((x-c)**2)/(2*s**2))

cold = triangle(x, 0, 10, 20)
comfortable = trapezoid(x, 15, 20, 25, 30)
hot = gaussian(x, 30, 5)

plt.plot(x, cold, label="Cold")
plt.plot(x, comfortable, label="Comfortable")
plt.plot(x, hot, label="Hot")

plt.xlabel("Temperature (°C)")
plt.ylabel("Membership Degree")
plt.title("Room Temperature Membership Functions")
plt.legend()
plt.grid()
plt.show()