from django.urls import path, include
from . import views as views

urlpatterns = [
    path('', views.MessengerHomeView.as_view(), name="messenger-home"),
    path('<replyto>/', views.MessengerAdminReplyView.as_view(), name="messenger-admin-reply"),
]
