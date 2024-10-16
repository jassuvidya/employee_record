from django.db import models


# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=256)
    phone = models.CharField(max_length=10)