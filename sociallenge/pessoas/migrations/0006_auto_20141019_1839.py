# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0005_auto_20141019_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='estado',
            new_name='uf',
        ),
        migrations.AlterField(
            model_name='configpessoa',
            name='impacto_social',
            field=models.CharField(default=b'2', max_length=1, choices=[(b'1', b'Sim'), (b'2', b'N\xc3\xa3o')]),
        ),
    ]
