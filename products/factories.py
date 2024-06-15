from factory.django import DjangoModelFactory
import factory

from products.models import Product, Category, Tag


class CategoryFactory(DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Category


class TagFactory(DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Tag

class ProductFactory(DjangoModelFactory):
    title = factory.Faker('word')
    price = factory.Faker('random_number', digits=2)

    class Meta:
        model = Product
