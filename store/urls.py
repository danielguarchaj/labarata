from django.urls import path, include
from .views import *
from rest_framework import routers

app_name = 'store'

router = routers.DefaultRouter()

router.register(r'products', ProductsViewSet, base_name='products')
router.register(r'sales', SalesViewSet, base_name='sales')
router.register(r'sale_detail', SaleDetailViewSet, base_name='sale-detail')

urlpatterns = [
  path('', include(router.urls)),
  path('sale/create/', SaleCreateView.as_view(), name='sale-create')
]