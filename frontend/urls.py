from django.conf.urls import url
from django.urls import path

from frontend.views import main_index, web_server

urlpatterns = [
    path('web_server/', web_server),
    path('main_index/', main_index),
]
