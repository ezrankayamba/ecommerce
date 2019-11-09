from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib import messages
from django.views.generic.edit import UpdateView
from . import forms


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


class AddToCartView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        print(models.ORDER_STATUS_CHOICES)
        user = request.user
        order = models.Order.objects.filter(
            user=user, status='CREATED').first()

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
        order = models.Order.objects.filter(
            user=user, status='CREATED').first()
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


class CartAndCheckoutView(LoginRequiredMixin, View):
    def get(self, request):
        print(models.ORDER_STATUS_CHOICES)
        user = request.user
        order = models.Order.objects.filter(
            user=user, status='CREATED').first()
        if order == None or order.cart_size() < 1:
            messages.warning(request,
                             'Cart is empty, start shopping!')
            return redirect('products-home')
        context = {'order': order}
        return render(request, 'products/cart-checkout.html', context)

    def post(self, request):
        user = request.user
        order = models.Order.objects.filter(
            user=user, status='CREATED').first()
        if order == None or order.cart_size() < 1 or not order.not_sent():
            messages.warning(request,
                             'Cart is empty, start shopping!')
            return redirect('products-home')
        order.status = 'SENT'
        order.save()
        messages.success(request,
                         'Successfully sent the order, proceed with payment!')
        return redirect('products-home')


class EditOrderItemView(UpdateView):
    template_name = 'products/edit-order-item-form.html'
    form_class = forms.OrderItemForm
    model = models.OrderItem

    def form_valid(self, form):
        return super().form_valid(form)


def remove_order_item(request, item_id):
    models.OrderItem.objects.get(id=item_id).delete()
    messages.success(request,
                     'Successfully removed item from cart!')
    return redirect('cart-and-checkout')
