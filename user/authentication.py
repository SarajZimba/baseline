# authentication.py

from django.contrib.auth.backends import BaseBackend
from .models import Customer

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Customer.objects.get(username=username)
            if user.check_password(password):
                return user
        except Customer.DoesNotExist:
            return None
