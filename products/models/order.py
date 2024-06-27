import uuid
from django.db import models
from django.contrib.auth.models import User

from products.models import Product


class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, related_name='products', through='OrderProduct')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    display_number = models.IntegerField(blank=False, null=True, default=0)
    @property
    def total_price(self):
        total_price = 0
        for order_product in self.order_products.all():
            total_price += order_product.price
        return total_price
