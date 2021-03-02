from rest_framework import mixins, generics
from pizza.models import Pizza, Topping, Size
from .serializers import PizzaSerializer, ToppingSerializer, SizeSerializer


class CreatePizza(generics.CreateAPIView):
    model = Pizza
    serializer_class = PizzaSerializer


class CreateTopping(generics.CreateAPIView):
    model = Topping
    serializer_class = ToppingSerializer


class CreateSize(generics.CreateAPIView):
    model = Size
    serializer_class = SizeSerializer


class ListAll(generics.ListAPIView):
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        return self.model.objects.all()


class ListByID(generics.ListAPIView):
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        pizzaID = self.kwargs['id']
        queryset = self.model.objects.filter(id=pizzaID)
        return queryset


class ListByName(generics.ListAPIView):
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        name = self.kwargs['customer_name']
        queryset = self.model.objects.filter(customer_name=name)
        return queryset


class ListBySize(generics.ListAPIView):
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        size = self.kwargs['size']
        queryset = self.model.objects.filter(pizza_size=size)
        return queryset


class ListByType(generics.ListAPIView):
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        pType = self.kwargs['type']
        queryset = self.model.objects.filter(pizza_type=pType)
        return queryset


class ListAllSize(generics.ListAPIView):
    model = Size
    serializer_class = SizeSerializer

    def get_queryset(self):
        return self.model.objects.all()


class ListAllTopping(generics.ListAPIView):
    model = Topping
    serializer_class = ToppingSerializer

    def get_queryset(self):
        return self.model.objects.all()


class Modify(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
