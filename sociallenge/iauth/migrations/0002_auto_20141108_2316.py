# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iauth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='period',
        ),
        migrations.AddField(
            model_name='profile',
            name='impacto_social',
            field=models.CharField(default=b'2', max_length=1, choices=[(b'1', b'Sim'), (b'2', b'N\xc3\xa3o')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='intervalo',
            field=models.CharField(default=b'3', max_length=1, choices=[(b'1', b'1 dia'), (b'2', b'2 dias'), (b'3', b'3 dias'), (b'4', b'4 dias'), (b'5', b'5 dias')]),
            preserve_default=True,
        ),
    ]
