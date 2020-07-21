from django.urls import path, include
from django.conf.urls.static import static

from alge import settings
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('register', views.register, name='register'),
    path('account', views.account, name='account'),
    path('change_password', views.change_password, name='change_password'),
    path('about_us', views.about_us, name='about_us'),
    path('new_model', views.new_model, name='new_model'),
    path('benchmark', views.benchmark, name='benchmark'),
    path('', include('django.contrib.auth.urls')),
    path('running', views.running, name='running'),
    path('healthcheck', views.healthcheck, name='helthcheck'),
    path('runs', views.runs, name='runs'),
    path('run/<str:run_id>', views.run, name='run'),
    path('rerun_selected_features/<str:old_run_id>', views.rerun_selected_features, name='rerun_selected_features'),
    path('models', views.models, name='models'),
    path('model/<str:model_id>', views.model, name='model'),
    path('hyperparameter_optimization/<str:model_id>', views.hyperparameter_optimization, name='hyperparameter_optimization'),
    path('tables', views.tables, name='tables'),
    path('table/<str:table_id>', views.table, name='table'),
    path('upload_table', views.upload_table, name='upload_table')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)