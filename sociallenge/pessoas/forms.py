# coding: utf-8

from django import forms
from sociallenge.pessoas.models import Pessoa,ConfigPessoa
from django.core.exceptions import ValidationError
from django.forms.widgets import Select,RadioSelect
from django.contrib import admin


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('email','nome','sobrenome','nascimento','relacionamento','genero')
        widgets ={
        		      'nome'     	      : forms.TextInput(attrs={'class':'form-control','size':18,'placeHolder':'Nome:'}),
                  'sobrenome'       : forms.TextInput(attrs={'class':'form-control','size':18,'placeHolder':'Sobrenome:'}),
                  'email'     		  : forms.TextInput(attrs={'class':'form-control','size':18,'placeHolder':'Email:'}),
                  'nascimento'      : forms.TextInput(attrs={'class':'form-control','size':18,'placeHolder':'Nascimento:'}),
                  'relacionamento' 	: Select(attrs={'class':'form-control',}),
                  'genero' : Select(attrs={'class':'form-control'}),
        }

class PessoaEnderecoForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('cep','endereco','numero','complemento','bairro','cidade','uf',)
        widgets ={
                  'cep'         : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'CEP:'}),
                  'endereco'    : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'Endereço:'}),
                  'numero'      : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'Número:'}),
                  'complemento' : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'Complemento:'}),
                  'bairro'      : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'Bairro:'}),
                  'cidade'      : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'Cidade:'}),
                  'uf'      : forms.TextInput(attrs={'class':'form-control','size':17,'placeHolder':'UF:'}),


        }




class LoginForm(forms.Form):
    username = forms.CharField(label='Login', max_length=32, widget=forms.TextInput(attrs={'class':'form-control','placeHolder':'Email'}))
    password = forms.CharField(label='Senha', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeHolder':'Senha'}))


class UserForm(forms.Form):
    password1 = forms.CharField(label='Senha', max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control','size':17,'placeHolder':'Senha:'}))
    password2 = forms.CharField(label='Confirme a Senha', max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control','size':17,'placeHolder':'Confirmação:'}))


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Confirme seu senha")
        if password1 != password2:
            raise forms.ValidationError("As senha estão diferentes")
        return password2

class ConfigPessoaForm(forms.ModelForm):
    class Meta:
        model = ConfigPessoa
        fields = ('intervalo','impacto_social',)
        widgets = {
            'intervalo'         : RadioSelect(attrs={'class':'form-control form-inline'}),
            'impacto_social'    : RadioSelect(attrs={'class':'form-control form-inline'}),
        }