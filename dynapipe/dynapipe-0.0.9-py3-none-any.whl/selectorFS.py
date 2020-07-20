#!/usr/bin/env python
             
'''
version : Version 0.1.0
Author : Tony Dong

First edited : 15 July 2020
Last edited : 17 July 2020
Description : 
 - This module is used as selectors reporsitory:
    * Support autoFS module's features selection function
    * Could add more selectors in the classes easily

 - Class and current available selectors
    * clf_fs - Class focusing on classification features selection
        $ kbest_f - SelectKBest() with f_classif core
        $ kbest_chi2 - SelectKBest() with chi2 core
        $ rfe_lr - RFE with LogisticRegression() estimator
        $ rfe_svm - RFE with SVC() estimator
        $ rfecv_svm - RFECV with SVC() estimator  
        $ rfe_tree - RFE with DecisionTreeClassifier() estimator
        $ rfecv_tree - RFECV with DecisionTreeClassifier() estimator
        $ rfe_rf - RFE with RandomForestClassifier() estimator
        $ rfecv_rf - RFECV with RandomForestClassifier() estimator
        
    * reg_fs - Class focusing on regression features selection
        $ kbest_f - SelectKBest() with f_regression core
        $ rfe_svm - RFE with SVC() estimator
        $ rfecv_svm - RFECV with SVC() estimator  
        $ rfe_tree - RFE with DecisionTreeRegressor() estimator
        $ rfecv_tree - RFECV with DecisionTreeRegressor() estimator
        $ rfe_rf - RFE with RandomForestRegressor() estimator
        $ rfecv_rf - RFECV with RandomForestRegressor() estimator
        
'''

import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2, RFE,RFECV, f_regression, f_classif
from sklearn.svm import SVC, SVR
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
warnings.filterwarnings('ignore', category=DeprecationWarning)

class clf_fs:
    def __init__(self,fs_num = None ,random_state = None,cv = None):
        self.fs_num = fs_num
        self.random_state = random_state
        self.cv = cv
    # GenericUnivariateSelect with chi2 method
    def kbest_f(self):
        selector = SelectKBest(score_func = f_classif, k = self.fs_num)
        return (selector)
    def kbest_chi2(self):
        selector = SelectKBest(score_func = chi2, k = self.fs_num)
        return (selector)
    def rfe_lr(self):
        estimator = LogisticRegression()
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfe_svm(self):
        estimator = SVC(kernel="linear")
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfe_tree(self):
        estimator = DecisionTreeClassifier()
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfe_rf(self):
        estimator = RandomForestClassifier(max_depth = 3, n_estimators = 5)
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfecv_svm(self):
        estimator = SVC(kernel="linear")
        selector = RFECV(estimator, min_features_to_select = self.fs_num, cv = self.cv)
        return(selector)
    def rfecv_tree(self):
        estimator = DecisionTreeClassifier()
        selector = RFECV(estimator, min_features_to_select = self.fs_num, cv = self.cv)
        return(selector)
    def rfecv_rf(self):
        estimator = RandomForestClassifier(max_depth = 3, n_estimators = 5)
        selector = RFECV(estimator, min_features_to_select = self.fs_num, cv = self.cv)
        return(selector)


class reg_fs:
    def __init__(self,fs_num,random_state = None,cv = None):
        self.fs_num = fs_num
        self.random_state = random_state
        self.cv = cv
    # GenericUnivariateSelect with chi2 method
    def kbest_f(self):
        selector = SelectKBest(score_func = f_regression, k = self.fs_num)
        return (selector)
    def rfe_svm(self):
        estimator = SVR(kernel="linear")
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfe_tree(self):
        estimator = DecisionTreeRegressor()
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfe_rf(self):
        estimator = RandomForestRegressor(max_depth = 3, n_estimators = 5)
        selector = RFE(estimator, n_features_to_select = self.fs_num)
        return(selector)
    def rfecv_svm(self):
        estimator = SVR(kernel="linear")
        selector = RFECV(estimator, min_features_to_select = self.fs_num, cv = self.cv)
        return(selector)
    def rfecv_tree(self):
        estimator = DecisionTreeRegressor()
        selector = RFECV(estimator, min_features_to_select = self.fs_num, cv = self.cv)
        return(selector)
    def rfecv_rf(self):
        estimator = RandomForestRegressor(max_depth = 3, n_estimators = 5)
        selector = RFECV(estimator, min_features_to_select = self.fs_num, cv = self.cv)
        return(selector)


