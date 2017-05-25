from django.conf.urls import url
from django.template.loader import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^login/$', views.login, name='login')
]
