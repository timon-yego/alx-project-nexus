from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Order, OrderItem, Payment
from .serializers import OrderSerializer, PaymentSerializer
from rest_framework import status
# Create your views here.


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        # Simulate payment processing logic
        order_id = request.data.get('order')
        order = Order.objects.get(id=order_id)
        payment = Payment.objects.create(order=order, amount=order.total_amount, status="Completed")
        
        # Update order status after successful payment
        order.status = "Paid"
        order.save()

        return Response({"message": "Payment successful", "payment_id": payment.id}, status=status.HTTP_201_CREATED)
