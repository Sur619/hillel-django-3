# import graphene
# import graphene_django
#
# from products.models import Product, Order
#
#
# class ProductObjectType(graphene_django.DjangoObjectType):
#     class Meta:
#         model = Product
#         fields = ['title', 'price', 'summary']
#
#
# class OrderObjectType(graphene_django.DjangoObjectType):
#     class Meta:
#         model = Order
#         fields = ['uuid', 'order_products']
#
#
# class Query(graphene.ObjectType):
#     products = graphene.List(ProductObjectType, offset=graphene.Int(), limit=graphene.Int())
#     orders = graphene.List(OrderObjectType, user_id=graphene.Int())
#     def resolve_products(self, info, offset=None, limit=None):
#         return Product.objects.all()[offset:offset + limit]
#
#     def resolve_orders(self, info, user_id=None):
#         if user_id is None:
#             return Order.objects.all()
#         return Order.objects.filter(user_id=user_id)
#
# schema = graphene.Schema(query=Query)
import time

import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from products.models import Product, Order, OrderProduct


# models.py
from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    summary = models.TextField()
    is_18_plus = models.BooleanField(default=False)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    display_number = models.CharField(max_length=255, unique=True)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_products', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()




class ProductObjectType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'summary', 'is_18_plus']

class OrderProductType(DjangoObjectType):
    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity']

class OrderObjectType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ['id', 'user', 'order_products', 'created_at', 'updated_at', 'display_number']

class OrderProductInput(graphene.InputObjectType):
    product_id = graphene.ID(required=True)
    quantity = graphene.Int(required=True)

class CreateOrderMutation(graphene.Mutation):
    class Arguments:
        user_id = graphene.ID(required=True)
        products = graphene.List(OrderProductInput, required=True)

    order = graphene.Field(OrderObjectType)
    user_errors = graphene.List(graphene.String)
    error = graphene.String()

    def mutate(self, info, user_id, products):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return CreateOrderMutation(order=None, user_errors=['User does not exist.'])

        if not products:
            return CreateOrderMutation(order=None, user_errors=['At least one product is required.'])

        try:
            order = Order.objects.create(user=user, display_number=f"ORD-{user_id}-{int(time.time())}")
            for item in products:
                try:
                    product = Product.objects.get(pk=item.product_id)
                    OrderProduct.objects.create(order=order, product=product, quantity=item.quantity)
                except Product.DoesNotExist:
                    return CreateOrderMutation(order=None, user_errors=[f'Product with ID {item.product_id} does not exist.'])

            return CreateOrderMutation(order=order)
        except Exception as e:
            return CreateOrderMutation(order=None, error=str(e))

class Mutation(graphene.ObjectType):
    create_order = CreateOrderMutation.Field()

schema = graphene.Schema(mutation=Mutation)



"""
mutation {
  createOrder(userId: "1", products: [{productId: "1", quantity: 2}, {productId: "2", quantity: 1}]) {
    order {
      id
      user {
        id
        username
      }
      orderProducts {
        product {
          title
        }
        quantity
      }
      createdAt
      updatedAt
      displayNumber
    }
    userErrors
    error
  }
}

"""
