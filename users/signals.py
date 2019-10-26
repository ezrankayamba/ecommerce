from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile
from allauth.socialaccount import signals as sa_sig
from allauth.account import signals as a_sig


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(sa_sig.social_account_added)
def social_account_added(request, sociallogin, **kwargs):
    print('Social Account: ', sociallogin)


@receiver(a_sig.user_logged_in)
def social_account_added(request, sociallogin, **kwargs):
    print('Social Account: ', sociallogin)
