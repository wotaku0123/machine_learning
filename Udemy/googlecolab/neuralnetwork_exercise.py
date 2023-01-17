import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
iris_data = iris.data
sl_data = iris_data[:100, 0].copy()#SetosaとCersicolor, Sepal length: copy()で元データが変更されない
sw_data = iris_data[:100, 1].copy()#SetosaとVersicolor, Sepal width

#平均値を０に
sl_ave = np.average(sl_data) #average
sl_data -= sl_ave # deduce the verage from the data
sw_ave = np.average(sw_data)
sw_data -= sw_ave

#入力をリストに格納
input_data = []
for i in range(100):
    input_data.append([sl_data[i], sw_data[i]])


#シグモイド関数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

#Neuron
class Neuron:
    def __init__(self): #First preference
        self.input_sum = 0.0
        self.output = 0.0

    def set_input(self, inp):
        self.input_sum += inp
    
    def get_output(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0

#Neural Network
class NeuralNetwork:
    def __init__(self): #first preference
        #weight
        self.w_im = [[4.0, 4.0], [4.0, 4.0], [4.0, 4.0]] #input:2 the number of neuron: 3
        self.w_mo = [[1.0, -1.0, 1.0]] # input:2 the number of neuron: 3

        #bias
        self.b_m = [3.0, 0.0, -3.0] #the number of neuron: 2
        self.b_o = [-0.5] #the number of neuron: 1

        #decrearation of each layers
        self.input_layer = [0.0, 0.0]
        self.middle_layer = [Neuron(), Neuron(), Neuron()]
        self.output_layer = [Neuron()]

    def commit(self, input_data): 
        #reset the each layers
        self.input_layer[0] = input_data[0]
        self.input_layer[1] = input_data[1]
        self.middle_layer[0].reset()
        self.middle_layer[1].reset()
        self.middle_layer[2].reset()
        self.middle_layer[0].reset()

    # input layer -> middle layer
        self.middle_layer[0].set_input(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].set_input(self.input_layer[1] * self.w_im[0][1])
        self.middle_layer[0].set_input(self.b_m[0])

        self.middle_layer[1].set_input(self.input_layer[0] * self.w_im[1][0])
        self.middle_layer[1].set_input(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].set_input(self.b_m[1])

        self.middle_layer[2].set_input(self.input_layer[0] * self.w_im[2][0])
        self.middle_layer[2].set_input(self.input_layer[1] * self.w_im[2][1])
        self.middle_layer[2].set_input(self.b_m[2])

    #middle layer -> output layer
        self.output_layer[0].set_input(self.middle_layer[0].get_output()*self.w_mo[0][0])
        self.output_layer[0].set_input(self.middle_layer[1].get_output()*self.w_mo[0][1])
        self.output_layer[0].set_input(self.middle_layer[2].get_output()*self.w_mo[0][2])
        self.output_layer[0].set_input(self.b_o[0])

        return self.output_layer[0].get_output()


#ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

#commit
st_predicted = [[], []] #Setosa
vc_predicted = [[], []] #versicolor
for data in input_data:
    if neural_network.commit(data) < 0.5:
        st_predicted[0].append(data[0]+sl_ave)
        st_predicted[1].append(data[1]+sw_ave)
    else:
        vc_predicted[0].append(data[0]+sl_ave)
        vc_predicted[1].append(data[1]+sw_ave)

# display the result on the graph
plt.scatter(st_predicted[0], st_predicted[1], label="Setosa")
plt.scatter(vc_predicted[0],vc_predicted[1], label="Versicolor")
plt.legend()

plt.xlabel("Sepal length(cm)")
plt.ylabel("Sepal width(cm)")
plt.title("Predicted")
plt.show()