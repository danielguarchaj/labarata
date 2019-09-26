from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth import views as auth_views

from store.models import (
  Product,
  Client,
  Sale,
  SaleDetail
)

def IndexView(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('frontend:dashboard'))
    else:
        return redirect(reverse_lazy('frontend:login'))


class LoginView(auth_views.LoginView):
    template_name = 'store/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('frontend:dashboard'))
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(auth_views.LogoutView):
    pass


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'store/dashboard.html'


class NewSaleView(LoginRequiredMixin, ListView):
  template_name = 'store/nueva_venta.html'
  model = Client
  context_object_name = 'clients'


class SaleDetailView(LoginRequiredMixin, DetailView):
  template_name = 'store/detalle_venta.html'
  model = Sale
  context_object_name = 'sale'

  def get_context_data(self, *args, **kwargs):
    context = super().get_context_data(**kwargs)
    context['sale_detail'] = SaleDetail.objects.filter(sale=context['sale'])
    return context
