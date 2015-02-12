from django.conf.urls import patterns, include, url

urlpatterns = patterns('bootcamp.administrativo.views',
    url(r'^home/$', 'administrativo_inicio', name='administrativo_inicio'),
)