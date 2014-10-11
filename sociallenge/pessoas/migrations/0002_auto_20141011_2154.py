# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='genero',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Masculino'), (b'B', b'Feminino')]),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='relacionamento',
            field=models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Solteiro(a)'), (b'B', b'Casado(a)'), (b'C', b'Namorando'), (b'D', b'Vi\xc3\xbavo(a)')]),
        ),
    ]
