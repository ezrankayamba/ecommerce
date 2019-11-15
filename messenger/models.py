from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='sent_messages')
    receiver = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='received_messages', null=True)
    record_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
    content = models.CharField(max_length=255)

    class Meta:
        ordering = ['-record_date']
