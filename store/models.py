from django.db import models


class Product(models.Model):
  barcode = models.CharField(max_length=25)
  description = models.CharField(max_length=150)
  sale_price_1  = models.FloatField()
  sale_price_2 = models.FloatField()
  cost_price = models.FloatField()
  observations = models.CharField(max_length=150)


class Client(models.Model):
  name = models.CharField(max_length=75)
  nit = models.CharField(max_length=15)


class Sale(models.Model):
  sale_number = models.IntegerField()
  date = models.DateField(auto_now=True)
  total = models.FloatField()
  client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales')


class SaleDetail(models.Model):
  sale_price = models.FloatField()
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sale_details')
  sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_details')
  unit = models.IntegerField()
  subtotal = models.FloatField()