import os
import numpy as np

from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV, Lasso, LassoCV, Ridge, LinearRegression, SGDClassifier, SGDRegressor
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB


THIS_PATH = os.path.dirname(os.path.abspath(__file__))


ML_MODELS = {'Logistic Regression (Classification)': LogisticRegression,
             'Random Forest (Classification)': RandomForestClassifier,
             'Neural Networks (Classification)': MLPClassifier,
             'BernoulliNB (Classification)': BernoulliNB,
             # 'SVM (Classification)': SVC,
             'Random Forest (Regression)': RandomForestRegressor,
             # 'SVM (Regression)': SVR,
             'GaussianNB (Regression)': GaussianNB,
             'Ridge (Regression)': Ridge,
             'Linear Regression (Regression)': LinearRegression,
             'SGD (Regression)': SGDRegressor,
             # 'SGD (Classification)': SGDClassifier,
             }


ML_MODELS_PROBLEM_TYPE_MAP = {'classification': ['BernoulliNB (Classification)',
                                                 'Logistic Regression (Classification)',
                                                 'Neural Networks (Classification)',
                                                 'Random Forest (Classification)',
                                                 # 'SGD (Classification)',
                                                 # 'SVM (Classification)',
                                                 ],
                              'regression': ['GaussianNB (Regression)',
                                             'Linear Regression (Regression)',
                                             'Ridge (Regression)',
                                             'Random Forest (Regression)',
                                             # 'SGD (Regression)',
                                             # 'SVM (Regression)',
                                             ]}


HYPERPARAMETER_OPTIMIZATION = {'Logistic Regression (Classification)': {'how': 'grid_search',
                                                       'run_parms': {'model__penalty': ['l1', 'l2'],
                                                                     'model__C': np.logspace(0, 4, 10)
                                                                  }
                                                       },
                               'Random Forest (Classification)': {'how': 'grid_search',
                                                 'run_parms': {'model__bootstrap': [True],
                                                            'model__max_depth': [1, 10, None],
                                                            'model__max_features': ['auto', 'sqrt'],
                                                            'model__min_samples_leaf': [1, 2, 4],
                                                            'model__min_samples_split': [2, 5, 10],
                                                            'model__n_estimators': [10, 100, 200, 1000]}},
                               'Random Forest (Regression)': {'how': 'grid_search',
                                                                  'run_parms': {'model__bootstrap': [True],
                                                                                'model__max_depth': [1, 10, None],
                                                                                'model__max_features': ['auto', 'sqrt'],
                                                                                'model__min_samples_leaf': [1, 2, 4],
                                                                                'model__min_samples_split': [2, 5, 10],
                                                                                'model__n_estimators': [10, 100, 200, 1000]}},
                               # 'Neural Networks (Classification)': None
                               }

METRICS_MAP = {'accuracy': metrics.accuracy_score,
               'balanced_accuracy': metrics.balanced_accuracy_score,
               'recall': metrics.recall_score,
               'precision': metrics.precision_score,
               'roc_auc': metrics.roc_auc_score,
               'mean_squared_error': metrics.mean_squared_error,
               'mean_absolute_error': metrics.mean_absolute_error
               }

METRIC_PROBLEM_TYPE_MAP = {'classification': ['accuracy',
                                              'balanced_accuracy',
                                              'recall',
                                              'precision',
                                              'roc_auc'],
                           'regression': ['mean_squared_error',
                                          'mean_absolute_error']}

FILTER_DATA = {
    # '<= 1 year old': {
    #     'column': 'dem_age_int',
    #     'function': lambda x: x <= 12
    # },
    # '> 1 year old': {
    #     'column': 'dem_age_int',
    #     'function': lambda x: x > 12
    # },
}

DEFAULT_METRIC = {'classification': 'roc_auc', 'regression': 'mean_squared_error'}

N_ROUND_METRICS = 3

N_CPUS = 4

IMPUTER_METHOD = 'median'