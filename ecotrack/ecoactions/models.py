from django.db import models
from ecousers.models import User
from ecoproducts.models import Product

# Create your models here

class EcoAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')
    action = models.CharField(max_length=200)  # E.g., "Bought a reusable bottle"
    carbon_saved = models.FloatField()  # Carbon saved by this action
    timestamp = models.DateTimeField(auto_now_add=True)

class Reward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
    points = models.IntegerField()  # Points earned
    reason = models.CharField(max_length=200)  # E.g., "Eco-friendly purchase"
    timestamp = models.DateTimeField(auto_now_add=True)

class CarbonImpact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carbon_impacts')
    total_carbon_saved = models.FloatField(default=0)  # Total carbon saved by the user
    last_updated = models.DateTimeField(auto_now=True)
