from django.shortcuts import render
from django.views.generic import ListView
from . import models


class ProductsHomeView(ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'products/home.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = models.ProductImage.objects.all()
        context['top_products'] = models.Product.objects.all()[:2]
        return context
