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


class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    pizza_type = models.CharField(max_length=10, choices=TYPES, null=False, blank=False)
    # pizza_size = models.CharField(max_length=30, choices=SIZES, default='Small')
    pizza_size = models.ForeignKey('Size', on_delete=models.CASCADE)
    topping = models.ManyToManyField('Topping', default='Tomato')
    customer_name = models.CharField(max_length=30)


class Topping(models.Model):
    topping = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.topping


class Size(models.Model):
    size = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.size
