from django.db import models

# Create your models here.

class product(models.Model):
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=30,default="")