from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.PaymentsHomeView.as_view(), name="payments-home"),
]
