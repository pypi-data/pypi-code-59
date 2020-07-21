

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
df = pd.read_csv(r'creditcard.csv')
X = df.iloc[:,:-1]
Y = df.iloc[:,-1]
s = MinMaxScaler()
s.fit(X)
X = s.transform(X)
train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(train_x,train_y)
print('KNN:',knn.score(test_x, test_y))