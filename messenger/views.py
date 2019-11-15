from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib import messages
from django.views.generic.edit import UpdateView, FormView
from . import forms
from django.db.models import Q
from django.contrib.auth.models import User


class MessengerHomeView(LoginRequiredMixin, FormView):
    form_class = forms.MessengerForm
    template_name = 'messenger/home.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return models.Message.objects.filter()
        else:
            return models.Message.objects.filter(Q(sender=user) | Q(receiver=user))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg_list'] = self.get_queryset()
        return context

    def form_valid(self, form):
        user = self.request.user
        data = form.cleaned_data
        models.Message.objects.create(sender=user, content=data['content'])
        return redirect('messenger-home')


class MessengerAdminReplyView(LoginRequiredMixin, FormView):
    form_class = forms.MessengerReplyForm
    template_name = 'messenger/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rt = self.kwargs.get('replyto')
        reply_to = User.objects.get(pk=rt)
        context['msg_list'] = models.Message.objects.filter(Q(sender=reply_to) | Q(receiver=reply_to))
        context['reply_to'] = reply_to
        return context

    def form_valid(self, form):
        user = self.request.user
        data = form.cleaned_data
        rt = self.kwargs.get('replyto')
        reply_to = User.objects.get(pk=rt)
        models.Message.objects.create(sender=user, content=data['content'], receiver=reply_to)
        return redirect('messenger-admin-reply', replyto=rt)
