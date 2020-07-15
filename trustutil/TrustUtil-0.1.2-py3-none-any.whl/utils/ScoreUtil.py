import pandas as pd
import numpy as np


def is_continuous_feautre(X, feature_name, threshold=10):
    if not isinstance(X, pd.DataFrame):
        raise TypeError("The input X data must be type of pd.DataFrame")
    if not (isinstance(feature_name, np.ndarray) or isinstance(feature_name, list)):
        raise TypeError("The input feature must be type of np.ndarray")

    ans = list()
    for item in feature_name:
        if item in X.columns:
            if X[item].nunique() >= threshold:
                ans.append(1)
            else:
                ans.append(0)
        else:
            ans.append(0)

    return np.array(ans, dtype=np.bool)