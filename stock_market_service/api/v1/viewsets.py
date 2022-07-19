import logging
from django.contrib.auth import authenticate

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from stock_market_service.models import *
from stock_market_service.api.v1.serializers import *
from stock_market_service.api.v1.permissions import ValidAPIKey, Throttling


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"], url_path="sign_up")
    def sign_up(self, request, *args, **kwargs):
        logging.warning("Sign up.")
        try:
            serializer = RegisterSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            username = serializer.validated_data["username"]
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            name = serializer.validated_data["name"]
            last_name = serializer.validated_data["last_name"]

            user = User.objects.create_user(
                username=username,
                email=email, 
                password=password,
                first_name=name,
                last_name=last_name,
                )
            SMSUser.objects.create(
                user=user,
                is_premium=False,
            )
            return Response(
                {
                    "message": "User created."
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response(
                {
                    "message": f"{e}"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=False, methods=["post"], url_path="get-api-key")
    def get_api_key(self, request, *args, **kwargs):
        logging.warning("API KEY request.")
        serializer = GetAPIkeySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            api_key = user.SMSUser.get_api_key()
            return Response(
                {
                    "message": f"User API KEY: {api_key}"
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {
                    "message": "Invalid username or password."
                },
                status=status.HTTP_201_CREATED,
            )


class StockMarketView(APIView):
    permission_classes = [ValidAPIKey]

    def get(self, request, *args, **kwargs):
        logging.warning("STOCK MARKET REQUEST")
        serializer = StockMarketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        symbol = serializer.validated_data["symbol"]
        data = serializer.get_stocks_data(symbol)

        return Response(
                {
                    "message": f"{data}"
                },
                status=status.HTTP_200_OK,  
            )


