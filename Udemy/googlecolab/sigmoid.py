import numpy as np 
import matplotlib.pyplot as plt

e = np.e

def sigmoid(x):
  s = 1 / (1 + e**-x)
  return s

dx = 0.1
x = np.linspace(-8, 8)
y_sig = sigmoid(x)
y_d = (sigmoid(x+dx) - sigmoid(x)) / dx

plt.plot(x, y_sig, label = "sigmoid")
plt.plot(x, y_d, label = "d_sigmoid")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()


# シグモイド関数の微分
import numpy as np 
import matplotlib.pyplot as plt

dx = 0.1
e = np.e

def sigmoid(x):
  s = 1 / (1 + e**-x)
  return s

def df_sigmoid(x):
  d = sigmoid(x)*(1 - sigmoid(x))
  return d

y_sig = sigmoid(x)
y_d = (sigmoid(x + dx) - sigmoid(x)) / dx
y_df = df_sigmoid(x)

plt.plot(x, y_sig, label = "sigmoid")
plt.plot(x, y_d, label = "d")
plt.plot(x, y_df, label="df")
plt.legend()

plt.xlabel("x", size=14)
plt.ylabel("y", size=14)
plt.grid()
plt.show()