# @Time : 2020/7/21 9:54 
# @Author : XX
# @File : one.py 
# @Software: PyCharm

from sklearn.preprocessing import MinMaxScaler# 最小值最大值归一化
from sklearn.model_selection import train_test_split # 训练测试分割
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor
import pandas as pd
df = pd.read_csv(r'creditcard.csv')
# 拆分为特征矩阵和目标向量
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
# 归一
s = MinMaxScaler()
s.fit(X)
X = s.transform(X)
# 分割训练集和测试集
train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_x,train_y)
print('KNN:',knn.score(test_x, test_y))