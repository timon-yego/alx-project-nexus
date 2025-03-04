from django.db import models
from django.contrib.auth.models import AbstractUser,  Group, Permission
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_eco_enthusiast = models.BooleanField(default=False)
    carbon_footprint = models.FloatField(default=0)  # Total footprint

    groups = models.ManyToManyField(
        Group,
        related_name="ecousers_users",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="ecousers_user_permissions",
        blank=True
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    eco_score = models.IntegerField(default=0)  # Points for sustainable actions
    sustainability_goal = models.TextField(blank=True, null=True)

class SustainabilityGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    goal = models.CharField(max_length=200)  # E.g., "Reduce plastic usage"
    target = models.FloatField()  # E.g., 10% reduction
    progress = models.FloatField(default=0)  # E.g., 5% achieved
