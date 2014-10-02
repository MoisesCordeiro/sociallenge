# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('nascimento', models.CharField(max_length=10)),
                ('relacionamento', models.CharField(max_length=1, choices=[(b'A', b'Solteiro(a)'), (b'B', b'Casado(a)'), (b'C', b'Namorando'), (b'D', b'Vi\xc3\xbavo(a)')])),
                ('genero', models.CharField(max_length=1, choices=[(b'A', b'Masculino'), (b'B', b'Feminino')])),
                ('user', models.OneToOneField(related_name=b'pessoa', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='pessoa',
            unique_together=set([('email',)]),
        ),
    ]
