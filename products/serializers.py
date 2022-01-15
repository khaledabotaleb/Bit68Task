from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    seller = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    def create(self, validated_data):
        user = validated_data["seller"]
        Product.objects.create(
            seller=user,
            name = validated_data['name'],
            price = validated_data['price']
        )
        return validated_data