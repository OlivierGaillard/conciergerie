# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 08:04
from __future__ import unicode_literals

from django.db import migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menages', '0003_auto_20170619_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='work_category',
            field=mptt.fields.TreeManyToManyField(blank=True, null=True, to='menages.WorkCategory'),
        ),
    ]
