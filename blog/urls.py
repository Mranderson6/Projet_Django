from django.conf.urls import url
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [

    url(r'^$', home,name='home'),
    url(r'^accueil/$', home, name='accueil'),
    url(r'^article/(?P<id>\d+)$', view_article, name='article'),
    url(r'^article/$', article_T, name='tout_article'),
    url(r'^redirection/$', vue_redirection, name='redi'),
    url(r'^date$', date_actuelle, name='date_act'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', addition),
    url(r'^user/$', affichage_info),
    url(r'^tag/$', test_tag),
    url(r'^enregistrement', sign_up, name='sign_up'),
    url(r'^inscription$', sign_in, name='sign_in'),
    url(r'^contact/$', contact, name= 'contact'),
    url(r'^form_art/$', Article_Formu, name='Article_Formu'),
    url(r'^photo/$', nouveau_contact, name= 'nouveau_contact'),
    url(r'^real/$', voir_contacts, name= 'voir_contacts'),
]
urlpatterns += staticfiles_urlpatterns()
