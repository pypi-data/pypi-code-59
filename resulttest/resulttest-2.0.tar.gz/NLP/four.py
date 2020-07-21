# @Time : 2020/7/21 10:55 
# @Author : XX
# @File : x.py
# @Software: PyCharm
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from keras.models import Sequential


model = Sequential()
model.add(Conv2D())
model.add(MaxPool2D())
model.add(Conv2D())
model.add(Conv2D())
model.add(Conv2D())
model.add(Conv2D())
model.add(MaxPool2D())
model.add(Flatten())
model.add(Dense())
model.add(Dense())
model.add(Dense())