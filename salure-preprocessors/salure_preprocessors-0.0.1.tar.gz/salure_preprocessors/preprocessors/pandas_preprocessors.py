from typing import List, Text

import sklearn
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class DropColumnsPreprocessor(BaseEstimator, TransformerMixin):

    def __init__(self, drop_columns: List[Text]):
        self.drop_columns = drop_columns

    def fit(self, X, y=None, **fit_params):
        return self

    def transform(self, X, y=None):
        return X.drop(columns=self.drop_columns)
