from django.conf.urls import url
from django.urls import path

from frontend import views

urlpatterns = [
    url(r'^$', views.main_index, name='post_list'),
]
