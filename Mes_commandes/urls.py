from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [

    url(r'^$', Les_commandes,name='commandes'),

]
urlpatterns += staticfiles_urlpatterns()
