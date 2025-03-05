from django.urls import path
from .views import OrderListCreateView, OrderDetailView, PaymentCreateView

urlpatterns = [
    path('orders/', OrderListCreateView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('payments/', PaymentCreateView.as_view(), name='payment-create'),
]
