from enum import unique

from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=300)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=True)



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
