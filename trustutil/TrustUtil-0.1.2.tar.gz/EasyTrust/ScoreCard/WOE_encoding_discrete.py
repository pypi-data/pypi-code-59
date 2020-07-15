import numpy as np
import pandas as pd
from multiprocessing import Pool
from functools import partial
import functools
import warnings
import pickle
warnings.filterwarnings('ignore')

class WOE_ENCODER_DISCRETE():
    def __init__(self, feature_name, num_thread = -1):
        self.bin_method = dict()
        self.num_thread = num_thread
        self.feature_name = feature_name

    def _udf_sort(self,x,y):
        if x["value"] == "null":
            return -1
        elif y["value"] == "null":
            return 1
        elif x["value"] > y["value"]:
            return 1
        else:
            return -1

    def export_model(self, path):
        fw = open(path, "wb")
        pickle.dump(self.bin_method, fw)

    def import_model(self, path):
        fr = open(path, "rb")
        self.bin_method = pickle.load(fr)


    def _find_best_split(self,X,Y,feature_name):
        ans = list()
        label_name = list(Y.to_frame().columns)[0]
        data = pd.concat([X[feature_name],Y],axis=1)
        label0_num = len(data[data[label_name]==0]) if(len(data[data[label_name]==0]) > 0) else 1.
        label1_num = len(data[data[label_name] == 1]) if (len(data[data[label_name] == 1]) > 0) else 1.
        eta = np.log(label1_num/label0_num)
        mask = data[feature_name].isnull()

        null_data = data[mask]
        if len(null_data) > 0:
            tmp0_num = len(null_data[null_data[label_name]==0]) if(len(null_data[null_data[label_name]==0]) > 0) else 1.
            tmp1_num = len(null_data[null_data[label_name]==1]) if(len(null_data[null_data[label_name]==1]) > 0) else 1.
            ans.append({"value": "null", "woe": np.log(tmp1_num/tmp0_num)-eta,  "IV": (tmp1_num / label1_num) * np.log(tmp1_num / label1_num) + (
                                tmp0_num / label0_num) * np.log(tmp0_num / label0_num), "bin_one": tmp1_num,
                        "bin_zero": tmp0_num})

        not_null_data = data[~mask].reset_index(drop=True)
        unique_not_null_data = not_null_data[feature_name].unique()
        for item in unique_not_null_data:
            item_data = not_null_data[not_null_data[feature_name] == item]

            tmp0_num = len(item_data[item_data[label_name] == 0]) if (
                        len(item_data[item_data[label_name] == 0]) > 0) else 1.
            tmp1_num = len(item_data[item_data[label_name] == 1]) if (
                        len(item_data[item_data[label_name] == 1]) > 0) else 1.
            ans.append({"value": item, "woe": np.log(tmp1_num / tmp0_num) - eta, "IV": (tmp1_num / label1_num) * np.log(tmp1_num / label1_num) + (
                                tmp0_num / label0_num) * np.log(tmp0_num / label0_num), "bin_one": tmp1_num,
                        "bin_zero": tmp0_num})

        return feature_name, ans

    def export_model_csv(self, path):
        with open(path, "w") as w:
            w.write("featureName,valueFrom,valueTo,WOE,bin_one,bin_zero,total_one,total_zero" + "\n")
            for feature in self.bin_method.keys():
                for item in self.bin_method[feature]:
                    w.write(feature + "," + str(item["value"]) + "," + str(item["value"]) + "," + str(
                        item["woe"]) + "," + str(item["bin_one"]) + "," + str(item["bin_zero"]) + "\n")

    def fit(self, Z, Y):
        if not isinstance(Z, pd.DataFrame):
            raise TypeError("The input X data must be type of pd.DataFrame")

        if not isinstance(Y, pd.Series):
            raise TypeError("The input Y data must be type of pd.core.series.Series")

        X = Z[self.feature_name]
        func = partial(self._find_best_split, X, Y)
        if self.num_thread == -1:
            pool = Pool()
            rsts = pool.map(func, list(X.columns))
            pool.close()
            pool.join()

        else:
            pool = Pool(self.num_thread)
            rsts = pool.map(func, list(X.columns))
            pool.close()
            pool.join()

        for rst in rsts:
            if len(rst[1]) <= 0:
                print("Feature {} is not bucketed successfully".format(rst[0]))
            else:
                self.bin_method[rst[0]] = sorted(rst[1], key=functools.cmp_to_key(self._udf_sort))


    def _find_woe_value(self,item,X):

        tmp_bin_method = self.bin_method[item]
        try:
            if np.isnan(X):
                return tmp_bin_method[0]["woe"]
            else:
                for k in tmp_bin_method:
                    if k["value"] == "null":
                        continue

                    elif k["value"] != "null" and k["value"] == X:
                        return k["woe"]

                return tmp_bin_method[len(tmp_bin_method)-1]["woe"]
        except:
            print(X)
            print(tmp_bin_method)


    def transform(self,X):
        if not isinstance(X, pd.DataFrame):
            raise TypeError("The input X data must be type of pd.DataFrame")
        for item in list(X.columns):
            if item in self.bin_method:
                func = partial(self._find_woe_value,item)
                X[item+"Trusfort"]= X[item].map(func)
                X = X.drop(item,axis=1).rename(columns={item+"Trusfort":item})

        return X









