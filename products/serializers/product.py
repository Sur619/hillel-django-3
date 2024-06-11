import time

from django.core.cache import cache
from rest_framework import serializers
from products.models import Product
from products.serializers.category import CategorySerializer
from products.serializers.tag import TagSerializer


class ProductReadOnlySerializer(serializers.ModelSerializer):
    price_usd = serializers.SerializerMethodField()
    price = serializers.FloatField()
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    additional_metadata = serializers.JSONField()

    def get_price_usd(self, obj: Product):
        price_usd = obj.price / 38

        return round(price_usd, 2)

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'price',
            'summary',
            'price_usd',
            'category',
            'tags',
            'is_18_plus',
            'created_at',
            'additional_metadata',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'summary', 'category', 'tags')
