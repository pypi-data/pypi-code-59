import numpy as np
import pandas as pd
from multiprocessing import Pool
from functools import partial
import functools
import pickle
import warnings

warnings.filterwarnings('ignore')

#
class WOE_ENCODER_CONTINUOUS():

    """Class that discretizes continous features with different method

    Parameters:
    -----------
    feauture_name: list[string]
        List of feature names that are prepared for discretization
    bin_num: list[int]
        List of int that represents the num of bins for each feature, and the length of bin_num is the same as feature_name
    num_thread: int
        The number of thread for finding discretizing values on each continous features, by default =-1 represent using all available cores in cpu
    gamma: float
        Regularization coefficient of finding split values for each continous features, useable only when strategy is ks,iv,chimerge,entropy
    min_sample_num: int
       The minimum number of examples in each bin
    step: int
       The length of search step, larger step will make fit process faster but will lose some precision
    sample_rate：float
       The ratio of sample rate when find best split values, has similar effect to parameter step above
    strategy : string
       The split strategy of WOE_ENCODER_CONTINUOUS,  legal choice are "ks", "iv", "chimerge", "entropy","fre","width","gini"
    -----------
    """
    def __init__(self, feauture_name, bin_num, num_thread=-1, gamma=0., min_sample_num=30, step=1, sample_rate=1.0, strategy="chimerge"):
        assert len(feauture_name) == len(bin_num), "The length of feature_name and bin_num must be the same"
        assert strategy in ["ks", "iv", "chimerge", "entropy","fre","width","gini"], "the bin strategy must be one of ks,iv,chimerge,entropy,fre,width,gini"
        self.feauture_name = feauture_name
        self.bin_num = bin_num
        self.bin_method = dict()
        self.num_thread = num_thread
        self.gamma = gamma
        self.min_sample_num = min_sample_num
        self.step = step
        self.strategy = strategy
        self.one = 0
        self.zero = 0
        self.sample_rate=sample_rate

    def _calculate_iv_woe(self, data, label_name, label0_num, label1_num, strategy):

        eta = np.log(label1_num / label0_num)
        tmp0_num = len(data[data[label_name] == 0]) if (
                len(data[data[label_name] == 0]) > 0) else 1.
        tmp1_num = len(data[data[label_name] == 1]) if (
                len(data[data[label_name] == 1]) > 0) else 1.

        if strategy == "iv":
            return np.log(tmp1_num / tmp0_num) - eta, (np.log(tmp1_num / tmp0_num) - eta) * (
                    tmp1_num / label1_num - tmp0_num / label0_num), tmp1_num, tmp0_num

        if strategy == "ks":
            return np.log(tmp1_num / tmp0_num) - eta, abs(
                tmp1_num / label1_num - tmp0_num / label0_num), tmp1_num, tmp0_num

        if strategy == "entropy":
            return np.log(tmp1_num / tmp0_num) - eta, -(tmp1_num / label1_num) * np.log(tmp1_num / label1_num) - (
                    tmp0_num / label0_num) * np.log(tmp0_num / label0_num), tmp1_num, tmp0_num

        if strategy == "gini":
            return np.log(tmp1_num / tmp0_num) - eta, np.power(tmp1_num /(tmp0_num+tmp1_num),2) + np.power(tmp0_num / (tmp0_num+tmp1_num), 2) - 1.0, tmp1_num, tmp0_num

    def _calculate_ChiMerge(self, leftdata, rightdata, label_name, label0_num, label1_num):
        eta = np.log(label1_num / label0_num)
        tmp0_left_num = len(leftdata[leftdata[label_name] == 0]) if (
                len(leftdata[leftdata[label_name] == 0]) > 0) else 1.
        tmp1_left_num = len(leftdata[leftdata[label_name] == 1]) if (
                len(leftdata[leftdata[label_name] == 1]) > 0) else 1.

        tmp0_right_num = len(rightdata[rightdata[label_name] == 0]) if (
                len(rightdata[rightdata[label_name] == 0]) > 0) else 1.
        tmp1_right_num = len(rightdata[rightdata[label_name] == 1]) if (
                len(rightdata[rightdata[label_name] == 1]) > 0) else 1.

        n = tmp0_left_num + tmp1_left_num + tmp0_right_num + tmp1_right_num

        return np.log(tmp1_left_num / tmp0_left_num) - eta, tmp1_left_num, tmp0_left_num, \
               np.log(tmp1_right_num / tmp0_right_num) - eta, tmp1_right_num, tmp0_right_num, \
               (n * (tmp0_left_num * tmp1_right_num - tmp1_left_num * tmp0_right_num) ** 2) / \
               ((tmp0_left_num + tmp0_right_num) * (tmp1_left_num + tmp1_right_num) * (
                       tmp0_left_num + tmp1_right_num) * (tmp0_right_num + tmp1_left_num))


    def _pre_find_bin(self, ans, index, bin_num, tuple_data ,not_null_data, label0_num, label1_num, feature_name, label_name):
        if index == len(tuple_data):
            return

        if bin_num == 1:
            eta = np.log(label1_num / label0_num)
            aim_data = not_null_data[not_null_data[feature_name] >= tuple_data[index][0]]
            tmp0_num = len(aim_data[aim_data[label_name] == 0]) if (
                    len(aim_data[aim_data[label_name] == 0]) > 0) else 1.
            tmp1_num = len(aim_data[aim_data[label_name] == 1]) if (
                    len(aim_data[aim_data[label_name] == 1]) > 0) else 1.
            ans.append({"begin": tuple_data[index][0], "end": tuple_data[len(tuple_data)-1][0]+0.01, "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                tmp1_num / label1_num - tmp0_num / label0_num),
                        "bin_one": tmp1_num, "bin_zero": tmp0_num})

        elif len(tuple_data[index:]) <= bin_num:
            eta = np.log(label1_num / label0_num)
            for i in range(index, len(tuple_data)):
                if i == len(tuple_data)-1:
                    aim_data = not_null_data[not_null_data[feature_name] >= tuple_data[i][0]]
                    tmp0_num = len(aim_data[aim_data[label_name] == 0]) if (
                            len(aim_data[aim_data[label_name] == 0]) > 0) else 1.
                    tmp1_num = len(aim_data[aim_data[label_name] == 1]) if (
                            len(aim_data[aim_data[label_name] == 1]) > 0) else 1.
                    ans.append({"begin": tuple_data[i][0], "end": tuple_data[i][0] + 0.01,
                                "woe": np.log(tmp1_num / tmp0_num) - eta,
                                "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                        tmp1_num / label1_num - tmp0_num / label0_num),
                                "bin_one": tmp1_num, "bin_zero": tmp0_num})
                else:
                    aim_data = not_null_data[(not_null_data[feature_name] >= tuple_data[i][0])&(not_null_data[feature_name] < tuple_data[i+1][0])]
                    tmp0_num = len(aim_data[aim_data[label_name] == 0]) if (
                            len(aim_data[aim_data[label_name] == 0]) > 0) else 1.
                    tmp1_num = len(aim_data[aim_data[label_name] == 1]) if (
                            len(aim_data[aim_data[label_name] == 1]) > 0) else 1.
                    ans.append({"begin": tuple_data[i][0], "end": tuple_data[i+1][0] + 0.01,
                                "woe": np.log(tmp1_num / tmp0_num) - eta,
                                "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                        tmp1_num / label1_num - tmp0_num / label0_num),
                                "bin_one": tmp1_num, "bin_zero": tmp0_num})

        else:
            each_num = sum(k for i,k in tuple_data[index:]) // bin_num
            now = 0
            pre_index = index
            while now < each_num:
                now += tuple_data[index][1]
                index += 1

            eta = np.log(label1_num / label0_num)
            if index == len(tuple_data):
                aim_data = not_null_data[not_null_data[feature_name] >= tuple_data[pre_index][0]]
            else:
                aim_data = not_null_data[(not_null_data[feature_name] >= tuple_data[pre_index][0]) & (not_null_data[feature_name] < tuple_data[index][0])]
            tmp0_num = len(aim_data[aim_data[label_name] == 0]) if (
                    len(aim_data[aim_data[label_name] == 0]) > 0) else 1.
            tmp1_num = len(aim_data[aim_data[label_name] == 1]) if (
                    len(aim_data[aim_data[label_name] == 1]) > 0) else 1.
            if index == len(tuple_data):
                ans.append({"begin": tuple_data[pre_index][0], "end": tuple_data[len(tuple_data) - 1][0] + 0.01,
                            "woe": np.log(tmp1_num / tmp0_num) - eta,
                            "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                    tmp1_num / label1_num - tmp0_num / label0_num),
                            "bin_one": tmp1_num, "bin_zero": tmp0_num})
            else:
                ans.append({"begin": tuple_data[pre_index][0], "end": tuple_data[index][0],
                            "woe": np.log(tmp1_num / tmp0_num) - eta,
                            "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                    tmp1_num / label1_num - tmp0_num / label0_num),
                            "bin_one": tmp1_num, "bin_zero": tmp0_num})

            self._pre_find_bin(ans, index, bin_num-1, tuple_data,not_null_data, label0_num, label1_num, feature_name, label_name)




    def _find_bin(self, X, Y, para):
        feature_name, bin_num = para[0], para[1]
        assert bin_num >= 2, "the number of bin_num must large than 2"
        label_name = Y.name
        data = pd.concat([X[feature_name], Y], axis=1)
        label0_num = len(data[data[label_name] == 0]) if (len(data[data[label_name] == 0]) > 0) else 1.
        label1_num = len(data[data[label_name] == 1]) if (len(data[data[label_name] == 1]) > 0) else 1.
        eta = np.log(label1_num / label0_num)
        mask = data[feature_name].isnull()
        ans = []

        null_data = data[mask]
        if (len(null_data) > 0):
            tmp0_num = len(null_data[null_data[label_name] == 0]) if (
                    len(null_data[null_data[label_name] == 0]) > 0) else 1.
            tmp1_num = len(null_data[null_data[label_name] == 1]) if (
                    len(null_data[null_data[label_name] == 1]) > 0) else 1.
            ans.append({"begin": "null", "end": "null", "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV": (np.log(tmp1_num / tmp0_num) - eta) * (tmp1_num / label1_num - tmp0_num / label0_num),
                        "bin_one": tmp1_num, "bin_zero": tmp0_num})
        not_null_data = data[~mask].sample(frac=self.sample_rate)


        if self.strategy == "width" and len(not_null_data)>0:
            max_ = max(not_null_data[feature_name].values)
            min_ = min(not_null_data[feature_name].values)
            interval = (max_-min_)/bin_num
            max_ += 0.01
            if interval == 0:
                tmp0_num = len(not_null_data[not_null_data[label_name] == 0]) if (
                        len(not_null_data[not_null_data[label_name] == 0]) > 0) else 1.
                tmp1_num = len(not_null_data[not_null_data[label_name] == 1]) if (
                        len(not_null_data[not_null_data[label_name] == 1]) > 0) else 1.
                ans.append({"begin": min_, "end": max_, "woe": np.log(tmp1_num / tmp0_num) - eta,
                            "IV": (np.log(tmp1_num / tmp0_num) - eta) * (tmp1_num / label1_num - tmp0_num / label0_num),
                            "bin_one": tmp1_num, "bin_zero": tmp0_num})

            else:
                now = min_
                for i in range(bin_num):
                    if i < bin_num-1:
                        aim_data = not_null_data[(not_null_data[feature_name]>=now) & (not_null_data[feature_name]<now+interval)]
                        tmp0_num = len(aim_data[aim_data[label_name] == 0]) if (
                                len(aim_data[aim_data[label_name] == 0]) > 0) else 1.
                        tmp1_num = len(aim_data[aim_data[label_name] == 1]) if (
                                len(aim_data[aim_data[label_name] == 1]) > 0) else 1.
                        ans.append({"begin": now, "end": now+interval, "woe": np.log(tmp1_num / tmp0_num) - eta,
                                    "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                                tmp1_num / label1_num - tmp0_num / label0_num),
                                    "bin_one": tmp1_num, "bin_zero": tmp0_num})
                    else:
                        aim_data = not_null_data[(not_null_data[feature_name] >= now) & (not_null_data[feature_name] < now + interval + 0.01)]
                        tmp0_num = len(aim_data[aim_data[label_name] == 0]) if (
                                len(aim_data[aim_data[label_name] == 0]) > 0) else 1.
                        tmp1_num = len(aim_data[aim_data[label_name] == 1]) if (
                                len(aim_data[aim_data[label_name] == 1]) > 0) else 1.
                        ans.append({"begin": now, "end": now + interval+0.01, "woe": np.log(tmp1_num / tmp0_num) - eta,
                                    "IV": (np.log(tmp1_num / tmp0_num) - eta) * (
                                            tmp1_num / label1_num - tmp0_num / label0_num),
                                    "bin_one": tmp1_num, "bin_zero": tmp0_num})
                    now += interval

        elif self.strategy == "fre" and len(not_null_data) > 0:
            group_data = not_null_data.groupby(not_null_data[feature_name]).size()
            tuple_data = list(zip(group_data.index, group_data.values))
            self._pre_find_bin(ans, 0, bin_num, tuple_data,not_null_data, label0_num, label1_num, feature_name, label_name)

        return feature_name, ans


    def _find_best_split(self, X, Y, para):
        feature_name, bin_num = para[0], para[1]
        assert bin_num >= 2, "the number of bin_num must large than 2"
        ans = list()
        label_name = Y.name
        data = pd.concat([X[feature_name], Y], axis=1)
        label0_num = len(data[data[label_name] == 0]) if (len(data[data[label_name] == 0]) > 0) else 1.
        label1_num = len(data[data[label_name] == 1]) if (len(data[data[label_name] == 1]) > 0) else 1.
        eta = np.log(label1_num / label0_num)
        mask = data[feature_name].isnull()

        null_data = data[mask]
        if (len(null_data) > 0):
            tmp0_num = len(null_data[null_data[label_name] == 0]) if (
                    len(null_data[null_data[label_name] == 0]) > 0) else 1.
            tmp1_num = len(null_data[null_data[label_name] == 1]) if (
                    len(null_data[null_data[label_name] == 1]) > 0) else 1.
            ans.append({"begin": "null", "end": "null", "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV": (np.log(tmp1_num / tmp0_num) - eta) * (tmp1_num / label1_num - tmp0_num / label0_num),
                        "bin_one": tmp1_num, "bin_zero": tmp0_num})

        not_null_data = data[~mask].sample(frac=self.sample_rate).sort_values([feature_name]).reset_index(drop=True)
        tmp0_num = len(not_null_data[not_null_data[label_name] == 0]) if (
                len(not_null_data[not_null_data[label_name] == 0]) > 0) else 1.
        tmp1_num = len(not_null_data[not_null_data[label_name] == 1]) if (
                len(not_null_data[not_null_data[label_name] == 1]) > 0) else 1.

        if self.strategy == "iv":
            ans.append({"begin": not_null_data[feature_name][0],
                        "end": not_null_data[feature_name][len(not_null_data) - 1] + 0.01,
                        "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV": (np.log(tmp1_num / tmp0_num) - eta) * (tmp1_num / label1_num - tmp0_num / label0_num),
                        "bin_one": tmp1_num, "bin_zero": tmp0_num})
        elif self.strategy == "ks":
            ans.append({"begin": not_null_data[feature_name][0],
                        "end": not_null_data[feature_name][len(not_null_data) - 1] + 0.01,
                        "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV": abs(tmp1_num / label1_num - tmp0_num / label0_num), "bin_one": tmp1_num,
                        "bin_zero": tmp0_num})

        elif self.strategy == "entropy":
            ans.append({"begin": not_null_data[feature_name][0],
                        "end": not_null_data[feature_name][len(not_null_data) - 1] + 0.01,
                        "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV": -(tmp1_num / label1_num) * np.log(tmp1_num / label1_num) - (
                                tmp0_num / label0_num) * np.log(tmp0_num / label0_num), "bin_one": tmp1_num,
                        "bin_zero": tmp0_num})

        elif self.strategy == "gini":
            ans.append({"begin": not_null_data[feature_name][0],
                        "end": not_null_data[feature_name][len(not_null_data) - 1] + 0.01,
                        "woe": np.log(tmp1_num / tmp0_num) - eta,
                        "IV":   np.power(tmp1_num /(tmp0_num+tmp1_num),2) + np.power(tmp0_num / (tmp0_num+tmp1_num), 2) - 1.0, "bin_one": tmp1_num,
                        "bin_zero": tmp0_num})

        else:
            ans.append({"begin": not_null_data[feature_name][0],
                        "end": not_null_data[feature_name][len(not_null_data) - 1] + 0.01,
                        "woe": np.log(tmp1_num / tmp0_num) - eta, "IV": 0, "bin_one": tmp1_num, "bin_zero": tmp0_num})

        record = dict()
        for i in range(bin_num - 1):
            for index, item in enumerate(ans):
                if self._encoding(item) in record:
                    continue
                else:
                    record[self._encoding(item)] = dict()

                if item["bin_one"] < 2 or item["bin_zero"] < 2 or item["begin"] == "null" or len(not_null_data[(not_null_data[feature_name] >= item["begin"]) & (
                        not_null_data[feature_name] < item["end"])]) < self.min_sample_num * 2:
                    record[self._encoding(item)]["state"] = "failure"
                    continue

                feature_tmp = not_null_data[
                    (not_null_data[feature_name] >= item["begin"]) & (not_null_data[feature_name] < item["end"])][
                    feature_name].values


                for j in range(self.min_sample_num, len(feature_tmp) - self.min_sample_num + 1, self.step):
                    if feature_tmp[j] == feature_tmp[j - 1]:
                        continue
                    left_data = not_null_data[
                        (not_null_data[feature_name] < feature_tmp[j]) & (not_null_data[feature_name] >= item["begin"])]
                    right_data = not_null_data[
                        (not_null_data[feature_name] >= feature_tmp[j]) & (not_null_data[feature_name] < item["end"])]

                    if self.strategy == "chimerge":
                        left_woe, left_tmp_one, left_tmp_zero, right_woe, right_tmp_one, right_tmp_zero, gain = self._calculate_ChiMerge(
                            left_data, right_data, label_name, label0_num, label1_num)

                        now_num = (len(not_null_data)) / (len(ans) + 1) * 1.0
                        tmp_gain = np.sqrt((left_tmp_one + left_tmp_zero - now_num) ** 2 + (
                                    right_tmp_one + right_tmp_zero - now_num) ** 2) * self.gamma

                        gain -= tmp_gain

                        if "gain" not in record[self._encoding(item)] or gain > record[self._encoding(item)]["gain"]:
                            record[self._encoding(item)]["state"] = "success"
                            record[self._encoding(item)]["gain"] = gain
                            record[self._encoding(item)]["original_gain"] = gain + tmp_gain
                            record[self._encoding(item)]["max_index"] = index
                            record[self._encoding(item)]["break_point"] = feature_tmp[j]
                            record[self._encoding(item)]["max_left_iv"] = 0
                            record[self._encoding(item)]["max_right_iv"] = 0
                            record[self._encoding(item)]["max_left_woe"] = left_woe
                            record[self._encoding(item)]["max_right_woe"] = right_woe
                            record[self._encoding(item)]["left_bin_one"] = left_tmp_one
                            record[self._encoding(item)]["left_bin_zero"] = left_tmp_zero
                            record[self._encoding(item)]["right_bin_one"] = right_tmp_one
                            record[self._encoding(item)]["right_bin_zero"] = right_tmp_zero


                    else:
                        left_woe, left_iv, left_tmp_one, left_tmp_zero = self._calculate_iv_woe(left_data, label_name,
                                                                                               label0_num, label1_num,
                                                                                               self.strategy)

                        right_woe, right_iv, right_tmp_one, right_tmp_zero = self._calculate_iv_woe(right_data,
                                                                                                   label_name,
                                                                                                   label0_num,
                                                                                                   label1_num,
                                                                                                   self.strategy)
                        gain = left_iv * len(left_data) / len(not_null_data) + right_iv * len(right_data) / len(
                            not_null_data) - item["IV"] * len(feature_tmp) / len(not_null_data)

                        now_num = (len(not_null_data)) / (len(ans) + 1) * 1.0

                        tmp_gain = np.sqrt((left_tmp_one+left_tmp_zero-now_num)**2 + (right_tmp_one+right_tmp_zero-now_num)**2) * self.gamma

                        gain -= tmp_gain
                        if "gain" not in record[self._encoding(item)] or gain > record[self._encoding(item)]["gain"]:
                            record[self._encoding(item)]["state"] = "success"
                            record[self._encoding(item)]["gain"] = gain
                            record[self._encoding(item)]["original_gain"] = gain + tmp_gain
                            record[self._encoding(item)]["max_index"] = index
                            record[self._encoding(item)]["break_point"] = feature_tmp[j]
                            record[self._encoding(item)]["max_left_iv"] = left_iv
                            record[self._encoding(item)]["max_right_iv"] = right_iv
                            record[self._encoding(item)]["max_left_woe"] = left_woe
                            record[self._encoding(item)]["max_right_woe"] = right_woe
                            record[self._encoding(item)]["left_bin_one"] = left_tmp_one
                            record[self._encoding(item)]["left_bin_zero"] = left_tmp_zero
                            record[self._encoding(item)]["right_bin_one"] = right_tmp_one
                            record[self._encoding(item)]["right_bin_zero"] = right_tmp_zero

                if "state" not in record[self._encoding(item)]:
                    record[self._encoding(item)]["state"] = "failure"

            now_index = -1
            for index, item in enumerate(ans):
                if record[self._encoding(item)]["state"] == "success":
                    now_index = index
                    break

            if now_index != -1:
                max_index = now_index
                for j in range(now_index+1,len(ans)):
                    if record[self._encoding(ans[j])]["state"] == "success":
                        now_num = len(not_null_data) / (len(ans) + 1) * 1.0
                        left_j_total = record[self._encoding(ans[j])]["left_bin_zero"] + record[self._encoding(ans[j])]["left_bin_one"]
                        right_j_total = record[self._encoding(ans[j])]["right_bin_zero"] + record[self._encoding(ans[j])]["right_bin_one"]
                        total_j = left_j_total + right_j_total
                        left_max_total =record[self._encoding(ans[max_index])]["left_bin_zero"] + record[self._encoding(ans[max_index])]["left_bin_one"]
                        right_max_total =record[self._encoding(ans[max_index])]["left_bin_zero"] + record[self._encoding(ans[max_index])]["left_bin_one"]
                        total_max=left_max_total+right_max_total
                        if record[self._encoding(ans[j])]["original_gain"] - self.gamma * np.sqrt((total_max-now_num)**2 + (left_j_total-now_num)**2 + (right_j_total-now_num)**2) > record[self._encoding(ans[max_index])]["original_gain"] - self.gamma * np.sqrt((total_j-now_num)**2 +(left_max_total-now_num)**2 +(right_max_total-now_num)**2):
                            max_index = j


                item_tmp = ans[max_index]
                del (ans[max_index])
                ans.append({"begin": item_tmp["begin"], "end": record[self._encoding(item_tmp)]["break_point"],
                            "woe": record[self._encoding(item_tmp)]["max_left_woe"],
                            "IV": record[self._encoding(item_tmp)]["max_left_iv"],
                            "bin_one": record[self._encoding(item_tmp)]["left_bin_one"],
                            "bin_zero": record[self._encoding(item_tmp)]["left_bin_zero"]})


                ans.append({"begin": record[self._encoding(item_tmp)]["break_point"], "end": item_tmp["end"],
                            "woe": record[self._encoding(item_tmp)]["max_right_woe"],
                            "IV": record[self._encoding(item_tmp)]["max_right_iv"],
                            "bin_one": record[self._encoding(item_tmp)]["right_bin_one"],
                            "bin_zero": record[self._encoding(item_tmp)]["right_bin_zero"]})
            else:
                break
        return feature_name, ans

    def _udf_sort(self, x, y):
        if x["begin"] == "null":
            return -1
        elif y["begin"] == "null":
            return 1
        elif x["begin"] > y["begin"]:
            return 1
        else:
            return -1

    def _encoding(self, item):
        return str(round(item["begin"], 5)) + "#" + str(round(item["end"], 5))



    def fit(self, Z, Y):
        '''
           Z: DataFrame
              DataFrame represents the feature input data, that does not contain label column
           Y: Series
              Series represets the label data,whose values can only be 0/1
           '''

        if not isinstance(Z, pd.DataFrame):
            raise TypeError("The input X data must be type of pd.DataFrame")

        if not isinstance(Y, pd.Series):
            raise TypeError("The input Y data must be type of pd.core.series.Series")

        X = Z[self.feauture_name]

        self.one = Y.sum()
        self.zero = Y.count() - self.one



        if self.strategy in ["ks", "iv", "chimerge", "entropy","gini"]:
            func = partial(self._find_best_split, X, Y)
        else:
            func = partial(self._find_bin, X, Y)

        if self.num_thread == -1:
            pool = Pool()
            rsts = pool.map(func, zip(list(X.columns), list(self.bin_num)))
            pool.close()
            pool.join()

        else:
            pool = Pool(self.num_thread)
            rsts = pool.map(func, zip(list(X.columns), list(self.bin_num)))
            pool.close()
            pool.join()

        for rst in rsts:
            if len(rst[1]) <= 0:
                print("Feature {} is not bucketed successfully".format(rst[0]))

            else:
                self.bin_method[rst[0]] = sorted(rst[1], key=functools.cmp_to_key(self._udf_sort))

    def export_model_csv(self, path):
        with open(path, "w") as w:
            w.write("featureName,valueFrom,valueTo,WOE,bin_one,bin_zero,total_one,total_zero" + "\n")
            for feature in self.bin_method.keys():
                for item in self.bin_method[feature]:
                    w.write(feature + "," + str(item["begin"]) + "," + str(item["end"]) + "," + str(
                        item["woe"]) + "," + str(item["bin_one"]) + "," + str(item["bin_zero"]) + "\n")

    def export_model(self, path):
        fw = open(path, "wb")
        pickle.dump(self.bin_method, fw)

    def import_model(self, path):
        fr = open(path, "rb")
        self.bin_method = pickle.load(fr)

    def _find_woe_value(self, item, X):

        tmp_bin_method = self.bin_method[item]
        try:
            if np.isnan(X):
                return tmp_bin_method[0]["woe"]
            else:
                index = 0
                for k in tmp_bin_method:
                    if k["begin"] == "null":
                        continue

                    elif k["begin"] != "null" and index == 0:
                        index = 1
                        if X < k["begin"]:
                            return k["woe"]
                        elif X >= k["begin"] and X < k["end"]:
                            return k["woe"]
                        else:
                            pass

                    elif k["begin"] != "null" and index == 1:
                        if X >= k["begin"] and X < k["end"]:
                            return k["woe"]
                        else:
                            pass
                    else:
                        pass
                return tmp_bin_method[len(tmp_bin_method) - 1]["woe"]
        except:
            print(tmp_bin_method)

    def transform(self, X):
        if not isinstance(X, pd.DataFrame):
            raise TypeError("The input X data must be type of pd.DataFrame")
        for item in list(X.columns):
            if item in self.bin_method:
                func = partial(self._find_woe_value, item)
                X[item + "Trusfort"] = X[item].map(func)
                X = X.drop(item, axis=1).rename(columns={item + "Trusfort": item})

        return X


