#!/usr/bin/env python
import time, sys
from IPython.display import clear_output
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score
from time import time
import numpy as np
import os

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



