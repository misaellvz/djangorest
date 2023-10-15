from django.db import models
from .choices import PRODUCT_STATUS, INACTIVE


class Category(models.Model):
    name = models.CharField(max_length=255)

    def _str_(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Image(models.Model):
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")


class Product(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(
        max_length=50,
        choices=PRODUCT_STATUS,
        default=INACTIVE,
    )
    categories = models.ManyToManyField(Category)
    images = models.ManyToManyField(Image)

    def _str_(self) -> str:
        return self.name
