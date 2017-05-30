from __future__ import unicode_literals
from django.db import models

''' these are for mapping the objects with the databases '''


class UserInfo(models.Model):
    '''class for user login '''
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class EndUser(models.Model):
    '''class for user login '''
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    state = models.CharField(max_length=100)


class Subscription(models.Model):
    username = models.CharField(max_length=100)
    eventid = models.CharField(max_length=100)

    # def getCount(self):

    # def dele(self, username):
    #     # print username
    #     k = Subscription.objects.filter(username=username)
    #     # print k.username
    #     return k
    #     try:
    #         Subscription.objects.filter(username=username).delete()
    #     except Exception as e:
    #         print e


class Event(models.Model):
    '''docstring for Event'''
    eventname = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    fees = models.IntegerField()
    info = models.CharField(max_length=100)
