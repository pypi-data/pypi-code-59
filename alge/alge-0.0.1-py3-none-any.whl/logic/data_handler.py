from itertools import groupby
from operator import itemgetter

from logic import settings

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def feature_drop(data):
    """Drops all medical irrelevant features"""
    # List of all features
    header_list = list(data.columns.values)

    # Threshold
    t = 0.005

    # List of features to drop based on clinical knowledge
    features_droped = ([x for x in header_list if (x.startswith('admin') or x.startswith('date_admit') 
                        or x.startswith('date_d0') or x.startswith('date_bcx') or x=='date_fever_last' or x=='date_fever_first'
                        or x=='date_month_d0' or x=='date_season_d0' or x=='dem_agecat' or x=='dem_aged'
                        or x=='dem_agem' or x=='dem_agey' or x=='dem_dob' 
                        or (x.startswith('sympcc_') and (x.endswith('3') or x.endswith('7')))
                        or x.startswith('ngs_') or x.startswith('dx_') or x.startswith('dxfinal_')
                        or x=='hist_vac_pcv3_date' or x.startswith('misc_') or x.startswith('out_')
                        or x=='signv_hr1_d1' or x=='signv_hr1_d3' or x=='signv_hr1_d7' or x.startswith('signv_hr2_') 
                        or x.startswith('signv_hr50_') or x.startswith('signv_hr75_') or x.startswith('signv_hr90_')
                        or x.startswith('signv_hr97_') or (x.startswith('signv_') and x.endswith('_d3'))
                        or (x.startswith('signv_') and x.endswith('_d7')) or x=='signv_rr50_d0' or x=='signv_rr75_d0'
                        or x.startswith('signv_rr9') or (x.startswith('symp_') and x.endswith('_d3'))
                        or x.startswith('ttt_') or x=='sign_danger_descr_d1' or x=='sign_abscess'
                        or (x.startswith('symp_') and x.endswith('_d0') and x!='symp_cns_sev_d0' 
                        and x!='symp_stools24h_d0')
                        or (x.startswith('sign_') and x.endswith('_d0') and x!='sign_dehyd_eye_d0' 
                        and x!='sign_restless_d0') 
                        or (x.startswith('sign_') and x.endswith('_d3')) or x=='sympcc_01' or x=='dxscore_strept'
                        or x.startswith('lab_ngs') or x=='lab_malaria_date' or x=='lab_malaria_hsrdt_pcr_d0' 
                        or x=='dxlab_malaria_pcr' or x.startswith('lab_malaria_pcr') or x=='lab_malaria_rdt_pcr_d0' 
                        or x=='lab_other_d3' or x=='lab_other_d7' or x=='lab_pglucose_d7' or x=='lab_typhoid_bcx_d0' 
                        or x=='lab_typhoid_bcx_d1_7' or x.startswith('lab_typhoid_rdt_d') 
                        or (x.startswith('lab_') and x.endswith('_d7')) or x=='lab_urine_type_d3' 
                        or x.startswith('signv_weight') or x=='signv_wazlow_d0' or x.startswith('signv_wfa3z')
                        or x=='rad_cxr01' or x=='merge_malaria') or x=='d' or x=='dxlab_typhoid_d0' 
                        or x=='sympcc_convuls2' or x=='dxlab_typhoid_d3' or x=='sign_convuls_statusep' 
                        or x=='sign_convulscompelx' or x=='sign_grunt'])

    # Drop medical irrelevant features 
    clean_data = data.drop(labels=features_droped, axis=1, level=None, inplace=False, errors='raise')
    object_drop = list(clean_data.select_dtypes(include=object))
    clean_data.drop(labels=object_drop, axis=1, level=None, inplace=True, errors='raise')
    # Drop features with single value
    clean_data = clean_data[clean_data.apply(pd.Series.value_counts).dropna(thresh=2, axis=1).columns]
    # Drop features with non-missing values < t*len(clean_data_no_single)
    clean_data = clean_data.loc[:, pd.notnull(clean_data).sum()>len(clean_data)*t]
    return clean_data

def filter_data(data, filter_name):
    if filter_name:
        function_to_filter = settings.FILTER_DATA.get(filter_name).get('function')
        column_to_filter = settings.FILTER_DATA.get(filter_name).get('column')

        return data[data[column_to_filter].apply(function_to_filter)]

    else:
        return data

def get_oversampling(X, y):
    n_0 = len(y[y==0])
    n_1 = len(y[y==1])
    n_resample = n_0 - n_1

    if n_1 / n_0 > 0.5:
        return X, y

    positions_1 = y[y==1].index
    added_positions = list(np.random.choice(positions_1, n_resample))

    X_added = pd.concat([X, X.loc[added_positions]], axis=0)
    y_added = pd.concat([y, y[added_positions]], axis=0)

    return X_added, y_added



def get_data(label, path, filter_name, oversampling, problem_type, seed=43, test_size=.3):
    data = pd.read_csv(path, low_memory=False)

    data = data[pd.notnull(data[label])]
    data = filter_data(data, filter_name)
    X = data
    y = data[label]

    if problem_type=='classification':
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        stratify=y,
                                                        test_size=test_size,
                                                        random_state=seed)
    else:
        X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                            test_size=test_size,
                                                            random_state=seed)

    if oversampling:
        X_train, y_train = get_oversampling(X_train, y_train)

    return (X_train, X_test, y_train.apply(int), y_test.apply(int))


def get_data_stats(y_train, y_test):
    return {
        'n_test': len(y_test),
        'n_train': len(y_train)
    }


def multi_level(variables):
    clusters = [(v, k) for k, v in variables]
    grouped_by_cluster = [(k, list(list(zip(*g))[1])) for k, g in groupby(clusters, itemgetter(0))]

    return dict(grouped_by_cluster)

