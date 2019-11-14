from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib import messages
from django.views.generic.edit import UpdateView
from . import forms


class MessengerHomeView(LoginRequiredMixin, ListView):
    model = models.Message
    context_object_name = 'payments'
    template_name = 'messenger/home.html'
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return models.Message.objects.filter()
        else:
            return models.Message.objects.filter(sender=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
