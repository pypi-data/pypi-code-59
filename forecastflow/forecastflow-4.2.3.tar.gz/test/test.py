import forecastflow
from forecastflow import DataSource, User, Project
from forecastflow.training import ClassifierTrainingSettings, RegressorTrainingSettings
from forecastflow.enums import ClassificationMetrics, RegressionMetrics

#forecastflow.config.forecastflow['api_base_url'] = 'http://localhost:5000'

email = 'nakata.yuta@gri.jp'
password = 'r8c2l91fdns7bsb6tnnho'

project_id = 'hxLgbTJxAtInphTmXhI1'
#train_data_id = 'Y2XhFbFU7THLHpB4qZDM'
train_data_id = 'ZXvQeElfDYMOM2vhqn3c'
test_data_id = 'ONGqQDVPIKUPHoXcdfcE'


user = User(email, password)
project = user.get_project(project_id)
train_data_source = DataSource(project, train_data_id)
test_data_source = DataSource(project, test_data_id)

cls_settings = ClassifierTrainingSettings(
    feature_excludes=['col2'],
    target='col5',
    metric=ClassificationMetrics.ACCURACY,
    primary_id='ids',
    secondary_ids=['col4'],
    random_state=11
)

cls_model = train_data_source.create_model(
    cls_settings,
    name='cls_test_api_v3_' + cls_settings.metric.value,
    test_frac=0.51)

pred = cls_model.create_prediction(test_data_source, name='a')
pred.wait_until_done()