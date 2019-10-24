from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.ProductsHomeView.as_view(), name="products-home"),
]
