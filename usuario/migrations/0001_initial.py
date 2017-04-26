# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPorRol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=100)),
                ('opcion', models.CharField(max_length=100)),
                ('template', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50, null=True)),
                ('ciudad', models.CharField(max_length=50, null=True)),
                ('intereses', models.CharField(max_length=200)),
                ('rol_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Rol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='menuporrol',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.Rol'),
        ),
        migrations.AlterUniqueTogether(
            name='menuporrol',
            unique_together=set([('rol', 'menu', 'opcion')]),
        ),
    ]
