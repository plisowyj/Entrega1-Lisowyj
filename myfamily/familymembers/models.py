from pyexpat import model
from django.db import models


class People(models.Model):
    id = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    identity = models.CharField(max_length=15)
    datebirth = models.DateField()
    address   = models.CharField(max_length=100)

class People_phones(models.Model):
    id = models.IntegerField(primary_key=True)
    id_people = models.IntegerField()
    phonenumber = models.CharField(max_length=15)
  
