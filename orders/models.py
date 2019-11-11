from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from products.models import Product


ORDER_STATUS_CHOICES = (
    ('CREATED', "Created"),
    ('SENT', 'Sent'),
    ('ADVANCEPAID', 'Advance Paid'),
    ('FULLYPAID', 'Fully Paid')
)


class Order(models.Model):
    user = models.ForeignKey(
        to=User, on_delete=models.PROTECT, related_name='orders')
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    total_amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    paid_amount = models.DecimalField(
        max_digits=20, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20, choices=ORDER_STATUS_CHOICES, default='CREATED')

    class Meta:
        ordering = ['-record_date']

    def __str__(self):
        return f'Order #{self.id} of {self.total_amount} by {self.user}'

    def cart_size(self):
        return sum(i.quantity for i in self.order_items.all())

    def order_amount(self):
        return sum(i.total_price() for i in self.order_items.all())

    def update_paid(self):
        return sum(p.amount for p in self.payments.all())

    def not_sent(self):
        return self.status == 'CREATED'


class OrderItem(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='product_order_items')
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    quantity = models.IntegerField(
        default=10, validators=[MinValueValidator(10)])
    remarks = models.CharField(max_length=255, null=True)

    def get_absolute_url(self):
        return reverse('cart-and-checkout', kwargs={})

    def __str__(self):
        return f'{self.quantity} x {self.product} @ $ {self.product.price}'

    def total_price(self):
        return self.product.price * self.quantity
