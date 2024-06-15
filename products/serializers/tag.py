from rest_framework import serializers
from products.models import Tag


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')

