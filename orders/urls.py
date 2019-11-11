from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.OrdersHomeView.as_view(), name="orders-home"),
    path('<product_id>/add-to-cart/',
         views.AddToCartView.as_view(), name="add-to-cart"),
    path('<product_id>/add-and-buy-now/',
         views.AddAndBuyNowView.as_view(), name="add-and-buy-now"),
    path('cart-and-checkout/',
         views.CartAndCheckoutView.as_view(), name="cart-and-checkout"),
    path('remove-order-item/<item_id>',
         views.remove_order_item, name="remove-order-item"),
    path('edit-order-item/<pk>',
         views.EditOrderItemView.as_view(), name="edit-order-item"),
]
