# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20141011_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigPessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caminho_foto', models.CharField(max_length=100, null=True, blank=True)),
                ('intervalo', models.CharField(max_length=1, choices=[(b'1', b'1 dia'), (b'2', b'2 dias'), (b'3', b'3 dias'), (b'4', b'4 dias'), (b'5', b'5 dias')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
