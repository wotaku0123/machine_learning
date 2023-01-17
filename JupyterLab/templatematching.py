import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5)
y = 2*x + 1


plt.plot()
plt.show()


import matplotlib.pyplot as plt

x = np.linspace(-3,3)
y_1 = 1.5 * x
y_2 = -2*x + 1

#x軸のラベル
plt.xlabel("x value", size = 14)

#y軸のラベル
plt.xlabel("y value", size = 14)

plt.title("My graph")

plt.grid()

plt.plot(x, y_1, label = "y_1")
plt.plot(x, y_2, label = "y_2", linestyle="dashed")
plt.legend()

plt.show()