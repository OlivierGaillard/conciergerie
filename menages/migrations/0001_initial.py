# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sejour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrivee', models.DateField()),
                ('depart', models.DateField()),
                ('visiteur', models.CharField(max_length=25, verbose_name='Nom hôte')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_name', models.CharField(default='Travail', max_length=50)),
                ('heure', models.SmallIntegerField(default=1)),
                ('minutes', models.SmallIntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('sejour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menages.Sejour')),
            ],
        ),
    ]
