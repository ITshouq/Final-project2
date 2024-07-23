from .models import Products
from .models import Customers
from .models import Suppliers
from .serializers import ProductsSerializer
from .serializers import CustomersSerializer
from .serializers import SuppliersSerializer
from rest_framework import viewsets


class ProductsViewSet(viewsets.ModelViewSet):

   serializer_class = ProductsSerializer
   queryset = Products.objects.all()


class CustomersViewSet(viewsets.ModelViewSet):

   serializer_class = CustomersSerializer
   queryset = Customers.objects.all()


class SuppliersViewSet(viewsets.ModelViewSet):

   serializer_class = SuppliersSerializer
   queryset = Suppliers.objects.all()