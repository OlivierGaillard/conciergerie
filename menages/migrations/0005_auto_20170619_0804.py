# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:04
from __future__ import unicode_literals

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menages', '0004_work_work_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work_category',
            field=mptt.fields.TreeManyToManyField(blank=True, to='menages.WorkCategory'),
        ),
    ]
