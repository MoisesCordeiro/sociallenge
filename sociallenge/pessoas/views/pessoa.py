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
    if request.method == 'POST':
        return endereco_post(request)
    else:
        form = PessoaEnderecoForm()
        return render(request,"pessoa_endereco_modal.html",{'form':form})

def endereco_post(request):
    '''
        @endereco_post: View para salvar o endereco de uma pessoa
    '''
    form = PessoaEnderecoForm(request.POST)
    if request.is_ajax():
        if form.is_valid():
            pessoa = request.user.pessoa
            pessoa.cep = request.POST.get('cep')
            pessoa.endereco = request.POST.get('endereco')
            pessoa.numero = request.POST.get('numero')
            pessoa.complemento = request.POST.get('complemento')
            pessoa.bairro = request.POST.get('bairro')
            pessoa.cidade = request.POST.get('cidade')
            pessoa.uf = request.POST.get('uf')
            pessoa.save()
             # Retornando para o Form que o formulario foi gravado com sucesso
            return HttpResponse(simplejson.dumps({'status':'OK'}))                                                          
        else:
            print "error"
            errors = form.errors
            return HttpResponse(simplejson.dumps(errors)) 
    else:
        print "error"
        pass

def pessoa_inicio(request):
    '''
        @pessoa_inicio: View para renderizar a página inicial de uma pessoa
    '''
    try:
        if request.user.pessoa:
            return render(request,"pagina_inicial.html")
        else:
            return HttpResponseRedirect("/")
    except:
         return render(request,"pagina_inicial.html")

def logar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            login(request, form.get_user())
            pessoa = request.user.pessoa

            try:
                config = ConfigPessoa.objects.get(pessoa=pessoa)
                return HttpResponseRedirect(r("pessoas:pessoa_inicio"))                
            except:
                return HttpResponseRedirect(r("pessoas:pessoa_config"))

        else:
            return render(request, "login.html", {'lform': form,'form':PessoaForm(),'uform':UserForm()})
    else:
        return HttpResponseRedirect(r("sociallenge.core.views.home")) 


def profile(request,pessoa_id):
    """
        @view para renderizar o profile de uma pessoa
    """
    pessoa = get_object_or_404(Pessoa,id=pessoa_id)

    #publicacoes

    return render(request,"profile.html",{'pessoa':pessoa})
