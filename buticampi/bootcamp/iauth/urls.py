from django.conf.urls import patterns, include, url

urlpatterns = patterns('bootcamp.iauth.views',
    url(r'^period/$', 'period', name='period'),
)