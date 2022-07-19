from django.contrib import admin
from .models import *

@admin.register(SMSUser)
class SMSUSerAdmin(admin.ModelAdmin):
    list_display = [
        "username",
    ]

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = [
        "key",
        "is_active",
        "number_of_requests",
    ]
    