#coding: utf-8

from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

from sociallenge.desafios.forms import DesafioForm
from sociallenge.desafios.models import Desafio

# Create your views here.

def desafio_lista(request):
	return render(request,"desafio_lista.html",{'desafios':Desafio.objects.all()})

def desafio_novo(request):
	if request.method == 'POST':
		return desafio_create_post(request)
	else:
		return render(request,"desafio_novo.html",{'form': DesafioForm()})

def desafio_create_post(request):
    '''
        @desafio_create_post: View para salvar um desafio
    '''
    form = DesafioForm(request.POST)
    if form.is_valid():
        obj = form.save()
        obj.save()
        return HttpResponseRedirect("/desafios/")
    else:
        return render(request,"desafio_novo.html",{'form':form})