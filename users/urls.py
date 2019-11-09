from django.urls import path, include
from django.views.generic import TemplateView
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', user_views.logout_view, name='users-logout'),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='users-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    path('changemypassword/', user_views.ChangeMyPasswordView.as_view(),
         name='change-password'),
]
