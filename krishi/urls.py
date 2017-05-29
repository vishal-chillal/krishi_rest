from django.conf.urls import url
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^administrator/signin/$', views.signin, name='signin'),
    url(r'^administrator/home/$', views.home, name='home'),
    url(r'^administrator/event/$', views.event, name='event'),
    url(r'^signin/$', views.usersignin, name='signin'),
    url(r'^home/$', views.userhome, name='home'),
    url(r'^home/(?P<myEvnt>[1-9]+)/$', views.showEventDetails, name='details'),
]
