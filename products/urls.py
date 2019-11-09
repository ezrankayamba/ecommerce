from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.ProductsHomeView.as_view(), name="products-home"),
    path('<product_id>/add-to-cart/',
         views.AddToCartView.as_view(), name="add-to-cart"),
    path('<product_id>/add-and-buy-now/',
         views.AddAndBuyNowView.as_view(), name="add-and-buy-now"),
]
