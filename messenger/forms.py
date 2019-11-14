from django import forms
from . import models


class MessengerForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control border-1', 'placeholder': 'Message the vendor ...'})
    )


class MessengerReplyForm(forms.Form):
    content = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control border-1', 'placeholder': 'Reply here ...'})
    )
