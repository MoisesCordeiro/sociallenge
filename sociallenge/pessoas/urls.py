#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('sociallenge.pessoas.views',

	url(r'^$','pessoa_create', name='pessoa_create'),
	url(r'^inicio/$', 'pessoa_inicio', name='pessoa_inicio'),
	url(r'^config/$', 'pessoa_config_desafio', name='pessoa_config_desafio'),
	url(r'^configuracao/$', 'pessoa_configuracao', name='pessoa_configuracao'),
	url(r'^save_configuracao/$', 'save_configuracao', name='save_configuracao'),

	url(r'^logar/$', 'logar', name='logar'),

	url(r'^cadastro_endereco_modal/$', 'endereco_form_modal', name='endereco_form_modal'),
	url(r'^profile/(?P<pessoa_id>\d+)/$', 'profile', name='profile'),
)