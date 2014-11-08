#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from sociallenge.pessoas.forms import PessoaForm,PessoaEnderecoForm,UserForm,LoginForm,ConfigPessoaForm
from sociallenge.pessoas.models import Pessoa,ConfigPessoa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse as r
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404


def pessoa_config_desafio(request):
    '''
        @pessoa_config: View para renderizar a página de configuração da pessoa
    '''
    if request.method == 'POST':
        return pessoa_config_post(request)
    else:
        form = ConfigPessoaForm()
        eForm = PessoaEnderecoForm()
        return render(request,"pessoa_config_desafio.html",{'form':form,'eForm':eForm})

def pessoa_config_post(request):
    '''
        @pessoa_config_post: View para salvar as configuracoes de uma pessoa quando ela termina de fazer o cadastro
    '''
    pessoa = request.user.pessoa
    form = ConfigPessoaForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.pessoa = pessoa
        obj.save()
        return HttpResponseRedirect(r("pessoas:pessoa_inicio"))   
    else:
        return render(request,"pessoa_config_desafio.html",{'form':form})

def pessoa_configuracao(request):
	'''
		@pessoa_configuracao: View para renderizar a página de configurações da pessoa
	'''

