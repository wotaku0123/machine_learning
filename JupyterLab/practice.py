import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from google.colab.patches import cv2_imshow

#画像を表示するための関数を定義
def show_img(input,Output):
    plt.subplot(121) #画像の位置
    plt.imshow(input)#画像を表示
    plt.title('Input')#画像の上にInputと表示
    plt.xticks([])#X軸の目盛りを非表示
    plt.yticks([])#Y軸のメモリを非表示

    plt.subplot(122)#画像の位置を指定
    plt.imshow(Output)#画像を表示
    plt.title('Output')#画像の上にInputと表示
    plt.xticks([])#X軸の目盛りを非表示
    plt.yticks([])#Y軸のメモリを非表示

#画像をグレースケール化して読み込み
original = cv2.imread('image/dog_image.jpg',0)