# 単一ニューロンの実装
import numpy as np

#　シグモイド関数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

# ニューロンクラス
class Neuron:
    def __init__(self): #初期設定
        self.input_sum = 0.0
        self.output = 0.0

    def set_input(self, inp):
        self.input_sum += inp
        
    def get_output(self):
        self.output = sigmoid(self.input_sum)
        return self.output

#ニューラルネットワーク
class NeuralNetwork:
    def __init__(self): #初期設定
        self.neuron = Neuron() #ニューロンのインスタンス
        self.w = [1.5, 0.75, -1] #重み

    def commit(self, input_data): #実行
        self.neuron.set_input(input_data[0] * self.w[0])
        self.neuron.set_input(input_data[1] * self.w[1])
        self.neuron.set_input(input_data[2] * self.w[2])
        return self.neuron.get_output()

neural_network = NeuralNetwork()

#実行
input_data = [1.0, 2.0, 3.0]
print(neural_network.commit(input_data))