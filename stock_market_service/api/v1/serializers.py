import requests

from rest_framework import serializers
from django.conf import settings

from stock_market_service.models import *


class UserSerializer(serializers.Serializer):
    class Meta:
        model= User
        fields = [
            "email",
            "username",
            "password",
        ]


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


class GetAPIkeySerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class StockMarketSerializer(serializers.Serializer):
    symbol = serializers.CharField(required=True)

    def get_stocks_data(self, symbol):
        KEY = settings.ALPHA_VANTAGE_KEY
        stock_qs = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=compact&apikey={KEY}"

        r = requests.get(stock_qs)
        data = r.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        previous_closing = data["Time Series (Daily)"][list(data["Time Series (Daily)"].keys())[1]]

        info = data["Time Series (Daily)"][last_refreshed]

        open = info["1. open"]
        high = info["2. high"]
        lower = info["3. low"]
        close1 = info["4. close"]
        close2 = previous_closing["4. close"]
        variation = round(float(close1) - float(close2), 4)

        information = {
            "open": open,
            "high": high,
            "lower": lower,
            "variation": variation,
        }
        return information