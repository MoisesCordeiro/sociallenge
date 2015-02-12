#coding:utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
from bootcamp.articles.models import Article, Tag, ArticleComment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bootcamp.articles.forms import ArticleForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from bootcamp.decorators import ajax_required
import markdown
from django.template.loader import render_to_string


def administrativo_inicio(request):
	raise Exception("aaa")
	return HttpResponse("oi")