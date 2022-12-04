from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^create', views.TaskCreate.as_view(), name='create'),
    re_path(r'^select', views.TaskSelect.as_view(), name='select'),
    re_path(r'^', views.Todo.as_view(), name='todo')
]