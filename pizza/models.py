from django.db import models

TYPES = (
    ('Regular', 'Regular'),
    ('Square', 'Square')
)

SIZES = (
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
    ("Extra large", "Extra large"),
)

TOPPINGS = (
    ("Onion", "Onion"),
    ("Tomato", "Tomato"),
    ("Corn", "Corn"),
    ("Capsicum", "Capsicum"),
    ("Cheese", "Cheese"),
    ("Jalapeno", "Jalapeno"),
)


class Pizza(models.Model):
    # _id = models.AutoField(primary_key=True)
    pizza_type = models.CharField(max_length=10, choices=TYPES, null=False, blank=False)
    pizza_size = models.CharField(max_length=30, choices=SIZES, default='Small')
    topping = models.ManyToManyField('Topping', default='Tomato')
    customer_name = models.CharField(max_length=30)


class Topping(models.Model):
    # _id = models.AutoField(primary_key=True)
    topping = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.topping
