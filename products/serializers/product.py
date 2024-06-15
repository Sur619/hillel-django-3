from rest_framework import serializers
from products.models import Product
from products.serializers.category import CategorySerializer
from products.serializers.tag import TagSerializers


class ProductReadOnlySerializer(serializers.ModelSerializer):
    price_usd = serializers.SerializerMethodField()
    price = serializers.FloatField()
    category = CategorySerializer()
    tags = TagSerializers()

    def get_price_usd(self, obj: Product):
        price_usd = obj.price / 40

        return round(price_usd, 2)

    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'price_usd', 'category', 'tags')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'price', 'category', 'tags')
