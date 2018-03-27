# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Society(models.Model):
  user = models.OneToOneField(User)
  soc_name = models.CharField(max_length=100)
  is_society = models.BooleanField(default = False)

  def __str__(self):
      return self.soc_name
