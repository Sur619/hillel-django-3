import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product

from telegram.client import send_message

class Order(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    products = models.ManyToManyField(Product, related_name='products', through='OrderProduct')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def total_price(self):
        total_price = 0
        for order_product in self.order_products.all():
            total_price += order_product.price
        return total_price


@receiver(post_save, sender=Order)
def send_order_telegram_message(sender, instance, created, **kwargs):
    if created:
        chat_id = 980106016
        text = f"new order {instance.uuid} created"
        send_message(chat_id, text)
