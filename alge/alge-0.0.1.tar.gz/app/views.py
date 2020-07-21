import os
import pandas as pd
from ast import literal_eval

from alge.settings import TABLES_PATH
from app import table_uploader
from app.logic_to_db import get_model_diagnostic, run_models, optimize_hyperparams_db
from app.models import Run, MLModel, Table
from app.helpers import get_forms_context, get_forms_context_benchmark, flatten, get_best_metrics_benchmark, get_benchmark_plot
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from logic import settings


def home(request):
    return redirect('/new_model')


def about_us(request):
    context = None
    return render(request, 'about_us.html', context=context)


def healthcheck(request):
    return HttpResponse(status=200)


@login_required(login_url='/login')
def change_password(request):
    if request.method=='POST':
         form = PasswordChangeForm(data=request.POST, user=request.user)
         if form.is_valid():
             form.save()
             update_session_auth_hash(request, form.user)
             return redirect('/new_model')
         else:
             return redirect('/change_password')
    else:
         context = {'form': PasswordChangeForm(user=request.user)}
         return render(request, 'user/change_password.html', context)

@login_required(login_url='/login')
def account(request):
    return render(request, 'user/account.html')


@login_required(login_url='/login')
def new_model(request):
    if request.method == 'GET':
        context = {'forms': get_forms_context()}
        return render(request, 'models/new_model.html', context=context)

    else:
        return HttpResponseRedirect('/running')


@login_required(login_url='/login')
def rerun_selected_features(request, old_run_id):
    old_run = Run.objects.get(run_id=old_run_id)
    label = old_run.label
    features = request.POST.getlist('selected-features')
    models_to_fit = [m.name for m in old_run.mlmodel_set.iterator()]
    external = old_run.filter
    metric = old_run.metric
    file_name = old_run.table.name
    oversampling = old_run.oversampling
    feature_selection_method = None

    try:
        run_id = run_models(request.user,
                            file_name,
                            label,
                            features,
                            feature_selection_method,
                            models_to_fit,
                            external,
                            oversampling,
                            metric)
        return redirect('/run/{}'.format(run_id))

    except Exception as e:
        return JsonResponse({'error': str(e)})


@login_required(login_url='/login')
def hyperparameter_optimization(request, model_id):
    model = MLModel.objects.get(model_id=model_id)
    run = model.run
    table = model.run.table
    label = run.label
    problem_type = table.tablecolumnsspec_set.get(column_name=label).problem_type
    features = literal_eval(run.selected_features)
    external = run.filter
    metric = run.metric
    oversampling = run.oversampling
    model_name = model.name

    try:
        run_id = optimize_hyperparams_db(table,
                                         run,
                                         label,
                                         problem_type,
                                         external,
                                         oversampling,
                                         model_name,
                                         features,
                                         metric)
        return redirect('/run/{}'.format(run_id))

    except Exception as e:
        return JsonResponse({'error': str(e)})


@login_required(login_url='/login')
def running(request):
    file_name = request.POST.get('file')
    label = request.POST.get('label')
    problem_type = Table.objects.get(name=file_name).tablecolumnsspec_set.get(column_name=label).problem_type
    features = request.POST.getlist('features')
    models_to_fit = request.POST.getlist('models')
    models_to_fit = models_to_fit if models_to_fit else settings.ML_MODELS_PROBLEM_TYPE_MAP[problem_type]
    external = request.POST.get('external')
    metric = request.POST.get('metric')
    metric = metric if metric else settings.DEFAULT_METRIC[problem_type]
    oversampling = True if request.POST.get('oversampling') else False
    feature_selection_method = request.POST.get('featureselection')

    try:
        run_id = run_models(request.user,
                            file_name,
                            label,
                            features,
                            feature_selection_method,
                            models_to_fit,
                            external,
                            oversampling,
                            metric)
        return redirect('run/{}'.format(run_id))
    except Exception as e:
        return JsonResponse({'error': str(e)})


@login_required(login_url='/login')
def run(request, run_id):
    try:
        models = [{'model': m,
                   'metrics': m.modelmetrics,
                   'sustainability': m.sustainability}
                  for m in Run.objects.get(run_id=run_id).mlmodel_set.order_by('name').iterator()]
        context = {
            'run': Run.objects.get(run_id=run_id),
            'problem_type': Run.objects.get(run_id=run_id).problem_type,
            'models': models,
        }

        return render(request, 'runs/run.html', context)

    except Exception as e:
        return JsonResponse({'error': str(e)})


