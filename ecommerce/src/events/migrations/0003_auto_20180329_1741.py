# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-29 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180329_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='hosting',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
