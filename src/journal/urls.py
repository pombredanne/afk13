from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView


urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/m/accueil'), name='home'),
)
