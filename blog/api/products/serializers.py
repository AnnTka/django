from rest_framework import serializers

from shop.models import STATUS_CHOICES


class ProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    cost = serializers.IntegerField()
    image = serializers.ImageField()
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    description = serializers.CharField()
