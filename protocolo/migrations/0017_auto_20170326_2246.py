# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 03:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protocolo', '0016_auto_20170326_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paso',
            name='salida',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
