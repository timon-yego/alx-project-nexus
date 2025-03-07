from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_email(user_email):
    send_mail(
        "Welcome to EcoTrack!",
        "Thank you for joining our platform!",
        "no-reply@ecotrack.com",
        [user_email],
    )
