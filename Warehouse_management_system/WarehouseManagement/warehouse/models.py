from django.db import models


class Products(models.Model):
   products_name = models.CharField(max_length=100)
   description = models.TextField(max_length=255)
   quantity = models.IntegerField(null=True)
   category = models.CharField(max_length=100)
   price = models.FloatField(null=True)

   def str(self):
       return self.products_name


class Customers(models.Model):
   customer_name = models.CharField(max_length=100)
   phone = models.IntegerField(null=True)
   email = models.EmailField(null=True)
   country = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   account_number = models.PositiveBigIntegerField(null=True)

   def str(self):
       return self.customer_name


class Suppliers(models.Model):
   suppliers_name = models.CharField(max_length=100)
   phone2 = models.IntegerField(null=True)
   email2 = models.EmailField(null=True)
   country2 = models.CharField(max_length=100)
   city2 = models.CharField(max_length=100)
   account_number2 = models.PositiveBigIntegerField(null=True)

   def str(self):
       return self.suppliers_name