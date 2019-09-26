from django_filters import rest_framework as filters
from .models import Product, Sale

class ProductFilter(filters.FilterSet):
  class Meta:
    model = Product
    fields = {
      "barcode": ["exact"],
      "description": ["icontains"],
    }


class SaleFilter(filters.FilterSet):
  class Meta:
    model = Sale
    fields = {
      "date": ["exact"],
    }