import django_filters

from products.models import Product


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product

        fields = \
            {   # contain , i - case insensitive
                'title': ['icontains'],
                # less than , greater than
                'price': ['lt', 'gt'],
                'category': ['exact'],
                'tags': ['exact'],
            }
