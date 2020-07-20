import forecastflow_fsdfefwefg
from forecastflow_fsdfefwefg import DataSource, User, Project
from forecastflow_fsdfefwefg.training import ClassifierTrainingSettings, RegressorTrainingSettings
from forecastflow_fsdfefwefg.enums import ClassificationMetrics, RegressionMetrics
import requests
import json

forecastflow_fsdfefwefg.config.forecastflow_fsdfefwefg['api_base_url'] = 'http://localhost:5000'

email = 'nakata.yuta@gri.jp'
password = 'd3c3cg9ulirhydwn209aqm'
project_id = 'FByW3B0gXH2zvx4GRIMg'
train_data_id = '071iuliZvwknmzoQrkvl'
test_data_id = 'Y2XhFbFU7THLHpB4qZDM'

user = User(email, password)
project = user.get_project(project_id)
train_data_source = DataSource(project, train_data_id)
test_data_source = DataSource(project, test_data_id)

data = {
    "idToken": user.id_token,
    "name": "cls_test_api_v3_recall", 
    "trainData": {"pid": "FByW3B0gXH2zvx4GRIMg", "did": "071iuliZvwknmzoQrkvl"}, 
    "trainSettings": {"target": "col5", "primaryID": "ids", "secondaryIDs": ["col4"], 
    "featureExcludes": ["col2"], "randomState": 11, 
    "modelType": "Classification", "metric": "f1"
    }, 
    "desc": "", "percentTest": 51}

print(requests.post(
        f'{forecastflow_fsdfefwefg.config.forecastflow_fsdfefwefg["api_base_url"]}/v3/createmodel',
        data=json.dumps(data)
    ).text.replace(r'\n', '\n'))