from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from base.models import BasePublishModel

from .validators import validate_blocked_words

User = settings.AUTH_USER_MODEL


# Create your models here.
class ProductModel(BasePublishModel):
    title = models.TextField()
    description = models.TextField(null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, db_index=True)
    price = models.FloatField()
    seller = models.TextField(null=True)
    color = models.TextField(null=True)
    product_dimensions = models.TextField(null=True)
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="products",
    )

    def get_absolute_url(self):
        return f"/products/{self.slug}/"

    def save(self, *args, **kwargs):
        self.title = validate_blocked_words(self.title)
        self.description = validate_blocked_words(self.description)
        self.seller = validate_blocked_words(self.seller)
        super().save(*args, **kwargs)


def slugify_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug or instance.slug == "":
        new_slug = slugify(instance.title)
        MyModel = instance.__class__
        qs = MyModel.objects.filter(slug__startswith=new_slug).exclude(
            id=instance.id
        )
        if qs.count() == 0:
            instance.slug = new_slug
        else:
            instance.slug = f"{new_slug}-{qs.count() + 1}"


pre_save.connect(slugify_pre_save, sender=ProductModel)
