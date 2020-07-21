import datetime
import os
import pandas as pd

from alge.settings import TABLES_PATH
from app.models import MLModel, ModelContingencyTable, ModelMetrics, ModelFeatureImportance, Run, Table, Sustainability
from logic import settings, data_handler, model_optimization
from logic.model_eval import get_contingency_table, get_feature_importance, get_metrics, get_roc_curve, get_pdps, \
    next_to_include, next_to_remove
from logic.models import fit, get_model_pipeline
from cumulator import base


def run_models(user_object,
               file_name,
               label,
               features,
               feature_selection_method,
               models_to_fit,
               external,
               oversampling,
               metric):

    table = Table.objects.get(name=file_name)
    data_path = os.path.join(TABLES_PATH, file_name + '.csv')
    features = (features if features else [x.column_name
                                           for x in table.tablecolumnsspec_set.filter(feature=True).iterator()
                                           if x.column_name!=label])

    problem_type = Table.objects.get(name=file_name).tablecolumnsspec_set.get(column_name=label).problem_type

    all_features_cat = [x.column_name
                        for x in table.tablecolumnsspec_set.filter(feature=True).filter(categorical=True).iterator()
                        if x.column_name!=label]
    all_features_num = [x.column_name
                        for x in table.tablecolumnsspec_set.filter(feature=True).filter(numerical=True).iterator()
                        if x.column_name!=label]

    X_train, X_test, y_train, y_test = data_handler.get_data(label, data_path, external, oversampling, problem_type)

    selected_features = model_optimization.feature_selection(X_train, y_train,
                                                             features, all_features_cat, all_features_num,
                                                             feature_selection_method)

    features_cat = [x for x in selected_features if x in all_features_cat]
    features_num = [x for x in selected_features if x in all_features_num]

    run_object = Run(**{
            'started_at': datetime.datetime.today(),
            'label': label,
            'filter': external,
            'metric': metric,
            'selection_method': feature_selection_method,
            'features': all_features_cat + all_features_num,
            'selected_features': selected_features,
            'problem_type': problem_type,
            'oversampling': oversampling,
            'n_train': len(y_train),
            'n_test': len(y_test),
            'table': table,
            'user': user_object
    })
    pipelines = [(x, get_model_pipeline(settings.ML_MODELS.get(x),
                                        features_cat, features_num)) for x in models_to_fit]

    fitted = [fit_db(run_object, n, p, X_train, y_train) for n, p in pipelines]
    metrics = [get_metrics_db(X_test, y_test, problem_type, f['pipeline'], f['model_object']) for f in fitted]
    contingency_table = [get_contingency_table_db(X_test, y_test, problem_type, f['pipeline'], f['model_object']) for f in fitted]
    run_object.last_update_at = datetime.datetime.today()
    run_object.save()
    [f['model_object'].save() for f in fitted]
    [f['sustainability'].save() for f in fitted]
    [m.save() for m in metrics]
    [c.save() for c in contingency_table]

    return run_object.run_id


def get_contingency_table_db(X, y, problem_type, pipeline, model_object):
    return ModelContingencyTable(model_object.model_id,
                                 **get_contingency_table(X, y, problem_type, pipeline))


def optimize_hyperparams_db(table_object, run_object,
                            label, problem_type,
                            external,
                            oversampling,
                            model_name, features,
                            metric):

    already_optimized = sum([m.optimized for m in run_object.mlmodel_set.filter(name=model_name)]) >= 1

    if already_optimized:
        return run_object.run_id

    data_path = os.path.join(TABLES_PATH, table_object.name + '.csv')

    X_train, X_test, y_train, y_test = data_handler.get_data(label, data_path, external, oversampling, problem_type)

    all_features_cat = [x.column_name for x in table_object.tablecolumnsspec_set.filter(feature=True).filter(categorical=True).iterator()
                        if x.column_name!=label]
    all_features_num = [x.column_name for x in table_object.tablecolumnsspec_set.filter(feature=True).filter(numerical=True).iterator()
                        if x.column_name!=label]
    features_cat = [x for x in all_features_cat if x in features]
    features_num = [x for x in all_features_num if x in features]

    started_at = datetime.datetime.today()

    fitted = model_optimization.optimize_hyperparams(X_train, y_train, model_name, features_cat, features_num, metric)

    finished_at = datetime.datetime.today()

    model = {'pipeline': fitted,
             'model_object': MLModel(**{
             'run':run_object,
             'name': model_name,
             'started_at': started_at,
             'finished_at': finished_at,
             'optimized': True,
             'hyperparameters': fitted['model'].get_params(),
         })}
    contingency_table = get_contingency_table_db(X_test, y_test, problem_type, **model)
    metrics = get_metrics_db(X_test, y_test, problem_type, **model)

    run_object.last_update_at = datetime.datetime.today()
    run_object.save()
    model['model_object'].save()
    contingency_table.save()
    metrics.save()

    return run_object.run_id


