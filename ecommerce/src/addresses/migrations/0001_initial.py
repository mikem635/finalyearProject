# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-23 17:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0003_auto_20180322_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr_type', models.CharField(choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120)),
                ('address_line_1', models.CharField(max_length=120)),
                ('address_line_2', models.CharField(blank=True, max_length=120, null=True)),
                ('address_line_3', models.CharField(blank=True, max_length=120, null=True)),
                ('town', models.CharField(max_length=120)),
                ('county', models.CharField(max_length=120)),
                ('eir_code', models.CharField(max_length=120)),
                ('payee_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.PayeeData')),
            ],
        ),
    ]
