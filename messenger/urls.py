from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.MessengerHomeView.as_view(), name="messenger-home"),
]
