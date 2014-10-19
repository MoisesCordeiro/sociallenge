# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_configpessoa_pessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configpessoa',
            name='caminho_foto',
        ),
        migrations.AddField(
            model_name='configpessoa',
            name='impacto_social',
            field=models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Sim'), (b'2', b'N\xc3\xa3o')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cep',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='complemento',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='estado',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='numero',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='configpessoa',
            name='intervalo',
            field=models.CharField(default=b'3', max_length=1, choices=[(b'1', b'1 dia'), (b'2', b'2 dias'), (b'3', b'3 dias'), (b'4', b'4 dias'), (b'5', b'5 dias')]),
        ),
    ]
