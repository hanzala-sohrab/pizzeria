from rest_framework import serializers
from pizza.models import Pizza, Topping, Size


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ToppingRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Topping.objects.get(topping=data)


class SizeRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Size.objects.get(size=data)


class PizzaSerializer(serializers.ModelSerializer):
    topping = ToppingRelatedField(
        queryset=Topping.objects.all(),
        many=True
    )

    pizza_size = SizeRelatedField(
        queryset=Size.objects.all(),
    )

    class Meta:
        model = Pizza
        extra_kwargs = {'type': {'required': True}}
        fields = ('id', 'pizza_type', 'pizza_size', 'topping')
