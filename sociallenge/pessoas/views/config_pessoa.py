#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect
from sociallenge.pessoas.forms import PessoaEnderecoForm,ConfigPessoaForm
from sociallenge.pessoas.models import Pessoa,ConfigPessoa
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse as r

from django.shortcuts import get_object_or_404
	
from sociallenge.pessoas.views.pessoa import get_pessoa 


def get_configuracao(pessoa):
	'''
		@get_configuracao: View para buscar uma configuracao
	'''
	return get_object_or_404(ConfigPessoa,pessoa=pessoa)

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
	pessoa = get_pessoa(request)
	configuracao = get_object_or_404(ConfigPessoa,pessoa=pessoa)
	form = ConfigPessoaForm(instance=configuracao)

	eform = PessoaEnderecoForm(instance=pessoa)

	return render(request,"pessoa_configuracao.html",{'form':form,'eform':eform})

def save_configuracao(request):
	'''
		@save_configuracao: View para salvar a configuracao
	'''
	pessoa = get_pessoa(request)
	configuracao = get_configuracao(pessoa)

	if request.method == 'POST':
		form = ConfigPessoaForm(request.POST,instance=configuracao)
		if form.is_valid():
			obj = form.save()
			obj.pessoa = pessoa
			obj.save()
			return HttpResponseRedirect(r("pessoas:pessoa_configuracao"))
		else:
			pass
	else:
		return HttpResponseRedirect(r("pessoas:pessoa_inicio"))