def fit_db(run,
           name,
           model_pipe,
           X_train, y_train):

    cumulator = base.Cumulator()
    started_at = datetime.datetime.today()
    cumulator.on()
    fitted = fit(X_train, y_train, model_pipe)
    cumulator.off()

    finished_at = datetime.datetime.today()
    model_object= MLModel(**{
        'run': run,
        'name': name,
        'started_at': started_at,
        'finished_at': finished_at,
        'optimized': False,
        'hyperparameters': fitted['model'].get_params(),
    })
    sustainability = Sustainability(model_object.model_id, cumulator.computation_costs())

    return {
        'pipeline': fitted,
        'model_object': model_object,
        'sustainability': sustainability
    }


def get_model_diagnostic(table_db, model_db, label, problem_type, features, filter, model_name, hyperparameters, oversampling, metric):
    data_path = os.path.join(TABLES_PATH, table_db.name + '.csv')
    X_train, X_test, y_train, y_test = data_handler.get_data(label, data_path, filter, oversampling, problem_type)
    model = settings.ML_MODELS.get(model_name)

    all_features_cat = [x.column_name for x in table_db.tablecolumnsspec_set.filter(feature=True).filter(categorical=True).iterator()
                                          if x.column_name!=label]
    all_features_num = [x.column_name for x in table_db.tablecolumnsspec_set.filter(feature=True).filter(numerical=True).iterator()
                    if x.column_name!=label]

    features_cat = [x for x in all_features_cat if x in features]
    features_num = [x for x in all_features_num if x in features]

    model_pipe = get_model_pipeline(model, features_cat, features_num, hyperparameters)
    model_pipe.fit(X_train, y_train)
    metrics = get_metrics(X_test, y_test, problem_type, model_pipe)
    roc_curve = get_roc_curve(model_pipe, X_test, y_test) if problem_type=='classification' else None
    pdps = get_pdps(model_pipe, X_train, features_cat, features_num)
    test_features_importances = get_feature_importance_db(model_db, model_pipe, features, X_test, y_test)
    feature_to_remove = test_features_importances[-1]['feature']
    include = next_to_include(X_train, y_train, X_test, y_test,
                              features_cat, features_num, model, all_features_cat, all_features_num,
                              metrics.get(metric), metric)
    remove = next_to_remove(X_train, y_train, X_test, y_test,
                            features_cat, features_num, feature_to_remove, model,
                            metrics.get(metric), metric) if problem_type=='classification' else None

    return {
        'roc_curve': roc_curve,
        'pdps': pdps,
        'test_features_importances': test_features_importances,
        'ordered_features_by_importance': list(pd.DataFrame(test_features_importances)
                                               .groupby('feature')
                                               .mean()
                                               .sort_values('importance')
                                               .index),
        'include': include,
        'remove': remove
    }


def get_metrics_db(X, y, problem_type, pipeline, model_object):
    return ModelMetrics(model_object.model_id, **get_metrics(X, y, problem_type, pipeline))


def get_feature_importance_db(model_db,
                              model_pipe,
                              features,
                              X, y,
                              n_repeats=15):

    if len(model_db.modelfeatureimportance_set.values())==0:
        importances = get_feature_importance(model_pipe, features, X, y, n_repeats)
        [ModelFeatureImportance(model=model_db, **i).save() for i in importances]

    return [{'feature': x['feature'], 'importance': x['importance']}
            for x in model_db.modelfeatureimportance_set.values()]