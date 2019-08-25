from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length = 25)
    price = models.FloatField()
    date_release = models.DateField()
    brand = models.CharField(max_length = 25)