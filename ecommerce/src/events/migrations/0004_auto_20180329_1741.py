# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-29 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20180329_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='event',
            name='hosting',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]