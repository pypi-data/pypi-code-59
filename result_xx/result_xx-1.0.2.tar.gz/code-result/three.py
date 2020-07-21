# @Time : 2020/7/21 9:57 
# @Author : XX
# @File : three.py 
# @Software: PyCharm

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
rfr.fit(train_x, train_y)
print(rfr.score(test_x, test_y))
# 使用pd.Series进行组合，值是特征重要性的值，index是样本特征，.sort_value 进行排序操作
feature_important = pd.Series(rfr.feature_importances_, index = df.V1).sort_values(ascending=False)
plt.bar(feature_important.index, feature_important.data)
#---------------------------------------
print(feature_important.data)