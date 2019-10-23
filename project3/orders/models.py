from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"
class Type(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.name}"

class DetailProductType(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    price = models.DecimalField(null=True, blank=True, max_digits=4,decimal_places=2)
    size = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        return f"{self.product} {self.type} {self.price} {self.size}"
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4,decimal_places=2)

    def __str__(self):
        return f"{self.user} {self.price}"

class DetailProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    state = models.BooleanField()

    def __str__(self):
        return f"{self.state}"