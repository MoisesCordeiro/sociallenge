# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0003_configpessoa'),
    ]

    operations = [
        migrations.AddField(
            model_name='configpessoa',
            name='pessoa',
            field=models.ForeignKey(blank=True, to='pessoas.Pessoa', null=True),
            preserve_default=True,
        ),
    ]
