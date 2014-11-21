# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iauth', '0002_auto_20141108_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='intervalo',
        ),
        migrations.AddField(
            model_name='profile',
            name='period',
            field=models.CharField(default=b'3', max_length=1, choices=[(b'1', b'1 dia'), (b'2', b'2 dias'), (b'3', b'3 dias'), (b'4', b'4 dias'), (b'5', b'5 dias')]),
            preserve_default=True,
        ),
    ]
