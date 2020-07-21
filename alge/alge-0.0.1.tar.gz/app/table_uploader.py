import os
import datetime
import pandas as pd
from app.models import Table, TableColumnsSpec

from alge.settings import TABLES_PATH


def get_column_spec(t, series):
    distinct_values = series.nunique()
    prop_null = pd.isnull(series).sum() / len(series)

    if distinct_values == 2:
        num_categories = distinct_values
        categorical = True
        numerical = False
        label = True
        feature = True
        problem_type = 'classification'
    elif distinct_values <= 6:
        num_categories = distinct_values
        categorical = True
        numerical = False
        label = False
        feature = True
        problem_type = 'classification'
    else:
        num_categories = None
        categorical = False
        numerical = True
        label = True
        feature = True
        problem_type = 'regression'

    cluster_name = series.name.split('_')[0]

    return {'table': t,
            'column_name': series.name,
            'label': label,
            'problem_type': problem_type,
            'feature': feature,
            'categorical': categorical,
            'num_categories': num_categories,
            'numerical': numerical,
            'cluster': cluster_name,
            'prop_null': prop_null,
            'distinct_values': distinct_values}


def handler(user, name):
    path = os.path.join(TABLES_PATH, name + '.csv')
    data = pd.read_csv(path, low_memory=False)

    table = Table(**{'user': user,
                     'name': name,
                     'created_at': datetime.datetime.today(),
                     'last_update_at': datetime.datetime.today(),
                     'n_rows': len(data),
                     'n_cols': data.shape[1]})

    specs = [get_column_spec(table, data[c]) for c in data.columns]

    table.save()
    [TableColumnsSpec(**s).save() for s in specs]

    return table.name


def refresh_data(name):
    table = Table.objects.get(name=name)
    path = os.path.join(TABLES_PATH, name + '.csv')
    data = pd.read_csv(path, low_memory=False)

    table.n_rows = len(data)
    table.n_cols = data.shape[1]
    table.last_update_at = datetime.datetime.today()

    specs = [get_column_spec(table, data[c]) for c in data.columns]

    table.save()
    TableColumnsSpec.objects.filter(table=table).delete()
    [TableColumnsSpec(**s).save() for s in specs]
