#!/usr/bin/env python 

'''
version : Version 0.1.0
Author : Tony Dong

First edited : 15 July 2020
Last edited : 17 July 2020
Description : 
 - This module is used for features selection:
    * Automate the feature selection with several selectors
    * Esemble the outputs from all selector methods, and ranked a final list of the top important features

 - Class
    * dynaFS_clf - Focus on classification problems
        $ fit_fs_clf() - fit method for classifier
    * dynaFS_reg - Focus on regression problems
        $ fit_fs_reg() - fit method for regressor
'''
from dynapipe.selectorFS import clf_fs,reg_fs
from sklearn.metrics import accuracy_score, precision_score, recall_score
from dynapipe.utilis_func import update_progress
import joblib
import datetime
import numpy as np
from time import time
from collections import Counter
import os
import warnings

path = os.getcwd()
def warn(*args, **kwargs):
    pass

def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]

def rank_fs_result(clf_sel_result = None,tr_features = None):
    mask = clf_sel_result.get_support()
    fs_features = []
    feature_names = list(tr_features.columns.values)
    for bool, feature in zip(mask, feature_names):
        if bool:
            fs_features.append(feature)
    return(fs_features)

class dynaFS_clf:
    def __init__(self, fs_num = None ,random_state = None,cv = None, input_from_file = True):
        self.fs_num = fs_num
        self.random_state = random_state
        self.cv = cv
        self.input_from_file = input_from_file

    def fit_fs_clf(self,tr_features,tr_labels):
        warnings.warn = warn
        if(self.input_from_file):
            tr_labels = tr_labels.values.ravel()
        
        clf = clf_fs(fs_num = self.fs_num ,random_state = self.random_state,cv = self.cv)
        selectors = ['kbest_f','kbest_chi2','rfe_lr','rfe_svm','rfe_tree','rfe_rf','rfecv_svm','rfecv_tree','rfecv_rf']
                    
        loop_num = 1
        total_loop = len(selectors)
        selected_features = [] 
        for selector in selectors:
            start_time = time()
            try:
                clf_selector = getattr(clf, selector)()
                clf_sel_result = clf_selector.fit(tr_features,tr_labels)
                fs_feature = rank_fs_result(clf_sel_result,tr_features.head(1))
                print(f'\n      *DynaPipe* autoFS Module ===> Selector {selector} gets outputs: {fs_feature}')
                selected_features.extend(fs_feature)
                update_progress(loop_num/total_loop)
                loop_num += 1

            except:
                print(selector+" selector is not availible.")
                update_progress(loop_num/total_loop)
                loop_num += 1
                pass
        
        counts = Counter(selected_features)
        fs_results = sorted(selected_features, key=lambda x: -counts[x])
        fs_results = unique(fs_results)[:self.fs_num]
        print(f"The DynaPipe autoFS identify the top {self.fs_num} important features for classification are: {fs_results}.")
        return(fs_results)           

class dynaFS_reg:
    def __init__(self, fs_num = None ,random_state = None,cv = None,input_from_file = True):
        self.fs_num = fs_num
        self.random_state = random_state
        self.cv = cv
        self.input_from_file = input_from_file

    def fit_fs_reg(self,tr_features,tr_labels):
        if(self.input_from_file):
            tr_labels = tr_labels.values.ravel()

        reg = reg_fs(fs_num = self.fs_num ,random_state = self.random_state,cv = self.cv)
        selectors = ['kbest_f','rfe_svm','rfe_tree','rfe_rf','rfecv_svm','rfecv_tree','rfecv_rf']
                    
        loop_num = 1
        total_loop = len(selectors)
        selected_features = [] 
        for selector in selectors:
            start_time = time()
            try:
                reg_selector = getattr(reg, selector)()
                reg_sel_result = reg_selector.fit(tr_features,tr_labels)
                fs_feature = rank_fs_result(reg_sel_result,tr_features.head(1))
                print(f'\n      *DynaPipe* autoFS Module ===> Selector {selector} gets outputs: {fs_feature}')
                selected_features.extend(fs_feature)
                update_progress(loop_num/total_loop)
                loop_num += 1

            except:
                print(selector+" selector is not availible.")
                update_progress(loop_num/total_loop)
                loop_num += 1
                pass
        
        counts = Counter(selected_features)
        fs_results = sorted(selected_features, key=lambda x: -counts[x])
        fs_results = unique(fs_results)[:self.fs_num]
        print(f"The DynaPipe autoFS identify the top {self.fs_num} important features for regression are: {fs_results}.")
        return(fs_results)   
