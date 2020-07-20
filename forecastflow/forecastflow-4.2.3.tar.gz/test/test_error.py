import forecastflow
from forecastflow import DataSource, User, Project, Model
from forecastflow.training import ClassifierTrainingSettings, RegressorTrainingSettings
from forecastflow.enums import ClassificationMetrics, RegressionMetrics

#forecastflow.config.forecastflow['api_base_url'] = 'http://localhost:5000'

email = 'nakata.yuta@gri.jp'
password = 'd3c3cg9ulirhydwn209aqm'
project_id = 'FByW3B0gXH2zvx4GRIMg'
train_data_id = '071iuliZvwknmzoQrkvl'
test_data_id = 'Y2XhFbFU7THLHpB4qZDM'

user = User(email, password)
project = user.get_project(project_id)
train_data_source = DataSource(project, train_data_id)
test_data_source = DataSource(project, test_data_id)

model_id = '1EwHS0F3Uw9KaljUCm5y'
model = Model(project, model_id)
model.wait_until_done()
