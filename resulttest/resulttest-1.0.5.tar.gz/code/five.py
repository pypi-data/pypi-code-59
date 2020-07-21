# @Time : 2020/7/21 10:03 
# @Author : XX
# @File : five.py 
# @Software: PyCharm

from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler# 最小值最大值归一化
from sklearn.model_selection import train_test_split # 训练测试分割
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor

df = pd.read_csv(r'G:\Desktop\科委资格认证\新建文件夹\考试题\数据挖掘\数据集\creditcard.csv')
# 拆分为特征矩阵和目标向量
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
# 归一
s = MinMaxScaler()
s.fit(X)
X = s.transform(X)
# 分割训练集和测试集
train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
# 显示出随机森林特征的重要性，并做条形图
rfr = RandomForestRegressor(min_samples_split=6, n_estimators=100)
#------------------------------
param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]

grid_search = GridSearchCV(rfr, param_grid, cv=5, scoring='neg_mean_squared_error')

grid_search.fit(train_x, train_y)