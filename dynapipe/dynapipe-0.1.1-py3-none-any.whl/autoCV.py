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


from dynapipe.estimatorCV import clf_cv,reg_cv
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score
from dynapipe.utilis_func import update_progress
import joblib
import datetime
import numpy as np
from time import time
import warnings
import os

path = os.getcwd()

def warn(*args, **kwargs):
    pass

def print_results(results,detail_flag = False):
    print('\nBest Parameters: {}\n'.format(results.best_params_))
    print('Best CV Score: {}\n'.format(results.best_score_))
    means = results.cv_results_['mean_test_score']
    stds = results.cv_results_['std_test_score']
    if (detail_flag):
        for mean, std, params in zip(means, stds, results.cv_results_['params']):
            print('{} (+/-{}) for {}'.format(round(mean, 3), round(std * 2, 3), params))

def evaluate_clf_model(name = None, model = None, features = None, labels = None):
    start = time()
    pred = model.predict(features)
    end = time()
    accuracy = round(accuracy_score(labels, pred), 3)
    precision = round(precision_score(labels, pred), 3)
    recall = round(recall_score(labels, pred), 3)
    print('{} -- Accuracy: {} / Precision: {} / Recall: {} / Latency: {}ms'.format(name,accuracy,precision,recall,round((end - start)*1000, 1)))
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
    

class dynaClassifier:
    def __init__(self,random_state = 13,cv_num = 5,input_from_file = True):
        self.random_state =random_state
        self.cv_num = cv_num
        self.input_from_file = input_from_file

    def fit_clf(self,tr_features = None,tr_labels = None, detail_info = False):
        warnings.warn = warn
        if(self.input_from_file):
            tr_labels = tr_labels.values.ravel()
        clf = clf_cv(cv_val = self.cv_num,random_state = self.random_state)
        estimators = ['lgr','svm','mlp','rf','ada','gb','xgb']
        loop_num = 1
        total_loop = len(estimators)

        pkl_folder = os.path.join(os.getcwd(),'pkl')
        if not os.path.exists(pkl_folder):
            os.makedirs(pkl_folder)

        for est in estimators:
            start_time = time()
            try:
                cv_est = getattr(clf, est)()
                cv_est.fit(tr_features,tr_labels)
                model_name = os.path.join(pkl_folder, f'{est}_clf_model.pkl')
                joblib.dump(cv_est.best_estimator_, model_name)
                print(f"\n    *DynaPipe* autoCV Module ===> {est}_CrossValidation with {self.cv_num} folds:")
                print_results(cv_est, detail_flag = detail_info)
                update_progress(loop_num/total_loop)
                loop_num += 1
            except:
                print(est+" estimator is not availible.")
                update_progress(loop_num/total_loop)
                loop_num += 1
                pass

class dynaRegressor:
    def __init__(self ,random_state = 25 ,cv_num = 5,input_from_file = True):
        self.random_state =random_state
        self.cv_num = cv_num
        self.input_from_file = input_from_file

    def fit_reg(self,tr_features = None,tr_labels = None, detail_info = False):
        
        if(self.input_from_file):
            tr_labels = tr_labels.values.ravel()
        reg = reg_cv(cv_val = self.cv_num,random_state = self.random_state)
        estimators = ['lr','knn','tree','svm','mlp','rf','gb','ada','xgb']
        pkl_folder = os.path.join(os.getcwd(),'pkl')
        if not os.path.exists(pkl_folder):
            os.makedirs(pkl_folder)
        loop_num = 1
        total_loop = len(estimators)
        
        for est in estimators:
            start_time = time()
            try:
                cv_est = getattr(reg, est)()
                cv_est.fit(tr_features,tr_labels)
                model_name = os.path.join(pkl_folder, f'{est}_reg_model.pkl')
                joblib.dump(cv_est.best_estimator_, model_name)
                print(f"\n    *DynaPipe* autoCV Module ===> {est} model CrossValidation with {self.cv_num} folds:")
                print_results(cv_est, detail_flag = detail_info)
                update_progress(loop_num/total_loop)
                loop_num += 1
            except:
                print(est+" estimator is not availible.")
                update_progress(loop_num/total_loop)
                loop_num += 1
                pass

