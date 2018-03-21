# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-19 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time_sale_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='time_sale_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
