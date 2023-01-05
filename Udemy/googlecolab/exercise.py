import numpy as np
import matplotlib.pyplot as plt

e = np.e

def approach_napier(x):
    y = (1 + 1/x)**x
    return y

x = np.linspace(0, 10000)

# y_e = e
y_app_napier = approach_napier(x)

# plt.plot(x, y_e, label = "napier")
plt.plot(x, y_app_napier, label = "approach_napier")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()