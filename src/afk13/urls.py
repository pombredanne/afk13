from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import compositeadmin


compositeadmin.site.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^', include('journal.urls')),
    url(r'^', include('base.urls')),

#    url(r'auth/', include('social_auth.urls')),

    url(r'^admin/', include(compositeadmin.site.include_urls())),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
