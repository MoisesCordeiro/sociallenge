#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from sociallenge.pessoas.forms import PessoaForm
from sociallenge.pessoas.models import Pessoa
from django.contrib.auth.models import User
# Create your views here.


def pessoa_create(request):
    '''
        @pessoa_create: View para definir se é GET ou POST na criação de uma pessoa
    '''
    if request.method == 'POST':
        return pessoa_create_post(request) 
    else:
        return render(request,"login.html",{'form':PessoaForm()})

def pessoa_create_post(request):
    '''
        @pessoa_create_post: View para salvar uma pessoa
    '''
    form = PessoaForm(request.POST)
    if form.is_valid():
        obj = form.save()
        username = obj.email
        password = request.POST['pass']
        obj.user = User.objects.create_user(username=username,password=request.POST['pass'])
        obj.save()
        return HttpResponse("salvou")
    else:
        return render(request,"login.html",{'form':form})

def pessoa_inicio(request,pessoa_id):
    '''
        @pessoa_inicio: View para renderizar a página inicial de uma pessoa
    '''