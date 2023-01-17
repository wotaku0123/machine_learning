import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Irisデータの読み込み
iris = datasets.load_iris()

#各花のサイズ
iris_data = iris.data
# print(iris_data)
# print(iris_data.shape)

# 散布図で表示
st_data = iris_data[:50] #Setosa
vc_data = iris_data[50:100] #Versicolor
plt.scatter(st_data[:,0], st_data[:, 1], label="Setosa") #Sepel length and Sepal width
plt.scatter(vc_data[:,0], vc_data[:, 1], label="Versicolor") #Sepel length and Sepal width
plt.legend()

plt.xlabel("Sepal length(cm)")
plt.ylabel("Sepal width(cm)")
plt.show()