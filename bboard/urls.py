
from django.conf.urls import url, include
from . import views



urlpatterns = [
    url('get_all/$', views.index),

]