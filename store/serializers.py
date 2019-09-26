from rest_framework import serializers

from .models import (
  Product,
  Sale,
  SaleDetail
)

class ProductSerializer (serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'


class SaleSerializer (serializers.ModelSerializer):
  class Meta:
    model = Sale
    fields = '__all__'
    depth = 1


class SaleDetailSerializer (serializers.ModelSerializer):
  class Meta:
    model = SaleDetail
    fields = '__all__'

