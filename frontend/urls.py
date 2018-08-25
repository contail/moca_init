from django.conf.urls import url
from django.urls import path

from frontend.views import main_index, web_server,env_settings,change_env_values

urlpatterns = [
    path('web_server/', web_server),
    path('main_index/', main_index),
    path('env_settings/',env_settings),
    path('change_env_values/',change_env_values)
]
