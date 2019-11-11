from django.contrib.auth.models import User
from . import models


class WorkingOrderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = request.user
        if user and user.is_authenticated:
            order = models.Order.objects.filter(
                user=user, status='CREATED').first()
            request.working_order = order
        response = self.get_response(request)
        return response
