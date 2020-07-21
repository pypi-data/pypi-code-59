#!/usr/bin/env python
import time, sys
from IPython.display import clear_output
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from time import time
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import os
import json

'''
# For App version with logging function only:
def delete_old_log_files(directory = None, delete_flag = False, logger = None, extension_list = None,filename_list = None, log_ts = None):
    file_list = os.listdir(directory)
    if delete_flag:
        logger.info('DELETE_FLAG is set to True')
        logger.info("All previous logfiles will be deleted")

        for item in file_list:
            ext_flag = [item.startswith(i) for i in filename_list]
            if np.sum(ext_flag) and (log_ts not in item):
                os.remove(os.path.join(directory, item))
                logger.info(f"Deleted file:{item}")
    return None
'''

def update_progress(progress):
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1
    block = int(round(bar_length * progress))
    clear_output(wait = True)
    text = "Progress: [{0}] {1:.1f}%".format("#" * block + "-" * (bar_length - block),progress * 100)
    print(text)

def reset_parameters():
    try:
        json_p = os.path.join(os.path.dirname(__file__), 'reset_parameters.json')
        with open(json_p,'r') as d_file:
            para = json.load(d_file)
        json_p = os.path.join(os.path.dirname(__file__), 'parameters.json')
        w_file = open(json_p, "w",encoding='utf-8')
        w_file. truncate(0)
        json.dump(para, w_file)
        w_file.close()
        print('Done with the parameters reset.')
    except:
        print('Failed to reset the parameters.')

# **kwargs: like C=[0.1,0.2],kernel=["linear", "poly", "rbf", "sigmoid"] 
def update_parameters(mode = str(None), estimator_name = str(None), **kwargs):
    try:
        json_p = os.path.join(os.path.dirname(__file__), 'parameters.json')
        with open(json_p,'r',encoding='utf-8') as d_file:
            para = json.load(d_file)
        print(f"Previous Parameters are: {para[mode][estimator_name]}")
        para[mode][estimator_name] = kwargs
        print(f"Current Parameters are updated as: {para[mode][estimator_name]}")
        json_p = os.path.join(os.path.dirname(__file__), 'parameters.json')
        w_file = open(json_p, "w",encoding='utf-8')
        json.dump(para, w_file)
        w_file.close()
        print('Done with the parameters update.')
    except:
        print('Failed to update the parameters.')

def export_parameters():
    exp_folder = os.path.join(os.getcwd(),'exported')
    if not os.path.exists(exp_folder):
        os.makedirs(exp_folder)
    try:
        json_p = os.path.join(os.path.dirname(__file__), 'parameters.json')
        with open(json_p,"r") as d_file:
            para = json.load(d_file)
        para_pd = pd.json_normalize(para["cls"])
        para_pd.to_csv(os.path.join(exp_folder,"exported_cls_parameters.csv"),index = False)
        para_pd = pd.json_normalize(para["reg"])
        para_pd.to_csv(os.path.join(exp_folder,"exported_reg_parameters.csv"),index = False)
        print('Done with the parameters setting file export.')
    except:
        print('Failed to export the parameters file.')

