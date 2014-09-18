#coding:utf-8

from django.shortcuts import render
from sociallenge.pessoas.forms import PessoaForm
from sociallenge.pessoas.models import Pessoa
# Create your views here.


def pessoa_create(request):
    '''
        @pessoa_create: View para definir se é GET ou POST na criação de uma pessoa
    '''
    if request.method == 'POST':
        pass
    else:
        return render(request,"login.html",{'form':PessoaForm()})