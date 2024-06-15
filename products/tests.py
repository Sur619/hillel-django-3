from django.test import TestCase

from products.models import Product


class ProductTestCase(TestCase):
    def test_str(self):
        product = Product.objects.create(title='a product')

        self.assertEqual(str(product), 'a product')