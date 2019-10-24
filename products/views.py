from django.shortcuts import render
from django.views.generic import ListView
from . import models


class ProductsHomeView(ListView):
    model = models.Product
