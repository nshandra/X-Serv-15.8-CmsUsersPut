from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/?$', login),
    url(r'^logout/?$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}),
    url(r'^$', 'cms.views.main'),
    url(r'^(.+)$', 'cms.views.get_page')
]
