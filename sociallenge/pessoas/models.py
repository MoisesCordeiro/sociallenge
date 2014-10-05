#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

RELACIONAMENTO = (
    ('A','Solteiro(a)'),
    ('B','Casado(a)'),
    ('C','Namorando'),
    ('D','Viúvo(a)'),
    )

GENERO = (
    ('A','Masculino'),
    ('B','Feminino'),
    )


class Pessoa(models.Model):
    email = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    nascimento = models.CharField(max_length=10)
    relacionamento = models.CharField(max_length=1,default='A',choices=RELACIONAMENTO)
    genero = models.CharField(max_length=1,default='A',choices=GENERO)

    user = models.OneToOneField(User,related_name='pessoa',null=True,blank=True)

    @models.permalink
    def inicio(self):
        return ('pessoas:pessoa_inicio', (), {'pessoa_id': self.id})

    class Meta:
        unique_together = ('email',)
    def __unicode__(self):
        return unicode(self.nome)