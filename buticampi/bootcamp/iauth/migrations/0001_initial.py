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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('url', models.CharField(max_length=50, null=True, blank=True)),
                ('job_title', models.CharField(max_length=50, null=True, blank=True)),
                ('period', models.CharField(default=b'3', max_length=1, choices=[(b'1', b'1 dia'), (b'2', b'2 dias'), (b'3', b'3 dias'), (b'4', b'4 dias'), (b'5', b'5 dias')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
