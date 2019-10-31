from django.urls import path, include
from django.views.generic import TemplateView
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', views.login_view, name='users-login'),
    # path('profile/', views.profile_view, name='users-profile'),
    path('logout/', user_views.logout_view, name='users-logout'),

    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='users-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='users-login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('changemypassword/', user_views.ChangeMyPasswordView.as_view(),
         name='change-password'),
]
