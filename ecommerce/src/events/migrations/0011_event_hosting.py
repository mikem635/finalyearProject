# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-15 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20180313_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='hosting',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
