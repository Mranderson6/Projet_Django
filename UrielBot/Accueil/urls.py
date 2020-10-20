from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', home,name='home'),

]
urlpatterns += staticfiles_urlpatterns()