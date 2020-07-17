#!/usr/bin/env python
              
'''
version : Version 0.1.0
Author : Tony Dong

First edited : 15 July 2020
Last edited : 17 July 2020
Description : 
 - This module is used for model selection:
    * Automate the models training with cross validation
    * GridSearch the best parameters
    * Export the optimized models as pkl, and saved in /pkl folders
    * Validate the optimized models, and select the best model 

 - Class
    * dynaClassifier - Focus on classification problems
        $ fit_clf() - fit method for classifier
    * dynaRegressor - Focus on regression problems
        $ fit_reg() - fit method for regressor
'''
'''
<Demo - Input from csv file - Regression Problem>

==> CODE:

import pandas as pd
from dynapipe.autoCV import dynaClassifier,evaluate_clf_model
import joblib

tr_features = pd.read_csv('./data/classification/train_features.csv')
tr_labels = pd.read_csv('./data/classification/train_labels.csv')
val_features = pd.read_csv('./data/classification/val_features.csv')
val_labels = pd.read_csv('./data/classification/val_labels.csv')
te_features = pd.read_csv('./data/classification/test_features.csv')
te_labels = pd.read_csv('./data/classification/test_labels.csv')

clf_cv_demo = dynaClassifier(random_state = 13,cv_num = 5)

clf_cv_demo.fit_clf(tr_features,tr_labels)

models = {}

for mdl in ['lgr','svm','mlp','rf','ada','gb','xgb']:
    models[mdl] = joblib.load('dynapipe/pkl/{}_clf_model.pkl'.format(mdl))

for name, mdl in models.items():
    evaluate_clf_model(name, mdl, val_features, val_labels)

==> OUTPUT:

      *DynaPipe* autoCV Module ===> lgr_CrossValidation with 5 folds:

Best Parameters: {'C': 1, 'random_state': 13}

Best CV Score: 0.7997178628107917

Progress: [###-----------------] 14.3%

      *DynaPipe* autoCV Module ===> svm_CrossValidation with 5 folds:

Best Parameters: {'C': 0.1, 'kernel': 'linear'}

Best CV Score: 0.7959619114794568

Progress: [######--------------] 28.6%

      *DynaPipe* autoCV Module ===> mlp_CrossValidation with 5 folds:

Best Parameters: {'activation': 'tanh', 'hidden_layer_sizes': (50,), 'learning_rate': 'constant', 'random_state': 13, 'solver': 'lbfgs'}

Best CV Score: 0.8184094515958386

Progress: [#########-----------] 42.9%

      *DynaPipe* autoCV Module ===> rf_CrossValidation with 5 folds:

Best Parameters: {'max_depth': 4, 'n_estimators': 250, 'random_state': 13}

Best CV Score: 0.8240521953800035

Progress: [###########---------] 57.1%

      *DynaPipe* autoCV Module ===> ada_CrossValidation with 5 folds:

Best Parameters: {'learning_rate': 0.1, 'n_estimators': 100, 'random_state': 13}

Best CV Score: 0.824034561805678

Progress: [##############------] 71.4%

      *DynaPipe* autoCV Module ===> gb_CrossValidation with 5 folds:

Best Parameters: {'learning_rate': 0.01, 'max_depth': 3, 'n_estimators': 300, 'random_state': 13}

Best CV Score: 0.8408746252865456

Progress: [#################---] 85.7%

      *DynaPipe* autoCV Module ===> xgb_CrossValidation with 5 folds:

Best Parameters: {'learning_rate': 0.1, 'max_depth': 3, 'n_estimators': 200, 'verbosity': 0}

Best CV Score: 0.8464292011990832

Progress: [####################] 100.0%
lgr -- Accuracy: 0.775 / Precision: 0.712 / Recall: 0.646 / Latency: 0.0ms
svm -- Accuracy: 0.747 / Precision: 0.672 / Recall: 0.6 / Latency: 2.0ms
mlp -- Accuracy: 0.787 / Precision: 0.745 / Recall: 0.631 / Latency: 4.1ms
rf -- Accuracy: 0.809 / Precision: 0.83 / Recall: 0.6 / Latency: 37.0ms
ada -- Accuracy: 0.792 / Precision: 0.759 / Recall: 0.631 / Latency: 21.4ms
gb -- Accuracy: 0.815 / Precision: 0.796 / Recall: 0.662 / Latency: 2.0ms
xgb -- Accuracy: 0.815 / Precision: 0.786 / Recall: 0.677 / Latency: 5.0ms
'''

from dynapipe.estimatorCV import clf_cv,reg_cv
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score
from dynapipe.utilis_func import delete_old_log_files,update_progress
import joblib
import logging
import datetime
import numpy as np
from time import time
import warnings
import os

path = os.getcwd()

def warn(*args, **kwargs):
    pass


LOG_TS = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
LOG_LEVEL = logging.DEBUG
DELETE_FLAG = True
TS = time()
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s','%d/%m %H:%M:%S')
fh = logging.FileHandler(filename = f'{".".join(__file__.split(".")[:-1])}_log_{LOG_TS}.log')
fh.setLevel(LOG_LEVEL)
fh.setFormatter(formatter)
logger.addHandler(fh)
Test_case = f'*Dynapipe* autoCV - Model Selection :: {LOG_TS}'
Test_comment = '-' * len(Test_case) * 3
Start_log = '#' * len(Test_case) * 3
logger.info(Start_log)
logger.info(Test_case)
logger.info(Start_log)
delete_old_log_files(directory = './' ,delete_flag = DELETE_FLAG, logger = logger, extension_list = ['.log'],filename_list = ['autoCV_log_'],log_ts = LOG_TS)
logger.info(Test_comment)

