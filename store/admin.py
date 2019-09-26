from django.contrib import admin

from .models import (
  Client,
  Product,
  Sale,
  SaleDetail
)

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleDetail)