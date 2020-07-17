import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from ngboost.distns import BetaBernoulli
from ngboost.scores import LogScore, CRPScore
from ngboost import NGBRegressor
from sklearn.model_selection import train_test_split



if __name__ == "__main__":

    df = pd.read_csv('./data/cs-training.csv')
    df.head()

    np.random.seed(123)

    features = [col for col in df.columns.tolist() if col not in ['Unnamed: 0', 'SeriousDlqin2yrs']]
    cat_features = list(df[features].select_dtypes(exclude=['float64','int64']).columns)
    for feature in cat_features:
        df[feature] = df[feature].astype('category').cat.codes

    train, test = train_test_split(df, test_size=0.2)
    print(train.shape)
    print(test.shape)

    X_train, X_val, Y_train, Y_val = train_test_split(train[features], train['SeriousDlqin2yrs'], test_size=0.05)
    print(X_train.shape)
    print(X_val.shape)

    X_train2, X_val2, Y_train2, Y_val2 = train_test_split(X_train, Y_train, test_size=0.95)
    print(X_train2.shape)
    print(X_val2.shape)

    learner = DecisionTreeRegressor(criterion='friedman_mse', max_depth=5)
    base_model = NGBRegressor(
                Dist=BetaBernoulli,
                Score=LogScore,
                Base=learner,
                n_estimators=2000,
                learning_rate=0.01,
                col_sample=1.0,
                natural_gradient=True,
                verbose_eval=20,
                minibatch_frac=1.0)
    base_model.fit(X_train2.fillna(-1).values, Y_train2.values, X_val=X_val.fillna(-1).values, Y_val=Y_val.values, early_stopping_rounds=2)

