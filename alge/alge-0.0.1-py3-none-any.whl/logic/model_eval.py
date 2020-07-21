import numpy as np
import logging
logger = logging.getLogger(__name__)

from sklearn import metrics
from sklearn.inspection import partial_dependence

from logic import settings, permutation_importance
from logic.helpers import trunc
from logic.models import get_model_pipeline, fit


def get_contingency_table(X, y, problem_type, pipeline):
    """
    Return contingency of a fitted model
    :param X: features matrix
    :param y: label vector
    :param problem_type: 'regression' or 'classification'
    :param pipeline: fitted pipeline, must have .predict method
    :return: dictionary with number of rows in each case
    """
    y_hat = pipeline.predict(X)
    if problem_type == 'classification':
        return {
            'true_positive': int(sum((y == 1) & (y_hat == 1))),
            'true_negative': int(sum((y == 0) & (y_hat == 0))),
            'false_positive': int(sum((y == 0) & (y_hat == 1))),
            'false_negative': int(sum((y == 1) & (y_hat == 0)))
        }
    else:
        return {
            'true_positive': None,
            'true_negative': None,
            'false_positive': None,
            'false_negative': None
        }


def metric_evaluation(y, y_hat, metric):
    """
    Get a specific metric value
    :param y: label vector
    :param y_hat: predicted label vector
    :param metric: metric name
    :return: metric value (float)
    """
    return round(100 * settings.METRICS_MAP.get(metric)(y, y_hat), 3)


def get_metrics(X, y, problem_type, pipeline):
    """
    Get all important metrics of a model (can replace `metric_evaluation`)
    :param X: features matrix
    :param y: label vector
    :param problem_type: 'classification' or 'regression'
    :param pipeline: fitted pipeline, must have .predict method
    :return: dictionary with value of metrics important for each problem_type
    """
    y_hat = pipeline.predict(X)

    if problem_type == 'classification':

        return {
            'roc_auc': trunc(metrics.roc_auc_score(y, y_hat) * 100),
            'accuracy': trunc(metrics.accuracy_score(y, y_hat) * 100),
            'balanced_accuracy': trunc(metrics.balanced_accuracy_score(y, y_hat) * 100),
            'recall': trunc(metrics.recall_score(y, y_hat) * 100),
            'precision': trunc(metrics.precision_score(y, y_hat) * 100),
            'f1_score': trunc(metrics.f1_score(y, y_hat) * 100)
        }

    elif problem_type == 'regression':
        return {
            'mean_squared_error': trunc(metrics.mean_squared_error(y, y_hat) * 100),
            'mean_absolute_error': trunc(metrics.mean_absolute_error(y, y_hat) * 100)
        }

    else:
        return {}


def get_roc_curve(pipeline, X, y):
    """
    Get roc curve values for classification problems
    :param pipeline: fitted pipeline, must have .predict_proba method
    :param X: features matrix
    :param y: label vector
    :return: list of dictionary with false positive rate, true positive rate and threshold
    """
    fpr, tpr, thresholds = metrics.roc_curve(y, pipeline.predict_proba(X)[::, 1])

    roc_curve = []
    for i in range(len(fpr)):
        d = {'fpr': fpr[i], 'tpr': tpr[i], 'threshold': thresholds[i]}
        roc_curve.append(d)

    return roc_curve


def get_feature_importance(model_pipe,
                           features,
                           X, y,
                           n_repeats=15):
    """

    :param model_pipe: fitted pipeline, must have .predict_proba method
    :param features: list with features name
    :param X: features matrix
    :param y: label vector
    :param n_repeats: number of interactions
    :return: list of dictionaries with keys `feature:str` and `importance:list of floats`
    """
    result = permutation_importance.get_permutation_importance(
        model_pipe,
        X[features], y,
        n_repeats=n_repeats,
        random_state=123,
        n_jobs=-1)

    sorted_idx = result.importances_mean.argsort()[::-1]

    importances = dict(zip(list(X[features].columns[sorted_idx]),
                           result.importances[sorted_idx].tolist()))

    return [{'feature': k, 'importance': x} for k, v in importances.items() for x in v]


