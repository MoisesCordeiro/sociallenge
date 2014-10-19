#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from sociallenge.pessoas.forms import PessoaForm,PessoaEnderecoForm,UserForm,LoginForm,ConfigPessoaForm
from sociallenge.pessoas.models import Pessoa,ConfigPessoa
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

def endereco_form_modal(request):
    '''
        @endereco_form_modal: View para salvar o endereço da pessoa
    '''
    form = PessoaEnderecoForm()
    return render(request,"pessoa_endereco_modal.html",{'form':form})

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
    if request.method == 'POST':
        return pessoa_config_post(request)
    else:
        form = ConfigPessoaForm()
        eForm = PessoaEnderecoForm()
        return render(request,"pessoa_config_desafio.html",{'form':form,'eForm':eForm})

def pessoa_config_post(request):
    '''
        @pessoa_config_post: View para salvar as configuracoes de uma pessoa
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
def logar(request):
    #raise Exception("teste")
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            login(request, form.get_user())

            #verificar se a pessoa já fez as configuracoes
            #return HttpResponseRedirect(r("pessoas:pessoa_inicio"))

            pessoa = request.user.pessoa

            try:
                config = ConfigPessoa.objects.get(pessoa=pessoa)
                return HttpResponseRedirect(r("pessoas:pessoa_inicio"))                
            except:
                return HttpResponseRedirect(r("pessoas:pessoa_config"))

        else:
            return render(request, "login.html", {'"lform': form,'form':PessoaForm(),'uform':UserForm()})
    else:
        raise Exception("sei la")