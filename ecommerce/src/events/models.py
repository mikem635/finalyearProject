# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=25.00)
    SEFS = 'SEFS'
    Medicine = 'Medicine'
    BusinessAndLaw = 'Business And Law'
    ARTS = 'arts'
    ALL = 'all'
    collegeOnSalleTo_choices = (
        (SEFS, 'SEFS'),
        (Medicine, 'Medicine'),
        (BusinessAndLaw, 'Business And Law'),
        (ARTS, 'Arts'),
        (ALL, 'All')
    )
    collegeOnSalleTo = models.CharField(max_length=2,
                                      choices=collegeOnSalleTo_choices,
                                      default=SEFS)


    def __str__(self):
        return self.title
# Create your models here.