@login_required(login_url='/login')
def model(request, model_id):
    try:
        model = MLModel.objects.get(model_id=model_id)
        hyperparameters = literal_eval(model.hyperparameters)
        features = literal_eval(model.run.selected_features)
        filter = model.run.filter
        label = model.run.label
        oversampling = model.run.oversampling

        context = get_model_diagnostic(model.run.table,
                                       model,
                                       label,
                                       model.run.problem_type,
                                       features,
                                       filter,
                                       model.name,
                                       hyperparameters,
                                       oversampling,
                                       model.run.metric)

        context['contingency'] = model.modelcontingencytable
        context['metrics'] = model.modelmetrics
        context['features'] = features
        context['model'] = model
        context['problem_type'] = model.run.problem_type
        # context['allowed_to_optimize'] = True if (not model.optimized) and (settings.HYPERPARAMETER_OPTIMIZATION.get(model.name)) else False
        context['allowed_to_optimize'] = False

        return render(request, 'models/model.html', context)

    except Exception as e:
        return JsonResponse({'error': str(e)})


@login_required(login_url='/login')
def table(request, table_id):
    this_table = Table.objects.get(name=table_id)
    is_owner = request.user.id == this_table.user.id

    if request.method=='GET':
        context = {'table_specs': this_table.tablecolumnsspec_set.iterator(),
                   'is_owner': is_owner,
                   'table': this_table}
    else:
        if request.POST.get('refresh-table'):
            file = request.FILES['table']
            file_name = file.name
            name = file_name.split('.')[0]

            data = file.file.readlines()
            path_file = os.path.join(TABLES_PATH, file_name)

            rows = []
            for row in data:
                row = row.decode('utf-8')[:-1].split(',')
                row = [x.replace('\r', '').replace('\n', '') for x in row]
                rows.append(row)

            df = pd.DataFrame(rows[1:], columns=rows[0])
            df.to_csv(path_file, index=False)

            table_uploader.refresh_data(name)

        elif request.POST.get('unactivate-table'):
            this_table.active = False
            this_table.save()
        elif request.POST.get('change-label'):
            column_name = request.POST.get('change-label')
            this_column = this_table.tablecolumnsspec_set.get(column_name=column_name)
            this_column.label = not this_column.label
            this_column.save()
        elif request.POST.get('change-feature'):
            column_name = request.POST.get('change-feature')
            this_column = this_table.tablecolumnsspec_set.get(column_name=column_name)
            this_column.feature = not this_column.feature
            this_column.save()
        elif request.POST.get('change-type'):
            column_name = request.POST.get('change-type')
            this_column = this_table.tablecolumnsspec_set.get(column_name=column_name)
            this_column.categorical = not this_column.categorical
            this_column.numerical = not this_column.numerical
            this_column.problem_type = 'regression' if this_column.problem_type=='classification' else 'classification'
            this_column.save()
        else:
            this_table.active = True
            this_table.save()

        context = {'table_specs': this_table.tablecolumnsspec_set.iterator(),
                   'is_owner': is_owner,
                   'table': Table.objects.get(name=table_id)}

    return render(request, 'file_tables/file_table.html', context)


@login_required(login_url='/login')
def runs(request):
    context = {'runs': Run.objects.iterator()}

    return render(request, 'runs/runs.html', context)


@login_required(login_url='/login')
def models(request):
    context = {'models': MLModel.objects.order_by('name').iterator()}

    return render(request, 'models/models.html', context)


@login_required(login_url='/login')
def tables(request):
    context = {'file_tables': Table.objects.iterator()}

    return render(request, 'file_tables/file_tables.html', context)


@login_required(login_url='/login')
def upload_table(request):
    if request.method == 'GET':
        context = None
        return render(request, 'file_tables/file_upload.html', context)
    else:
        file = request.FILES['table']
        file_name = file.name
        name = file_name.split('.')[0]

        if len(Table.objects.filter(name=name)) > 0:
            context = {'message': 'Fail: there is already a table with the same name! Please, change its name and upload it again'}
            return render(request, 'file_tables/file_upload.html', context)

        data = file.file.readlines()
        path_file = os.path.join(TABLES_PATH, file_name)

        rows = []
        for row in data:
            row = row.decode('utf-8')[:-1].split(',')
            row = [x.replace('\r', '').replace('\n', '') for x in row]
            rows.append(row)

        df = pd.DataFrame(rows[1:], columns=rows[0])
        df.to_csv(path_file, index=False)

        table_name = table_uploader.handler(request.user, name)

        return redirect('table/{}'.format(table_name))


@login_required(login_url='/login')
def benchmark(request):
    if request.method == 'GET':
        context = {'forms': get_forms_context_benchmark(),
                   'graph': None}
        return render(request, 'models/benchmark.html', context=context)
    else:
        file_name = request.POST.get('file')
        label = request.POST.get('label')

        table = Table.objects.get(name=file_name)
        problem_type = table.tablecolumnsspec_set.get(column_name=label).problem_type
        run_ids = [x['run_id'] for x in table.run_set.values_list().filter(label=label).values()]
        all_models = [MLModel.objects.filter(run_id=run_id) for run_id in run_ids]
        all_models = list(flatten(all_models))
        best_models = get_best_metrics_benchmark(all_models, problem_type)

        context = {'forms': get_forms_context_benchmark(),
                   'graph': get_benchmark_plot(best_models, problem_type)}
        return render(request, 'models/benchmark.html', context=context)
