"""
description
"""

# imports
from sklearn.datasets import make_classification
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import weles as ws


def dataset():
    return make_classification(random_state=1410)


def test_evaluator():
    metrics = {"accuracy": accuracy_score}
    clfs = {"GNB": GaussianNB(),
            "KNC": KNeighborsClassifier(),
            "DTC": DecisionTreeClassifier()}

    ev = ws.evaluation.Evaluator(datasets={"dup": dataset()})
    ev.process(clfs=clfs)
    ev.score(metrics=metrics)
