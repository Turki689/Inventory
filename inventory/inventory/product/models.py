from django.db import models
from mptt.models import TreeForeignKey, MPTTModel


class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, related_name='children', null=True, blank=True,)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True, blank=True,
                                 default=None)

    def __str__(self):
        return self.name
