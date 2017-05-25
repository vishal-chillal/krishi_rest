from django.conf.urls import url
from django.template.loader import *
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^login/$', views.login, name='login')
]
