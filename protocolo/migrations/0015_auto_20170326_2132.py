# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 02:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0014_auto_20170326_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolo',
            name='codigo',
            field=models.CharField(blank=True, default=b'PRO-000', max_length=10),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='fecha_creacion',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
