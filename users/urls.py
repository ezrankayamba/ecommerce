from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='users-login'),
    path('profile/', views.profile_view, name='users-profile'),
    path('logout/', views.logout_view, name='users-logout'),
]
