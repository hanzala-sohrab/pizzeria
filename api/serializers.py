from django.utils.encoding import smart_text
from rest_framework import serializers
from pizza.models import Pizza, Topping
from bson import ObjectId
from bson.errors import InvalidId


# class ObjectIdField(serializers.Field):
#     """ Serializer field for Djongo ObjectID fields """
#     def to_internal_value(self, data):
#         # Serialized value -> Database value
#         try:
#             return ObjectId(str(data))  # Get the ID, then build an ObjectID instance using it
#         except InvalidId:
#             raise serializers.ValidationError(
#                 '`{}` is not a valid ObjectID'.format(data)
#             )
#
#     def to_representation(self, value):
#         # Database value -> Serialized value
#         if not ObjectId.is_valid(value):  # User submitted ID's might not be properly structured
#             raise InvalidId
#         return smart_text(value)


class ToppingSerializer(serializers.ModelSerializer):
    # _id = ObjectIdField(read_only=True)

    class Meta:
        model = Topping
        fields = '__all__'


class ToppingRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Topping.objects.get(topping=data)


class PizzaSerializer(serializers.ModelSerializer):
    topping = ToppingRelatedField(
        queryset=Topping.objects.all(),
        many=True
    )

    class Meta:
        model = Pizza
        extra_kwargs = {'type': {'required': True}}
        fields = ('id', 'pizza_type', 'pizza_size', 'topping')
