from django.db import models


# Create your models here.
class ProductModel(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    seller = models.TextField()
    color = models.TextField()
    product_dimensions = models.TextField()
