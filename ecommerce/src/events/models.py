# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random
import os

def get_ext(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    return name, ext

#to remove white spave from a file uploaded
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,5000000)
    name, ext = get_ext(filename)
    new_file = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "events/{new_filename}/{new_file}".format(new_filename=new_filename,
                                                        new_file=new_file)

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=25.00)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
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
    collegeOnSalleTo = models.CharField(max_length=20,
                                      choices=collegeOnSalleTo_choices,
                                      default=SEFS)


    def __str__(self):
        return self.title
# Create your models here.
