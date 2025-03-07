from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from ecoorders.models import Order

@shared_task
def send_order_confirmation_email(order_id):
    try:
        order = Order.objects.get(id=order_id)
        subject = "Order Confirmation - EcoTrack"
        message = f"Hello {order.user.email},\n\nYour order #{order.id} has been placed successfully!"
        recipient = [order.user.email]

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient)
        return f"Email sent to {order.user.email}"
    
    except Order.DoesNotExist:
        return "Order not found"
