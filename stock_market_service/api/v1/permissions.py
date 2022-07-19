from rest_framework.permissions import BasePermission
from stock_market_service.models import *


class ValidAPIKey(BasePermission):
    def has_permission(self, request, view):
        api_key = request.META["QUERY_STRING"][8:]
        if APIKey.objects.filter(key=api_key, is_active=True).exists():
            return True
        
        return False


class Throttling(BasePermission):
    def has_permission(self, request, view):
        api_key = request.META["QUERY_STRING"][8:]
        key = APIKey.objects.get(key=api_key, is_active=True)
        user = SMSUser.objects.get(api_key=key)

        if user.is_premium:
            return True
        return False
