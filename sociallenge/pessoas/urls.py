#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('sociallenge.pessoas.views',
	url(r'^','pessoa_create', name='pessoa_create'),
	url(r'^inicio/$', 'pessoa_inicio', name='pessoa_inicio'),
)