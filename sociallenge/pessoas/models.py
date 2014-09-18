#coding: utf-8
from django.db import models

# Create your models here.

RELACIONAMENTO = (
    ('A','Solteiro(a)'),
    ('B','Casado(a)'),
    ('C','Namorando'),
    ('D','Viúvo(a)'),
    )

class Pessoa(models.Model):
    email = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=10)
    relacionamento = models.CharField(max_length=1,choices=RELACIONAMENTO)

    def __unicode__(self):
        return unicode(self.nome)