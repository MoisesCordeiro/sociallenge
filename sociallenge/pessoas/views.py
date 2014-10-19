#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from sociallenge.pessoas.forms import PessoaForm,UserForm,LoginForm
from sociallenge.pessoas.models import Pessoa
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse as r
from django.contrib.auth.forms import AuthenticationForm 

def pessoa_create(request):
    '''
        @pessoa_create: View para definir se é GET ou POST na criação de uma pessoa
    '''

    if request.method == 'POST':
        return pessoa_create_post(request) 
    else:
        lform = AuthenticationForm()
        return render(request,"login.html",{'form':PessoaForm(),'lform':lform})

def pessoa_create_post(request):
    '''
        @pessoa_create_post: View para salvar uma pessoa
    '''
    form = PessoaForm(request.POST)
    uform = UserForm(request.POST)
    if form.is_valid() and uform.is_valid():
        obj = form.save()
        username = obj.email
        password = request.POST.get('password1')
        user = User.objects.create_user(username=username,email=username,password=request.POST['password1'])
        user.save()
        obj.user = user
        obj.save()
        user = authenticate(username=user.username,password=request.POST['password1'])
        login(request, user)
        return HttpResponseRedirect(r('pessoas:pessoa_config'))
    else:
        return render(request,"login.html",{'form':form,'lform':LoginForm(),'uform':uform})

def pessoa_inicio(request):
    '''
        @pessoa_inicio: View para renderizar a página inicial de uma pessoa
    '''
    if request.user.pessoa:
        return render(request,"pagina_inicial.html")
    else:
        return HttpResponseRedirect("/")

def pessoa_config(request):
    '''
        @pessoa_config: View para renderizar a página de configuração da pessoa
    '''
    return render(request,"pessoa_config_desafio.html")

def logar(request):
    #raise Exception("teste")
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            login(request, form.get_user())

            #verificar se a pessoa já fez as configuracoes
            #return HttpResponseRedirect(r("pessoas:pessoa_inicio"))

            return HttpResponseRedirect(r("pessoas:pessoa_config"))
        else:
            return render(request, "login.html", {'"lform': form,'form':PessoaForm(),'uform':UserForm()})
    else:
        raise Exception("sei la")