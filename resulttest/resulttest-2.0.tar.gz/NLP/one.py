# @Time : 2020/7/21 10:49 
# @Author : XX
# @File : v.py
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
model.fit(datas,Y,epochs=200)




































# """1.Query 纠错"""
# """1.Query 纠错，顾名思义，也即对用户输入 query 出现的错误进行检测和纠正的过程。用户在使用搜索过程中，
# 可能由于先验知识掌握不够或输入过程引入噪音 ( 如：语音识别有误、快速输入手误等 ) 输入的搜索 query 会存在一定的错误。
# 如果不对带有错误的 query 进行纠错，除了会影响 QU 其他模块的准确率，还会影响召回的相关性及排序的合理性，
# 最终影响到用户的搜索体验。
# 除了搜索场景，query 纠错还可以应用于输入法、人机对话、语音识别、内容审核等应用场景。不同的业务场景需要解决的错误类型会不太一样，
# 比如 ASR 语音识别主要解决同谐音、模糊音等错误，而输入法及搜索等场景则需要面临解决几乎所有错误类型，如同谐音、模糊音 ( 平舌翘舌、前后鼻音等 )、
# 混淆音、形近字 ( 主要针对五笔和笔画手写输入法 )、多漏字等错误。根据 query 中是否有不在词典中本身就有错误的词语 ( Non-word )，可以将 query 错
# 误类型主要分为 Non-word 和 Real-word 两类错误。
# 其中，Non-word 错误一般出现在带英文单词或数字的 query 中，由于通过输入法进行输入，不会存在错误中文字的情况，所以中文 query 如果以字作为最小语
# 义单元的话一般只会存在 Real-word 错误，而带英文数字的 query 则可能存在两类错误。"""
#
#
# """请简述意图识别的难点(三个即可)"""
# """2.用户输入 query 不规范：由于用户先验知识的差异，必然导致用户在通过自然语言组织表达同一需求时千差万别，
# 甚至可能会出现 query 表达错误、遗漏等情况；
#
# 歧义性&多样性：用户的搜索 query 表达不够明确带来的意图歧义性或用户本身搜索意图存在多样性，
# 比如：搜索 query "择天记"可能是想下载仙侠玄幻类游戏，可能是玄幻小说类 app，也可能是想看择天记电视剧而下视频类 app。
# 此时衍生出来的另一个问题是当某个 query 存在多个意图可能时，需要合理地量化各个意图的需求强度；
#
# 如何根据用户及其所处 context 的不同实现个性化意图，比如用户的性别、年龄不同，搜索同一 query 的意图可能不一样，
# 用户当前时刻搜索 query 的意图可能和上一时刻搜索 query 相关等。"""
#
#
# """1.为什么LSTM模型中既存在sigmoid又存在tanh两种激活函数，而不是选择统一一种sigmoid或者tanh？这样做的目的是什么？"""
# """sigmoid 用在了各种gate上，产生0~1之间的值，这个一般只有sigmoid最直接了。
# tanh 用在了状态和输出上，是对数据的处理，这个用其他激活函数或许也可以。"""
#
#
#
# """什麽样的资料集不适合用深度学习？"""
# """（1）数据集太小，数据样本不足时，深度学习相对其它机器学习算法，没有明显优势。
# （2）数据集没有局部相关特性，目前深度学习表现比较好的领域主要是图像／语音／自然语言处理等领域，
# 这些领域的一个共性是局部相关性。图像中像素组成物体，语音信号中音位组合成单词，文本数据中单词组合成句子，
# 这些特征元素的组合一旦被打乱，表示的含义同时也被改变。对于没有这样的局部相关性的数据集，不适于使用深度学习算法进行处理。
# 举个例子：预测一个人的健康状况，相关的参数会有年龄、职业、收入、家庭状况等各种元素，将这些元素打乱，并不会影响相关的结果。"""
#
#
# """1.GRU是什么？GRU对LSTM做了哪些改动？"""
# """GRU是Gated Recurrent Units，是循环神经网络的一种。
# GRU只有两个门（update和reset），LSTM有三个门（forget，input，output），GRU直接将hidden state 传给下一个单元，而LSTM用memory cell 把hidden state 包装起来。"""
#
#
# """缓解过拟合：
# ① Dropout
# ② 加L1/L2正则化
# ③ BatchNormalization
# ④ 网络bagging"""