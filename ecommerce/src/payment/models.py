# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL
class PayeeData(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)

def new_user(sender, instance, created, *args, **kwargs):
    if created:
        PayeeData.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(new_user, sender=User)
