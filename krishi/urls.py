from django.conf.urls import url
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^administrator/signin/$', views.signin, name='signin'),
    url(r'^administrator/home/$', views.home, name='home'),
    url(r'^administrator/event/$', views.event, name='event'),
    url(r'^administrator/event/(?P<myEvnt>[1-9]+)/$', views.showEventDetails, name='details'),
    url(r'^signin/$', views.usersignin, name='signin'),
    url(r'^home/$', views.userhome, name='home'),
    url(r'^home/[1-9]+/(?P<evnt>[A-Z]+[_]+[1-9]+)/$', views.handle_event, name='handle_events'),
    url(r'^home/(?P<myEvnt>[1-9]+)/$', views.showEventDetails, name='details'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
