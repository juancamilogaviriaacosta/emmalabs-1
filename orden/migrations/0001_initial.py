# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
