
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier,KNeighborsRegressor

df = pd.read_csv(r'creditcard.csv')
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
s = MinMaxScaler()
s.fit(X)
X = s.transform(X)
train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)


rfr = RandomForestRegressor(min_samples_split=6, n_estimators=100)
rfr.fit(train_x, train_y)
print(rfr.score(test_x, test_y))
feature_important = pd.Series(rfr.feature_importances_, index = df.V1).sort_values(ascending=False)
plt.bar(feature_important.index, feature_important.data)
print(feature_important.data)