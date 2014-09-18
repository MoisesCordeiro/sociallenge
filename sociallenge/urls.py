from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sociallenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sociallenge.core.views.home', name='home'),
    url(r'^pessoas/',include('sociallenge.pessoas.urls', namespace='pessoas')),
)
