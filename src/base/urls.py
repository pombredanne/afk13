from django.conf.urls import patterns, url

from views import Login
from views import Content
from views import Masonry
from views import Rubrique
from views import Redirect


urlpatterns = patterns(
    '',
    url(r'^m/(?P<slug>[\w-]+)/$', Masonry.as_view(), name='masonry'),
    url(r'^r/(?P<slug>[\w-]+)/$', Rubrique.as_view(), name='rubrique'),
    url(r'^c/(?P<slug>[\w-]+)/$', Content.as_view(), name='content'),
    url(r'^x/(?P<slug>[\w-]+)/$', Redirect.as_view(), name='redirect'),
    url(r'^login$', Login.as_view()),
)