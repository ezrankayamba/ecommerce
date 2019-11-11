from django.forms import ModelForm, Textarea
from . import models


class OrderItemForm(ModelForm):
    class Meta:
        model = models.OrderItem
        fields = ['quantity', 'remarks']
        widgets = {
            'remarks': Textarea(attrs={'rows': 3}),
        }
