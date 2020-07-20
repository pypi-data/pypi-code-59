import forecastflow_fsdfefwefg
from forecastflow_fsdfefwefg import DataSource, User, Project
from forecastflow_fsdfefwefg.training import ClassifierTrainingSettings, RegressorTrainingSettings
from forecastflow_fsdfefwefg.enums import ClassificationMetrics, RegressionMetrics

#forecastflow_fsdfefwefg.config.forecastflow_fsdfefwefg['api_base_url'] = 'http://localhost:5000'

email = 'nakata.yuta@gri.jp'
password = 'd3c3cg9ulirhydwn209aqm'
project_id = 'FByW3B0gXH2zvx4GRIMg'
train_data_id = '071iuliZvwknmzoQrkvl'
test_data_id = 'o4PNtCIA6KGrQmCtmesZ'

user = User(email, password)
project = user.get_project(project_id)
train_data_source = DataSource(project, train_data_id)
test_data_source = DataSource(project, test_data_id)

cls_settings = RegressorTrainingSettings(
    feature_excludes=['col2'],
    target='col1',
    metric=RegressionMetrics.MEAN_ABSOLUTE_ERROR,
    primary_id='ids',
    secondary_ids=['col4'],
    random_state=11
)

cls_model = train_data_source.create_model(
    cls_settings,
    name='cls_test_api_v3_' + cls_settings.metric.value,
    test_data_source=test_data_source)

cls_model.wait_until_done()

cls_model.create_prediction(test_data_source, 'fsdfwef')