from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from . import models


@receiver(post_save, sender=models.Payment)
def payment_saved(sender, instance, created, **kwargs):
    order = instance.order
    if order:
        order.paid_amount = order.update_paid()
        order.save()


@receiver(post_delete, sender=models.Payment)
def payment_deleted(sender, instance, **kwargs):
    order = instance.order
    if order:
        order.paid_amount = order.update_paid()
        order.save()
