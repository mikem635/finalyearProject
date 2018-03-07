from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  course = models.CharField(max_length=100)
  college = models.CharField(max_length=100)
  year = models.CharField(max_length=1)


  def __str__(self):
          return "%s's profile" % self.user
