from sys import maxsize
from django.db import models
from django.forms import IntegerField

class Items(models.Model):


    itemname = models.CharField(max_length=255)
    startprice =models.IntegerField()

    starttime=models.CharField(max_length=255)
    endtime=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    userid=models.CharField(max_length=255,default=" ")
    highprice=models.IntegerField()

    