from rest_framework import viewsets
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, SaleSerializer, SaleDetailSerializer
from .filters import ProductFilter, SaleFilter

from .models import Product, Sale, SaleDetail, Client

class ProductsViewSet(viewsets.ModelViewSet):
  queryset = Product.objects.all()
  filterset_class = ProductFilter
  serializer_class = ProductSerializer


class SalesViewSet(viewsets.ModelViewSet):
  queryset = Sale.objects.all()
  serializer_class = SaleSerializer
  filterset_class = SaleFilter

class SaleDetailViewSet(viewsets.ModelViewSet):
  queryset = SaleDetail.objects.all()
  serializer_class = SaleDetailSerializer


import json
from rest_framework.response import Response

class SaleCreateView(APIView):
  def post(self, request, format=None):       
    response = {}
    response['status'] = 201

    sale_data = request.data
    
    sale_number = Sale.objects.count()
    client = Client.objects.get(pk=sale_data['client'])
    new_sale = Sale.objects.create(
      sale_number=1000 + sale_number + 1,
      client=client,
      total=sale_data['total']
    )
    response['sale_pk'] = new_sale.pk
    return Response(response)