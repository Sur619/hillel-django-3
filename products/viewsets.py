from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from CourseDjango.permissions import IsOwnerOrReadOnly
from products.filters import ProductFilter
from products.models import Product, Order, Recipe
from products.serializers import ProductSerializer, ProductReadOnlySerializer, OrderSerializer
from products.serializers.recipe import RecipeSerializer


class ProductViewSet(viewsets.ModelViewSet):
    # select_related - for ForeignKey ----делают join на таблицу которая связана по связанному полю----
    # prefetch_related - for ManyToMany ----делают join на таблицу которая связана по связанному полю----

    queryset = Product.objects.select_related('category').prefetch_related('tags').all()

    filterset_class = ProductFilter  # подключаем фильтер клас
    filter_backends = [DjangoFilterBackend]

    pagination_class = PageNumberPagination
    def get_serializer_class(self):
        if self.action == ['list', 'retrieve']:  # еслли екшин лист или ретрив (хотим взять продукты )
            return ProductReadOnlySerializer
        else:
            return ProductSerializer

    # кастомный ендпоинт можно добавлтять и во viewsets
    @action(detail=False, methods=['get'])
    def latest(self, request, *args, **kwargs):
        latest_product = self.queryset.latest('created_at')
        return Response(self.get_serializer_class()(latest_product).data)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().prefetch_related('order_products',
                                                    'order_products__product')

    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.queryset
        return self.queryset.filter(user=self.request.user)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
