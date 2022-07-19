from django.urls import path, include
from rest_framework.routers import DefaultRouter

from stock_market_service.api.v1.viewsets import *

router = DefaultRouter()
router.register("SMSUsers", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("stocks", StockMarketView.as_view(), name="stocks")
]