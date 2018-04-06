from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
  user = models.OneToOneField(User)
  course = models.CharField(max_length=100)
  SEFS = 'SEFS'
  Medicine = 'Medicine'
  BusinessAndLaw = 'Business And Law'
  ARTS = 'arts'
  college_choices = (
      (SEFS, 'SEFS'),
      (Medicine, 'Medicine'),
      (BusinessAndLaw, 'Business And Law'),
      (ARTS, 'Arts'),
  )
  college = models.CharField(max_length=20,
                                    choices=college_choices,
                                    default=SEFS)
  year = models.CharField(max_length=1)
  is_activated = models.BooleanField(default=False)
  activation_key = models.CharField(max_length=40,null=True)
  key_expires = models.DateTimeField(blank=True, null=True)


  def __str__(self):
          return "%s's profile" % self.user
