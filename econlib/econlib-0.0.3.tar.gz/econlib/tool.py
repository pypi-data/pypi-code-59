"""
This module contains useful tools for data analysis.
"""

import pandas as pd


def weighted_mean(df: pd.DataFrame, weight: str or pd.Series = None, index: str or list = None) -> pd.DataFrame:
    if weight is None:
        return df.mean()
    elif type(weight) is not pd.Series:
        weight = df[weight]
    if index is None:
        return (df.multiply(weight, axis=0) / weight.sum()).sum()
    else:
        if type(index) is list and len(index) == 1:
            index = index[0]
        weight.index = df[index]
        group_weight = weight.groupby(by=index).sum()
        df = df.set_index(index)
        return df.multiply(weight, axis=0).groupby(by=index).sum().div(group_weight, axis=0)


if __name__ == "__main__":
    df = pd.DataFrame([['A', 1, 3], ['B', 3, 5], ['C', 6, 8], ['C', 4, 8]], columns=['index', "data", "weight"])
    result = weighted_mean(df, "weight", ["index"])
