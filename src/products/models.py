from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    title = models.CharField(max_length=100)
    # description = models.TextField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(unique=True)

    # Redirects to the product's detail page using its slug
    # after creating a new product instance.
    def get_absolute_url(self):
        return f"/products/products/{self.slug}/"

    def get_edit_url(self):
        return f"/products/my-products/{self.slug}"

    def get_delete_url(self):
        return f"/products/my-products/{self.slug}/delete"

    def __str__(self):
        return self.title


class DigitalProduct(Product):
    class Meta:
        proxy = True

    def __str__(self):
        return f"{self.title} (Digital Product)"
