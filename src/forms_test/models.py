from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return f"/products/{self.slug}/"

    def __str__(self):
        return self.title
