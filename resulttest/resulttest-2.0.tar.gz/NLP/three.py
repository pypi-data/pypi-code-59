# @Time : 2020/7/21 10:54 
# @Author : XX
# @File : z.py
# @Software: PyCharm
import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def get_text(text):
    return jieba.lcut(text)

df = pd.read_csv()
X = df.iloc[:,1:]
Y = df.iloc[:,0]
# tokenizer分词器,停用词
with open(r'') as r:
    stop_words = r.readlines()
tf = TfidfVectorizer(tokenizer=get_text,stop_words=stop_words)
X = tf.fit_transform(df['content'])
train_X,test_X,train_Y,test_Y = train_test_split(X,Y)
tree = DecisionTreeClassifier()
tree.fit(train_X,train_Y)
print(tree.score(test_X,test_Y))