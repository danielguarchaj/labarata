from django.urls import path

from . import views

app_name = 'frontend'

urlpatterns = [
  path('', views.IndexView, name='index'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),

  path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
  path('sale/', views.NewSaleView.as_view(), name='sale'),
  path('sale/<int:pk>/', views.SaleDetailView.as_view(), name='sale_detail')
]
