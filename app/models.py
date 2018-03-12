# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    anniversary = models.IntegerField()
    name = models.TextField()
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=1000)
    description = models.TextField()
