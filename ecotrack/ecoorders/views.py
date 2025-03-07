from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .models import Order, OrderItem, Payment
from .serializers import OrderSerializer, PaymentSerializer
from rest_framework import status
from ecoorders.tasks import send_order_confirmation_email
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @swagger_auto_schema(
        operation_description="Create a new order",
        request_body=OrderSerializer,
        responses={201: OrderSerializer, 400: "Bad Request"},
    )
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        order_id = response.data["id"]
        
        # Trigger Celery task asynchronously
        send_order_confirmation_email.delay(order_id)
        
        return Response({"message": "Order placed successfully!", "order": response.data}, status=status.HTTP_201_CREATED)

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer