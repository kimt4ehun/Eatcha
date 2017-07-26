from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)   #FIXME: BAD CASE//
    ID = models.CharField(max_length=20)



