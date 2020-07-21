#!/usr/bin/env python
             
'''
version : Version 0.1.0
Author : Tony Dong

First edited : 15 July 2020
Last edited : 17 July 2020
Description : 
 - This module is used as estimators reporsitory:
    * Support autoCV module's models training with cross validation
    * Could add more estimators/methods in the classes easily
    * The parameters for each estimator are selected by experience 

 - Class and current available estimators
    * clf_cv - Class focusing on classification estimators
        $ lgr - Logistic Regression (aka logit, MaxEnt) classifier - LogisticRegression()
        $ svm - C-Support Vector Classification - SVM.SVC()
        $ mlp - Multi-layer Perceptron classifier - MLPClassifier()
        $ ada - An AdaBoost classifier - AdaBoostClassifier()
        $ rf - Random Forest classifier - RandomForestClassifier()
        $ gb - Gradient Boost classifier - GradientBoostingClassifier()
        $ xgb = XGBoost classifier - xgb.XGBClassifier()
    * reg_cv - Class focusing on regression estimators
        $ lr - Linear Regression - LinearRegression()
        $ knn - Regression based on k-nearest neighbors - KNeighborsRegressor()
        $ svr - Epsilon-Support Vector Regression - SVM.SVR()
        $ rf - Random Forest Regression - RandomForestRegressor()
        $ ada - An AdaBoost regressor - AdaBoostRegressor()
        $ gb - Gradient Boosting for regression -GradientBoostingRegressor()
        $ tree - A decision tree regressor - DecisionTreeRegressor()
        $ mlp - Multi-layer Perceptron regressor - MLPRegressor()
        $ xgb - XGBoost regression - XGBRegressor()
'''
import pandas as pd
from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.svm import SVC,SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,AdaBoostRegressor,AdaBoostClassifier
from sklearn.neural_network import MLPClassifier,MLPRegressor
from sklearn.ensemble import GradientBoostingClassifier,GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
import xgboost as xgb

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

# import importlib.resources
import json
import os

json_path = os.path.join(os.path.dirname(__file__), 'parameters.json')
with open(json_path, encoding='utf-8') as data_file:
    para_data = json.load(data_file)
data_file.close()

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

class clf_cv:

    def __init__(self,cv_val = None,random_state = None):
        self.cv = cv_val
        self.random_state = random_state

    def lgr(self):
        lgr_cv = LogisticRegression()
        # parameters = {
        #     'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
        #     'random_state': [self.random_state]
        #     }
        parameters = para_data["cls"]["lgr"]
        parameters['random_state'] = self.random_state
        return (GridSearchCV(lgr_cv, parameters,cv = self.cv))
    def svm(self):
        svm_cv = SVC()
        parameters = para_data["cls"]["svm"]
        # parameters = {
        #     'kernel':['linear', 'poly', 'rbf', 'sigmoid'],
        #     'C': [0.1, 1, 10]
        #     }
        return(GridSearchCV(svm_cv, parameters, cv = self.cv))
    def mlp(self):
        mlp_cv = MLPClassifier()
        # parameters = {
        #     'hidden_layer_sizes': [(10,), (50,), (100,)],
        #     'activation': ['identity','relu', 'tanh', 'logistic'],
        #     'learning_rate': ['constant', 'invscaling', 'adaptive'],
        #     'activation' : ['identity', 'logistic', 'tanh', 'relu'],
        #     'solver' : ['lbfgs', 'sgd', 'adam'],
        #     'random_state': [self.random_state]
        # }
        parameters = para_data["cls"]["mlp"]
        parameters['random_state'] = self.random_state
        return(GridSearchCV(mlp_cv, parameters, cv = self.cv))
    def ada(self):
        ada_cv = AdaBoostClassifier()
        # parameters = {
        #     'n_estimators': [50,100,150],
        #     'learning_rate': [0.01,0.1, 1, 5, 10],
        #     'random_state': [self.random_state]  
        #     }
        parameters = para_data["cls"]["ada"]
        parameters['random_state'] = self.random_state
        return(GridSearchCV(ada_cv, parameters, cv=self.cv))
    def rf(self):
        rf_cv = RandomForestClassifier()
        # parameters = {
        #     'n_estimators': [5, 50, 250],
        #     'max_depth': [2, 4, 8, 16, 32],
        #     'random_state': [self.random_state]
            
        #     }
        parameters = para_data["cls"]["rf"]
        parameters['random_state'] = self.random_state
        return(GridSearchCV(rf_cv, parameters, cv=self.cv))
    def gb(self):
        gb_cv = GradientBoostingClassifier()
        # parameters = {
        #     'n_estimators': [50,100,150,200,250,300],
        #     'max_depth': [1, 3, 5, 7, 9],
        #     'learning_rate': [0.01, 0.1, 1, 10, 100],
        #     'random_state': [self.random_state]
        #     }
        parameters = para_data["cls"]["gb"]
        parameters['random_state'] = self.random_state
        return(GridSearchCV(gb_cv, parameters,cv=self.cv))
    def xgb(self):
        xgb_cv = xgb.XGBClassifier()
        # parameters = {
        #     'n_estimators': [50,100,150,200,250,300],
        #     'max_depth': [3, 5, 7, 9],
        #     'learning_rate': [0.01, 0.1, 0.2,0.3,0.4],
        #     'verbosity' : [0]
        #     }
        parameters = para_data["cls"]["gb"]
        return(GridSearchCV(xgb_cv, parameters,cv=self.cv))

