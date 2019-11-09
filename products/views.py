from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib import messages


class ProductsHomeView(ListView):
    model = models.Product
    context_object_name = 'products'
    template_name = 'products/home.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = models.ProductImage.objects.all()
        context['top_products'] = models.Product.objects.all()[:2]
        order = self.request.user.orders.first()
        print('Current Cart Order: ', order)
        return context


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        print(models.ORDER_STATUS_CHOICES)
        user = request.user
        order = models.Order.objects.filter(user=user).first()

        if order == None:
            order = models.Order.objects.create(user=user)
        print('Cart Size: ', order.cart_size())
        product = models.Product.objects.get(id=product_id)
        order_item = models.OrderItem.objects.filter(
            order=order, product=product).first()
        if order_item == None:
            order_item = models.OrderItem.objects.create(
                order=order, product=product)
        else:
            order_item.quantity = order_item.quantity + 1
            order_item.last_update = datetime.now()
            order_item.save()
        print('Qty: ', order_item.quantity)
        messages.success(request,
                         'Successfully added to cart!')
        return redirect('products-home')


class AddAndBuyNowView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        print(models.ORDER_STATUS_CHOICES)
        user = request.user
        order = models.Order.objects.filter(user=user).first()

        if order == None:
            order = models.Order.objects.create(user=user)
        print('Cart Size: ', order.cart_size())
        product = models.Product.objects.get(id=product_id)
        order_item = models.OrderItem.objects.filter(
            order=order, product=product).first()
        if order_item == None:
            order_item = models.OrderItem.objects.create(
                order=order, product=product)
        else:
            order_item.quantity = order_item.quantity + 1
            order_item.last_update = datetime.now()
            order_item.save()
        print('Qty: ', order_item.quantity)
        messages.success(request,
                         'Successfully added to cart!')
        return redirect('products-home')


class OrderItemView(LoginRequiredMixin, DetailView):
    model = models.OrderItem
    context_object_name = 'order_item'
