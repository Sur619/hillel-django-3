from django.db import models
from products.models.category import Category
from products.models.tag import Tag

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    summary = models.TextField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    is_18_plus = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    tags = models.ManyToManyField(Tag, blank=True, related_name='products')

    order = models.ManyToManyField('Order', through='OrderProduct')

    def __str__(self):
        return self.title