def print_results(results):
    print('\nBest Parameters: {}\n'.format(results.best_params_))
    print('Best CV Score: {}\n'.format(results.best_score_))
    logger.info('Best Paramaters: {}\n'.format(results.best_params_))
    logger.info('Best CV Score: {}\n'.format(results.best_score_))
    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, results.cv_results_['params']):
        logger.info('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))

def evaluate_clf_model(name = None, model = None, features = None, labels = None):
    start = time()
    pred = model.predict(features)
    end = time()
    accuracy = round(accuracy_score(labels, pred), 3)
    precision = round(precision_score(labels, pred), 3)
    recall = round(recall_score(labels, pred), 3)
    print('{} -- Accuracy: {} / Precision: {} / Recall: {} / Latency: {}ms'.format(name,accuracy,precision,recall,round((end - start)*1000, 1)))
    logger.info('{} -- Accuracy: {} / Precision: {} / Recall: {} / Latency: {}ms'.format(name,accuracy,precision,recall,round((end - start)*1000, 1)))
    return(None)

def evaluate_reg_model(name = None, model = None, features = None, labels = None):
    start = time()
    pred = model.predict(features)
    end = time()
    R2 = round(metrics.r2_score(labels, pred),3)
    MAE = round(metrics.mean_absolute_error(labels, pred),3)
    MSE = round(metrics.mean_squared_error(labels, pred),3)
    RMSE = round(metrics.mean_squared_error(labels, pred),3)
    print(f'{name} -- R^2 Score: {R2} / Mean Absolute Error: {MAE} / Mean Squared Error: {MSE} / Root Mean Squared Error: {RMSE} / Latency: {round((end - start)*1000, 1)}ms')
    logger.info(f'{name} -- R Squared Score: {R2} / Mean Absolute Error: {MAE} / Mean Squared Error: {MSE} / Root Mean Squared Error: {RMSE} / Latency: {round((end - start)*1000, 1)}ms')
    


class dynaClassifier:
    def __init__(self,random_state = 13,cv_num = 5,input_from_file = True):
        self.random_state =random_state
        self.cv_num = cv_num
        self.input_from_file = input_from_file

    def fit_clf(self,tr_features,tr_labels):
        warnings.warn = warn
        if(self.input_from_file):
            tr_labels = tr_labels.values.ravel()
        clf = clf_cv(cv_val = self.cv_num,random_state = self.random_state)
        estimators = ['lgr','svm','mlp','rf','ada','gb','xgb']
        loop_num = 1
        total_loop = len(estimators)
        
        for est in estimators:
            start_time = time()
            logger.info(Test_comment)
            logger.info(f"Current Running:" + est +" estimator")

            try:
                cv_est = getattr(clf, est)()
                cv_est.fit(tr_features,tr_labels)
                joblib.dump(cv_est.best_estimator_, './pkl/'+est+'_clf_model.pkl')
                print(f"\n      *DynaPipe* autoCV Module ===> {est}_CrossValidation with {self.cv_num} folds:")
                print_results(cv_est)
                update_progress(loop_num/total_loop)
                logger.info(f"This estimator executed {round((time()-start_time)/60,4)} minutes")
                loop_num += 1
            except:
                print(est+" estimator is not availible.")
                update_progress(loop_num/total_loop)
                logger.info(f"This estimator executed {round((time()-start_time)/60,4)} minutes")
                loop_num += 1
                pass

class dynaRegressor:
    def __init__(self ,random_state = 25 ,cv_num = 5,input_from_file = True):
        self.random_state =random_state
        self.cv_num = cv_num
        self.input_from_file = input_from_file

    def fit_reg(self,tr_features,tr_labels):
        
        if(self.input_from_file):
            tr_labels = tr_labels.values.ravel()
        reg = reg_cv(cv_val = self.cv_num,random_state = self.random_state)
        estimators = ['lr','knn','tree','svm','mlp','rf','gb','ada','xgb']

        loop_num = 1
        total_loop = len(estimators)
        
        for est in estimators:
            start_time = time()
            logger.info(Test_comment)
            logger.info(f"Current Running:" + est +" estimator")
            try:
                cv_est = getattr(reg, est)()
                cv_est.fit(tr_features,tr_labels)
                joblib.dump(cv_est.best_estimator_, 'dynapipe/pkl/'+est+'_reg_model.pkl')
                print(f"\n      *DynaPipe* autoCV Module ===> {est} model CrossValidation with {self.cv_num} folds:")
                print_results(cv_est)
                update_progress(loop_num/total_loop)
                logger.info(f"This estimator executed {round((time()-start_time)/60,4)} minutes")
                loop_num += 1
            except:
                print(est+" estimator is not availible.")
                update_progress(loop_num/total_loop)
                logger.info(f"This estimator executed {round((time()-start_time)/60,4)} minutes")
                loop_num += 1
                pass

