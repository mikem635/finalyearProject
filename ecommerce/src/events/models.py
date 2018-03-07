# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=4)
# Create your models here.
