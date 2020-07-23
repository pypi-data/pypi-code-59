from django.conf.urls import re_path
from republictime import views

app_name = 'republictime'

urlpatterns = [
    re_path(r'^$', views.HomePageView.as_view(), name='home_page_view')
]