# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-05 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_userprofile_is_activated'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
    ]
