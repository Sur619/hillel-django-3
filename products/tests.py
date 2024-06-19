from django.test import TestCase

from products.models import Product, order, order_product, Order
from telegram.client import send_message


class ProductTestCase(TestCase):
    def test_str(self):
        product = Product.objects.create(title='a product')

        self.assertEqual(str(product), 'a product')
