from django.db import models

from products.models import Product


class ProductAdditionslInfornation(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='additionslinfornation')
    additional_information = models.TextField()