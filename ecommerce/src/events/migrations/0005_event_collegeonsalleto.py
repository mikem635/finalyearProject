# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-09 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20180308_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='collegeOnSalleTo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]