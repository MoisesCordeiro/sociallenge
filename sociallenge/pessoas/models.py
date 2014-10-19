#coding: utf-8
from django.db import models
from django.contrib.auth.models import User
#from sociallenge.thumbs import ImageWithThumbsField
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


    cep = models.CharField(max_length=20,blank=True,null=True)
    endereco = models.CharField(max_length=100,blank=True,null=True)
    numero = models.CharField(max_length=10,blank=True,null=True)
    complemento = models.CharField(max_length=100,blank=True,null=True)
    bairro = models.CharField(max_length=100,blank=True,null=True)
    cidade = models.CharField(max_length=100,blank=True,null=True)
    estado = models.CharField(max_length=100,blank=True,null=True)






    @models.permalink
    def inicio(self):
        return ('pessoas:pessoa_inicio', (), {'pessoa_id': self.id})

    class Meta:
        unique_together = ('email',)
    def __unicode__(self):
        return unicode(self.nome)

INTERVALO = (
    ('1','1 dia'),
    ('2','2 dias'),
    ('3','3 dias'),
    ('4','4 dias'),
    ('5','5 dias'),
)

IMPACTO_SOCIAL = (
    ('1','Sim'),
    ('2','Não'),
)

class ConfigPessoa(models.Model):
    #foto = ImageWithThumbsField(upload_to=get_upload_path, sizes=((125,125),(40,40)),blank=True,null=True,verbose_name="Foto")
    
    #caminho_foto = models.CharField(max_length=100,null=True,blank=True)
    intervalo = models.CharField(max_length=1,default='3',choices=INTERVALO)
    pessoa = models.ForeignKey(Pessoa,null=True,blank=True)
    impacto_social = models.CharField(max_length=1,default='2',choices=IMPACTO_SOCIAL)