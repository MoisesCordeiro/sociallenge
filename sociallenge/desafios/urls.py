#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('sociallenge.desafios.views',
	url(r'^$', 'desafio_lista', name='desafio_lista'),
	url(r'^novo/$', 'desafio_novo', name='desafio_novo'),
)
