#coding: utf-8
from django.db import models


NIVEL = (
	('A','Facil'),
	('B','Moderado'),
	('C','Dificil'),
	('D','Muito Dificil'),
)

TIPO = (
	('A','Generico'),
	('B','Pessoal'),
	('C','Grupo'),
)

class Desafio(models.Model):
	titulo = models.CharField(max_length=100)
	descricao = models.CharField(max_length=100)
	nivel = models.CharField(max_length=1, choices=NIVEL)
	tipo = models.CharField(max_length=1,choices=TIPO)
	#tempo = models.IntegerField()	