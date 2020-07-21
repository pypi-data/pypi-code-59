# @Time : 2020/7/21 10:53 
# @Author : XX
# @File : j.py
# @Software: PyCharm


import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from keras.layers import Conv2D,MaxPool2D,Dense,Flatten
from keras.utils import np_utils
from keras.models import Sequential
from sklearn.model_selection import train_test_split
model = Sequential()
# 1. 两个卷积层，一个池化层
#     卷积层：64个卷积核
model.add(Conv2D(filters=64,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=64,kernel_size=(3,3),padding='same'))
model.add(MaxPool2D(pool_size=(2,2)))
# 2. 两个卷积一个池化
#     卷积层：128个卷积核
model.add(Conv2D(filters=128,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=128,kernel_size=(3,3),padding='same'))
model.add(MaxPool2D(pool_size=(2,2)))
# 3. 三个卷积一个池化
#     卷积：256个卷积核
model.add(Conv2D(filters=256,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=256,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=256,kernel_size=(3,3),padding='same'))
model.add(MaxPool2D(pool_size=(2,2)))
# 4. 三个卷积一个池化
#     卷积：512个卷积核
model.add(Conv2D(filters=512,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=512,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=512,kernel_size=(3,3),padding='same'))
model.add(MaxPool2D(pool_size=(2,2)))
# 5. 三个卷积一个池化
#     卷积：512个卷积核
model.add(Conv2D(filters=512,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=512,kernel_size=(3,3),padding='same'))
model.add(Conv2D(filters=512,kernel_size=(3,3),padding='same'))
model.add(MaxPool2D(pool_size=(2,2)))
# 6. 全连接层：
#     1. 神经元：4096个，Relu
model.add(Flatten())
model.add(Dense(units=4096,activation='relu'))
#     2. 神经元：4096个，Relu
model.add(Dense(units=4096,activation='relu'))
#     3. 神经元：1000个，SoftMax
model.add(Dense(units=5,activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
# model.fit(datas,Y,epochs=200)
#
# Result = model.predict(X)
# Return HTTPResponse('result.html',{'result':result})