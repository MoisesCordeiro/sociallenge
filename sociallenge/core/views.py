#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from sociallenge.pessoas.forms import PessoaForm,LoginForm,UserForm
# Create your views here.

def home(request):
	return render(request,"base.html",{'form':PessoaForm(),'lform':AuthenticationForm(),'uform':UserForm})
	

def termos_condicoes(request):
	return render(request,"termos_e_condicoes.html")


def politica_privacidade(request):
	return render(request,"politica_de_privacidade.html")