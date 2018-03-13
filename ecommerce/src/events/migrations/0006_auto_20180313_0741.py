# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-13 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_collegeonsalleto'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='events/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='collegeOnSalleTo',
            field=models.CharField(choices=[('SEFS', 'SEFS'), ('Medicine', 'Medicine'), ('Business And Law', 'Business And Law'), ('arts', 'Arts'), ('all', 'All')], default='SEFS', max_length=2),
        ),
    ]