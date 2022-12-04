from django.urls import re_path, path
from .views import RegisteUser, AppLogin
from .views import index

app_name = "login"

urlpatterns = [
    
    re_path(r'^registe_user', RegisteUser.as_view(), name="registe_user" ),
    re_path(r'^AppLogin', AppLogin.as_view(), name="AppLogin" ),
]
