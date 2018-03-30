# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
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

class EventManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

class Event(models.Model):

    objects = EventManager()
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True, unique=True)
    description = models.TextField(max_length=1000)
    hosting = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    max_per_person = models.IntegerField(default=2)
    price = models.DecimalField(decimal_places=2, max_digits=4, default=25.00)
    time_sale_start = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    time_sale_end = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    number_tickets_on_sale = models.IntegerField(default=0)
    sales_total = models.IntegerField(default=0)
    tickets_sold = models.IntegerField(default=0)
    image = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    SEFS = 'SEFS'
    Medicine = 'Medicine'
    BusinessAndLaw = 'Business And Law'
    ARTS = 'Arts'
    ALL = 'All'
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

    def update_sales(self, quantity):
        self.tickets_sold += quantity
        sale = self.price * quantity
        self.sales_total += sale



    def get_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


    def __str__(self):
        return self.title
