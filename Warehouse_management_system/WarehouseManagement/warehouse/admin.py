from django.contrib import admin
from .models import Products
from .models import Customers
from .models import Suppliers

# Register your models here.
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Suppliers)