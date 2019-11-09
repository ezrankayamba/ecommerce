from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    title = models.CharField(max_length=100)
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=10.00)
    description = models.CharField(
        max_length=1000, default='Generic sandals wear. Buy you will enjoy its durability for sure :)')

    class Meta:
        ordering = ('-record_date',)

    def __str__(self):
        return f'{self.title}'

    def image_sequence(self):
        return range(self.images.count())


class ProductImage(models.Model):
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images')
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ('-record_date',)

    def __str__(self):
        return f'{self.product.title} - {self.image.url}'


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

    def __str__(self):
        return f'{self.user} - {self.status}'

    def cart_size(self):
        return sum(i.quantity for i in self.order_items.all())


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


class Payment(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.PROTECT, related_name='payments')
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
