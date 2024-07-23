from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Products
from .models import Customers
from .models import Suppliers


class ProductsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Products
       fields = ['products_name', 'description', 'quantity', 'category', 'price']


class CustomersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Customers
       fields = ['customer_name', 'phone', 'email', 'country', 'city', 'account_number']


class SuppliersSerializer(serializers.ModelSerializer):
   class Meta:
       model = Suppliers
       fields = ['suppliers_name', 'phone', 'email', 'country', 'city', 'account_number']