# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desafio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('nivel', models.CharField(max_length=1, choices=[(b'A', b'Facil'), (b'B', b'Moderado'), (b'C', b'Dificil'), (b'D', b'Muito Dificil')])),
                ('tipo', models.CharField(max_length=1, choices=[(b'A', b'Generico'), (b'B', b'Pessoal'), (b'C', b'Grupo')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
