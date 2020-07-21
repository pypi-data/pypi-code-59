from itertools import compress

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LassoCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from boruta import BorutaPy

from logic import settings, models



def optimize_hyperparams(X_train, y_train,
                         model_name, features_cat, features_num,
                         metric_cv):

    optimization_strategy = settings.HYPERPARAMETER_OPTIMIZATION.get(model_name)

    model_pipe = models.get_model_pipeline(settings.ML_MODELS.get(model_name),
                                           features_cat, features_num,
                                           default_params={})

    if optimization_strategy.get('how') == 'grid_search':
        space = optimization_strategy.get('run_parms')
        gs = GridSearchCV(model_pipe, space, n_jobs=-1, cv=3, scoring=metric_cv)
        gs.fit(X_train, y_train)
        model_pipe.set_params(**gs.best_params_)

    return model_pipe.fit(X_train, y_train)


def feature_selection(X_train, y_train, features, all_features_cat, all_features_num, method=None, seed=98304):
    if not method:
        selected_features = features

    elif method=='lasso':
        features_cat = [x for x in features if x in all_features_cat]
        features_num = [x for x in features if x in all_features_num]

        pipeline = models.get_model_pipeline(LassoCV, features_cat, features_num, {'n_alphas': 100, 'random_state': seed})

        coefs = pipeline.fit(X_train, y_train)['model'].coef_

        ohe_categories = (pipeline['preprocessor'].named_transformers_['categorical']['onehotencoder'].categories_
                          if features_cat else [])
        new_ohe_features = [f"{col}__{val}" for col,
                                                vals in zip(features_cat, ohe_categories) for val in vals]

        coefs_0 = coefs != 0
        features_names = features_num + new_ohe_features
        selected_features = list(set([f.split('__')[0]
                                      for f in compress(features_names, coefs_0)]))

    elif method=='boruta':
        rf = RandomForestClassifier(n_jobs=-1, class_weight='balanced', max_depth=2, random_state=seed)
        preprocessor = ColumnTransformer([('features',
                                           SimpleImputer(strategy='median'),
                                           features)])

        feat_selector = BorutaPy(rf, n_estimators='auto', verbose=0, random_state=145)
        feat_selector.fit(preprocessor.fit_transform(X_train), y_train)

        selected_features = list(compress(features, feat_selector.support_))


    return selected_features