# coding: utf-8
from django import forms
from sociallenge.desafios.models import Desafio
from django.core.exceptions import ValidationError
from django.contrib import admin

class DesafioForm(forms.ModelForm):
	class Meta:
		model = Desafio
		fields = ('titulo','descricao','nivel','tipo',)