def next_to_include(X_train, y_train,
                    X_test, y_test,
                    features_cat, features_num,
                    model,
                    all_features_cat, all_features_num,
                    old_metric,
                    metric):
    """
    Run the model with more features and select the one that gives more improvement in the metric
    :param X_train: train features matrix
    :param y_train: train label vector
    :param X_test: test features matrix
    :param y_test: test label vector
    :param features_cat: list of categorical features
    :param features_num: list of numerical features
    :param model: model instance
    :param all_features_cat: list of all categorical features
    :param all_features_num: list of all numerical features
    :param old_metric: value of metric of model with all features
    :param metric: str with metric name
    :return: dictionary with the metric improvement
    """
    evaluations = []

    for f in all_features_cat:
        if f not in features_cat:
            features_with = features_cat + [f]
            pipe_with = get_model_pipeline(model, features_with, features_num)
            fitted_model_with = fit(X_train, y_train, pipe_with)
            metric_eval = metric_evaluation(y_test,
                                            fitted_model_with.predict(X_test),
                                            metric)

            evaluations.append({'feature_name': f,
                                'metric_eval': trunc(metric_eval),
                                'improvement': trunc(100 * (metric_eval / old_metric - 1)),
                                'metric': metric})

    for f in all_features_num:
        if f not in features_num:
            features_with = features_num + [f]
            pipe_with = get_model_pipeline(model, features_cat, features_with)
            fitted_model_with = fit(X_train, y_train, pipe_with)
            metric_eval = metric_evaluation(y_test,
                                            fitted_model_with.predict(X_test),
                                            metric)

            evaluations.append({'feature_name': f,
                                'metric_eval': trunc(metric_eval),
                                'improvement': trunc(100 * (metric_eval / old_metric - 1)),
                                'metric': metric})

    if evaluations:
        return evaluations[np.argmax([x['metric_eval'] for x in evaluations])]


def next_to_remove(X_train, y_train,
                   X_test, y_test,
                   features_cat, features_num,
                   feature_to_remove,
                   model,
                   old_metric,
                   metric):
    """
    Remove feature from the model and reevaluate it
    :param X_train: train features matrix
    :param y_train: train label vector
    :param X_test: test features matrix
    :param y_test: test label vector
    :param features_cat: list of categorical features
    :param features_num: list of numerical features
    :param feature_to_remove: str with feature to remove from the model
    :param model: model instance
    :param old_metric: value of metric of model with all features
    :param metric: str with metric name
    :return: dictionary with the metric improvement
    """
    if len(features_cat + features_num) == 1:
        return

    new_features_cat = [x for x in features_cat if x != feature_to_remove]
    new_features_num = [x for x in features_num if x != feature_to_remove]
    pipe_without = get_model_pipeline(model, new_features_cat, new_features_num)
    fitted_model_without = fit(X_train, y_train, pipe_without)
    metric_eval = metric_evaluation(y_test, fitted_model_without.predict(X_test), metric)

    return {'feature_name': feature_to_remove,
            'metric_eval': round(metric_eval, 3),
            'improvement': 100 * round(metric_eval / old_metric - 1, 3),
            'metric': metric}


def get_pdps(model, X_train, features_cat, features_num):
    """
    Get Partial Dependency Curves
    :param model: fitted pipeline, must have `preprocessor` key
    :param X_train: features matrix
    :param features_cat: list of categorical features
    :param features_num: list of numerical features
    :return: list of dicionaries where the keys are `feature: str` and `pdp: list[float]`
    """
    X_train = X_train[features_num + features_cat]

    ohe_categories = model['preprocessor'].named_transformers_['categorical'][
        'onehotencoder'].categories_ if features_cat else []
    new_ohe_features = [f"{col}__{val}" for col, vals in zip(features_cat, ohe_categories) for val in vals]

    result = []
    X_ok = model['preprocessor'].transform(X_train)

    if X_ok.shape[1] < len(features_num) + len(new_ohe_features): # handle weird behavior of sklearn - investigate better for lab_db_d3 (high nulls)
        return result

    for i, f in enumerate(features_num):
        pdp, levels = partial_dependence(model['model'], X_ok, [i])
        pdp = list(pdp[0])
        levels = list(levels[0])
        result.append({'feature': f,
                       'pdp': [levels, pdp]})

    i = len(features_num)

    for f in features_cat:
        ohes = [x for x in new_ohe_features if x.split('__')[0] == f]
        levels = []
        pdp = []
        start = i
        end = i + len(ohes)

        for k, j in enumerate(range(start, end)):
            levels.append(float(new_ohe_features[k].split('__')[1]))
            points = partial_dependence(model['model'],
                                        X_ok,
                                        [j])[0][-1]

            if len(points)==2:
                p, _ = points
            else:
                p = points[0]

            pdp.append(p)

        result.append({'feature': f,
                       'pdp': [levels, pdp]})
        i += len(ohes)

    return result
