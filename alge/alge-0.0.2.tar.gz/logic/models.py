import numpy as np
from logic import settings
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder


def fit(X_train, y_train,
        model_pipe):

    return model_pipe.fit(X_train, y_train)


def get_model_pipeline(model, features_cat, features_num, default_params={}):

    preprocessor = ColumnTransformer([
        ("numerical",
         SimpleImputer(strategy=settings.IMPUTER_METHOD),
         features_num),
        ("categorical",
         make_pipeline(SimpleImputer(strategy='most_frequent'),
                       OneHotEncoder(handle_unknown='ignore')),
         features_cat)])

    random_state = np.random.choice(range(10000), 1)[0]
    try:
        instance_model = model(**default_params)
    except:
        instance_model = model()
    default_params['random_state'] = random_state

    return Pipeline([('preprocessor', preprocessor),
                     ('model', instance_model)])
