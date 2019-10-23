from django.contrib import admin
from .models import Product, DetailProductType, Type, Order, DetailProductOrder
# Register your models here.

admin.site.register(Product)
admin.site.register(Type)
admin.site.register(DetailProductType)
admin.site.register(Order)
admin.site.register(DetailProductOrder)
