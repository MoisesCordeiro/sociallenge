# coding: utf-8

from django import forms
from sociallenge.pessoas.models import Pessoa
from django.core.exceptions import ValidationError

from django.contrib import admin


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('email','nome','sobrenome','nascimento','relacionamento',)