from django.db import models
from django.contrib.auth.models import User
from secrets import token_urlsafe

# SMS = Stock Market Service
class SMSUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="SMSUser",
        )
    api_key = models.ForeignKey(
        "stock_market_service.APIKey", 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True,
        related_name="user",
        )
    is_premium = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.first_name
    
    def generate_api_key(self):
        if self.api_key:
            self.disable_api_key()
        new_api_key = APIKey.objects.create(
            key = token_urlsafe(60),
            is_active = True,
        )
        self.api_key = new_api_key
        self.save()

    def disable_api_key(self):
        self.api_key.is_active = False
        self.api_key.save()

    def get_api_key(self):
        if self.api_key:
            return self.api_key
        else:
            self.generate_api_key()
            return self.api_key

    @property
    def username(self):
        return self.user.username


class APIKey(models.Model):
    key = models.CharField(
        max_length=60,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    number_of_requests = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.key