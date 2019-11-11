from django.db import models
from orders.models import Order

PAYMENT_CHANNEL_CHOICES = (
    ('WESTERNUNION', "Western Union"),
    ('BANKTRANSFER', 'Bank Transfer'),
    ('OTHER', 'Other'),
)


class Payment(models.Model):
    order = models.ForeignKey(
        to=Order, on_delete=models.PROTECT, related_name='payments')
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    channel = models.CharField(max_length=20, choices=PAYMENT_CHANNEL_CHOICES, default='OTHER')
    reference = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)

    def __str__(self):
        return f'# {self.id} - $ {self.amount} for {self.order}'
