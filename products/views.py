from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib import messages
from django.views.generic.edit import UpdateView
from . import forms


class ProductsHomeView(LoginRequiredMixin, ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'products/home.html'
    paginate_by = 6

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated and not self.request.user.email:
            messages.warning(request,
                             'Email address is required to send you the invoice. Kindly provide update your profile')
            return redirect('users-profile')
        return super(ProductsHomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['product_images'] = models.ProductImage.objects.all()
        context['top_products'] = models.Product.objects.all()[:2]
        return context
