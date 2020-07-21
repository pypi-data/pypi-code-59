import numpy as np
import plotly.graph_objs as go
from app.models import Run, MLModel, Table
from logic import settings


def get_forms_context():
    tables = [[x.name, x, x.n_rows] for x in Table.objects.filter(active=True).iterator()]

    all = {}
    for name, t, n in tables:
        all[name] = {}
        all[name]['labels'] = [[x.column_name, x.problem_type, int(x.prop_null * 100)]
                               for x in t.tablecolumnsspec_set.filter(label=True).iterator()]
        all[name]['features'] = [[x.column_name, x.cluster, int(x.prop_null * 100)]
                                 for x in t.tablecolumnsspec_set.filter(feature=True).iterator()]

    return {
        'externals': settings.FILTER_DATA.keys(),
        'models': settings.ML_MODELS_PROBLEM_TYPE_MAP,
        'metrics': settings.METRIC_PROBLEM_TYPE_MAP,
        'fitted_models': [],
        'files': tables,
        'specs': all
    }


def get_forms_context_benchmark():
    tables = [[x.name, x, x.n_rows] for x in Table.objects.iterator()]

    all = {}
    for name, t, n in tables:
        all[name] = {}
        all[name]['labels'] = [[x.column_name, x.problem_type, int(x.prop_null * 100)]
                               for x in t.tablecolumnsspec_set.filter(label=True).iterator()]
    return {
        'files': tables,
        'specs': all
    }


def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item


def get_best_metrics_benchmark(models, problem_type):
    # TODO: 1% function (Tristan)
    split_by_model = {}
    for m in models:
        if m.name in split_by_model:
            split_by_model[m.name] = split_by_model[m.name] + [m]
        else:
            split_by_model[m.name] = [m]

    best_models = {}
    if problem_type == 'classification':
        metric_name = 'accuracy'
        for name, models in split_by_model.items():
            best_index = np.argmax([getattr(m.modelmetrics, metric_name) for m in models])
            best_model = models[best_index]
            best_run = Run.objects.get(run_id=best_model.run_id)
            best_metrics = {'carbon_footprint': best_model.sustainability.carbon_footprint,
                            metric_name: best_model.modelmetrics.accuracy,
                            'model_id': best_model.model_id,
                            'oversampling': best_run.oversampling,
                            'selected_features': best_run.selected_features,
                            'feature_selection_method': best_run.selection_method}
            best_models[best_model.name] = best_metrics
    else:
        metric_name = 'mean_squared_error'
        for name, models in split_by_model.items():
            best_index = np.argmin([getattr(m.modelmetrics, metric_name) for m in models])
            best_model = models[best_index]
            best_run = Run.objects.get(run_id=best_model.run_id)
            best_metrics = {'carbon_footprint': best_model.sustainability.carbon_footprint,
                            metric_name: best_model.modelmetrics.mean_squared_error,
                            'model_id': best_model.model_id,
                            'oversampling': best_run.oversampling,
                            'selected_features': best_run.selected_features,
                            'feature_selection_method': best_run.selection_method}
            best_models[best_model.name] = best_metrics

    return best_models


def get_benchmark_plot(data, problem_type):
    if problem_type == 'classification':
        metric_name = 'accuracy'
    else:
        metric_name = 'mean_squared_error'

    x1 = [v[metric_name] for k, v in data.items()]
    x2 = [v['carbon_footprint'] for k, v in data.items()]

    y = [k.split(' (')[0] for k, v in data.items()]
    feature_selection_method = [v['feature_selection_method'] for k, v in data.items()]
    model_id = [v['model_id'] for k, v in data.items()]
    oversampling = [v['oversampling'] for k, v in data.items()]

    for i in range(0, len(y)):
        if oversampling[i] == True:
            y[i] = y[i] + ' with oversampling'
        if feature_selection_method[i] == 'lasso':
            y[i] = y[i] + ', lasso'
        if feature_selection_method[i] == 'boruta':
            y[i] = y[i] + ', boruta'
        y[i] = y[i] + ', ' + str(model_id[i])


    metric_values = go.Bar(x=x1, y=y, orientation='h', name=metric_name, marker=dict(color='rgb(66,133,250)'),
                           text=x1, textposition='auto')
    carbon_footprint = go.Bar(x=x2, y=y, orientation='h', name='carbon footprint', marker=dict(color='rgb(220,67,55)'),
                              text=x2, textposition='auto', xaxis='x2')
    trace1 = go.Bar(x=np.zeros(np.size(x1)), y=y, orientation='h')
    trace2 = go.Bar(x=np.zeros(np.size(x1)), y=y, orientation='h', xaxis='x2')
    data = go.Data([carbon_footprint, trace2, trace1, metric_values, ])
    layout = go.Layout(xaxis=dict(title=metric_name, showgrid=False),
                       xaxis2=dict(title='carbon footprint in gCO2eq', side='top', overlaying='x', showgrid=False),
                       showlegend=False)
    return go.Figure(data=data, layout=layout).to_html(full_html=False, default_height=500, default_width=1000)

