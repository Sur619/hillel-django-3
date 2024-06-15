from django.utils import timezone
from rest_framework import serializers

from products.models import Order
from products.serializers.order_product import OrderProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.IntegerField(read_only=True)

    time_since_created = serializers.SerializerMethodField()

    def get_time_since_created(self, obj):
        return f"{(timezone.now() - obj.created_at).total_seconds()} days ago"

    class Meta:
        model = Order
        fields = ['id', 'user', "order_products", "total_price", "created_at", "updated_at", "time_since_created", "user_id"]

    def create(self, validated_data):
        # validated_data = {
        # 'user':1,
        # 'order_products': [{'product_id': 1, 'quantity': 3}
        # ]}
        order_products = validated_data.pop('order_products')
        # validated_data = {'user': 1}

        order = Order.objects.create(**validated_data)
        # order.objects.create(user=1)

        for order_product in order_products:
            order.order_products.create(**order_product)
        return order