class reg_cv:

    def __init__(self,cv_val = None,random_state = None):
        self.cv = cv_val
        self.random_state = random_state

    def lr(self):
        lr_cv = LinearRegression()
        parameters = {
            'normalize' : [True,False]
            } 
        return (GridSearchCV(lr_cv, parameters,cv = self.cv))
    def knn(self):
        knn_cv = KNeighborsRegressor()
        # parameters = {
        #     'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
        #     'n_neighbors': [5, 10, 15, 20, 25],
        #     'weights': ['uniform', 'distance'],
        #     }
        parameters = para_data["reg"]["knn"]
        return(GridSearchCV(knn_cv, parameters, cv = self.cv))
    def svm(self):
        svm_cv = SVR()
        # parameters = {
        #     'kernel':['linear', 'poly', 'rbf', 'sigmoid'],
        #     'C': [0.1, 1, 10]
        #     }
        parameters = para_data["reg"]["svm"]
        return(GridSearchCV(svm_cv, parameters, cv = self.cv))
    def mlp(self):

        mlp_cv = MLPRegressor()
        # parameters = {
        #     'hidden_layer_sizes': [(10,), (50,), (100,)],
        #     'activation': ['identity','relu', 'tanh', 'logistic'],
        #     'learning_rate': ['constant', 'invscaling', 'adaptive'],
        #     'activation' : ['identity', 'logistic', 'tanh', 'relu'],
        #     'solver' : ['lbfgs', 'adam'],
        #     'random_state': [self.random_state]
        # }

        parameters = para_data["reg"]["mlp"]
        parameters['random_state'] = self.random_state
        return(GridSearchCV(mlp_cv, parameters, cv = self.cv))  
    def rf(self):
        rf_cv = RandomForestRegressor()
        parameters = {
            'n_estimators': [5, 50, 250],
            'max_depth': [2, 4, 8, 16, 32]
            }
        parameters = para_data["reg"]["rf"]   
        return(GridSearchCV(rf_cv, parameters, cv=self.cv))
    def gb(self):
        gb_cv = GradientBoostingRegressor()
        # parameters = {
        #     'n_estimators': [50,100,150,200,250,300],
        #     'max_depth': [3, 5, 7, 9],
        #     'learning_rate': [0.01, 0.1, 0.2,0.3,0.4]
        #     }
        parameters = para_data["reg"]["gb"]
        return(GridSearchCV(gb_cv, parameters,cv=self.cv))
    def tree(self):
        tree_cv = DecisionTreeRegressor()
        # parameters = {
        #     'splitter':['best', 'random'],
        #     'max_depth': [1, 3, 5, 7, 9],
        #     'random_state': [self.random_state],
        #     'min_samples_leaf':[1,3,5]
        #     }
        parameters = para_data["reg"]["tree"]
        return(GridSearchCV(tree_cv, parameters,cv=self.cv))       
    def ada(self):
        ada_cv = AdaBoostRegressor()
        # parameters = {
        #     'n_estimators': [50,100,150,200,250,300],
        #     'loss':['linear','square','exponential'],
        #     'learning_rate': [0.01, 0.1, 0.2,0.3,0.4],
        #     'random_state': [self.random_state]            
        #     }
        parameters = para_data["reg"]["ada"]
        parameters['random_state'] = self.random_state
        return(GridSearchCV(ada_cv, parameters,cv=self.cv))
    def xgb(self):
        xgb_cv = xgb.XGBRegressor()
        # parameters = {
        #     'n_estimators': [50,100,150,200,250,300],
        #     'max_depth': [3, 5, 7, 9],
        #     'learning_rate': [0.01, 0.1, 0.2,0.3,0.4],
        #     'verbosity' : [0]
        #     }
        parameters = para_data["reg"]["xgb"]
        return(GridSearchCV(xgb_cv, parameters,cv=self.cv))

