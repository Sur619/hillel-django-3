from django.db import models


class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_products')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='order_products')
    quantity = models.FloatField(default=1)
    @property
    def price(self):
        return float(self.product.price) * self.quantity
