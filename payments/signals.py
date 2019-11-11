from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Payment)
def create_profile(sender, instance, created, **kwargs):
    order = instance.order
    if order:
        order.paid_amount = order.update_paid()
        order.save()
