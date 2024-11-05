from django.db import models

# Create your models here.
class data(models.Model):
    lattitude=models.FloatField(max_length=100, blank=True)
    longitude= models.FloatField(max_length=100,blank=True)