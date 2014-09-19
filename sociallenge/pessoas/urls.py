#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('sociallenge.pessoas.views',
	url(r'^inicio/$', 'pessoa_inicio', name='pessoa_inicio'),
)