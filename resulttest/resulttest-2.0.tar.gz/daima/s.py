

from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import GridSearchCV
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
param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]

grid_search = GridSearchCV(rfr, param_grid, cv=5, scoring='neg_mean_squared_error')

grid_search.fit(train_x, train_y)