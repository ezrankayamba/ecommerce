from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('orders', include('orders.urls')),
    path('auth/', include('allauth.urls')),
    path('users/', include('users.urls')),
    path('payments/', include('payments.urls')),
    path('messenger/', include('messenger.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
