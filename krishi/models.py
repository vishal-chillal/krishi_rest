from __future__ import unicode_literals

from django.db import models


class UserInfo(models.Model):
    """class for user login """
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Event(models.Model):
    """docstring for Event"""
    

# Create your models here.
