from django.db import models

# Create your models here.

class Category(models.Model):
     name = models.CharField(max_length=256)


class Producty(models.Model):
     title = models.CharField(max_length=256)
     description = models.TextField()
     price = models.FloatField(default=0)
     category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Review(models.Model):
     text = models.CharField(max_length=256)
     producty = models.ForeignKey(Producty, on_delete=models.CASCADE)