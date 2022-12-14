from django.db import models

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    prise_day = models.FloatField()
    prise_dayafter = models.FloatField()
    prise_week = models.FloatField()
    prise_monthe = models.FloatField()

class TestModel(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateTimeField()