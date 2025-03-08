from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .models import Order, Payment
from .serializers import OrderSerializer, PaymentSerializer
from rest_framework import status
from ecoorders.tasks import send_order_confirmation_email
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import IsAuthenticated

import requests
from django.conf import settings
from django.utils.timezone import now
from ecoorders.models import Order, Payment
from ecoorders.serializers import OrderSerializer, PaymentSerializer


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Initiate Chapa payment",
        request_body=PaymentSerializer,
        responses={201: "Chapa Payment Initiated", 400: "Error initiating payment"},
    )
    def create(self, request, *args, **kwargs):
        """
        Initiates a Chapa payment for an order.
        """
        try:
            # ✅ Ensure 'order' is provided in the request data
            order_id = request.data.get("order")
            if not order_id:
                return Response({"error": "Order ID is required"}, status=status.HTTP_400_BAD_REQUEST)

            # ✅ Get order from database
            try:
                order = Order.objects.get(id=order_id)
            except Order.DoesNotExist:
                return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

            # ✅ Define Chapa payment payload
            payload = {
                "amount": str(order.total_amount),  # Convert to string for Chapa API
                "currency": "ETB",
                "email": request.user.email,
                "tx_ref": f"tx_{order.id}",
                "callback_url": "https://yourdomain.com/payment/callback/",
                "return_url": "https://yourdomain.com/payment/success/",
                "customization": {
                    "title": "EcoTrack Order Payment",
                    "description": "EcoTrack order payment via Chapa",
                },
            }

            # ✅ Make Chapa request
            headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
            response = requests.post(f"{settings.CHAPA_BASE_URL}transaction/initialize", json=payload, headers=headers)
            data = response.json()

            # ✅ Check if payment was successful
            if response.status_code == 200 and data.get("status") == "success":
                transaction_id = data["data"]["tx_ref"]
                
                # ✅ Store payment details in database
                Payment.objects.create(order=order, transaction_id=transaction_id, status="pending")

                return Response(
                    {"message": "Payment initiated", "chapa_url": data["data"]["checkout_url"]},
                    status=status.HTTP_201_CREATED,
                )

            return Response(  # ✅ Ensure return is within function
                {"error": "Failed to initiate payment", "details": data},
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    

    @swagger_auto_schema(
        operation_description="Verify Chapa payment status",
        responses={200: "Payment status verified", 400: "Payment verification failed"},
    )
    def verify_payment(self, request, transaction_id):
        headers = {"Authorization": f"Bearer {settings.CHAPA_SECRET_KEY}"}
        response = requests.get(f"{settings.CHAPA_BASE_URL}transaction/verify/{transaction_id}", headers=headers)
        data = response.json()

        if response.status_code == 200 and data.get("status") == "success":
            payment = Payment.objects.get(transaction_id=transaction_id)
            payment.status = "successful"
            payment.paid_at = now()
            payment.save()

            # Update Order status
            order = payment.order
            order.status = "completed"
            order.save()

            return Response({"message": "Payment successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST)
        
        