from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, PaymentViewSet

router = DefaultRouter()
router.register('orders', OrderViewSet)
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("payments/verify/<str:transaction_id>/", PaymentViewSet.as_view({"get": "verify_payment"}), name="verify-payment"),
]
