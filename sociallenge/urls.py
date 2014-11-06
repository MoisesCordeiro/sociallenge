from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sociallenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'sociallenge.core.views.home', name='home'),
    #url(r'^','sociallenge.pessoas.views.pessoa_create', name='pessoa_create'),
    #url(r'^logar/$','sociallenge.pessoas.views.logar', name='logar'),
    url(r'^login/$','django.contrib.auth.views.login',{"template_name":'login.html'}),
    url(r'^logout/','django.contrib.auth.views.logout_then_login',{'login_url': '/'}),

    url(r'^desafios/',include('sociallenge.desafios.urls', namespace='desafios')),
    url(r'^pessoas/',include('sociallenge.pessoas.urls', namespace='pessoas')),

    url(r'^politica_privacidade/$', 'sociallenge.core.views.politica_privacidade', name='politica_privacidade'),
    url(r'^termos_condicoes/$', 'sociallenge.core.views.termos_condicoes', name='termos_condicoes'),
)
